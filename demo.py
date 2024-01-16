# encoding=utf-8

from airtest.core.api import *

deviceid = "emulator-5554"
# 屏幕分辨率
resolution = (1920, 1080)
auto_setup(devices=[
            f"Android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP"
            f"&&ori_method=MINICAPORI"
            f"&&touch_method=MAXTOUCH"
        ])


def next_level():
    """
    忍者考试下一关
    :return:
    """
    # fight_btn = Template(r"img/tpl1705393786480.png", record_pos=(0.405, 0.237), resolution=resolution)
    next_btn = Template(r"img/tpl1705394203127.png", record_pos=(0.197, 0.244), resolution=resolution)
    while 1:
        try:
            if exists(next_btn):
                touch(next_btn)
        except Exception:
            pass


def nameit():
    pass
