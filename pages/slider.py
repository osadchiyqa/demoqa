from pages.base_page import BasePage
from components.components import WebElement


class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.slider = WebElement(driver, '.range-slider')
        self.inp = WebElement(driver, '#sliderValue')