from pages.basePage import BasePages


class HomePage(BasePages):

    def __init__(self):
        super().__init__("homepage")

    @property
    def start_app(self):
        """启动app"""
        return self.get_image("start_app", record_pos=(0.153, -0.777))

    @property
    def task(self):
        """任务按钮"""
        return self.get_image("task", record_pos=(-0.331, -0.456))

    @property
    def plot_mode(self):
        """剧情模式"""
        return self.get_image("plot_mode", record_pos=(-0.02, -0.24))

    @property
    def classic_mode(self):
        """经典模式"""
        return self.get_image("classic_mode", record_pos=(0.003, 0.056))

    @property
    def crazy_against(self):
        """经典模式"""
        return self.get_image("crazy_against", record_pos=(0.051, 0.274))

    @property
    def achievement(self):
        """成就"""
        return self.get_image("achievement", record_pos=(0.365, -0.213))

    @property
    def mail(self):
        """邮件"""
        return self.get_image("mail", record_pos=(0.358, -0.338))

    @property
    def share(self):
        """分享"""
        return self.get_image("share", record_pos=(0.37, -0.451))

    @property
    def skill(self):
        """技能"""
        return self.get_image("skill", record_pos=(-0.305, 0.694))

    @property
    def skin(self):
        """皮肤"""
        return self.get_image("skin", record_pos=(0.105, 0.686))

    @property
    def mall(self):
        """商城"""
        return self.get_image("mall", record_pos=(0.317, 0.687))

    @property
    def recharge(self):
        """分享"""
        return self.get_image("recharge", record_pos=(-0.333, -0.307))

    @property
    def buy_strength(self):
        """购买体力"""
        return self.get_image("buy_strength", record_pos=(-0.081, -0.094))

    @property
    def strength_change_button(self):
        """购买体力提交按钮"""
        return self.get_image("strength_change_button", record_pos=(0.001, 0.226))

    @property
    def strength_change_close(self):
        """购买体力关闭弹窗按钮"""
        return self.get_image("strength_change_close", record_pos=(0.306, -0.222))

    @property
    def strength_change_success(self):
        """购买体力成功提示"""
        return self.get_image("strength_change_success", record_pos=(-0.016, 0.026))

    @property
    def gold(self):
        """金币按钮"""
        return self.get_image("gold", record_pos=(0.24, -0.661))

    @property
    def joy_beans(self):
        """欢乐豆"""
        return self.get_image("joy_beans", record_pos=(0.003, -0.659))

    @property
    def rank(self):
        """排行榜"""
        return self.get_image("rank", record_pos=(-0.33, -0.159))

    @property
    def rank_num_one(self):
        """排行榜第一"""
        return self.get_image("rank_num_one", record_pos=(-0.247, -0.213))

    @property
    def wx_share(self):
        """微信分享"""
        return self.get_image("wx_share", record_pos=(-0.14, -0.203))

    @property
    def wx_login_title(self):
        """微信登录标题"""
        return self.get_image("wx_login_title", record_pos=(0.017, -0.59))

    @property
    def wx_user(self):
        """微信用户名"""
        return self.get_image("wx_user", record_pos=(-0.061, -0.397))

    @property
    def wx_pwd(self):
        """微信密码"""
        return self.get_image("wx_pwd", record_pos=(-0.115, -0.261))

    @property
    def wx_share_prize_title(self):
        """微信分享成功后奖励标题"""
        return self.get_image("wx_share_prize_title", record_pos=(0.006, -0.247))

    @property
    def share_success_doc(self):
        """分享成功回来后的弹层文案"""
        return self.get_image("share_success_doc", record_pos=(-0.022, 0.012))

    @property
    def share_success_confirm(self):
        """分享成功回来后的弹层确定按钮"""
        return self.get_image("share_success_confirm", record_pos=(-0.012, 0.185))

    @property
    def login_seven_flag(self):
        """第7天登录活动标识"""
        return self.get_image("login_seven_flag")

    @property
    def task_receive(self):
        """任务领取按钮"""
        return self.get_image("task_receive")

    @property
    def task_prize_title(self):
        """任务领取成功奖励标题"""
        return self.get_image("task_prize_title")
