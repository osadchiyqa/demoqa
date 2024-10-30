from pages.demoqa import DemoQa
from pages.radio import Radio
import pytest


@pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_1(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disable' in radio.no.get_dom_attribute('class')