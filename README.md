
# Arabic-News

Arabic News for language modelling collected from 

* BBC Arabic 
* EuroNews 
* Aljazeera 
* CNN Arabic 
* RT Arabic 

These news are collected by [news-please](https://github.com/fhamborg/news-please) python library

To extract news and titles 
`python json2corpus.py`


Crawl Date: 19-04-2019

---

# Corpus information 
| Corpus  | Size | number of words |
| ------- |:----:| ---------------:|
| JSC | 395M | 1525372 |
| RT | 713M |  3411451 |
| CNN | 94M | 317260 |
| BBC | 854M | 1764796 |
| Euronews | 279M | 517227 |



---
Log: 

```
corpus name: 09/arabic.euronews.com/
processing /home/motaz/newsgitrepo/data/2019/04/09/arabic.euronews.com/
# of files 46468
46079 is done out of 46468
number of files 46468
{'ar': 46468}
short count 389
.json
number of num_parts 18000
len of sub_lists 3
.txt
number of num_parts 18000
len of sub_lists 3
-------------------------------
corpus name: 09/bbc.com/
processing /home/motaz/newsgitrepo/data/2019/04/09/bbc.com/
# of files 212271
94734 is done out of 212271
number of files 212271
{'pt': 1, 'ar': 97468, 'fa': 114648, 'en': 154}
short count 2734
.json
number of num_parts 18000
len of sub_lists 6
.txt
number of num_parts 18000
len of sub_lists 6
-------------------------------
corpus name: 19/aljazeera.net/
processing /home/motaz/newsgitrepo/data/2019/04/19/aljazeera.net/
# of files 249106
109141 is done out of 249106
number of files 249106
{'ar': 170003, 'en': 3}
short count 60862
.json
number of num_parts 18000
len of sub_lists 7
.txt
number of num_parts 18000
len of sub_lists 7
-------------------------------
corpus name: 19/arabic.rt.com/
processing /home/motaz/newsgitrepo/data/2019/04/19/arabic.rt.com/
# of files 368920
334268 is done out of 368920
number of files 368920
{'ar': 368857}
short count 34589
.json
number of num_parts 18000
len of sub_lists 19
.txt
number of num_parts 18000
len of sub_lists 19
-------------------------------
corpus name: 19/arabic.cnn.com/
processing /home/motaz/newsgitrepo/data/2019/04/19/arabic.cnn.com/
# of files 30338
30140 is done out of 30338
number of files 30338
{'ar': 30338}
short count 198
.json
number of num_parts 18000
len of sub_lists 2
.txt
number of num_parts 18000
len of sub_lists 2
-------------------------------
all done
```
---

## compress files in a directory 
```
$ tree dir1/
dir1/
|-- dir11
|   |-- file11
|   |-- file12
|   `-- file13
|-- file1
|-- file2
`-- file3
```

now run the gzip command

`$ gzip -r dir1`

after

```
$ tree dir1/
dir1/
|-- dir11
|   |-- file11.gz
|   |-- file12.gz
|   `-- file13.gz
|-- file1.gz
|-- file2.gz
`-- file3.gz
```


# delete a lot of files 

`find . -name '*.html.gz' -print0 | xargs -0 rm`

# compress files using 7z 




















