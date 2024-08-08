import subprocess
import time

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
def full_energy():
    # 依次点击四个坐标来完成能量充值
    for location in feeds_locations:
        adb_click(*location)
    
def exit_feed_page():
    # 点击feeds_locations的最后一个坐标
    adb_click(*feeds_locations[-1])
    time.sleep(2)

# full_energy()