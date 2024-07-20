import os
import time
from PIL import Image

# 定义截图保存路径和裁剪参数
screenshot_path_on_phone = '/sdcard/screenshot.png'
save_path_on_computer = 'screenshots/'
cropped_save_path_on_computer = 'cropped_screenshots/'
crop_box = (86, 1234, 993, 1826)  # 左上角和右下角坐标 (left, top, right, bottom)

def take_screenshot():
    os.system('adb shell screencap -p {} '.format(screenshot_path_on_phone))
    print("Screenshot taken.")

def pull_screenshot():
    os.system('adb pull {} {}'.format(screenshot_path_on_phone, save_path_on_computer))
    print("Screenshot pulled to computer.")

def crop_image(filename):
    img = Image.open(os.path.join(save_path_on_computer, filename))
    cropped_img = img.crop(crop_box)
    cropped_filename = 'cropped_' + filename
    cropped_img.save(os.path.join(cropped_save_path_on_computer, cropped_filename))
    print("Image cropped and saved.")

def delete_screenshot_on_phone():
    os.system('adb shell rm {}'.format(screenshot_path_on_phone))
    print("Screenshot deleted from phone.")

def process_screenshots():
    if not os.path.exists(save_path_on_computer):
        os.makedirs(save_path_on_computer)
    if not os.path.exists(cropped_save_path_on_computer):
        os.makedirs(cropped_save_path_on_computer)
    take_screenshot()
    pull_screenshot()
    files = os.listdir(save_path_on_computer)
    for file in files:
        if file.endswith('.png'):
            crop_image(file)
            delete_screenshot_on_phone()

start_time = time.time()
process_screenshots()
end_time = time.time()
print("Screenshots processed in {} seconds.".format(end_time - start_time))

