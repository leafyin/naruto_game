# encoding=utf-8
from datetime import datetime

from airtest.core.api import *
from airtest.core.error import *
from airtest.core.settings import *

ST.OPDELAY = 1
resolution = (1280, 720)


challenge_btn = Template(r"img/tpl1705393786480.png", record_pos=(0.405, 0.237), resolution=resolution)
next_btn = Template(r"img/tpl1705394203127.png", record_pos=(0.197, 0.244), resolution=resolution)

task_btn = Template(r"img/tpl1705650949967.png", record_pos=(-0.427, -0.159), resolution=resolution)
main_task_btn = Template(r"img/tpl1705651266306.png", record_pos=(-0.427, -0.159), resolution=resolution)
other_task_btn = Template(r"img/tpl1705651584086.png", record_pos=(-0.407, -0.092), resolution=resolution)
day_task_btn = Template(r"img/tpl1705651674717.png", record_pos=(-0.408, -0.035), resolution=resolution)
week_task_btn = Template(r"img/tpl1705651688297.png", record_pos=(-0.408, 0.02), resolution=resolution)

# 玩法
wanfa_btn = Template(r"img/tpl1705653060271.png")
fengraozhijian_btn = Template(r"img/tpl1728661026148.png")
money_entry = Template(r"img/tpl1728661370929.png")
exp_entry = Template(r"img/tpl1728951290763.png")
vision_entry = Template(r"img/tpl1729132985504.png")

reward_entry = Template(r"img/tpl1728948837371.png")

quickly_fight = Template(r"img/tpl1728661514790.png", record_pos=(0.134, 0.231), resolution=resolution)

# 主页
main_duihuan_btn = Template(r"img/tpl1728691142644.png")
main_fuli_btn = Template(r"img/tpl1728737903016.png")

free_refresh_btn = Template(r"img/tpl1728693507109.png", record_pos=(0.365, 0.235), resolution=resolution)

week_reward_tab = Template(r"img/tpl1728738062720.png", record_pos=(-0.413, 0.019), resolution=resolution)
get_energy_tab = Template(r"img/tpl1728740006743.png", record_pos=(-0.412, -0.041), resolution=resolution)

# 浮动按钮
sign_entry = Template(r"img/tpl1728937306250.png")

# 通用按钮，这些按钮通常不需要给定坐标，通过图像识别去点击
accept_btn = Template(r"img/tpl1728937718836.png")
confirm_btn = Template(r"img/tpl1728693845195.png")

receive_reward_btn = Template(r"img/tpl1705651327964.png")
exchange_btn = Template(r"img/tpl1728691620710.png")
agree_btn = Template(r"img/tpl1728661653449.png")
onekey_receive_btn = Template(r"img/tpl1728948614242.png")

close_btn = Template(r"img/tpl1728949714777.png")


def touch_(t):
    # 捕获一些常见的异常，确保不会出错
    try:
        sleep(1)
        touch(t)
    except TargetNotFoundError as e:
        print(e.value)
        pass


def relative_position(xy: tuple, resolution_: tuple):
    """
    计算相对位置
    :param xy: 绝对坐标
    :param resolution_: 分辨率
    :return tuple: 相对坐标
    """
    return round(xy[0] / resolution_[0], 2), round(xy[1] / resolution_[1], 2)


def close(t):
    """
    关闭按钮
    1 = float window
    2 = panel window
    3 = small float window
    :return:
    """
    sleep(1)
    close1_pos = relative_position((1200, 40), resolution)
    close2_pos = relative_position((1240, 30), resolution)
    close3_pos = relative_position((1045, 100), resolution)
    if t == 1:
        touch_(close1_pos)
    if t == 2:
        touch_(close2_pos)
    if t == 3:
        # 小窗口
        touch_(close3_pos)


def onekey_finish():
    """
    一键操作
    :return:
    """
    sign()
    money_reward()
    exp_reward()
    vision_reward()
    pass


