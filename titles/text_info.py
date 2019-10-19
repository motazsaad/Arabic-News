import glob
import json
import logging
import os, sys 
from collections import defaultdict
from tabulate import tabulate
import operator


def corpus_info(corpus_file, topn=50):
	print('## corpus File:', corpus_file)
	corpus = open(corpus_file, encoding='utf-8').read()
	line_count = len(corpus.split('\n'))
	word_freq = {} 
	for word in corpus.split():
		word_freq[word] = word_freq.get(word, 0) + 1 

	# print('vocabulary size:', len(word_freq))
	vocab_size = len(word_freq)
	word_count = 0 
	for v in word_freq.values():
		word_count += v 
	# print('word count:', word_count)
	print('## Corpus Characteristics')
	corpus_desc = [[line_count, word_count, vocab_size]]
	print(tabulate(corpus_desc, headers=["Lines", "Terms", "Vocabulary"], tablefmt="github"))
	
	sorted_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
	most_freq = [list(i) for i in sorted_freq[:topn]]  # list of lists
	print('### Most frequent words')
	print(tabulate(most_freq, headers=["Word", "Frequency"], tablefmt="github", showindex=True))
	least_freq = [list(i) for i in sorted_freq[-1*topn:]]  # list of lists
	print('### Hapax words')
	print(tabulate(least_freq, headers=["Word", "Frequency"], tablefmt="github", showindex=True))
	print('---')
	
	
if __name__ == '__main__':
	outfile = sys.argv[0][:-3] + '_corpus_desc.md'
	sys.stdout = open(outfile, mode='w', encoding='utf-8')
	corpus_info('aljazeera.net_20190419_titles.txt')
	corpus_info('arabic.rt.com_20190419_titles.txt')
	corpus_info('arabic.cnn.com_20190419_titles.txt')
	corpus_info('arabic.euronews.com_20190409_titles.txt')
	corpus_info('bbc.com_20190409_titles.txt')


