import os

from spiders.spider_zhilianzhaoping import ZhiLianSpider
from company.constants import JOB_DIRECTION_TO_VERBOSE_NAME


"""
usage:
    python manage.py runscript spider_zhilianzhaoping 
"""


def run():
    all_spider = list()
    for keyword in JOB_DIRECTION_TO_VERBOSE_NAME.values():
        all_spider.append(ZhiLianSpider(keyword=keyword.lower()))

    downloaded_file_set = set()
    for filename in os.listdir('./data/'):
        kw = filename.split('.')[0]
        kw = kw.split('_')
        if len(kw) == 1:
            continue
        kw = kw[1]
        kw = kw.lower()
        downloaded_file_set.add(kw)

    dont_run_spider = list()
    for spider in all_spider:
        if spider.keyword in downloaded_file_set:
            continue
        dont_run_spider.append(spider)

    print('即将运行的爬虫: {}'.format(dont_run_spider))
    start = input('是否要进行爬取y/n: ')
    if start == 'y':
        for spider in dont_run_spider:
            spider.download_data_to_file()
            print('{} 运行成功.'.format(str(spider)))
    else:
        print('爬虫并未允许')




