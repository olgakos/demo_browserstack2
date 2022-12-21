import os
import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from appium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from utils import attachment


#from wikipedia.util import attachments

@pytest.fixture(scope='session', autouse=True)
def driver_management():
    load_dotenv()
    USER_NAME = os.getenv('userName')
    ACCESS_KEY = os.getenv('accessKey')
    APP = os.getenv('app')
    PLATFORM_NAME = os.getenv('platformName')
    options = UiAutomator2Options()

    options.load_capabilities({
        "app": f"{APP}",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": f"{PLATFORM_NAME}",
        "project": "Python project",
        "build": "wikipedia-build",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-2-demo2022-12-21_selene",
            "sessionName": "BStack first_test",
            "userName": f"{USER_NAME}",
            "accessKey": f"{ACCESS_KEY}",
        }
    })
    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options,
    )
    browser.config.timeout = 4
    yield driver_management
    attach.add_video(browser)
    browser.quit()