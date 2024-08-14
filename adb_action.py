import subprocess
import time
from datetime import datetime

def adb_swipe_hold(start_x, start_y, end_x, end_y, hold_time=0.5, duration=1000):
    """
    使用 ADB 执行从 (start_x, start_y) 到 (end_x, end_y) 的滑动操作，并停留 hold_time 秒。
    :param start_x: 起点 x 坐标
    :param start_y: 起点 y 坐标
    :param end_x: 终点 x 坐标
    :param end_y: 终点 y 坐标
    :param hold_time: 停留时间（秒）
    :param duration: 滑动持续时间（毫秒）
    """
    adb_command = f"adb shell input swipe {start_x} {start_y} {end_x} {end_y} {duration}"
    
    # 执行 ADB 命令
    subprocess.run(adb_command, shell=True)
    
    # 停留指定时间
    time.sleep(hold_time)

# 示例：从 (100, 200) 滑动到 (300, 400)，停留 0.5 秒
# adb_swipe_hold(538, 1726, 538, 1529, hold_time=3, duration=1000)

def adb_click(x, y):
    """
    使用 ADB 执行点击操作。
    :param x: 点击位置的 x 坐标
    :param y: 点击位置的 y 坐标
    """
    adb_command = f"adb shell input tap {x} {y}" 
    
    print(adb_command)
    # 执行 ADB 命令
    subprocess.run(adb_command, shell=True) 
    #停留指定时间
    time.sleep(2)
    
feeds_locations =  [(546, 645), (793, 2073), (309, 2080), (132, 533)]
feeds_locations_without_speed =  [(546, 645), (793, 2073), (132, 533)]
full_cnt = 0
def full_energy():
    global full_cnt
    _locations = []
    if full_cnt % 2 == 0:
        _locations = feeds_locations
    else:
        _locations = feeds_locations_without_speed
    # 依次点击四个坐标来完成能量充值
    for location in _locations:
        adb_click(*location)
    full_cnt += 1
def exit_feed_page():
    # 点击feeds_locations的最后一个坐标
    adb_click(*feeds_locations[-1])
    time.sleep(2)

# full_energy()

reload_locations = [(1014, 178), (784, 319), (130, 754)]
def reload_page():
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}reload_page...")
    adb_click(*reload_locations[0])
    time.sleep(2)
    adb_click(*reload_locations[1])
    time.sleep(40)
    adb_click(*reload_locations[2])
    time.sleep(10)
    adb_click(*reload_locations[2])
    
    

# reload_page()
