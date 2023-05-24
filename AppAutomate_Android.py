import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.environ.get("JENKINS_LABEL", "Android Devices:Wikipedia")

desired_cap = [{
    "platformName" : "android",
    "platformVersion" : "13.0",
    "deviceName" : "Google Pixel 7 Pro",
    "app" : "bs://9efe81dd25c709c3d1561af7f1ad3a086963f370",
    'build': build_name
},
{
    "platformName" : "android",
    "platformVersion" : "11.0",
    "deviceName" : "Xiaomi Redmi Note 11",
    "app" : "bs://9efe81dd25c709c3d1561af7f1ad3a086963f370",
    'build': build_name
},
{
    "platformName" : "android",
    "platformVersion" : "13.0",
    "deviceName" : "Samsung Galaxy S23 Ultra",
    "app" : "bs://9efe81dd25c709c3d1561af7f1ad3a086963f370",
    'build': build_name
}
]

for i in desired_cap:
    driver = webdriver.Remote("https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub", i)
    search_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
    search_input.send_keys("BrowserStack")
    time.sleep(5)
    search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert (len(search_results) > 0)
    driver.quit()
