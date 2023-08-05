import sys
import os
# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import *
from constants.xpath.authentication import *
from constants.xpath.solution import *
from library.data_helper import *
import time


def login(url):
    driver = open_browser(url)
    data = read_csv_data("/Users/chiranth.c/Documents/tsSeleniumProject/constants/data/raman_login.csv")
    print(data)
    username = data[0]['username']
    password = data[0]['password']
    print(username , ":",  password)
    time.sleep(20)
    wait_until_element_is_visible(driver, txt_welcome_note)
    enter_text_in_element(driver,txt_box_env,"raman")
    enter_text_in_element(driver,txt_box_org,"tsqa1")
    click_element(driver,btn_element)
    enter_text_in_element(driver,txt_box_username,username)
    enter_text_in_element(driver,txt_box_password,password)
    click_element(driver,btn_element)
    time.sleep(20)
    message = wait_until_element_is_visible(driver, nav_bar_ts)
    return driver

