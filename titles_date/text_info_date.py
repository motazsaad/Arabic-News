import glob
import json
import logging
import os, sys 
from collections import defaultdict
from tabulate import tabulate
import operator


def corpus_info(corpus_file):
	year_count = {}
	print('### corpus File:', corpus_file)
	corpus = open(corpus_file, encoding='utf-8').read()
	lines = corpus.split('\n')
	for line in lines:
		if line.strip():
			try:
				title, date = line.split('\t')
				year = date[:4]
				year_count[year] = year_count.get(year, 0) + 1 
			except ValueError:
				continue
	corpus_desc = [(date, count) for date, count in sorted(year_count.items())]
	print(tabulate(corpus_desc, headers=["Year", "Count"], tablefmt="github"))
	print('---')
	
	
if __name__ == '__main__':
	outfile = sys.argv[0][:-3] + '_corpus_date_desc.md'
	sys.stdout = open(outfile, mode='w', encoding='utf-8')
	print('## Corpus Date Characteristics')
	corpus_info('aljazeera.net_20190419_date_titles.txt')
	corpus_info('arabic.rt.com_20190419_date_titles.txt')
	corpus_info('arabic.cnn.com_20190419_date_titles.txt')
	corpus_info('arabic.euronews.com_20190409_date_titles.txt')
	corpus_info('bbc.com_20190409_date_titles.txt')


