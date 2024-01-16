# encoding=utf-8

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout

deviceid = "emulator-5554"
poco = AndroidUiautomationPoco()

auto_setup(devices=[
            f"Android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP"
            f"&&ori_method=MINICAPORI"
            f"&&touch_method=MAXTOUCH"
        ])

fight_btn = Template(r"tpl1705393786480.png", record_pos=(0.405, 0.237), resolution=(1920, 1080))
next_btn = Template(r"tpl1705394203127.png", record_pos=(0.197, 0.244), resolution=(1920, 1080))
while 1:
    try:
        if exists(next_btn):
            touch(next_btn)
    except PocoTargetTimeout:
        pass
