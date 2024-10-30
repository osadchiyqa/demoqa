from pages.slider import Slider
from selenium.webdriver.common.keys import Keys

def test_slider_v3(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.inp.get_dom_attribute('value') == '50'

#   """ Неправильное решение """
# def test_slider_v1(browser):
#     slider = Slider(browser)
#
#     slider.visit()
#     assert slider.slider.exist()
#     assert slider.inp.exist()
#
#     slider.inp.send_keys('50')
#     slider.slider.send_keys('50')
#
#     assert slider.inp.get_dom_attribute('value') == '50'
