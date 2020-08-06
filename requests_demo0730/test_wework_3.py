import pytest

from requests_demo0730 import utils
from requests_demo0730.wework_company_label_fixture_session_3 import WWCompanyLabel


class TestWework:
    def setup_class(self):
        self.wework = WWCompanyLabel()
    #     最开始的时候需要删除所有的标签组，这样保证每次测试的时候环境数据干净的
    #

    def setup(self):
        pass

    # 获取企业标签库
    def test_tags_list(self, access_token_3):
        # 获取企业标签库
        r = self.wework.get_corp_tag_list(access_token_3)
        assert r.status_code == 200
        utils.print_json(r)
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group']) > 0

    # 添加企业客户标签--测试用例可以包含中英文、特殊字符、纯数字、字母等各种测试数据
    def test_add_corp_tag(self, access_token_3):
        # 方法一：加上时间戳保证测试数据的唯一性
        # 方法二：维护可重复使用的测试数据
        # group_name = 'group_普通客户'
        # tag_name = 'name_砖石'
        # r = self.wework.add_corp_tag(group_name,tag_name)

        group_name = 'group_普通客户2222'
        tag_name = 'name_砖石22222'
        r = self.wework.add_corp_tag(group_name, tag_name, access_token_3)

        utils.print_json(r)
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize(('group_name,tag_name'),[
        ('group_dell','tag_dell'),
        ('中文标签组组','中文标签名名'),
        ('1233','4566'),
        ('@+++','@---')
    ])
    # 删除企业客户标签
    def test_del_corp_tag(self,group_name,tag_name,access_token):
        # 先添加一个标签
        r = self.wework.add_corp_tag(group_name,tag_name,access_token)

        # 添加之后获取tag_id
        tag_id = self.wework.get_group_tag_id_by_name(tag_name=tag_name,access_token=access_token)
        utils.print_json(r)

        # 添加完成之后需要断言是否添加成功
        assert tag_id != None

        # 删除指定tag_id的标签
        r = self.wework.del_corp_tag(tag_id=tag_id,access_token=access_token)

        # 删除之后获取tag_id
        tag_id = self.wework.get_group_tag_id_by_name(tag_name=tag_name,access_token=access_token)

        utils.print_json(r)

        # 删除成功之后断言
        # assert r.json()['errcode'] == 0
        assert tag_id == None






