from pages.alerts import Alerts
import time

def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.timerAlertButton.click()
    time.sleep(5)
    assert alert_page.alert()
    alert_page.alert().accept()
    assert not alert_page.alert()