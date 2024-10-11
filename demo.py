# encoding=utf-8

from airtest.core.api import *
from airtest.core.settings import *

# 需要设置几个常量:deviceid、屏幕分辨率(这里是1920*1080分辨率做参照)
deviceid = "emulator-5556"
resolution = (1280, 720)

auto_setup(devices=[
            f"Android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP"
            f"&&ori_method=MINICAPORI"
            f"&&touch_method=MAXTOUCH"
        ])


class Res:
    challenge_btn = Template(r"img/tpl1705393786480.png", record_pos=(0.405, 0.237), resolution=resolution)
    next_btn = Template(r"img/tpl1705394203127.png", record_pos=(0.197, 0.244), resolution=resolution)

    task_btn = Template(r"img/tpl1705650949967.png", record_pos=(-0.427, -0.159), resolution=resolution)
    main_task_btn = Template(r"img/tpl1705651266306.png", record_pos=(-0.427, -0.159), resolution=resolution)
    other_task_btn = Template(r"img/tpl1705651584086.png", record_pos=(-0.407, -0.092), resolution=resolution)
    day_task_btn = Template(r"img/tpl1705651674717.png", record_pos=(-0.408, -0.035), resolution=resolution)
    week_task_btn = Template(r"img/tpl1705651688297.png", record_pos=(-0.408, 0.02), resolution=resolution)

    receive_reward_btn = Template(r"img/tpl1705651327964.png", record_pos=(0.414, -0.034), resolution=resolution)

    # 玩法
    wanfa_btn = Template(r"img/tpl1705653060271.png", record_pos=(0.45, 0.058), resolution=resolution)
    fengraozhijian_btn = Template(r"img/tpl1728661026148.png", record_pos=(-0.226, -0.085), resolution=resolution)
    money_entry = Template(r"img/tpl1728661370929.png", record_pos=(-0.283, 0.02), resolution=resolution)
    quickly_fight = Template(r"img/tpl1728661514790.png", record_pos=(0.134, 0.231), resolution=resolution)
    confirm_tab = Template(r"img/tpl1728661645563.png", record_pos=(0.002, -0.001), resolution=resolution)
    agree_btn = Template(r"img/tpl1728661653449.png", record_pos=(0.146, 0.116), resolution=resolution)


class NarutoGame:

    def __init__(self):
        ST.OPDELAY = 1
        pass

    def next_level(self):
        """
        忍者考试下一关
        """
        while 1:
            try:
                if exists(Res.next_btn):
                    touch(Res.next_btn)
                    sleep(1)
            except Exception:
                pass

    def close(self):
        touch()

    def receive_task_reward(self):
        """
        领取任务奖励
        :return:
        """
        touch(Res.task_btn)
        rrb = Res.receive_reward_btn
        task_bts = [Res.main_task_btn, Res.other_task_btn, Res.day_task_btn, Res.week_task_btn]
        for b in task_bts:
            touch(b)
            while 1:
                if b == Res.other_task_btn or b == Res.week_task_btn:
                    times = 2
                    while times > 0:
                        # todo 这里是几个任务奖励的坐标，不同设备坐标可能不一致，下次优化成绝对坐标
                        touch((785, 970))
                        touch((1030, 970))
                        touch((1300, 970))
                        touch((1550, 970))
                        touch((1820, 970))
                        times -= 1
                if exists(rrb):
                    touch(rrb)
                else:
                    break

    def finish_big_reward(self):
        """
        完成丰饶之间
        :return:
        """
        touch(Res.wanfa_btn)
        touch(Res.fengraozhijian_btn)
        touch(Res.money_entry)
        for i in range(0, 2):
            touch(Res.quickly_fight)
            if exists(Res.agree_btn):
                touch(Res.agree_btn)
                touch((650, 550))


if __name__ == '__main__':
    ng = NarutoGame()
    ng.receive_task_reward()
