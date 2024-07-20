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
