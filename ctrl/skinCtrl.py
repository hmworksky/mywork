from pages.skin_page import SkinPage
from pages.homePage import HomePage

from airtest.core.api import *


class SkinCtrl:
    """皮肤"""
    skin = SkinPage()
    home = HomePage()

    def buy_bubble_skin(self, color="black"):
        color_list = {
            # 黑色泡泡
            "black": self.skin.black_bubble
        }
        color_template = color_list.get(color)
        # 打开皮肤页面
        touch(self.home.skin)

        # 选择切换至泡泡选项卡
        touch(self.skin.bubble_label)

        # 点击选择颜色泡泡
        touch(color_template)

        # 点击快速购买
        touch(self.skin.quick_buy_button)

        # 点击弹层的确认购买
        touch(self.skin.quick_confirm)
