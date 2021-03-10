import requests
import json
import logging

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

url = 'https://fe-api.zhaopin.com/c/i/search/positions?at=f5fd0fcc7cd54faa956be86dc704ca0a&rt=bda665ca30684fb49b464c8e80fbfa0e&_v=0.58186874&x-zp-page-request-id=937cbb24ffb740c9955b180f864e8616-1615124663188-784338&x-zp-client-id=c8efb2b8-9362-4217-9af7-60f5a0513b83&MmEwMD=5kG17xKOvk.DX.Oim1FVjOUt.VMk8lnDH9Gf8u9V6.uz7viqkdg_.pKqnC2LBGmWoW_Mwtm1Frunp8QWjmSxeHZFazLfV_mKKzn.GnW3DlrDM1LqBJlRwGFQsdBvkgiqkP1IdxSIEV.mY8EidBGLo_bWhS7BJ93.DmSqxB1TMCGOd3Qhqfl.D69mgZRCZrrpRfrrtEFOGTP8FGOeSnlHtv7my072NzGacyWbyBdISSZb3XVhh4V11Z3lZ9.I50LKdnBMURGbGNHqaC1NsN4ew06hwdLfI5r18SYUwysao7zb4soDdw1.zcygUkHC7eZzdKmzGhQ.plsEJNyJO2ls_dbIkK_R2Jx9tTqQpYgxxpdYBlasAZqRNI45z7y9iMhPNNl9L6PRp6h_OZMG6WpfAHN2NsScmC90Hm_f3caAxFCpwZbLvkg_YXSodk5dak45t_Ie'
# url = 'https://fe-api.zhaopin.com/c/i/search/positions'


class ZhiLianSpider:
    def __init__(self):
        self.headers = headers
        self.url = url

    def get_data(self, keyword='Java开发'):
        data = {
            "S_SOU_FULL_INDEX": keyword,
            "S_SOU_WORK_CITY": "653",  # 653代表杭州
            "pageSize": 30,
            "pageIndex": 1,
            "cvNumber": "JI301770812R90500000000",
            "eventScenario": "pcSearchedSouSearch"
        }

        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200 and response.json()['code'] == 200:
            result = response.json()['data']['list']
            job_list = list()
            for res in result:
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
                job_list.append(job_info)
            with open('./data/智联_{}.json'.format(data['S_SOU_FULL_INDEX']), 'w') as f:
                f.write(json.dumps(job_list, ensure_ascii=False))
            logging.info('save success.')
        else:
            logging.info('download failed.')


if __name__ == "__main__":
    logger.info('xxx')
