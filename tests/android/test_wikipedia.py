from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


def test_search():
    with step('Enter'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_settings')).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageButton")).click()

    with step('Search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()

    with step('Type text in field'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')

    with step('Check'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

    with step('Clear field'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).clear()

    with step('Type second text in field'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Erik Bruhn')

    with step('Check'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))