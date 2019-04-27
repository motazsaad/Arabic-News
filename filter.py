import argparse
import glob
import os 

from tqdm import tqdm

parser = argparse.ArgumentParser(description='extract text news from json')
parser.add_argument('-i', '--indir', type=str, help='input directory', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    lang_count = {}
    directory = args.indir
    json_files = glob.glob(directory + '*.json')
    removed_files  = 0
    print('json.gz files', len(json_files))
    pbar = tqdm(total=len(json_files))
    for json_file in json_files:
    	text_file = json_file.replace('.json', '.txt')
    	if not os.path.exists(text_file):
    		os.remove(json_file)
    		removed_files += 1 
    	pbar.update()
    print('removed files', removed_files)