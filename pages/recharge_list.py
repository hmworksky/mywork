from pages.basePage import BasePages


class RechargeListPage(BasePages):

    def __init__(self):
        super().__init__("recharge_list")

    @property
    def one_yuan(self):
        """金币充值一元"""
        return self.get_image("one_yuan", record_pos=(0.256, -0.319))

    @property
    def amount_input(self):
        """余额充值输入框"""
        return self.get_image("amount_input", record_pos=(-0.265, 0.549))

    @property
    def key_one(self):
        """键盘1"""
        return self.get_image("key_one", record_pos=(-0.392, 0.458))

    @property
    def key_confirm(self):
        """键盘确定"""
        return self.get_image("key_confirm", record_pos=(0.392, 0.52))

    @property
    def recharge_buy_button(self):
        """余额充值购买按钮"""
        return self.get_image("recharge_buy_button", record_pos=(-0.01, 0.685))
