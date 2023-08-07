import sys
import os
import time
# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from scripts.ts_test_case_1 import edit_time_sheet_for_current_date
from constants.xpath.xpath_dynamic import create_dynamic_xpath_2
from constants.xpath.timesheet import *

def main():
    driver =  login("")
    time.sleep(10)
    newXpath =  create_dynamic_xpath_2(select_date_2,"August",2)
    print(newXpath)
    # calling 1st test case to run
    result = edit_time_sheet_for_current_date(driver)
    if(result):
        print("Successfully completed 1st test case automation")
    else:
        print("Sorry you are not lucky")
main()

