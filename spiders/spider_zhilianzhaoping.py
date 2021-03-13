import requests
import json
import logging
import time
import os

logging.basicConfig(
    level=logging.INFO,
    filename='output.log',
    filemode='a',
    format='[%(asctime)s][%(name)s][%(levelname)s]: %(message)s'
)
logger = logging.getLogger('ZLZP')

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

url = 'https://fe-api.zhaopin.com/c/i/search/positions'
query_params = {
    'at': 'b8594d0a259b41d88e2aff63d156aa2d',
    'rt': 'fbf00e2676924102b476add8a7da0316',
    '_v': '0.55004901',
    'x-zp-page-request-id': 'aa6d3a7a6d044276b229c8e7c28cd5b0-1615648192792-220092',
    'x-zp-client-id': 'c8efb2b8-9362-4217-9af7-60f5a0513b83',
    'MmEwMD': '5Al.PFnFNAHdGgo6hr5z9auu2od_AUKdr6l3AGqzygUVP0jyJ7Qk2cnyZ2rpfufTxI8PsRf.V1UhIJgT9KYauQ3O5I_Y4zTwd5v6IFVvXAIqx9CmSO_MXJcH83rKc9L2SCWSpjTqY4Db2HVta2gmtRYwsuI51ngPC67skWeY_ovYSMY4okgEwy3UphNsg9ZF.XP8dVP_EZN5ihBr7grbIC8rx3A6afeAuzXGY3zCaeB4iv0XUaXcz_AHOulGbMPvJXPPp2SFmnvMYIT4mrOrx4JYoGdyJkdJ1LnZXSlHBzigFzWo6aStR9jxl0eFZP21bcaQIXz3DCQU1z3ydBlTa4UHa76cCmuurZQYZQZrwOiz._k4AGxmIae3oTIBqiuvr5LqEgGRkGTQx9kYAXHCI8y61_VHbewxts4I.XgmIOk2ZDI7dKSSk9toR6.G9GAXwRCF'
}


def handle_query_params(query_params: dict):
    kv_list = list()
    for key, value in query_params.items():
        kv_list.append('{}={}'.format(key, value))
    return '&'.join(kv_list)


url = '{}?{}'.format(url, handle_query_params(query_params))


class ZhiLianSpider:
    def __init__(self, keyword='Java开发'):
        self.headers = headers
        self.url = url
        self.count = 0
        self.data_list = list()
        self.end = False
        self.job_list = list()
        self.keyword = keyword
        self.page_index = 1

    def get_data(self):
        data = {
            "S_SOU_FULL_INDEX": self.keyword,
            "S_SOU_WORK_CITY": "653",  # 653代表杭州
            "pageSize": 30,
            "pageIndex": self.page_index,
            "cvNumber": "JI301770812R90500000000",
            "eventScenario": "pcSearchedSouSearch"
        }

        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200 and response.json()['code'] == 200:
            result = response.json()
            self.count = result['data']['count']
            self.data_list.extend(result['data']['list'])
            self.end = result['data']['isEndPage'] == 1
            logger.info(f"data list len: {len(result['data']['list'])}")
        else:
            logger.error('download failed.')

    def parse_data(self):
        for res in self.data_list:
            job_info = {
                'company_info': res.get('companyName'),
                'name': res.get('name'),
                'location': '{}-{}-{}'.format(res.get('workCity'), res.get('cityDistrict'), res.get('tradingArea')),
                'education': res.get('education'),
                'salary': res.get('salary60'),
                'work_experience': res.get('workingExp'),
                'skill_label': [i.get('value') for i in res.get('skillLabel')],
                'welfare_label': [i.get('value') for i in res.get('welfareLabel')],
            }
            self.job_list.append(job_info)

    def download_data_to_file(self):
        while not self.end:
            self.get_data()
            self.page_index += 1
            time.sleep(1)

        logger.info(f'download data count: {self.count}, len: {len(self.data_list)}')
        self.parse_data()

        with open(f'./data/智联_{self.keyword}.json', 'w') as f:
            f.write(json.dumps(self.job_list, ensure_ascii=False))
        logger.info(f'save success. len: {len(self.job_list)}')

    def __str__(self):
        return '{} spider'.format(self.keyword)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    # logger.info('xxx')
    java_spider = ZhiLianSpider()
    python_spider = ZhiLianSpider(keyword='Python开发')
    fe_spider = ZhiLianSpider(keyword='前端开发')
    php_spider = ZhiLianSpider(keyword='PHP开发')
    all_spider = [java_spider, python_spider, fe_spider, php_spider]

    downloaded_file_set = set()
    for filename in os.listdir('./data/'):
        kw = filename.split('.')[0]
        kw = kw.split('_')
        if len(kw) == 1:
            continue
        kw = kw[1]
        downloaded_file_set.add(kw)

    dont_run_spider = list()
    for spider in all_spider:
        if spider.keyword in downloaded_file_set:
            continue
        dont_run_spider.append(spider)

    print('即将运行的爬虫: {}'.format(dont_run_spider))
    # for spider in dont_run_spider:
    #     spider.download_data_to_file()
