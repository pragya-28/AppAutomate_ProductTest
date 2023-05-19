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

desired_cap = {
    "platformName" : "ios",
    "platformVersion" : "16.0",
    "deviceName" : "iPhone 14",
    "app" : "bs://a3129b2292fe6e8544f151efa019555ab058ac97",
    'build': build_name
}

driver = webdriver.Remote("https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub",desired_cap)

# search_element = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
# )
# search_element.click()
# search_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable(
#         (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
# )
# search_input.send_keys("BrowserStack")
# time.sleep(5)
# search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
# assert (len(search_results) > 0)
driver.quit()
