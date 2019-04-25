from airtest.core.api import *
from public.basePageImport import BubbleBasePage


class ShareCtrl(BubbleBasePage):
    """游戏分享"""
    def __init__(self):
        pass

    def wx_share(self):
        """微信分享"""
        # 点击微信按钮
        touch(self.home.wx_share)
        # 稍微等待下，点击风沙 TODO 这里要添加判断微信是否登录逻辑,暂且认为已登录微信
        sleep(3)
        touch(self.wx.wx_fengsha)
        # 弹出分享框中点击分享
        touch(self.wx.wx_share_button)
        sleep(0.5)
        # 点击返回1768
        touch(self.wx.back_app)

    def open_homepage_share(self):
        """打开首页分享"""
        wait(self.home.share, timeout=30)
        touch(self.home.share)
        sleep(3)

    def is_success_share(self):
        """微信是否分享成功"""
        success_flag = exists(self.home.share_success_doc)
        success_title = exists(self.pub.prize_title)
        return any([success_flag, success_title])

    def wx_friend_share(self):
        """微信朋友圈分享"""
        pass


if __name__ == '__main__':
    wx = ShareCtrl()
    wx.open_homepage_share()
