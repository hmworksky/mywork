from pages.basePage import BasePages


class MailPage(BasePages):

    def __init__(self):
        super().__init__("mail")

    @property
    def delete_mail(self):
        """删除邮件"""
        return self.get_image("delete_mail")

    @property
    def mail_content(self):
        """邮件标题和内容，一般后台发送邮件后找邮件或点击用这个"""
        return self.get_image("mail_content")
