from pages.homePage import HomePage
from pages.check_point_page import CheckpointPage
from pages.pve_game_page import PveGamingPage
from pages.pvp_gaming import PvpGamingPage
from pages.pvp_game_over import PvpGameOverPage
from pages.mode_list import ModeListPage
from airtest.core.api import *


class PlayCtrl:
    """游戏相关控制层"""
    home = HomePage()
    checkpoint = CheckpointPage()
    pve_gaming = PveGamingPage()
    pvp_gaming = PvpGamingPage()
    mode_list = ModeListPage()
    pvp_game_over = PvpGameOverPage()

    def in_pve_game(self, is_add_three=False):
        """进入pve游戏页面"""
        # 进入关卡
        touch(self.home.plot_mode)
        sleep(2)
        # 选择关卡
        touch(self.checkpoint.checkpoint_sixteen)

        # 判断是否+3
        if is_add_three:
            # 点击购买购买+3
            touch(self.checkpoint.add_three)

        # 开始游戏
        touch(self.checkpoint.start_game)
        sleep(20)
        guide_flag = exists(self.pve_gaming.guide_title)
        if guide_flag:
            touch(self.pve_gaming.guide_start)

    def pve_foreach_use_item(self):
        """循环使用道具"""
        # TODO 这里要初始化很多道具，或者做购买道具的操作
        success_flag = exists(self.checkpoint.success_pass)
        while not success_flag:
            touch(self.pve_gaming.light_item)
            sleep(0.5)

            touch(self.pve_gaming.sixteen_launch_area)
            success_flag = exists(self.checkpoint.success_pass)

    def pve_foreach_send_bubble(self, used_item=False):
        """循环打泡泡，发现+5道具的弹层标题则继续发送"""

        five_title_flag = exists(self.pve_gaming.five_title)
        while not five_title_flag:
            # 判断是否使用道具
            if used_item:
                touch(self.pve_gaming.light_item)
                sleep(0.5)

            touch(self.pve_gaming.sixteen_launch_area)
            five_title_flag = exists(self.pve_gaming.five_title)

            if five_title_flag:
                touch(self.pve_gaming.five_first)
                sleep(1.5)

    def play_win_pve(self):
        """pve游戏胜利"""
        # 先进入游戏
        self.in_pve_game()

        # 循环使用道具
        self.pve_foreach_use_item()

    def play_win_pvp(self):
        """pvp游戏胜利"""
        # 先进入游戏
        self.in_classic_mode()

        # 循环使用消除一排道具
        self.pvp_foreach_use_item()

    def pvp_foreach_use_item(self):
        """循环使用消除一排道具"""

        success_flag = exists(self.pvp_game_over.rematch)
        while not success_flag:
            touch(self.pvp_gaming.remove_one_row_item)
            sleep(0.5)
            success_flag = exists(self.checkpoint.success_pass)

    def quit_pve(self):
        """PVE游戏中退出"""
        touch(self.pve_gaming.quit_game)
        touch(self.pve_gaming.quit_confirm)
        touch(self.pve_gaming.quit_second_confirm)
        sleep(3)

    def quit_pvp(self):
        """PVP退出游戏"""
        # 退出游戏,避免复盘弹层，影响其它
        touch(self.pvp_gaming.quit)
        sleep(1)
        touch(self.pvp_gaming.quit_first_confirm)
        sleep(1)
        touch(self.pvp_gaming.quit_second_confirm)
        sleep(5)

    def in_classic_mode(self):
        """进入经典模式初级场"""
        # 点击经典模式
        touch(self.home.classic_mode)
        # 加载有点慢，稍微等待下
        sleep(5)
        touch(self.mode_list.primary_mode)

    def in_crazy_mode(self):
        """进入疯狂模式初级场"""
        # 点击经典模式
        touch(self.home.crazy_against)
        # 加载有点慢，稍微等待下
        sleep(5)
        touch(self.mode_list.primary_mode)

