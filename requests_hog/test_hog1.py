from jsonpath import jsonpath
from hamcrest import *
from requests_demo0730 import utils
import requests
from requests.auth import HTTPBasicAuth
class TestHog1:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.text)
        assert r.status_code ==200

    def test_query(self):
        payload = {
            "level":1,
            "name":'echo'
        }
        r = requests.get("http://httpbin.testing-studio.com/get",params=payload)
        print(r.text)
        assert r.status_code ==200

    def test_heaaders(self):
        header = {
            "h": 'header demo'
        }
        r = requests.get("http://httpbin.testing-studio.com/get", headers=header)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": 'echo'
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    # "Content-Type": "application/json"
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": 'echo'
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    # requests没有提供对xml封装的接口，所有使用data（文本）来发送数据，同时需要修改headers中的Content-Type
    # "Content-Type": "application/xml"
    def test_post_xml(self):
        pass

    def test_hog_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        utils.print_json(r)
        assert r.json()['category_list']['categories'][1]['name'] == '开源项目'
        assert jsonpath(r.json(),'$..name')[1] == '开源项目'

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        utils.print_json(r)
        assert_that(r.json()['category_list']['categories'][1]['name'],equal_to('开源项目'))
        assert_that(jsonpath(r.json(), '$..name')[1],equal_to('开源项目'))

    def test_cookies1(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        headers = {'Cookie':'echo'}
        r = requests.get(url=url,headers = headers)
        utils.print_json(r)

    def test_cookies2(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        headers = {'User-Agent':'echo'}
        cookies = {'cookie1':'echo1','cookies2':'echo2'}
        r = requests.get(url=url,headers = headers,cookies = cookies)
        utils.print_json(r)

    def test_auth(self):
        r = requests.get('http://httpbin.testing-studio.com/basic-auth/echo/1234',auth=HTTPBasicAuth('echo','1234'))
        print(r.status_code)