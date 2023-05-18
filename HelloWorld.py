import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.environ.get("JENKINS_LABEL", "0")

desired_cap = [
{
    "platformName" : "android",
    "platformVersion" : "13.0",
    "deviceName" : "Google Pixel 7 Pro",
    "app" : "bs://f9529d2e64d5fb2183d28680ff7e3af0b4a2ea47",
    'build': build_name
},
{
    "platformName" : "android",
    "platformVersion" : "13.0",
    "deviceName" : "Samsung Galaxy S23 Ultra",
    "app" : "bs://f9529d2e64d5fb2183d28680ff7e3af0b4a2ea47",
    'build': build_name
},
{
    "platformName" : "android",
    "platformVersion" : "11.0",
    "deviceName" : "OnePlus 9",
    "app" : "bs://f9529d2e64d5fb2183d28680ff7e3af0b4a2ea47",
    'build': build_name
}
]

for i in desired_cap:
    print(i['deviceName'])
    driver = webdriver.Remote("https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub", i)

time.sleep(10)
driver.quit()
