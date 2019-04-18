from airtest.core.api import *
from cases.bubbleImport import BubbleBaseImport
from pages.homePage import HallPage
import pytesseract
from PIL import Image


class HomeCase(BubbleBaseImport):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.home = HallPage()

    def test_home_task_exists(self):
        """判断主页任务按钮是存在并且可以点击的"""
        self.assertTrue(exists(self.home.task))

        self.assertTrue(touch(self.home.task))

        sleep(30)

    def test_home_strength_exists(self):
        """查看主页购买体力按钮存在并且可点击"""
        self.assertTrue(exists(self.home.buy_strength))

        self.assertTrue(touch(self.home.buy_strength))
        sleep(30)

