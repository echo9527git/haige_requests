import requests

class TestHttpDemo1():
    # def test_get(self):
    #     r = requests.get('https://httpbin.ceshiren.com/get')
    #     print(r.request)
    #     print(r.content)
    #     print(r.text)

    def test_post(self):
        r = requests.post('https://httpbin.ceshiren.com/post',data={'key':'value'})
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        r = requests.post('https://httpbin.ceshiren.com/post', json={'key': 'value'})
        print(r.text)
        assert r.status_code == 200