import argparse
import glob
import json
from shutil import copy
import os, sys 


def do_work2(directory, corpus_name, dist, time_stamp):
	print('corpus name: {}'.format(corpus_name))
	lang_count = {}
	short_count = 0
	src_dir = directory + corpus_name
	print('processing', src_dir)
	json_files = glob.glob(src_dir + '*.json')
	num_files = len(json_files)
	print('# of files', num_files)
	target = '/home/motaz/newsgitrepo/Arabic-News/titles_date/'
	titles_outfile_name = target + corpus_name[3:][:-1] + time_stamp + '_date_titles.txt'
	title_writer = open(titles_outfile_name, mode='w', encoding='utf-8')
	json_list = list()
	text_list = list()
	process_count = 0
	for json_file in json_files:
		try:
			json_text = open(json_file, encoding='utf-8').read()
			data = json.loads(json_text)
		except UnicodeDecodeError:
			continue
		except json.decoder.JSONDecodeError: 
			continue
		lang = data.get('language')
		if lang:
			lang_count[lang] = lang_count.get(lang, 0) + 1
		if lang != 'ar':
			continue
		title = data.get('title', '')
		date_publish = data.get('date_publish', '')
		# print(date_publish)
		text = data.get('text', '')
		if not title or not text:
			short_count += 1
			continue
		if len(title.split()) < 5 or len(text.split()) < 20:
			short_count += 1
			continue
		json_list.append(json_text)
		# print(date_publish[:10])
		try:
			title_writer.write('{}\t{}\n'.format(title, date_publish[:10]))
			process_count += 1
			sys.stdout.write('{} is done out of {}\r'.format(process_count, num_files))
		except TypeError as error:
			continue
	print('\nnumber of files', len(json_files))
	print(lang_count)
	print('short count', short_count)
	print('-------------------------------')


if __name__ == '__main__':
	src = '/home/motaz/newsgitrepo/data/2019/04/'
	dist = '/home/motaz/newsgitrepo/Arabic-News/json/data/2019/04/'
	
	# do_work2(src, '09/arabic.euronews.com/', dist, '_20190409')
	# do_work2(src, '09/bbc.com/' , dist, '_20190409' )
	do_work2(src, '19/aljazeera.net/', dist, '_20190419' )
	do_work2(src, '19/arabic.rt.com/', dist, '_20190419' )
	do_work2(src, '19/arabic.cnn.com/', dist, '_20190419' )
	print('all done')
		
