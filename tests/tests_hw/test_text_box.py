from pages.text_box import TextBox

def test_placeholder (browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.name.send_keys('tester')
    text_box_page.current_address.send_keys('testreet')
    text_box_page.btn_submit.click_force()

    assert text_box_page.output_name.get_text() == 'Name:tester'
    assert text_box_page.output_current_address.get_text() == 'Current Address :testreet'