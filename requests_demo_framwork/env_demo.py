import requests

class API:
    @classmethod
    def send_env(self, data: dict):
        res = requests.request(method=data['method'], url=data['url'], headers=data['headers'])
        return res