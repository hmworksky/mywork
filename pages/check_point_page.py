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

    @property
    def chapter_lock(self):
        """章节锁标识"""
        return self.get_image("chapter_lock")

    @property
    def chapter_unlock_button(self):
        """章节解锁解锁按钮"""
        return self.get_image("chapter_unlock_button")

    @property
    def get_more_star(self):
        """章节解锁弹层获得更多星按钮"""
        return self.get_image("get_more_star")

    @property
    def chapter_unlock_share(self):
        """章节解锁分享按钮"""
        return self.get_image("chapter_unlock_share")

    @property
    def flaunt(self):
        """闯关成功炫耀"""
        return self.get_image("flaunt")

    @property
    def success_close(self):
        """闯关成功关闭按钮"""
        return self.get_image("success_close")

    @property
    def success_pass(self):
        """PVE成功过关文案"""
        return self.get_image("success_pass")

    @property
    def try_again(self):
        """闯关成功再试一次按钮"""
        return self.get_image("try_again")

