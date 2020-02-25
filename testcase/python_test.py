from appium import webdriver
import time


def get_driver():
    # "noReset": "true" 不需要重置
    capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:21503",
        "app": "D:\\download\\imooc7.3.110102001android.apk",
        "appActivity": "com.imooc.component.imoocmain.index.MCMainActivity",

    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(10)
    return driver


# 获取屏幕的宽、高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


def swipe_left():
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


def swipe_right():
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)


def swipe_up():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y)


def swipe_down():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    elif direction == 'right':
        swipe_right()


driver = get_driver()

def go_login():
    element = driver.find_element_by_id('cn.com.open.mooc:id/tab_layout').find_element_by_class_name(
        'android.widget.LinearLayout').find_elements_by_class_name('androidx.appcompat.app.ActionBar$Tab')
    element[4].click()
    driver.find_element_by_link_text('点击登录').click()

def login_by_ui_automator():
    driver.find_element_by_android_uiautomator('new UiSelector().text("账号")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击登录")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")').send_keys('1234')

def close_ad():
    driver.find_element_by_id('cn.com.open.mooc:id/iv_cancel').click()

# login_by_ui_automator()
# close_ad()