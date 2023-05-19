import os
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.environ.get("JENKINS_LABEL", "Build_iOS")

options = XCUITestOptions().load_capabilities({
    "platformName" : "ios",
    "platformVersion" : "16.0",
    "deviceName" : "iPhone 14",
    "app" : "bs://a3129b2292fe6e8544f151efa019555ab058ac97",
    'build': build_name
},
{
    "platformName" : "ios",
    "platformVersion" : "16.0",
    "deviceName" : "iPhone 14 Pro Max",
    "app" : "bs://a3129b2292fe6e8544f151efa019555ab058ac97",
    'build': build_name
}
)

for i in options:
	driver = webdriver.Remote("https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub", options=options[i])

# Test case for the BrowserStack sample iOS app.
# If you have uploaded your app, update the test case here. 
text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()
text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com"+"\n")
time.sleep(5)
text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
)
if text_output!=None and text_output.text=="hello@browserstack.com":
	assert True
else:
	assert False

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
