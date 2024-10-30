from pages.modal_dialogs import ModalDialogs
import pytest
import time


@pytest.fixture(autouse=True)
def test_available(browser):
    modal_dialogs_form = ModalDialogs(browser)

    if not modal_dialogs_form.is_available(): # метод .is_available() добавлен в base_page.py
        pytest.skip("Страница недоступна")

def test_check_modal(browser):
    modal_dialogs_form = ModalDialogs(browser)

    modal_dialogs_form.visit()
    assert modal_dialogs_form.btns_size_modal.check_count_elements(count=2)

    assert modal_dialogs_form.btn_small_modal.exist()
    assert modal_dialogs_form.btn_small_modal.get_text() == 'Small modal'
    modal_dialogs_form.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialogs_form.modal_window.exist()
    assert modal_dialogs_form.btn_close_small_modal.exist()
    assert modal_dialogs_form.btn_close_modals.exist()
    modal_dialogs_form.btn_close_small_modal.click()
    time.sleep(2)
    assert not modal_dialogs_form.modal_window.exist()

    assert modal_dialogs_form.btn_large_modal.exist()
    assert modal_dialogs_form.btn_large_modal.get_text() == 'Large modal'
    modal_dialogs_form.btn_large_modal.click()
    time.sleep(2)
    assert modal_dialogs_form.modal_window.exist()
    assert modal_dialogs_form.btn_close_large_modal.exist()
    assert modal_dialogs_form.btn_close_modals.exist()
    modal_dialogs_form.btn_close_large_modal.click()
    time.sleep(2)
    assert not modal_dialogs_form.modal_window.exist()

    """ Проверка закрытия форм при нажатии на Х """
    modal_dialogs_form.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialogs_form.modal_window.exist()
    modal_dialogs_form.btn_close_modals.click()
    time.sleep(2)
    assert not modal_dialogs_form.modal_window.exist()

    modal_dialogs_form.btn_large_modal.click()
    time.sleep(2)
    assert modal_dialogs_form.modal_window.exist()
    modal_dialogs_form.btn_close_modals.click()
    time.sleep(2)
    assert not modal_dialogs_form.modal_window.exist()
    pass