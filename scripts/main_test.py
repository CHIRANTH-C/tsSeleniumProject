import sys
import os


# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from library.search_filter import searchts
from library.basic_functions import wait_until_element_is_visible , click_element
from library.ts_actions import add_activity, edit_ts_entry
from constants.xpath.timesheet import *
from constants.xpath.solution import *
from scripts.search_ts_with_invalied_tech import *
from scripts.ts_test_case_1 import edit_time_sheet_for_current_date

def main():
    driver =  login("")
    
    # calling 1st test case to run
    result = edit_time_sheet_for_current_date(driver)
    if(result):
        print("Successfully completed 1st test case automation")
    else:
        print("Sorry you are not lucky")

    # click_element(driver,nav_bar_ts)
    # from_filter_result=filter_from_date(driver)
    # from_to_result=filter_to_date(driver)
    # drop_down_result=drop_down(driver)
    # print(from_filter_result)
    # print(from_to_result)
    # print(drop_down_result)
    
    # result_name_selected = wait_until_element_is_visible(driver,ts_name_row)
    # print(result_name_selected)
    # result_date_selected = wait_until_element_is_visible(driver,ts_date_row)
    # print(result_date_selected)
    # time.sleep(10)
    # # hover_result = hover_over_on_ts_entry(driver)
    # edit_result = edit_ts_entry(driver)
    # print(edit_result)

    # add_activity_result=add_activity(driver)
    # print(add_activity_result)



    # search_result = invalied_tech(driver)
    # obj = MyClass()
    # filter_result = filter_date(driver)
    # print(search_result)
    # print("Hello")
    # print(filter_result)

main()

