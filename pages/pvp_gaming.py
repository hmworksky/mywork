from pages.basePage import BasePages


class PvpGamingPage(BasePages):

    def __init__(self):
        super().__init__("pvp_gaming")

    @property
    def is_gaming_flag(self):
        """有彩蛋奖励字样代表在游戏中了"""
        return self.get_image("is_gaming_flag", record_pos=(0.144, -0.54))

    @property
    def launch_area(self):
        """发射区域"""
        return self.get_image("launch_area", record_pos=(0.008, 0.439))

    @property
    def remove_one_row_item(self):
        """消除一排道具"""
        return self.get_image("remove_one_row_item", record_pos=(0.203, 0.678))

    @property
    def quit(self):
        """退出游戏"""
        return self.get_image("quit", record_pos=(0.37, -0.663))

    @property
    def quit_first_confirm(self):
        """pvp游戏中退出游戏第一次确认"""
        return self.get_image("quit_first_confirm", record_pos=(-0.005, -0.053))

    @property
    def quit_second_confirm(self):
        """pvp游戏中退出游戏二次确认"""
        return self.get_image("quit_second_confirm", record_pos=(0.17, 0.194))

