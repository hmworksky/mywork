from unittest import TestCase
from airtest.core.api import *
from public.basePageImport import BubbleBasePage
from airtest.core.error import TargetNotFoundError
from ctrl.payCtrl import PayCtrl
from ctrl.playCtrl import PlayCtrl
from ctrl.shareCtrl import ShareCtrl
from ctrl.skinCtrl import SkinCtrl
from ctrl.skillCtrl import SkillCtrl


class BubbleBaseImport(TestCase, BubbleBasePage):
    """泡泡龙登录页面用例"""

    pay_ctrl = PayCtrl()
    play_ctrl = PlayCtrl()
    share_ctrl = ShareCtrl()
    skin_ctrl = SkinCtrl()
    skill_ctrl = SkillCtrl()

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
        # TODO 连接设备需要删掉
        connect_device("Android:///")
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
            touch(self.b.play_game)

    def tearDown(self):
        print('not in')
        touch(self.p.platform_refresh)
        # stop_app("com.pingan.gamehall")
        # clear_app("com.pingan.gamehall")



