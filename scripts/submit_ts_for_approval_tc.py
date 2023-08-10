## TS TEST CASE 1 ##
## Edit time sheet and add all type of activities
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import wait_until_element_is_visible , click_element
from library.ts_actions import edit_ts_entry, navigate_to_page, submit_ts
from constants.xpath.timesheet import *
from constants.xpath.solution import *
from scripts.search_ts_with_invalied_tech import *

def submit_ts_for_approval(driver, tech_name):
    # Step 1 - navigate to time sheet page
    click_element(driver,nav_bar_ts)
    time.sleep(10)

    # Step 2 - Filter the time range
    from_filter_result=filter_from_date(driver)
    from_to_result=filter_to_date(driver)
    drop_down_result=drop_down(driver)
    print(from_filter_result)
    print(from_to_result)
    print(drop_down_result)
    
    # Step 2 - Filter the technitian
    result_name_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , tech_name))
    print(result_name_selected)
    result_date_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , tech_name))
    print(result_date_selected)
    time.sleep(10)
    edit_result = edit_ts_entry(driver, tech_name)
    print(edit_result)
    result = submit_ts(driver)
    navigate_to_page(driver,nav_pending_review_page)
    
    if(result):
        print("Done!!!")
