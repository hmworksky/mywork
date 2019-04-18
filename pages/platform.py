from pages.basePage import BasePages


class PlatformStartPage(BasePages):

    def __init__(self):
        super().__init__("platform")

    def start_app(self):
        """启动app"""
        return self.get_image("start_app", record_pos=(0.153, -0.777))

    def search(self):
        """1768APP首页搜索框"""
        return self.get_image("search_input", record_pos=(0.07, -0.642))

    def search_button(self):
        """1768APP首页搜索按钮"""
        return self.get_image("search_button", record_pos=(0.153, -0.777))

    def enter_game(self):
        """1768APP搜索页赚欢乐值进入游戏按钮"""
        return self.get_image("enter_game", record_pos=(0.345, -0.45))

    @property
    def welfare_close(self):
        """平台首页超值福利关闭按钮"""
        return self.get_image("welfare_close", record_pos=(0.392, -0.609))

    @property
    def platform_back(self):
        """APP顶部返回"""
        return self.get_image("platform_back", record_pos=(-0.415, -0.77))

    @property
    def platform_home(self):
        """返回1768APP首页"""
        return self.get_image("platform_home", record_pos=(0.424, -0.765))

    @property
    def platform_refresh(self):
        """顶部刷新"""
        return self.get_image("platform_refresh", record_pos=(0.276, -0.769))


if __name__ == '__main__':
    p = BubbleStartPage()
    res = p.get_image("start")
    print(res)

