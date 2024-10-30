from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'

        super().__init__(driver, self.base_url)

        # self.btn_delete_row = WebElement(driver, 'span[title="Delete"]')
        self.btn_delete_row = WebElement(driver, '//span[@title="Delete"]', 'xpath')
        self.no_data = WebElement(driver, 'div.rt-noData')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btn_submit = WebElement(driver, '#submit')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.line_4 = WebElement(driver, 'div.rt-tr-group:nth-child(4) > div:nth-child(1)')
        self.btn_edit_4 = WebElement(driver, '#edit-record-4')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4')
        self.btn_rows = WebElement(driver, '.select-wrap > select:nth-child(1)')
        self.btn_5_rows = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select/option[1]', 'xpath')
        self.btn_previous = WebElement(driver, '.-previous > button:nth-child(1)')
        self.btn_next = WebElement(driver, '.-next > button:nth-child(1)')
        self.total_pages = WebElement(driver, '.-totalPages')
        self.current_page = WebElement(driver, '.-pageJump > input:nth-child(1)')


        self.header_first_name = WebElement(driver, 'div.rt-th:nth-child(1)')
        self.header_last_name = WebElement(driver, 'div.rt-th:nth-child(2)')
        self.header_email = WebElement(driver, 'div.rt-th:nth-child(3)')
        self.header_age = WebElement(driver, 'div.rt-th:nth-child(4)')
        self.header_salary = WebElement(driver, 'div.rt-th:nth-child(5)')
        self.header_department = WebElement(driver, 'div.rt-th:nth-child(6)')
        self.header_action = WebElement(driver, 'div.rt-th:nth-child(7)')