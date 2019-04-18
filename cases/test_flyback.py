from airtest.core.api import *
from cases.bubbleImport import BubbleBaseImport


class HomeCase(BubbleBaseImport):

    def tearDown(self):
        pass

    def test_complete_task(self):
        """领取一次任务奖励"""
        pass
        # self.home.task

    def test_buy_once_strength(self):
        """购买一次体力"""
        # 点击体力按钮
        touch(self.home.buy_strength)
        # 弹框中点击购买
        touch(self.home.strength_change_button)
        sleep(1)

        # 判断购买成功与否
        success_flag = exists(self.home.strength_change_success)
        self.assertTrue(success_flag)
        # 关闭弹层
        touch(self.home.strength_change_close)

    def test_buy_skill(self):
        """购买一次技能"""
        touch(self.home.skill)
        # 选中老虎技能
        touch(self.skill.tiger_skill)
        # 点击激活3天
        touch(self.skill.activation_three)
        # 点击确定购买
        touch(self.skill.skill_confirm)
        sleep(2)
        buy_skill_status = exists(self.skill.buy_success_word)
        self.assertTrue(buy_skill_status)
        # 点击确认激活
        touch(self.skill.skill_confirm)

    def test_buy_skin(self):
        """购买一次皮肤"""
        touch(self.home.skin)
        sleep(1)
        # 切换至泡泡栏
        touch(self.skin.bubble_label)

        # TODO

    def test_buy_flash_sales(self):
        """购买一次限时特惠"""
        pass

    def test_complete_new_guide(self):
        """完成新手指引"""
        pass

    def test_pve_confirm(self):
        """完成一次pve闯关"""
        # 进入关卡
        touch(self.home.plot_mode)
        sleep(2)
        # 选择关卡
        touch(self.ck.checkpoint_sixteen)
        # 开始游戏
        touch(self.ck.start_game)
        sleep(20)
        guide_flag = exists(self.pve_gaming.guide_title)
        if guide_flag:
            touch(self.pve_gaming.guide_start)

        # 回收一次能量
        touch(self.pve_gaming.power_meter)

        # 发射一次泡泡
        touch(self.pve_gaming.sixteen_launch_area)

        # 使用一次闪电道具
        touch(self.pve_gaming.light_item)
        touch(self.pve_gaming.sixteen_launch_area)

        # 退出游戏
        touch(self.pve_gaming.quit_game)
        touch(self.pve_gaming.quit_confirm)
        touch(self.pve_gaming.quit_second_confirm)
        sleep(3)

    def test_pve_chapter_unlock(self):
        """完成章节解锁"""
        pass

    def test_receive_mail(self):
        """领取一封邮件"""
        pass

    def test_buy_add_three_item(self):
        """购买+3道具成功"""
        # 进入关卡
        touch(self.home.plot_mode)
        sleep(2)
        # 选择关卡
        touch(self.ck.checkpoint_sixteen)
        # 购买+3
        touch(self.ck.add_three)
        # 开始游戏
        touch(self.ck.start_game)
        sleep(20)
        # 先点掉战斗开始指引
        guide_flag = exists(self.pve_gaming.guide_title)
        if guide_flag:
            touch(self.pve_gaming.guide_start)

        bubble_num_is_sixteen = exists(self.pve_gaming.bubble_num)
        # 判断+3道具是否购买成功
        self.assertTrue(bubble_num_is_sixteen)

    def test_game_over_buy_add_five_item(self):
        """游戏结束购买三次+5道具成功"""

        # 进入关卡
        touch(self.home.plot_mode)
        sleep(2)

        # 选择关卡
        touch(self.ck.checkpoint_sixteen)

        # 开始游戏
        touch(self.ck.start_game)
        sleep(20)
        guide_flag = exists(self.pve_gaming.guide_title)
        if guide_flag:
            touch(self.pve_gaming.guide_start)

        # 循环打泡泡，发现+5道具的弹层标题则继续发送
        five_title_flag = exists(self.pve_gaming.five_title)
        while not five_title_flag:
            touch(self.pve_gaming.sixteen_launch_area)
            five_title_flag = exists(self.pve_gaming.five_title)

            if five_title_flag:
                touch(self.pve_gaming.five_first)
                sleep(1.5)

        # 判断炮台还有5个泡泡
        five_num_flag = exists(self.pve_gaming.five_num)
        self.assertTrue(five_num_flag)

        # 退出游戏
        touch(self.pve_gaming.quit_game)
        touch(self.pve_gaming.quit_confirm)
        touch(self.pve_gaming.quit_second_confirm)
        sleep(3)

    def test_receive_achievement(self):
        """领取一次成就"""
        touch(self.home.achievement)
        sleep(1)
        touch(self.achievement.recruit_talent)
        sleep(1)
        touch(self.achievement.receive)
        sleep(1)
        progress_flag = exists(self.achievement.progress_sixteen)
        receive_flag = exists(self.achievement.to_complete)
        self.assertTrue(any([progress_flag, receive_flag]))

    def test_complete_sign_activity(self):
        """完成一次签到活动"""
        pass

    def test_jump_platform_recharge(self):
        """金币充值成功"""
        # 点击金币充值按钮
        touch(self.home.gold)
        sleep(0.5)
        # 点击充值一元
        touch(self.recharge_list.one_yuan)

        # 选择钻石支付
        touch(self.platform_pay.diamond)
        touch(self.platform_pay.pay_button)
        sleep(1)
        # 判断是否有支付成功的文案
        success_flag = exists(self.platform_pay.pay_success_doc)
        self.assertTrue(success_flag)
        sleep(2)
        # 点击确认，返回游戏首页
        touch(self.platform_pay.pay_success_confirm)
        # 要加载首页所以等待时间较长。。。
        sleep(10)
        # 确认返回了首页,看下排行按钮在不在
        rank_flag = exists(self.home.rank)
        self.assertTrue(rank_flag)

    def test_rank(self):
        """排行榜有数据显示"""
        touch(self.home.rank)
        sleep(1.5)
        num_one_flag = exists(self.home.rank_num_one)
        self.assertTrue(num_one_flag)

    def test_classic_mode(self):
        """完成一次经典模式战斗"""
        # 点击经典模式
        touch(self.home.classic_mode)
        # 加载有点慢，稍微等待下
        sleep(5)
        touch(self.mode_list.primary_mode)
        flag = True
        try:
            wait(self.pvp_gaming.is_gaming_flag, timeout=60)
            # 先使用一次道具
            touch(self.pvp_gaming.remove_one_row_item)
            # 再发射一次泡泡
            touch(self.pvp_gaming.launch_area)
        except TargetNotFoundError:
            flag = False
        self.assertTrue(flag)

        # 退出游戏,避免复盘弹层，影响其它
        touch(self.pvp_gaming.quit)
        sleep(1)
        touch(self.pvp_gaming.quit_first_confirm)
        sleep(1)
        touch(self.pvp_gaming.quit_second_confirm)
        sleep(5)

        # 发现有结算弹层就先点确认
        lose_flag = exists(self.pvp_game_over.lose_doc)
        if lose_flag:
            touch(self.pvp_game_over.settle_confirm)
        sleep(1)

        touch(self.pvp_game_over.go_back)
        print("####")

    def test_crazy_mode(self):
        """完成一次疯狂模式战斗"""
        # 点击经典模式
        touch(self.home.crazy_against)
        # 加载有点慢，稍微等待下
        sleep(5)
        touch(self.mode_list.primary_mode)
        flag = True
        try:
            wait(self.pvp_gaming.is_gaming_flag, timeout=60)
            # 先使用一次道具
            touch(self.pvp_gaming.remove_one_row_item)
            # 再发射一次泡泡
            touch(self.pvp_gaming.launch_area)
        except TargetNotFoundError:
            flag = False
        self.assertTrue(flag)

        # 退出游戏,避免复盘弹层，影响其它
        touch(self.pvp_gaming.quit)
        sleep(0.5)
        touch(self.pvp_gaming.quit_first_confirm)
        sleep(0.5)
        touch(self.pvp_gaming.quit_second_confirm)
        sleep(5)

        # 发现有结算弹层就先点确认
        lose_flag = exists(self.pvp_game_over.lose_doc)
        if lose_flag:
            touch(self.pvp_game_over.settle_confirm)
        sleep(1)

        touch(self.pvp_game_over.go_back)

    def test_pvp_rematch(self):
        """PVP再战一场"""
        wait(self.home.rank, timeout=30)

        # 点击经典模式
        touch(self.home.classic_mode)
        # 加载有点慢，稍微等待下
        sleep(5)
        touch(self.mode_list.primary_mode)
        flag = True
        try:
            wait(self.pvp_gaming.is_gaming_flag, timeout=60)
            # 先使用一次道具
            touch(self.pvp_gaming.remove_one_row_item)
            # 再发射一次泡泡
            touch(self.pvp_gaming.launch_area)
        except TargetNotFoundError:
            flag = False
        self.assertTrue(flag)

        # 退出游戏
        touch(self.pvp_gaming.quit)
        sleep(1)
        touch(self.pvp_gaming.quit_first_confirm)
        sleep(1)
        touch(self.pvp_gaming.quit_second_confirm)
        sleep(10)

        # 发现有结算弹层就先点确认
        lose_flag = exists(self.pvp_game_over.lose_doc)
        if lose_flag:
            touch(self.pvp_game_over.settle_confirm)

        # 点击重新匹配
        touch(self.pvp_game_over.rematch)

        flag = True
        try:
            wait(self.pvp_gaming.is_gaming_flag, timeout=60)
        except TargetNotFoundError:
            flag = False
        self.assertTrue(flag)

        # 再次退出，避免复盘
        touch(self.pvp_gaming.quit)
        sleep(1)
        touch(self.pvp_gaming.quit_first_confirm)
        sleep(1)
        touch(self.pvp_gaming.quit_second_confirm)
        sleep(5)

        # 发现有结算弹层就先点确认
        lose_flag = exists(self.pvp_game_over.lose_doc)
        if lose_flag:
            touch(self.pvp_game_over.settle_confirm)
        touch(self.pvp_game_over.go_back)

    def test_buy_gold(self):
        """余额充值"""
        wait(self.home.rank, timeout=30)
        touch(self.home.joy_beans)
        sleep(3)
        touch(self.recharge_list.amount_input)
        sleep(1)
        touch(self.recharge_list.key_one)
        sleep(1)
        touch(self.recharge_list.key_confirm)
        sleep(0.5)
        touch(self.recharge_list.recharge_buy_button)
        # 使用钻石购买
        sleep(3)
        touch(self.platform_pay.diamond)
        sleep(1)
        touch(self.platform_pay.pay_button)
        sleep(2)
        success_flag = exists(self.platform_pay.pay_success_doc)
        sleep(1)
        touch(self.platform_pay.pay_success_confirm)
        sleep(8)
        home_flag = exists(self.home.rank)
        self.assertTrue(all([success_flag, home_flag]))

    def test_pvp_egg_receive(self):
        """PVP彩蛋领取"""
        # todo 需要修改后台配置以及机器人使用道具频率
        pass

    def test_gold_auto_replenished(self):
        """金币自动补足"""
        # todo 需要先调用扣除金币接口
        pass

    def test_home_page_share(self):
        """主页面分享"""
        wait(self.home.share, timeout=30)
        touch(self.home.share)
        sleep(3)
        touch(self.home.wx_share)
        sleep(1)
        wait(self.home.wx_login_title)
        touch(self.home.wx_user)
        text("2875057261")
        sleep(2)
        touch(self.home.wx_pwd)
        text("test1324")



    def test_pvp_settlement_share(self):
        """PVP胜利结算分享"""
        pass

    def test_sign_three_day_share(self):
        """签到7天分享"""
        pass

    def test_buy_skill_share(self):
        """激活技能分享"""
        pass

    def test_buy_bubble_skin_share(self):
        """购买泡泡皮肤分享"""
        pass

    def test_pvp_egg_share(self):
        """PVP彩蛋分享"""
        pass

    def test_pve_pass_share(self):
        """PVE过关分享"""
        pass
