from pages.base_page import BasePage
from components.components import WebElement


class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, 'div.custom-control:nth-child(2)')
        self.impressive = WebElement(driver, 'div.custom-control:nth-child(3)')
        self.no = WebElement(driver, 'div.custom-control:nth-child(4)')
        self.text = WebElement(driver, '.text-success')
