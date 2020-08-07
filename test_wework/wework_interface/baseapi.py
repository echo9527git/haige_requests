"""
封装企业微信所有接口的公共部分
1、请求
2、url
"""
import requests
class BaseApi():
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/"
    get_token_url = base_url+"gettoken"
    _corpid = 'ww3c6b51ae743ae4ec'
    _company_label_corpsecret = 'xvmyVvTMnJaR0q2eitVBAOqJA-vQKt6zPjpQXixT8do'
    _member_mengement_corpsecret = '5qphgTlpn7pzuqFC3S6OBYFQnT46-S_7RTC0WOpxeyQ'

    company_label_token_params = {
        'corpid': _corpid,
        'corpsecret': _company_label_corpsecret
    }

    member_mangement_token_params = {
        'corpid': _corpid,
        'corpsecret': _member_mengement_corpsecret
    }

    company_label_get_corp_tag_list_url = base_url+"externalcontact/get_corp_tag_list"
    company_label_add_corp_tag_url = base_url+"externalcontact/add_corp_tag"
    company_label_edit_corp_tag_url = base_url+"externalcontact/edit_corp_tag"
    company_label_del_corp_tag_url = base_url+"externalcontact/del_corp_tag"

    member_mangement_user_create_url = base_url+"user/create"
    member_mangement_user_get_url = base_url+"user/get"
    member_mangement_user_update_url = base_url+"user/update"
    member_mangement_user_delete_url = base_url+"user/delete"

    def send(self,data):
        return requests.request(**data).json()

    def send_data(self, method='get', url=None, params=None, json=None):
        data = {
            "method":method,
            "url":url,
            "params":params,
            "json":json
        }
        return data

