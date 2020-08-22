import re

import pytest
import requests


from test_wework.utils import utils
from test_wework.wework_interface.member_mangement import MemberMengement


class TestMemberMengement:
    def setup_class(self):
        self.member_mengement = MemberMengement()

    def test_token(self):
        assert self.member_mengement.access_token != None
        return self.member_mengement.access_token

    @pytest.mark.parametrize("userid,name,mobile", utils.create_data(1,5))
    def test_create(self,userid,name,mobile):
        r = self.member_mengement.create(userid,name,mobile)
        utils.print_json(r)
        assert "created" == r['errmsg']
        # 添加之后获取一下看是否添加成功
        r = self.member_mengement.get(userid)
        assert name == r['name']

    @pytest.mark.parametrize("userid,name,mobile",[("123455","wangwu","13999990013")])
    def test_get(self,userid,name,mobile):
        r = self.member_mengement.create(userid, name, mobile)
        utils.print_json(r)
        assert "created" == r['errmsg']
        r = self.member_mengement.get(userid)
        utils.print_json(r)
        assert 'wangwu' == r['name']

    @pytest.mark.parametrize("userid,name,mobile", [("01001558", "wang01105", "13979805667")])
    def test_update(self,userid,name,mobile):
        r = self.member_mengement.create(userid, name, mobile)
        assert "created" == r['errmsg']
        r = self.member_mengement.update(userid,"echo13",mobile)
        utils.print_json(r)
        assert 'updated' == r['errmsg']
        r = self.member_mengement.get(userid)
        utils.print_json(r)
        assert "echo13" == r['name']

    def test_delete(self):
        r = self.member_mengement.delete('11131535')
        # 修改成功之后进行删除
        assert "deleted" == r["errmsg"]
        # 删除之后再查一次看是否删除成功
        r = self.member_mengement.get('11131535')
        assert 60111 == r["errcode"]


    # def test_create_data():
    #     # send_data = [(str(random.randint(0,9999999)),
    #     #          "zhangsan",
    #     #          str(random.randint(13888880000, 13888889999))) for x in range(0,10)]
    #
    #     send_data = [("aaa125bbb"+ str(x),"zhansan","138%08d"%x) for x in range(1,20)]
    #     print(send_data)
    #     return send_data


    # @pytest.mark.parametrize("userid,name,mobile",test_create_data())
    # def test_all(userid,name,mobile,test_token):
    #     # 先获取一个我需要添加的成员看是否存在，如果存在就先删除再创建，或者是：在创建的时候看是否会出现已经存在该id的异常进行处理
    #     try:
    #         assert "created" == test_create(userid,name,mobile,test_token)['errmsg']
    #     except AssertionError as e:
    #         if 'mobile existed' in e.__str__():
    #     #         如果存在就删除,先找到userid
    #     #         re_userid = re.findall(":(.*)'$",e.__str__())[0]
    #             re_userid = re.findall(":(.*)",e.__str__())[0]
    #             if re_userid.endswith("'") or re_userid.endswith('"'):
    #                 re_userid = re_userid[:-1]
    #             print('re_userid='+re_userid)
    #             assert  "deleted" == test_delete(re_userid,test_token)["errmsg"]
    #             assert 60111 == test_get(re_userid)["errcode"]
    #             assert "created" == test_create(userid, name, mobile, test_token)['errmsg']
    #     # 添加之后获取一下看是否添加成功
    #     print(test_get(userid,test_token))
    #     assert name == test_get(userid,test_token)['name']
    #     # 成功添加之后进行修改
    #     assert "updated" == test_update(userid,"宋江",mobile,test_token)["errmsg"]
    #     # 修改之后获取一下看是否修改成功
    #     assert "宋江" == test_get(userid,test_token)['name']
    #     # 修改成功之后进行删除
    #     assert "deleted" == test_delete(userid,test_token)["errmsg"]
    #     # 删除之后再查一次看是否删除成功
    #     assert 60111 == test_get(userid,test_token)["errcode"]