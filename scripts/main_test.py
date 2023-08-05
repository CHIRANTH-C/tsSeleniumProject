import sys
import os
# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from library.search_filter import searchts
from library.basic_functions import wait_until_element_is_visible , click_element
from constants.xpath.timesheet import *
from constants.xpath.solution import *
from scripts.search_ts_with_invalied_tech import *

def main():
    driver =  login("A")
    search_result = invalied_tech(driver)

main()

