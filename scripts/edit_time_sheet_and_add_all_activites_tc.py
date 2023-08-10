## TS TEST CASE 2 ##
## Edit time sheet and add all type of activities
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from library.search_filter import searchts
from library.basic_functions import wait_until_element_is_visible , click_element
from library.ts_actions import edit_ts_entry , add_activity_and_handle_conflict
from constants.xpath.timesheet import *
from constants.xpath.solution import *
from scripts.search_ts_with_invalied_tech import *


def edit_time_sheet_and_add_all_activites(driver, technitian_name , activity_name , start_time_hrs , start_time_mins , end_time_hrs, end_time_mins , pop_up_xpath,isAM=False,isTaskType=False,task_id=None):
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
    result_name_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , technitian_name))
    print(result_name_selected)
    result_date_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , technitian_name))
    print(result_date_selected)
    time.sleep(10)
    edit_result = edit_ts_entry(driver, technitian_name)
    print(edit_result)
    # isAM = False
    # Add Overtime activity and hangle time range conflict pop up
    add_activity_result=add_activity_and_handle_conflict(driver,activity_name, start_time_hrs, start_time_mins, end_time_hrs, end_time_mins, pop_up_xpath, isAM ,isTaskType,task_id)
    print(add_activity_result)
    string_val = "Element found: "+create_new_dynamic_xpath(activity_entry,activity_name)+"."
    print(string_val)
    "Element found: //div[@class='tabledata styles_default__3REJC' and contains(text(),'Overtime')]."
    if(add_activity_result==string_val):
        return True
    else:
        return False