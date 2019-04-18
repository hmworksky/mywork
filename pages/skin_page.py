from pages.basePage import BasePages


class SkinPage(BasePages):

    def __init__(self):
        super().__init__("skin")

    @property
    def bubble_label(self):
        """泡泡标签"""
        return self.get_image("bubble_label", record_pos=(-0.33, -0.265))

    @property
    def black_bubble(self):
        """黑色泡泡"""
        return self.get_image("black_bubble", record_pos=(0.228, 0.494))

    @property
    def quick_buy_button(self):
        """快速购买"""
        return self.get_image("quick_buy_button", record_pos=(0.045, -0.026))

    @property
    def quick_confirm(self):
        """快速购买确定"""
        return self.get_image("quick_confirm", record_pos=(0.135, 0.249))

    @property
    def prize_confirm(self):
        """奖励弹框确定"""
        return self.get_image("prize_confirm", record_pos=(-0.224, 0.489))




