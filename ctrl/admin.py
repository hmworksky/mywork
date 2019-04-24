import requests
import base64


class AdminCtrl:

    def __init__(self):
        self.session = requests.Session()
        self.location = "http://9test74-admin.stg3.1768.com"
        self.send_mail_url = "{}/index.php?act=bubble_mail&st=send_mail".format(self.location)

    def login(self):
        """后台登录"""
        pwd = base64.b64encode("ceshiadmin123".encode("utf-8"))
        user = "admin"
        image_code = "xxxx"
        login_url = "{}/?act=index&st=login".format(self.location)
        login_data = {
            "username": user,
            "password": pwd,
            "image_code": image_code
        }
        self.session.post(login_url, data=login_data)

    def send_mail(self, user_id):
        self.login()
        """泡泡龙给个人发送邮件"""
        mail_data = {
            "type": 1,
            "attachment": 0,
            "send_type": 0,
            "send_time": "",
            "ids": user_id,
            "title": "auto_test_out",
            "content": "auto_test_out"
        }
        result = self.session.post(self.send_mail_url, data=mail_data)
        print(result.content)


if __name__ == '__main__':
    p = AdminCtrl()
    p.send_mail(2038983941)
