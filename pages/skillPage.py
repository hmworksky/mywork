from pages.basePage import BasePages


class SkillPage(BasePages):

    def __init__(self):
        super().__init__("skill")

    @property
    def tiger_skill(self):
        """老虎技能"""
        return self.get_image("tiger_skill", record_pos=(0.231, 0.519))

    @property
    def skill_quit(self):
        """叉叉"""
        return self.get_image("skill_quit", record_pos=(0.294, -0.247))

    @property
    def skill_confirm(self):
        """确定"""
        return self.get_image("skill_confirm", record_pos=(0.133, 0.249))

    @property
    def skill_cancel(self):
        """取消"""
        return self.get_image("skill_cancel", record_pos=(-0.163, 0.245))

    @property
    def permanent_activation(self):
        """永久激活"""
        return self.get_image("permanent_activation", record_pos=(0.197, -0.065))

    @property
    def buy_success_word(self):
        """购买成功"""
        return self.get_image("buy_success_word", record_pos=(-0.199, 0.001))

    @property
    def activation_three(self):
        """激活三天"""
        return self.get_image("activation_three", record_pos=(-0.192, -0.069))
