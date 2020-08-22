import requests
from ruamel import yaml

class BaseApi():
    def send(self, data):
        return requests.request(**data).json()

    def send_data(self, method='get', url=None, params=None, json=None):
        data = {
            "method": method,
            "url": url,
            "params": params,
            "json": json
        }
        return data

    def template(self,yaml_file,**sourse_target):
        """
        将yaml文件读出并替换被$标记的字段
        :param yaml_file:yaml文件名
        :param sourse_target:需要被替换的原字段及目标数据的字典格式数据
        :return:返回从yaml文件中读出并被替换之后的结果数据
        """
        from string import Template
        re = Template(open(yaml_file).read()).substitute(**sourse_target)
        print("re=",re)
        return yaml.safe_load(re)

if __name__ == '__main__':
     # get_token_data = yaml.safe_load(open("get_token.yaml"))
    api = BaseApi()
    sourse_target = {
        "corpid":"ww3c6b51ae743ae4ec",
        "corpsecret":"xvmyVvTMnJaR0q2eitVBAOqJA-vQKt6zPjpQXixT8do"
    }
    # get_token_data = api.template("get_token.yaml",**sourse_target)
    get_token_data = api.template("get_token.yaml",**sourse_target)
    print("get_token_data=",get_token_data)
    res = api.send(get_token_data)
    print(res)