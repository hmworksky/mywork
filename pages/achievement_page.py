from pages.basePage import BasePages


class AchievementPage(BasePages):

    def __init__(self):
        super().__init__("achievement")

    @property
    def recruit_talent(self):
        """闯关达人按钮"""
        return self.get_image("recruit_talent", record_pos=(-0.27, -0.321))

    @property
    def receive(self):
        """成就领取按钮"""
        return self.get_image("receive", record_pos=(0.02, 0.314))

    @property
    def to_complete(self):
        """成就领取完前去完成按钮"""
        return self.get_image("to_complete", record_pos=(0.008, 0.316))

    @property
    def progress_sixteen(self):
        """成就领取完进度,初始8领取完后16"""
        return self.get_image("progress_sixteen", record_pos=(0.022, 0.144))


