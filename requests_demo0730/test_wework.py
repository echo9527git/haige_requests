import json

import requests


class TestWework:
    def setup_class(self):
        corpsecret = 'xvmyVvTMnJaR0q2eitVBAOdyetWp8FvG6WscIEmorRw'
        corpid = 'ww3c6b51ae743ae4ec'

        # 先获取到access_token
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params={
            'corpid': corpid,
            'corpsecret': corpsecret
        })
        assert r.status_code == 200
        print(r.json())
        self.access_token = r.json()['access_token']

    def setup(self):
        pass

    # 获取企业标签库
    def test_tags_list(self):
        # 获取企业标签库
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',params={
            'access_token':self.access_token
        })
        assert r.status_code == 200
        self.print_json(r)
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group']) > 0

    # 添加企业客户标签--测试用例可以包含中英文、特殊字符、纯数字、字母等各种测试数据
    def test_add_corp_tag(self):
        # 方法一：加上时间戳保证测试数据的唯一性
        # 方法二：维护可重复使用的测试数据
        group_name = 'group_普通客户'
        tag_name = 'name_砖石'
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token':self.access_token},
            json = {
                "group_name": group_name,
                "tag":[{"name": tag_name}]
            }
        )
        self.print_json(r)
        assert r.json()['errcode'] == 0

    # 删除企业客户标签
    def test_del_corp_tag(self):
        # 获取企业标签库--封装复用
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list', params={
            'access_token': self.access_token
        })

        # 遍历获取到需要删除的tag_id
        tag_id = ""
        for group in r.json()['tag_group']:
            for tag in group['tag']:
                if tag['name'] == "name_砖石":
                    tag_id = tag["id"]

        # 删除指定tag_id的标签
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params = {'access_token':self.access_token},
            json={
                'tag_id':[tag_id]
            }

        )
        assert r.json()['errcode'] == 0
        # TODO:仅仅返回errcode=0是不行的，还需要判断是否成功删除

    def print_json(self,j):
        print(json.dumps(j.json(), indent=2, ensure_ascii=False))
