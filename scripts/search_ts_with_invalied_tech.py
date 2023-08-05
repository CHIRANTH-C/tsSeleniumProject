import sys
import os
# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import wait_until_element_is_visible , click_element
from constants.xpath.solution import *
from constants.xpath.timesheet import *
from library.search_filter import *
import time

def invalied_tech(driver):
    click_element(driver,nav_bar_ts)
    searchts(driver)
    result = wait_until_element_is_visible(driver,empty_msg)
    time.sleep(10)
    print(result)