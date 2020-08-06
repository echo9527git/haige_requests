import pytest

from requests_demo0730 import utils
from requests_demo0730.wework_company_label_fixture_token_4 import WWCompanyLabel


class TestWework:
    def setup_class(self):
        self.wework = WWCompanyLabel()
    #     最开始的时候需要删除所有的标签组，这样保证每次测试的时候环境数据干净的
    # TODO

    def setup(self):
        pass

    # 获取企业标签库
    def test_tags_list(self,session_4):
        # 获取企业标签库
        r = self.wework.get_corp_tag_list(session_4)
        assert r.status_code == 200
        utils.print_json(r)
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group']) > 0

    # 添加企业客户标签--测试用例可以包含中英文、特殊字符、纯数字、字母等各种测试数据
    def test_add_corp_tag(self,session_4):
        # 方法一：加上时间戳保证测试数据的唯一性
        # 方法二：维护可重复使用的测试数据
        # group_name = 'group_普通客户'
        # tag_name = 'name_砖石'
        # r = self.wework.add_corp_tag(group_name,tag_name)

        group_name = 'group_普通客户11111'
        tag_name = 'name_砖石1111111'
        r = self.wework.add_corp_tag(session_4,group_name,tag_name)

        utils.print_json(r)
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize(('group_name,tag_name'),[
        ('group_del','tag_del'),
        ('中文标签组','中文标签名'),
        ('123','456'),
        ('@++','@--')
    ])
    # 删除企业客户标签
    def test_del_corp_tag(self,session_4,group_name,tag_name):
        # 先添加一个标签
        r = self.wework.add_corp_tag(session_4,group_name,tag_name)

        # 添加之后获取tag_id
        tag_id = self.wework.get_group_tag_id_by_name(session_4,tag_name=tag_name)
        utils.print_json(r)

        # 添加完成之后需要断言是否添加成功
        assert tag_id != None

        # 删除指定tag_id的标签
        r = self.wework.del_corp_tag(session_4,tag_id=tag_id)

        # 删除之后获取tag_id
        tag_id = self.wework.get_group_tag_id_by_name(session_4,tag_name=tag_name)

        utils.print_json(r)

        # 删除成功之后断言
        assert r.json()['errcode'] == 0
        assert tag_id == None






