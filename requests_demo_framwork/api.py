import base64
import json

import requests
from ruamel import yaml


class BaseApi():

    @classmethod
    def send(self,params):
        res = requests.request(params['method'],params['url'],headers = params['headers'])
        if params['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))
        # 如果是第三方加密，那么把结果拿到之后再请求第三方解密再返回解密之后信息
        elif params['encoding'] == 'private':
            return  requests.request('post','url',data= res.content)

