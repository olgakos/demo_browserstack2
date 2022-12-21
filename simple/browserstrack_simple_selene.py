from allure_commons._allure import step
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",

    # Set URL of the application under test
    "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c", #wiki app

    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-2-demo2022-12-21_selene",
        "sessionName" : "BStack first_test",

        # Set your access credentials
        "userName" : "sadovayasonya_Ih4tsF",
        "accessKey" : "3z6kuhUCmNhvLZbp59Dx"
    }
})

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
with step('Enter to App'):
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
with step('Search field'):
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
with step('Type text in field'):
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
with step('Check'):
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
with step('Quit from App'):
    browser.quit()