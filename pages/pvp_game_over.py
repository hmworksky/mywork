from pages.basePage import BasePages


class PvpGameOverPage(BasePages):

    def __init__(self):
        super().__init__("pvp_game_over")

    @property
    def lose_doc(self):
        """PVP游戏结束战局结算弹层失败文案"""
        return self.get_image("lose_doc", record_pos=(-0.242, -0.205))

    @property
    def rematch(self):
        """重新匹配"""
        return self.get_image("rematch", record_pos=(-0.192, 0.714))

    @property
    def settle_confirm(self):
        """PVP战局结算弹层确认按钮"""
        return self.get_image("settle_confirm", record_pos=(-0.003, 0.391))

    @property
    def share(self):
        """PVP结算页面分享按钮"""
        return self.get_image("share", record_pos=(0.338, 0.609))

    @property
    def go_back(self):
        """结算页面返回"""
        return self.get_image("go_back", record_pos=(-0.351, -0.647))
