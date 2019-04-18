from pages.basePage import BasePages


class PveGamingPage(BasePages):

    def __init__(self):
        super().__init__("pve_game")

    @property
    def guide_title(self):
        """16关引导文案"""
        return self.get_image("guide_title", record_pos=(-0.014, -0.417))

    @property
    def guide_start(self):
        """登录"""
        return self.get_image("guide_start", record_pos=(0.222, 0.462))

    @property
    def power_meter(self):
        """能量槽"""
        return self.get_image("power_meter", record_pos=(-0.383, 0.287))

    @property
    def light_item(self):
        """闪电道具"""
        return self.get_image("light_item", record_pos=(0.001, 0.689))

    @property
    def sixteen_launch_area(self):
        """16关可以点击的发射区域"""
        return self.get_image("sixteen_launch_area", record_pos=(0.282, 0.174))

    @property
    def quit_game(self):
        """退出游戏"""
        return self.get_image("quit_game", record_pos=(0.361, -0.645))

    @property
    def quit_confirm(self):
        """退出确认"""
        return self.get_image("quit_confirm", record_pos=(-0.139, 0.191))

    @property
    def quit_second_confirm(self):
        """退出二次确认"""
        return self.get_image("quit_second_confirm", record_pos=(-0.011, 0.156))

    @property
    def bubble_num(self):
        """十六关配置尽量不要动，+3道具之前是13，使用了之后是16，这里是16的数字"""
        return self.get_image("bubble_num", record_pos=(0.005, 0.501))

    @property
    def five_title(self):
        """+5道具购买确认弹框"""
        return self.get_image("five_title", record_pos=(0.03, -0.17))

    @property
    def five_first(self):
        """+5道具购买第一次确认"""
        return self.get_image("five_first", record_pos=(-0.028, 0.192))

    @property
    def five_second(self):
        """+5道具购买第二次确认"""
        return self.get_image("five_second", record_pos=(-0.026, 0.194))

    @property
    def five_three(self):
        """+5道具购买第三次确认"""
        return self.get_image("five_three", record_pos=(-0.03, 0.191))

    @property
    def restart_challenge(self):
        """重新挑战"""
        return self.get_image("restart_challenge", record_pos=(-0.011, 0.156))

    @property
    def five_num(self):
        """购买+5道具后，炮台泡泡数量5"""
        return self.get_image("five_num", record_pos=(0.006, 0.503))
