from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert accordion.section_1_content.visible()

    accordion.btn_section_heading.click()
    time.sleep(2)
    assert not accordion.section_1_content.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert not accordion.section_2_content_1.visible()
    assert not accordion.section_2_content_2.visible()
    assert not accordion.section_3_content.visible()