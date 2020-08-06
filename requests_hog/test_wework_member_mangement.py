import random
import re

from filelock import FileLock
import pytest
import requests


@pytest.fixture(scope='session')
def test_token():
    _corpsecret = '5qphgTlpn7pzuqFC3S6OBYFQnT46-S_7RTC0WOpxeyQ'
    _corpid = 'ww3c6b51ae743ae4ec'
    access_token = None
    # 在使用pytest-xdist并行运行的时候可能会出现多次获取session，加一个锁
    while FileLock("session.lock"):

        # 先获取到access_token
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params={
            'corpid': _corpid,
            'corpsecret': _corpsecret
        })
        access_token = r.json()['access_token']
    return access_token

def test_create(userid,name,mobile,test_token):
    data = {
        'userid':userid,
        'name':name,
        'mobile':mobile,
        'department':[1]
    }
    r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",json=data)
    print('test_create')
    print(r.json())
    return r.json()

def test_get(userid,test_token):
    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return r.json()

def test_update(userid,name,mobile,test_token):
    data = {
        'userid':userid,
        'name':name,
        'mobile':mobile,
        'department':[1]
    }
    r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",json=data)
    return r.json()

def test_delete(userid,test_token):
    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return r.json()

def test_create_data():
    # data = [(str(random.randint(0,9999999)),
    #          "zhangsan",
    #          str(random.randint(13888880000, 13888889999))) for x in range(0,10)]

    data = [("aaa125bbb"+ str(x),"zhansan","138%08d"%x) for x in range(1,20)]
    print(data)
    return data


@pytest.mark.parametrize("userid,name,mobile",test_create_data())
def test_all(userid,name,mobile,test_token):
    # 先获取一个我需要添加的成员看是否存在，如果存在就先删除再创建，或者是：在创建的时候看是否会出现已经存在该id的异常进行处理
    try:
        assert "created" == test_create(userid,name,mobile,test_token)['errmsg']
    except AssertionError as e:
        if 'mobile existed' in e.__str__():
    #         如果存在就删除,先找到userid
    #         re_userid = re.findall(":(.*)'$",e.__str__())[0]
            re_userid = re.findall(":(.*)",e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            print('re_userid='+re_userid)
            assert  "deleted" == test_delete(re_userid,test_token)["errmsg"]
            assert 60111 == test_get(re_userid)["errcode"]
            assert "created" == test_create(userid, name, mobile, test_token)['errmsg']
    # 添加之后获取一下看是否添加成功
    print(test_get(userid,test_token))
    assert name == test_get(userid,test_token)['name']
    # 成功添加之后进行修改
    assert "updated" == test_update(userid,"宋江",mobile,test_token)["errmsg"]
    # 修改之后获取一下看是否修改成功
    assert "宋江" == test_get(userid,test_token)['name']
    # 修改成功之后进行删除
    assert "deleted" == test_delete(userid,test_token)["errmsg"]
    # 删除之后再查一次看是否删除成功
    assert 60111 == test_get(userid,test_token)["errcode"]