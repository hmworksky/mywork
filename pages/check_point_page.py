from pages.basePage import BasePages


class CheckpointPage(BasePages):

    def __init__(self):
        super().__init__("checkpoint")

    @property
    def checkpoint_sixteen(self):
        """关卡十六图标"""
        return self.get_image("checkpoint_sixteen", record_pos=(0.012, 0.512))

    @property
    def add_three(self):
        """+3道具"""
        return self.get_image("add_three", record_pos=(0.026, -0.069))

    @property
    def start_game(self):
        """开始游戏"""
        return self.get_image("start_game", record_pos=(0.028, 0.16))

    @property
    def national_rank(self):
        """全国排行"""
        return self.get_image("national_rank", record_pos=(-0.27, 0.587))

    @property
    def friend_rank(self):
        """好友排行"""
        return self.get_image("friend_rank", record_pos = (-0.269, 0.401))

    @property
    def num_one(self):
        """第一标识"""
        return self.get_image("num_one", record_pos=(-0.16, 0.344))

    @property
    def friend_face(self):
        """好友头像"""
        return self.get_image("friend_face", record_pos=(-0.072, 0.343))