def sign():
    """
    每日签到
    :return:
    """
    touch_(sign_entry)
    touch_((0.5, 0.5))
    touch_(accept_btn)
    touch_(confirm_btn)
    close(1)


def get_energy():
    """
    领取体力
    :return:
    """
    touch_(main_fuli_btn)
    touch_(get_energy_tab)

    touch_(receive_reward_btn)
    touch_(receive_reward_btn)
    touch_(receive_reward_btn)
    close(2)
    pass


def next_level():
    """
    忍者考试下一关
    """
    while 1:
        touch_(next_btn)


def buy_coin_stuff():
    """
    购买兑换页面中的铜币货物
    :return:
    """
    y = 280
    pos1 = relative_position((400, y), resolution)
    pos2 = relative_position((600, y), resolution)
    pos3 = relative_position((840, y), resolution)
    print(f"{pos1}-{pos2}-{pos3}")
    touch_(main_duihuan_btn)
    for i in range(0, 2):
        # 第一个免费商品
        touch_(pos1)
        touch_(exchange_btn)
        # 第二个免费商品
        touch_(pos2)
        touch_(exchange_btn)
        # 第三个免费商品
        touch_(pos3)
        touch_(exchange_btn)
        # 免费刷新
        touch_(free_refresh_btn)
        touch_(confirm_btn)
    close(1)


def receive_task_reward():
    """
    领取任务奖励
    :return:
    """
    touch_(task_btn)
    rrb = receive_reward_btn
    task_bts = [main_task_btn, other_task_btn, day_task_btn, week_task_btn]
    for b in task_bts:
        touch_(b)
        while 1:
            if b == other_task_btn or b == week_task_btn:
                times = 2
                while times > 0:
                    touch_((785, 970))
                    touch_((1030, 970))
                    touch_((1300, 970))
                    touch_((1550, 970))
                    touch_((1820, 970))
                    times -= 1
            if exists(rrb):
                touch_(rrb)
            else:
                break


def money_reward():
    """
    赏金
    :return:
    """
    touch_(wanfa_btn)
    touch_(fengraozhijian_btn)
    touch_(money_entry)
    r_pos = relative_position((650, 550), resolution)
    for i in range(0, 2):
        sleep(1)
        touch_(quickly_fight)
        if exists(agree_btn):
            touch_(agree_btn)
            sleep(1)
            touch_(r_pos)
    touch_(reward_entry)
    touch_(onekey_receive_btn)
    sleep(1)
    touch_(r_pos)
    close(3)
    close(2)
    close(2)


def exp_reward():
    """
    经验
    :return:
    """
    touch_(wanfa_btn)
    touch_(fengraozhijian_btn)
    touch_(exp_entry)
    r_pos = relative_position((650, 550), resolution)
    for i in range(0, 2):
        sleep(1)
        touch_(quickly_fight)
        if exists(agree_btn):
            touch_(agree_btn)
            sleep(1)
            touch_(r_pos)
    touch_(reward_entry)
    touch_(onekey_receive_btn)
    sleep(1)
    touch_(r_pos)
    close(3)
    close(2)
    close(2)


def vision_reward():
    """
    幻想奖励
    :return:
    """
    touch_(wanfa_btn)
    touch_(fengraozhijian_btn)
    touch_(vision_entry)
    r_pos = relative_position((650, 550), resolution)
    for i in range(0, 2):
        sleep(1)
        touch_(quickly_fight)
        if exists(agree_btn):
            touch_(agree_btn)
            sleep(1)
            touch_(r_pos)
    close(2)
    close(2)


def reward_of_week():
    """
    一周礼包
    :return:
    """
    today = datetime.today().date()
    # 0-6
    day_of_week = today.weekday()
    touch_(main_fuli_btn)
    touch_(week_reward_tab)
    if day_of_week == 5:
        touch_(receive_reward_btn)
    if day_of_week == 6:
        touch_(receive_reward_btn)
    if day_of_week == 0:
        touch_(receive_reward_btn)
    close(2)


if __name__ == '__main__':
    pass
