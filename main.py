from disgust import disgust_pic
from win10toast import ToastNotifier
import random
import time
from datetime import datetime
from merge import adb_swipe_hold
from screenshot import process_screenshots
start_pos = (86, 1234)
random.seed()  # 使用系统当前时间作为随机种子
source_img = 'cropped_screenshots/cropped_screenshot.png'
def shuffle_array(arr):
    """
    打乱数组中的元素顺序。
    :param arr: 输入数组
    :return: 打乱顺序后的数组
    """
    random.shuffle(arr)
    return arr

def swap_elements(arr, index1, index2):
    """
    交换数组中两个指定位置的元素。
    :param arr: 输入数组
    :param index1: 第一个元素的位置
    :param index2: 第二个元素的位置
    """
    if index1 >= len(arr) or index2 >= len(arr):
        raise IndexError("索引超出数组范围")
    
    # 交换元素
    arr[index1], arr[index2] = arr[index2], arr[index1]
start_time = time.time()
total_cnt = 5
while True:
    process_screenshots()
    found = []
    swipe_cnt = 0
    try: 
        for i in range(20, 7, -1):
            target_img = 'pooper_items/' + str(i) + '.png'
            threshold = 0.4
            # TODO: 优化
            if i >= 12:
                threshold = 0.3
            if i in [15, 14]:
                threshold = 0.25
            matched = disgust_pic(source_img, target_img, threshold)
            print(f"{target_img} found {len(matched)}")
            while len(matched) >= 2:
                matched = shuffle_array(matched)
                if matched[1][1] > matched[0][1]:
                    swap_elements(matched, 0, 1)
                print(f"found {i}")
                print(f"first item pos: {matched[0][0]+start_pos[0]}, {matched[0][1]+start_pos[1]}")
                print(f"second item pos: {matched[1][0]+start_pos[0]}, {matched[1][1]+start_pos[1]}" )
                found.append([matched[0][0]+start_pos[0], matched[0][1]+start_pos[1], matched[1][0]+start_pos[0], matched[1][1]+start_pos[1]])
                matched = matched[2:]
    except Exception as e:
        print(f"图像识别发生错误: {e}")
    # merge poopers
    for i in found:
        print(f"swiping: {i}")
        random_number = round(random.uniform(2, 4.5), 1)
        adb_swipe_hold(i[0],i[1],i[2],i[3], random_number, 800)
        swipe_cnt = swipe_cnt + 1
    
    if swipe_cnt == 0:
        total_cnt = total_cnt - 1
        time.sleep(8)
        if total_cnt == 0:
            end_time = time.time()
            duration = (end_time - start_time)/60
            print(f"no poopers found, swiping back")         
            toaster = ToastNotifier()
            toaster.show_toast("dogPooper运行结束", f"已于{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}结束运行时长为：{duration} 分钟", duration=5)
            exit(0)
    else:
        total_cnt = 5

