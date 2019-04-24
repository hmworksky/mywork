from pages.platform_pay import PlatformPayPage
from pages.homePage import HomePage
from pages.recharge_list import RechargeListPage
from airtest.core.api import *


class PayCtrl:
    """平台公共支付"""
    pay_page = PlatformPayPage()
    home = HomePage()
    recharge_list = RechargeListPage()

    def diamond_pay(self):
        """钻石支付"""
        # 选择钻石
        touch(self.pay_page.diamond)
        sleep(1)
        # 点击支付
        touch(self.pay_page.pay_button)
        sleep(1)
        # 点击确认
        touch(self.pay_page.pay_success_confirm)

    def open_gold_pay(self):
        """打开金币列表"""
        touch(self.home.joy_beans)

    def choice_amount(self, amount=1):
        """选择充值的金币"""
        if amount == 1:
            touch(self.recharge_list.one_yuan)
        sleep(0.5)

