""" Standart test cases"""
import os

import allure
from allure_commons.types import AttachmentType

from confHelper.configHelperIOS.selectorHelper import find_element_by_id, find_element_by_xpath, \
     find_element_by_accessibility_id
from elements.elementsIOS import elements, list_activity, elements_path
import time


directory = '%s/results/appiumscr/' % os.getcwd()
file_name = 'screenshot.png'
F_EXT = "1.png"

def click_by_id(driver, id, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_id(elements.get(id), driver)
    btn.click()

    if sleep is True:
         time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def send_keys_by_id(driver, id, key, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    cnt = find_element_by_id(elements.get(id), driver)
    cnt.send_keys(key)

    if sleep is True:
         time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def click_by_xpath(driver, path, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_xpath(elements.get(path), driver)
    btn.click()

    if sleep is True:
        time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def send_keys_by_xpath(driver, path, key, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    cnt = find_element_by_xpath(elements.get(path), driver)
    cnt.send_keys(key)

    if sleep is True:
         time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def click_by_accessibility_id(driver, id, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    btn = find_element_by_accessibility_id(elements.get(id), driver)
    btn.click()

    if sleep is True:
         time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def send_keys_by_accessibility_id(driver, id, key, sleep=None, scrn=None):
    driver.implicitly_wait(10)
    cnt = find_element_by_accessibility_id(elements.get(id), driver)
    cnt.send_keys(key)

    if sleep is True:
         time.sleep(10)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def confirm_alert(driver, sleep=None, scrn=None):
    driver.switch_to_alert().accept()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def TouchAction(driver, X, Y, X1, Y2, sleep=None, scrn=None):
    driver.implicitly_wait(5)
    cnt = TouchAction(driver).press(x=X, y=Y).move_to(x=X1, y=Y2)
    cnt.release().perform()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)