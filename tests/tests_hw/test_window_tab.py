from pages.links import Links
import time


def test_window_tab(browser):
    links = Links(browser)
    links.visit()

    assert len(browser.window_handles) == 1
    assert links.linkHome.exist()
    assert links.linkHome.get_text() == 'Home'
    assert links.linkHome.get_dom_attribute('href') == 'https://demoqa.com'
    links.linkHome.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2