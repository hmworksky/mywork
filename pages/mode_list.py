from pages.basePage import BasePages


class ModeListPage(BasePages):

    def __init__(self):
        super().__init__("mode_list")

    @property
    def primary_mode(self):
        """初级场"""
        return self.get_image("primary_mode", record_pos=(-0.18, 0.208))
