from pages.skillPage import SkillPage
from pages.homePage import HomePage

from airtest.core.api import *


class SkillCtrl:
    """技能"""
    skill = SkillPage()
    home = HomePage()

    def active_skill(self, skill_type="tiger"):
        """购买道具+激活技能"""
        skill_list = {
            # 黑色泡泡
            "tiger": self.skill.tiger_skill
        }
        skill_template = skill_list.get(skill_type)

        # 购买技能
        self.buy_skill_item(skill_template)

        sleep(3)

        # 确认激活
        touch(self.skill.skill_confirm)

    def buy_skill_item(self, skill_template):
        """购买技能道具"""
        # 打开技能页面
        touch(self.home.skill)
        sleep(2)

        # 选择老虎激活
        touch(skill_template)
        sleep(3)
        # 点击激活3天
        touch(self.skill.activation_three)
        sleep(3)
        # 确定
        touch(self.skill.skill_confirm)
        sleep(3)
        # 再次点确定
        touch(self.skill.skill_confirm)
