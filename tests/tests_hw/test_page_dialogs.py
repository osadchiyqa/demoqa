from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    modal_dialogs_form = ModalDialogs(browser)

    modal_dialogs_form.visit()
    assert modal_dialogs_form.btns_third_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    demo_qa_page = DemoQa(browser)
    modal_dialogs_form = ModalDialogs(browser)

    modal_dialogs_form.visit()
    modal_dialogs_form.refresh()
    modal_dialogs_form.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)