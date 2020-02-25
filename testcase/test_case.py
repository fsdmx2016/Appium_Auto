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
driver = get_driver()
def login_by_ui_automator():
    driver.find_element_by_android_uiautomator('new UiSelector().text("账号")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击登录")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")').send_keys('1234')
login_by_ui_automator()
