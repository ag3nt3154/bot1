import os
from icrawler.builtin import GoogleImageCrawler
path = os.getcwd()
path = path + '\img'
print(path)
print(os.listdir(path))
# google_crawler = GoogleImageCrawler(storage={'root_dir': path})
# google_crawler.crawl(keyword='memes', max_num=10)

