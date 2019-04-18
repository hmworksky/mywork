from airtest.core.api import touch, text
from pages.passport_login import WltLoginPage
from pages.passportOtpPage import OtpLoginPage


class Login:
    w = WltLoginPage()
    o = OtpLoginPage()

    @classmethod
    def wlt_login(cls, username, pwd):
        """wlt登录"""
        touch(cls.w.wlt_label())
        touch(cls.w.wlt_user())
        text(username)
        touch(cls.w.wlt_pwd())
        text(pwd)
        touch(cls.w.wlt_submit())

    @classmethod
    def paw_login(cls):
        """平安玩登录"""
        pass

    @classmethod
    def opt_login(cls, phone_num, otp_num):
        """OTP登录"""

        # 点击跳转OTP登录页面
        touch(cls.w.otp_login)

        # 输入手机号
        touch(cls.o.phone_input)
        text(phone_num)

        # 输入验证码
        touch(cls.o.otp_input)
        text(otp_num)

        # 提交
        touch(cls.o.otp_login_button)
