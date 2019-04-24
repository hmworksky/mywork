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

from pages.mode_list import ModeListPage
from pages.pvp_gaming import PvpGamingPage
from pages.pvp_game_over import PvpGameOverPage
from pages.weixin import WxPage
from pages.mail import MailPage


class BubbleBasePage:
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
