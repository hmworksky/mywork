from unittest import TestCase
from airtest.core.api import *
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


class BubbleBaseImport(TestCase):
    """泡泡龙登录页面用例"""

    @classmethod
    def load_page(cls):
        cls.p = PlatformStartPage()
        cls.b = BubbleStartPage()
        cls.login = Login()
        cls.home = HomePage()
        cls.skin = SkinPage()
        cls.ck = CheckpointPage()
        cls.pve_gaming = PveGamingPage()
        cls.achievement = AchievementPage()
        cls.skill = SkillPage()
        cls.recharge_list = RechargeListPage()
        cls.platform_pay = PlatformPayPage()
        cls.mode_list = ModeListPage()
        cls.pvp_gaming = PvpGamingPage()
        cls.pvp_game_over = PvpGameOverPage()
        cls.wx = WxPage()

    @classmethod
    def setUpClass(cls):
        connect_device("Android:///")
        cls.back = keyevent("BACK")
        cls.first = False
        start_app("com.pingan.gamehall")
        cls.load_page()
        cls.p.start_app()
        sleep(2.0)
        if exists(cls.p.welfare_close):
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



