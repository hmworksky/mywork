from unittest import TestCase
from airtest.core.api import *
from pages.start import BubbleStartPage
from public.login import Login
from pages.platform import PlatformStartPage
from airtest.core.error import TargetNotFoundError


class BubbleBaseImport(TestCase):
    """泡泡龙登录页面用例"""

    # def exists(self):
    #     exists

    @classmethod
    def setUpClass(cls):
        connect_device("Android:///")
        cls.p = PlatformStartPage()
        cls.b = BubbleStartPage()
        cls.login = Login()
        cls.back = keyevent("BACK")
        cls.first = False
        start_app("com.pingan.gamehall")

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
            touch(cls.b.play_game())
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



