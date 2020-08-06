import pytest
import requests



@pytest.fixture(scope='session')
# 获取access_token
def access_token_3():
    _baseurl = 'https://qyapi.weixin.qq.com/cgi-bin'
    _corpsecret = 'xvmyVvTMnJaR0q2eitVBAOdyetWp8FvG6WscIEmorRw'
    _corpid = 'ww3c6b51ae743ae4ec'

    # 先获取到access_token
    r = requests.get(_baseurl + '/gettoken', params={
        'corpid': _corpid,
        'corpsecret': _corpsecret
    })
    access_token = r.json()['access_token_3']
    return access_token


@pytest.fixture(scope='session')
# 获取access_token
def session_4():
    _baseurl = 'https://qyapi.weixin.qq.com/cgi-bin'
    _corpsecret = 'xvmyVvTMnJaR0q2eitVBAOdyetWp8FvG6WscIEmorRw'
    _corpid = 'ww3c6b51ae743ae4ec'

    # 通过requests.session()维持回话，这样以后请求的时候就不需要传access_token
    session = requests.session()

    session.get(_baseurl + '/gettoken', params={
        'corpid': _corpid,
        'corpsecret': _corpsecret
    })
    return session
