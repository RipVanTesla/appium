from confHelper.configHelperAndroid.standards import *

def Test_authorization(driver, number, passw, qr=True, low_ballance=True):
    driver.implicitly_wait(100)
    # click_by_id(driver, "btn_confirm", "UseConditionConfirmActivity", scrn=True)
    # m = driver.find_element_by_id("kg.o.nurtelecom:id/et_input")
    # m.send_keys("702 242 516")
    send_keys_by_id(driver, "cnt_phone_number", number, sleep=None, scrn=True)
    click_by_id(driver, "btn_phone_number_next", scrn=True)
    send_keys_by_xpath(driver, "cnt_phone_pswrd", passw, scrn=True)
    # send_keys_by_xpath(driver, "cnt_phone_pswrd", "Qwerty654321", scrn=True)
    click_by_id(driver, "btn_phone_pswrd_next", scrn=True)
    click_by_xpath(driver, "btn_cancel_system_secure", scrn=True)
    driver.wait_activity(".ui.main.MainActivity", 10)
    if low_ballance:
        click_by_id(driver, "touch_outside", scrn=True)
    if qr:
        # click_by_id(driver, "space_out_cntn", scrn=True)
        click_by_id(driver, "btn_scanner_cancel", scrn=True)
