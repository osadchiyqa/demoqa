import time
import allure
from pages.tables import Tables


# """Lesson_11_committed"""
# def test_tables(browser):
#     """Проверка блока No rows found"""
#     page_tables = Tables(browser)
#
#     page_tables.visit()
#     assert not page_tables.no_data.exist()
#
#     """ Удаляем все записи """
#     while page_tables.btn_delete_row.exist():
#         page_tables.btn_delete_row.click()
#
#     time.sleep(2)
#     assert page_tables.no_data.exist()

""" Homework_11_1 """
def test_add_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    assert page_tables.line_4.get_text() == '       '
    page_tables.btn_add.click()
    assert page_tables.modal_dialog.exist()
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.modal_dialog.exist()
    page_tables.first_name.send_keys('tester')
    page_tables.last_name.send_keys('testerovich')
    page_tables.email.send_keys('test@test.tt')
    page_tables.age.send_keys('35')
    page_tables.salary.send_keys('11111')
    page_tables.department.send_keys('QA')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert not page_tables.modal_dialog.exist()
    assert page_tables.line_4.get_text() == 'tester\ntesterovich\n35\ntest@test.tt\n11111\nQA'
    page_tables.btn_edit_4.click()
    time.sleep(2)
    assert page_tables.modal_dialog.exist()
    page_tables.first_name.clear()
    page_tables.first_name.send_keys('supertester')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.line_4.get_text() == 'supertester\ntesterovich\n35\ntest@test.tt\n11111\nQA'
    page_tables.btn_delete_4.click()
    time.sleep(2)
    assert page_tables.line_4.get_text() == '       '

""" Homework_11_2 """
def test_second_page(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    page_tables.btn_rows.scroll_to_element()
    page_tables.btn_rows.click()
    time.sleep(2)
    page_tables.btn_5_rows.click()
    time.sleep(2)

    page_tables.btn_previous.click()
    time.sleep(2)
    assert page_tables.btn_previous.get_dom_attribute('disabled') == "true"
    page_tables.btn_next.click()
    time.sleep(2)
    assert page_tables.btn_next.get_dom_attribute('disabled') == "true"

    assert page_tables.total_pages.get_text() == '1'
    assert page_tables.current_page.get_dom_attribute('value') == "1"

    page_tables.btn_add.click()
    time.sleep(2)
    page_tables.first_name.send_keys('junior')
    page_tables.last_name.send_keys('juniorovich')
    page_tables.email.send_keys('junior@test.tt')
    page_tables.age.send_keys('35')
    page_tables.salary.send_keys('11111')
    page_tables.department.send_keys('QA')
    page_tables.btn_submit.click()
    time.sleep(2)

    page_tables.btn_add.click()
    time.sleep(2)
    page_tables.first_name.send_keys('middle')
    page_tables.last_name.send_keys('middleovich')
    page_tables.email.send_keys('middle@test.tt')
    page_tables.age.send_keys('35')
    page_tables.salary.send_keys('22222')
    page_tables.department.send_keys('QA')
    page_tables.btn_submit.click()
    time.sleep(2)

    page_tables.btn_add.click()
    time.sleep(2)
    page_tables.first_name.send_keys('senior')
    page_tables.last_name.send_keys('seniorovich')
    page_tables.email.send_keys('senior@test.tt')
    page_tables.age.send_keys('35')
    page_tables.salary.send_keys('33333')
    page_tables.department.send_keys('QA')
    page_tables.btn_submit.click()
    time.sleep(2)

    assert page_tables.total_pages.get_text() == '2'
    assert not page_tables.btn_next.get_dom_attribute('disabled') == "true"
    page_tables.btn_next.click()
    time.sleep(2)

    assert page_tables.current_page.get_dom_attribute('value') == "2"
    assert not page_tables.btn_previous.get_dom_attribute('disabled') == "true"
    page_tables.btn_previous.click()
    time.sleep(2)
    assert page_tables.current_page.get_dom_attribute('value') == "1"
