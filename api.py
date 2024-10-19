import json
import platform
import subprocess

from bottle import *
from demo import *


@route('/')
def index():
    items = ['每日签到', '一周礼包', '丰饶之间-赏金', '丰饶之间-经验',
             '领取体力', '购买货物', '领取任务奖励', '忍者考试下一关']
    return template('index', items=items)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


@route('/action/<index1:int>')
def action(index1):
    funcs = [sign, reward_of_week, money_reward, exp_reward,
             get_energy, buy_coin_stuff, receive_task_reward, next_level]
    for index_, func in enumerate(funcs):
        if index1 == index_:
            callable(func())
            break
    return


@route('/selectDevice/<deviceid>')
def select_device(deviceid):
    if deviceid:
        auto_setup(devices=[
            f"Android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP"
            f"&&ori_method=MINICAPORI"
            f"&&touch_method=MAXTOUCH"
        ])
    return


@route('/onekey')
def onekey():
    onekey_finish()
    return


@route('/dropdown')
def dropdown():
    response.content_type = 'application/json'
    devices = []
    system = platform.system()
    if system == 'Windows':
        cmd = "adb devices"
    elif system in ['Darwin', 'Linux']:
        cmd = "adb devices"
    else:
        return
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, encoding='utf-8')
    # 处理子进程结束
    process.wait()
    # 确保文件关闭
    with process.stdout as stdout:
        stdout_str = stdout.readlines()
        # 去掉头部尾部
        stdout_str.pop(0)
        stdout_str.pop(len(stdout_str) - 1)
        for i in range(len(stdout_str)):
            if ":" or "emulator" in stdout_str[i]:
                devices.append(stdout_str[i].split("device")[0].strip("\t"))
        print(f"{len(devices)} devices have been found {devices}")
    return json.dumps(devices)


if __name__ == '__main__':
    run(host='localhost', port=9547, debug=True, reloader=True)
