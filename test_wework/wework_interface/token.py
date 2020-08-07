"""
获取access_token的类，因为每个业务模块都需要access_token，但是每个模块的又不一样
"""
from test_wework.wework_interface.baseapi import BaseApi


class Token(BaseApi):
    def get_company_label_token(self):
        """
        获取管理企业标签access_token
        :return:
        """
        # send_data = {
        #     "method":"get",
        #     "url":self.get_token_url,
        #     "params":self.company_label_token_params
        # }

        data = self.send_data(
            method='get',
            url=self.get_token_url,
            params=self.company_label_token_params
        )
        access_token = self.send(data)['access_token']
        return access_token

    def get_member_mangement_token(self):
        """
        获取成员管理access_token
        :return:
        """
        data = {
            "method":"get",
            "url":self.get_token_url,
            "params":self.member_mangement_token_params
        }
        access_token = self.send(data)['access_token']
        return access_token
