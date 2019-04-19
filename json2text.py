import argparse
import glob
import json

from tqdm import tqdm

parser = argparse.ArgumentParser(description='extract text news from json')
parser.add_argument('-i', '--indir', type=str, help='input directory', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    lang_count = {}
    short_count = 0
    directory = args.indir
    json_files = glob.glob(directory + '*.json')
    pbar = tqdm(total=len(json_files))
    for json_file in json_files:
        json_text = open(json_file, encoding='utf-8').read()
        data = json.loads(json_text)
        lang = data.get('language')
        pbar.update()
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1
        if lang != 'ar':
            continue
        outfilename = json_file.replace('.json', '.txt')
        title = data.get('title', '')
        date_publish = data.get('date_publish', '')
        text = data.get('text', '')
        if not title or not text:
            short_count += 1
            continue
        with open(outfilename, encoding='utf-8', mode='w') as writer:
            writer.write('{}\n'.format(title))
            writer.write('{}\n'.format(date_publish))
            writer.write('{}\n'.format(text))

    pbar.close()
    print('number of files', len(json_files))
    print(lang_count)
    print('short count', short_count)
