"""
初步理解接口测试的po设计模式：
1、将每个业务封装成一个py文件；
2、将业务中的所有接口都封装成独立的方法，方法名就使用接口定义发的字段名--识别度高；
3、将某些同一模块中复用的功能单独封装成一个方法；
"""
import requests



class WWCompanyLabel:
    _baseurl = 'https://qyapi.weixin.qq.com/cgi-bin'

    # # 获取access_token
    # def get_access_token(self):
    #     _corpsecret = 'xvmyVvTMnJaR0q2eitVBAOdyetWp8FvG6WscIEmorRw'
    #     _corpid = 'ww3c6b51ae743ae4ec'
    #
    #     # 先获取到access_token
    #     r = requests.get(self._baseurl+'/gettoken', params={
    #         'corpid': _corpid,
    #         'corpsecret': _corpsecret
    #     })
    #     self.access_token_3 = r.json()['access_token_3']
    #     return self.access_token_3

    # 获取企业标签库
    def get_corp_tag_list(self,access_token):
        r = requests.post(self._baseurl+'/externalcontact/get_corp_tag_list', params={
            'access_token_3': access_token
        })
        return r

    # 添加企业客户标签---两个都是必填参数
    def add_corp_tag(self,group_name,tag_name,access_token):
        r = requests.post(self._baseurl+'/externalcontact/add_corp_tag',
                          params={'access_token_3': access_token},
                          json={
                              "group_name": group_name,
                              "tag": [{"name": tag_name}]
                          }
                          )
        return r

    # 编辑企业客户标签
    def edit_corp_tag(self,access_token):
        pass

    # 删除企业客户标签
    def del_corp_tag(self,group_id=None,tag_id=None,access_token=None):
        # 因为删除是可以单独删除group也可以单独删除tag或者同时删除，所有参数想要区别对待
        json = {}
        if group_id != None and tag_id != None:
            json = {
                'tag_id': [tag_id],
                'group_id': [group_id]
            }
        elif group_id != None:
            json = {'group_id':[group_id]}
        elif tag_id != None:
            json = {'tag_id': [tag_id]}

        r = requests.post(self._baseurl+'/externalcontact/del_corp_tag',
                      params={'access_token_3': access_token},
                      json=json
        )
        return r

    # 获取tag_id或者是group_id
    def get_group_tag_id_by_name(self,group_name=None,tag_name=None,access_token=None):
        group_id = None
        tag_id = None

        r = self.get_corp_tag_list(access_token)
        # 如果group_name != None说明需要获取group_id
        if group_name != None:
            print("group_name:"+group_name)
            for group in r.json()['tag_group']:
                if group['group_name'] == group_name:
                    group_id = group['group_id']
                    break
            # 循环结束判断是否获取到想要的id来进行返回，如果没有找到就给出提示或者抛出异常
            if group_id != None:
                return group_id
            # else:
            #     raise NameError(f'输入值group_name：{group_name}不存在')
        # 如果tag_name != None说明需要获取tag_id
        elif tag_name != None:
            for group in r.json()['tag_group']:
                for tag in group['tag']:
                    if tag['name'] == tag_name:
                        tag_id = tag["id"]
                        break
            # 循环结束判断是否获取到想要的id来进行返回，如果没有找到就给出提示或者抛出异常
            if tag_id != None:
                return tag_id
            # else:
            #     raise NameError(f'输入值group_name：{tag_name}不存在')

        # # 说明参数没有输入
        # else:
        #     raise NameError('未输入任何的group_name或者tag_name参数')
