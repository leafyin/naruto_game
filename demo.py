# encoding=utf-8
from datetime import datetime

import bottle
from bottle import route, run, response, template, static_file

from airtest.core.api import *
from airtest.core.settings import *


@route('/')
def index():
    items = ['一周礼包', '丰饶之间', '领取体力', '购买货物', '领取任务奖励', '忍者考试下一关']
    return template('index', items=items)


@route('/action/<index1:int>')
def action(index1):
    funcs = [reward_of_week, finish_big_reward, get_energy, buy_coin_stuff, receive_task_reward, next_level]
    print(index1)
    for index_, func in enumerate(funcs):
        if index1 == index_:
            callable(func())
            return


# 需要设置几个常量:deviceid、屏幕分辨率(这里是1280*720分辨率做参照)
deviceid = "emulator-5556"
resolution = (1280, 720)
ST.OPDELAY = 1

auto_setup(devices=[
    f"Android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP"
    f"&&ori_method=MINICAPORI"
    f"&&touch_method=MAXTOUCH"
])


challenge_btn = Template(r"img/tpl1705393786480.png", record_pos=(0.405, 0.237), resolution=resolution)
next_btn = Template(r"img/tpl1705394203127.png", record_pos=(0.197, 0.244), resolution=resolution)

task_btn = Template(r"img/tpl1705650949967.png", record_pos=(-0.427, -0.159), resolution=resolution)
main_task_btn = Template(r"img/tpl1705651266306.png", record_pos=(-0.427, -0.159), resolution=resolution)
other_task_btn = Template(r"img/tpl1705651584086.png", record_pos=(-0.407, -0.092), resolution=resolution)
day_task_btn = Template(r"img/tpl1705651674717.png", record_pos=(-0.408, -0.035), resolution=resolution)
week_task_btn = Template(r"img/tpl1705651688297.png", record_pos=(-0.408, 0.02), resolution=resolution)

receive_reward_btn = Template(r"img/tpl1705651327964.png")

# 玩法
wanfa_btn = Template(r"img/tpl1705653060271.png", record_pos=(0.45, 0.058), resolution=resolution)
fengraozhijian_btn = Template(r"img/tpl1728661026148.png", record_pos=(-0.226, -0.085), resolution=resolution)
money_entry = Template(r"img/tpl1728661370929.png", record_pos=(-0.283, 0.02), resolution=resolution)
quickly_fight = Template(r"img/tpl1728661514790.png", record_pos=(0.134, 0.231), resolution=resolution)
agree_btn = Template(r"img/tpl1728661653449.png", record_pos=(0.146, 0.116), resolution=resolution)

# 主页
main_duihuan_btn = Template(r"img/tpl1728691142644.png", record_pos=(0.288, -0.188), resolution=resolution)
main_fuli_btn = Template(r"img/tpl1728737903016.png", record_pos=(0.221, -0.189), resolution=resolution)

duihuan_btn = Template(r"img/tpl1728691620710.png", record_pos=(0.145, 0.117), resolution=resolution)
free_refresh_btn = Template(r"img/tpl1728693507109.png", record_pos=(0.365, 0.235), resolution=resolution)
confirm_btn = Template(r"img/tpl1728693845195.png", record_pos=(0.146, 0.117), resolution=resolution)

week_reward_tab = Template(r"img/tpl1728738062720.png", record_pos=(-0.413, 0.019), resolution=resolution)
get_energy_tab = Template(r"img/tpl1728740006743.png", record_pos=(-0.412, -0.041), resolution=resolution)


def close(t):
    """
    关闭按钮
    1=float window
    2=panel window
    :return:
    """
    close1_pos = relative_position((1200, 40), resolution)
    close2_pos = relative_position((1240, 30), resolution)
    if t == 1:
        touch(close1_pos)
    if t == 2:
        touch(close2_pos)


def relative_position(xy: tuple, resolution_: tuple):
    """
    计算相对位置
    :param xy: 绝对坐标
    :param resolution_: 分辨率
    :return tuple: 相对坐标
    """
    return round(xy[0] / resolution_[0], 2), round(xy[1] / resolution_[1], 2)


def get_energy():
    """
    领取体力
    :return:
    """
    touch(main_fuli_btn)
    touch(get_energy_tab)

    touch(receive_reward_btn)
    touch(receive_reward_btn)
    touch(receive_reward_btn)
    close(2)
    pass


def next_level():
    """
    忍者考试下一关
    """
    while 1:
        try:
            if exists(next_btn):
                touch(next_btn)
                sleep(1)
        except Exception:
            pass


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

    for i in range(0, 2):
        touch(main_duihuan_btn)
        # 第一个免费商品
        touch(pos1)
        touch(duihuan_btn)
        # 第二个免费商品
        touch(pos2)
        touch(duihuan_btn)
        # 第三个免费商品
        touch(pos3)
        touch(duihuan_btn)

        # 免费刷新
        touch(free_refresh_btn)
        touch(confirm_btn)

    close(1)


def receive_task_reward():
    """
    领取任务奖励
    :return:
    """
    touch(task_btn)
    rrb = receive_reward_btn
    task_bts = [main_task_btn, other_task_btn, day_task_btn, week_task_btn]
    for b in task_bts:
        touch(b)
        while 1:
            if b == other_task_btn or b == week_task_btn:
                times = 2
                while times > 0:
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


def finish_big_reward():
    """
    完成丰饶之间
    :return:
    """
    touch(wanfa_btn)
    touch(fengraozhijian_btn)
    touch(money_entry)
    r_pos = relative_position((650, 550), resolution)
    for i in range(0, 2):
        touch(quickly_fight)
        if exists(agree_btn):
            touch(agree_btn)
            touch(r_pos)
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
    touch(main_fuli_btn)
    touch(week_reward_tab)
    if day_of_week == 5:
        touch(receive_reward_btn)
    if day_of_week == 6:
        touch(receive_reward_btn)
    if day_of_week == 0:
        touch(receive_reward_btn)
    close(2)


if __name__ == '__main__':
    run(host='localhost', port=9547, debug=True, reloader=True)
