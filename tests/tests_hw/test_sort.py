from pages.tables import Tables
import time

def test_sort_columns(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    headers = [page_tables.header_first_name,
              page_tables.header_last_name,
              page_tables.header_email,
              page_tables.header_age,
              page_tables.header_salary,
              page_tables.header_department,
              page_tables.header_action]

    for header in headers:
        """Проверка, что толбец неотсортирован"""
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
        header.click()
        time.sleep(2)
        """Проверка, что толбец отсортирован"""
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        header.click()
        time.sleep(2)
        """Проверка, что после 2-х нажатий толбец отсортирован в обратном порядке"""
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-desc -cursor-pointer"
        time.sleep(2)