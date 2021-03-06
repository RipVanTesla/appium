import allure
import pytest

from confHelper.configHelperAndroid.configHelperAndroid import capsAnroid
from confHelper.configHelperAndroid.standards import send_keys_by_xpath
from confHelper.configHelperAndroid.authAndroid import *


@allure.epic("Epic #3 - Модуль О!Деньги")
@allure.feature("Feature #1 - О!Деньги")
@allure.severity(allure.severity_level.BLOCKER)
class Test_OMoney(capsAnroid):
    @allure.story("Story #1 - Главная страница Личного кабинета О!Деньги")
    @allure.title("Тест.переходы на главном экране О!Деньги")
    @allure.description("Проверка работоспособности переходов на главной странице О!Деньги")
    # @pytest.mark.skip(reason="не требуется")
    def test_omoney(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 516", "Qwerty654321")
        with allure.step("Step 1 Проверка перехода в модуль О!Деньги"):
            click_by_id(driverAndroid, "btn_o!dengi", scrn=True, sleep=True)
        with allure.step("Step 1 Проверка перехода в экран пополнения ewallet"):
            click_by_id(driverAndroid, "btn_self_refill", scrn=True, sleep=True)
            driverAndroid.back()
        with allure.step("Step 2 Проверка перехода в экран карт"):
            click_by_id(driverAndroid, "btn_cards", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step 3 ППроверка перехода в экран бонусы"):
            click_by_id(driverAndroid, "btn_bonuses", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step 4 Проверка перехода в экран история"):
            click_by_id(driverAndroid, "btn_history", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step 5 Проверка перехода в экран штрафы"):
            click_by_id(driverAndroid, "btn_fines", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step 6 Проверка перехода в экран история"):
            click_by_id(driverAndroid, "btn_history", sleep=True, scrn=True)
            driverAndroid.back()
        with allure.step("Step 7 Проверка перехода в экран сканер"):
            click_by_id(driverAndroid, "btn_qr_scanner", sleep=True, scrn=True)
            driverAndroid.back()
        # with allure.step("Step 9 Проверка перехода в окно 'Избранные'"):
        #     click_by_id(driverAndroid, "btn_add_fav", sleep=True, scrn=True)
        #     driverAndroid.back()
        # with allure.step("Step 10 Проверка перехода в окно 'Каталог'"):
        #     click_by_id(driverAndroid, "btn_search_catalog", sleep=True, scrn=True)
        #     driverAndroid.back()
        #     driverAndroid.back()

    @allure.story("Story #2 - Пополнение собственного mwallet")
    @allure.title("Тест.Пополнение собственного mwallet")
    @allure.description("Проверка работоспособности пополнение своего mwallet О!Деньги")
    # @pytest.mark.skip(reason="работает только если есть фунционал новой платежки")
    def test_self_payment_mwallet(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 516", "Qwerty654321")
        with allure.step("Step 1 Проверка перехода в модуль О!Деньги"):
            click_by_id(driverAndroid, "btn_o!dengi", scrn=True, sleep=True)
        # with allure.step("Step 2 скрытие попапа о сканере"):
        #     click_by_id(driverAndroid, "btn_scanner_course_cancel", sleep=True, scrn=True)
        with allure.step("Step 3 Проверка перехода на окно 'пополнение своего баланса'"):
            click_by_xpath(driverAndroid, "btn_self_refill_mwallet", sleep=True, scrn=True)
        with allure.step("Step 4 Проверка перехода на окно завершения пополнения самого себя"):
            click_by_id(driverAndroid, "btn_self_payment_cont", sleep=True, scrn=True)
        with allure.step("Step 5 Проверка перехода на окно выбора способа платежа"):
            click_by_id(driverAndroid, "btn_choose_payment_wallet", sleep=True, scrn=True)
        with allure.step("Step 6 Проверка выбора оплаты с mwallet"):
            click_by_xpath(driverAndroid, "btn_payment_type_mwallet", sleep=True, scrn=True)
        with allure.step("Step 7 Проверка заполнениея суммы пополнения"):
            send_keys_by_xpath(driverAndroid, "cnt_payment_value", "10", sleep=True, scrn=True)
        with allure.step("Step 8 Проверка подтверждения создания платежа"):
            click_by_xpath(driverAndroid, "btn_self_payment_cont1", sleep=True, scrn=True)
        with allure.step("Step 9 Проверка подтверждения создания платежа"):
            click_by_xpath(driverAndroid, "btn_self_payment_cont2", sleep=True, scrn=True)

    @allure.story("Story #3 - Пополнение собственного ewallet")
    @allure.title("Тест.Пополнение собственного ewallet")
    @allure.description("Проверка работоспособности пополнение своего ewallet О!Деньги")
    # @pytest.mark.skip(reason="работает только если есть фунционал новой платежки")
    def test_self_payment_ewallet(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 516", "Qwerty654321")
        with allure.step("Step 1 Проверка перехода в модуль О!Деньги"):
            click_by_id(driverAndroid, "btn_o!dengi", scrn=True, sleep=True)
        # with allure.step("Step 2 скрытие попапа о сканере"):
        #     click_by_id(driverAndroid, "btn_scanner_course_cancel", sleep=True, scrn=True)
        with allure.step("Step 3 Проверка перехода на окно 'пополнение своего ewallet'"):
            click_by_xpath(driverAndroid, "btn_self_refill_ewallet", sleep=True, scrn=True)
        with allure.step("Step 4 Проверка ввода суммы пополнения в контейнер"):
            click_by_xpath(driverAndroid, "btn_50_ammount", sleep=True, scrn=True)
        with allure.step("Step 5 Проверка нажатия кнопки пополнения"):
            click_by_id(driverAndroid, "btn_self_payment_cont", sleep=True, scrn=True)
        # with allure.step("Step 6 Проверка нажатия кнопки согласия проведения транзакции"):
        #     c = driver.find_element_by_id("android:id/button1")
        #     c.click()
        #     time.sleep(5)
        #     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.story("Story #4 - Перевод средств между ewallet")
    @allure.title("Тест.Перевод средств между ewallet")
    @allure.description("Проверка работоспособности переводов между ewallet")
    # @pytest.mark.skip(reason="работает проверять во время ночных")
    def test_transfer_payment_ewallet(self, driverAndroid):
        with allure.step("Step 0 блок успешной авторизации"):
            Test_authorization(driverAndroid, "+996 702 242 516", "Qwerty654321")
        with allure.step("Step 1 Проверка перехода в модуль О!Деньги"):
            click_by_id(driverAndroid, "btn_o!dengi", scrn=True, sleep=True)
        # with allure.step("Step 2 скрытие попапа о сканере"):
        #     click_by_id(driverAndroid, "btn_scanner_course_cancel", sleep=True, scrn=True)
        with allure.step("Step 3 проверка открытия окна переводов ewallet"):
            click_by_xpath(driverAndroid, "btn_ewallet_transfer", sleep=True, scrn=True)
        with allure.step("Step 4 проверка ввода номера в поле реквизита"):
            send_keys_by_id(driverAndroid, "cnt_req_ewallet", "700000201", sleep=True, scrn=True)
        with allure.step("Step 5 проверка ввода суммы в поле суммы"):
            send_keys_by_id(driverAndroid, "cnt_amount", "5", sleep=True, scrn=True)
        # with allure.step("Step 5 проверка проведения транзакции"):
            # click_by_id(driverAndroid, "btn_trans_ewallet", scrn=True)