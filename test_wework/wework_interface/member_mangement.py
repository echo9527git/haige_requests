"""
成员管理接口
"""
from test_wework.wework_interface.token import Token


class MemberMengement(Token):
    def __init__(self):
        self.access_token = self.get_member_mangement_token()


    def create(self,userid, name, mobile):
        data = self.send_data(
            method='post',
            url=self.member_mangement_user_create_url,
            params={"access_token":self.access_token},
            json={
                'userid': userid,
                'name': name,
                'mobile': mobile,
                'department': [1]
            }
        )

        return self.send(data)

    def get(self,userid):
        data = self.send_data(
            method='get',
            url=self.member_mangement_user_get_url,
            params={
                "access_token":self.access_token,
                "userid":userid}
        )
        return self.send(data)

    def update(self,userid, name, mobile):
        data = self.send_data(
            method='post',
            url=self.member_mangement_user_update_url,
            params={"access_token": self.access_token},
            json={
                'userid': userid,
                'name': name,
                'mobile': mobile,
                'department': [1]
            }
        )
        return self.send(data)

    def delete(self,userid):
        data = self.send_data(
            method='get',
            url=self.member_mangement_user_delete_url,
            params={
                "access_token": self.access_token,
                "userid": userid}
        )
        return self.send(data)