from pages.basePage import BasePages


class WxPage(BasePages):

    def __init__(self):
        super().__init__("weixin")

    @property
    def wx_fengsha(self):
        """微信好友风沙"""
        return self.get_image("wx_fengsha", record_pos=(-0.269, -0.281))

    @property
    def wx_share_button(self):
        """分享按钮"""
        return self.get_image("wx_share_button", record_pos=(0.203, 0.289))

    @property
    def wx_share_doc(self):
        """微信分享文案中泡泡龙文案"""
        return self.get_image("wx_share_doc", record_pos=(0.076, -0.065))

    @property
    def wx_share_status(self):
        """分享成功文案"""
        return self.get_image("wx_share_status", record_pos=(-0.001, -0.203))

    @property
    def back_app(self):
        """返回APP"""
        return self.get_image("back_app", record_pos=(-0.199, 0.189))
