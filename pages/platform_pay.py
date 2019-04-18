from pages.basePage import BasePages


class PlatformPayPage(BasePages):

    def __init__(self):
        super().__init__("platform_pay")

    @property
    def diamond(self):
        """钻石支付"""
        return self.get_image("diamond", record_pos=(-0.39, 0.166))

    @property
    def pay_button(self):
        """支付按钮"""
        return self.get_image("pay_button", record_pos=(0.317, 0.703))

    @property
    def pay_success_doc(self):
        """支付弹层成功文案"""
        return self.get_image("pay_success_doc", record_pos=(0.078, -0.172))

    @property
    def pay_success_confirm(self):
        """支付成功确认"""
        return self.get_image("pay_success_confirm", record_pos=(0.008, 0.062))
