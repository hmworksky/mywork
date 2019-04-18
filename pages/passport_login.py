from pages.basePage import BasePages


class WltLoginPage(BasePages):

    def __init__(self):
        super().__init__("passport")

    def wlt_label(self):
        """passport登陆页wlt登录标签"""
        return self.get_image("wlt_label", record_pos=(-0.012, -0.478))

    def wlt_user(self):
        """万里通登录用户名"""
        return self.get_image("wlt_user", record_pos=(-0.219, -0.344))

    def wlt_pwd(self):
        """万里通登录密码"""
        return self.get_image("wlt_pwd", record_pos=(-0.226, -0.219))

    def wlt_submit(self):
        """万里通登录登录提交按钮"""
        return self.get_image("wlt_login_button", record_pos=(-0.011, 0.016))

    @property
    def otp_login(self):
        """跳转otp登录页面"""
        return self.get_image("otp_login_button", record_pos=(-0.099, 0.163))
