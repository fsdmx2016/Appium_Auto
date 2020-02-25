# coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self, i):
        # devices_name adb devices
        # port
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": "D:\\download\\imooc7.3.110102001android.apk",
            "appActivity": "com.imooc.component.imoocmain.index.MCMainActivity",
        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        time.sleep(10)
        return driver
