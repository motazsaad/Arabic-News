import argparse
import glob
import os 
import gzip
import sys


from tqdm import tqdm

parser = argparse.ArgumentParser(description='extract text news from json')
parser.add_argument('-i', '--indir', type=str, help='input directory', required=True)
parser.add_argument('-o', '--outfile', 
					type=argparse.FileType(mode='w', encoding='utf-8'), 
					help='outfile', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    directory = args.indir
    text_files = glob.glob(directory + '*.txt')
    print('# of files', len(text_files))
    corpus = ''
    pbar = tqdm(total=len(text_files))
    for text_file in text_files:
    	with open(text_file, mode='r', encoding='utf-8') as f:
    		corpus += f.read() + '\n'
    	pbar.update()
    
    args.outfile.write(corpus)
    args.outfile.close()
    print('all done')
    sys.exit(0)

