from pages.basePage import BasePages


class PublicElementPage(BasePages):

    def __init__(self):
        super().__init__("public")

    @property
    def prize_title(self):
        """分享奖励标题"""
        return self.get_image("prize_title")

    @property
    def share_button(self):
        """分享按钮"""
        return self.get_image("share_button")

    @property
    def wx_share(self):
        """微信分享按钮"""
        return self.get_image("wx_share")

    @property
    def green_confirm(self):
        """绿色确定"""
        return self.get_image("green_confirm")

    @property
    def blue_confirm(self):
        """蓝色确定"""
        return self.get_image("blue_confirm")

    @property
    def close(self):
        """蓝色关闭按钮"""
        return self.get_image("close")
