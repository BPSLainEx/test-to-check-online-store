import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket').text)
    assert button > 0, 'button is not found'