import time

from pages.alerts import Alerts


def test_alert(browser):
    """Проверка видимости алерта"""
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()

def test_alert_text(browser):
    """Подтверждение и текст алерта"""
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_confirm(browser):
    """Отмена алерта"""
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    """Проверка ввода текста в алерт"""
    alert_page = Alerts(browser)
    name = 'Kirill'

    alert_page.visit()
    alert_page.promtButton.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == f'You entered { name }'
    time.sleep(2)
