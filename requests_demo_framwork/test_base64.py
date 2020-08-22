import base64
import json

import requests

from requests_demo_framwork.api import BaseApi

url = 'http://127.0.0.1:10000/b64demo.txt'

class TestBase64():

    def test1(self):
        res = requests.get(url=url)
        data = base64.b64decode(res.content)
        print("res=",res.text)
        print(json.loads(data))

    def test2(self):
        data = {
            'method': 'get',
            'url': 'http://127.0.0.1:10000/b64demo.txt',
            'headers': None,
            'encoding': 'base64'
        }
        res = BaseApi.send(data)
        print(res)