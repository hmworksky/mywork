from unittest import TestCase
from airtest.core.api import *
from ctrl.admin import AdminCtrl
from pages.start import BubbleStartPage
from public.login import Login
from pages.platform import PlatformStartPage
from pages.homePage import HomePage
from pages.skillPage import SkillPage
from pages.skin_page import SkinPage
from pages.check_point_page import CheckpointPage
from pages.pve_game_page import PveGamingPage
from pages.achievement_page import AchievementPage
from pages.recharge_list import RechargeListPage
from pages.platform_pay import PlatformPayPage
from airtest.core.error import TargetNotFoundError
from pages.mode_list import ModeListPage
from pages.pvp_gaming import PvpGamingPage
from pages.pvp_game_over import PvpGameOverPage
from pages.weixin import WxPage
from pages.mail import MailPage
from ctrl.payCtrl import PayCtrl
from ctrl.playCtrl import PlayCtrl


class BubbleBaseImport(TestCase):
    """泡泡龙登录页面用例"""

    p = PlatformStartPage()
    b = BubbleStartPage()
    login = Login()
    home = HomePage()
    skin = SkinPage()
    ck = CheckpointPage()
    pve_gaming = PveGamingPage()
    achievement = AchievementPage()
    skill = SkillPage()
    recharge_list = RechargeListPage()
    platform_pay = PlatformPayPage()
    mode_list = ModeListPage()
    pvp_gaming = PvpGamingPage()
    pvp_game_over = PvpGameOverPage()
    wx = WxPage()
    admin = AdminCtrl()
    mail = MailPage()
    pay_ctrl = PayCtrl()
    play_ctrl = PlayCtrl()

    @classmethod
    def setUpClass(cls):
        connect_device("Android:///")
        cls.back = keyevent("BACK")
        cls.first = False
        start_app("com.pingan.gamehall")
        cls.p.start_app()
        sleep(2.0)
        welfare_flag = exists(cls.p.welfare_close)
        if welfare_flag:
            touch(cls.p.welfare_close)
        sleep(1.5)
        touch(cls.p.search_button())
        sleep(1.0)
        touch(cls.p.search())
        text("熊猫泡泡龙")
        sleep(3)
        touch(cls.p.enter_game())
        sleep(12)

        login_flag = exists(cls.b.login)
        sleep(5)
        # 判断没有登录的话先登录
        if login_flag:
            print("####")
            try:
                touch(cls.b.login)
                sleep(5)
                cls.login.opt_login("13830000022", "111111")
            except TargetNotFoundError:
                pass
        else:
            touch(cls.b.play_game)
        sleep(30)
        cls.first = True
        cls.user_id = "2038983941"

    def setUp(self):
        if self.first:
            pass
        else:
            login_flag = exists(self.b.login)
            # 判断没有登录的话先登录
            if login_flag:
                print("################")
                res = exists(self.b.login)
                print(res)
                touch(self.b.login)
                sleep(5)
                try:
                    self.login.opt_login("13830000022", "111111")
                except TargetNotFoundError:
                    pass
            else:
                touch(self.b.play_game())
            sleep(30)
            self.first = False

    def tearDown(self):
        print('not in')
        touch(self.p.platform_refresh)
        # stop_app("com.pingan.gamehall")
        # clear_app("com.pingan.gamehall")



