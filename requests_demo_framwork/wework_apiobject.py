"""
 api object模式与原则
    思想和pageobject相通
    隔离变与不变的内容
    接口细节与业务进行抽离

原则：
    每个公共方法代表接口所提供功能
    不要暴露api内部细节
    不要在接口实现层写断言
    每个method返回其他的api object或者用来做断言的信息
    不需要每个api都进行实现
"""
import requests


class Token:
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/"
    get_token_url = base_url + "gettoken"
    _corpid = 'ww3c6b51ae743ae4ec'
    _company_label_corpsecret = 'xvmyVvTMnJaR0q2eitVBAOqJA-vQKt6zPjpQXixT8do'
    company_label_token_params = {
        'corpid': _corpid,
        'corpsecret': _company_label_corpsecret
    }

    def get_company_label_token(self):
        """
        获取管理企业标签access_token
        :return:
        """
        data = self.send_data(
            method='get',
            url=self.get_token_url,
            params=self.company_label_token_params
        )
        res = requests.request(**data).json()
        access_token = res['access_token']
        return access_token

    def send_data(self, method='get', url=None, params=None, json=None):
        data = {
            "method":method,
            "url":url,
            "params":params,
            "json":json
        }
        return data

if __name__ == '__main__':
    token = Token()
    t = token.get_company_label_token()
    print(t)
