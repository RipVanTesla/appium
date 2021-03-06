"""This file stores selectors"""
APP_PREFIX = "kg.o.nurtelecom:id/"

def find_element_by_id(el_id, driver):
    return driver.find_element_by_id(f"{APP_PREFIX}{el_id}")

def find_element_by_xpath(el_path, driver):
    return driver.find_element_by_xpath(el_path)

def find_element_by_accessibility_id(el_acs: object, driver: object) -> object:
    return driver.find_element_by_accessibility_id(el_acs)

