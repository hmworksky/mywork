from pages.basePage import BasePages


class OtpLoginPage(BasePages):

    def __init__(self):
        super().__init__("otp_login")

    @property
    def otp_input(self):
        """短信验证码输入框"""
        return self.get_image("otp_input", record_pos=(-0.169, -0.288))

    @property
    def phone_input(self):
        """手机号输入框"""
        return self.get_image("phone_input", record_pos=(-0.088, -0.454))

    @property
    def send_opt(self):
        """发送验证码"""
        return self.get_image("send_opt", record_pos=(0.294, -0.302))

    @property
    def otp_login_button(self):
        """OTP登录登录提交按钮"""
        return self.get_image("otp_login_button", record_pos=(-0.017, -0.063))

