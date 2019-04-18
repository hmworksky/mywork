from pages.basePage import BasePages


class BubbleStartPage(BasePages):

    def __init__(self):
        super().__init__("start")

    def play_game(self):
        """开始游戏"""
        return self.get_image("start", record_pos=(0.012, 0.512))

    @property
    def login(self):
        """登录"""
        return self.get_image("login", record_pos=(0.019, 0.515))
