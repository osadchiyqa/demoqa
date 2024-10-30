from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, '.show > ul:nth-child(1) > li')
        self.icon = WebElement(driver, '#app > header > a')

        self.btns_size_modal = WebElement(driver, 'div > button')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')
        self.btn_close_modals = WebElement(driver, '.close > span:nth-child(1)')
        self.modal_window = WebElement(driver, '.modal-content')