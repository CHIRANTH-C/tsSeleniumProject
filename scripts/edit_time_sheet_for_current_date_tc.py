## TS TEST CASE 1 ##
## Edit time sheet and add all type of activities
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from library.search_filter import searchts
from library.basic_functions import wait_until_element_is_visible , click_element
from library.ts_actions import add_activity, edit_ts_entry
from constants.xpath.timesheet import *
from constants.xpath.solution import *
from scripts.search_ts_with_invalied_tech import *

def edit_time_sheet_for_current_date(driver, tech_name):
    click_element(driver,nav_bar_ts)
    time.sleep(10)
    from_filter_result=filter_from_date(driver)
    from_to_result=filter_to_date(driver)
    drop_down_result=drop_down(driver)
    print(from_filter_result)
    print(from_to_result)
    print(drop_down_result)
    
    result_name_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , tech_name))
    print(result_name_selected)
    result_date_selected = wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row , tech_name))
    print(result_date_selected)
    time.sleep(10)
    
    edit_result = edit_ts_entry(driver , tech_name)
    print(edit_result)

    add_activity_result=add_activity(driver, "01", "00","02","00")
    print(add_activity_result)

    if(add_activity_result=="Element found: //div[@class='tabledata styles_default__3REJC' and contains(text(),'Overtime')]."):
        return True
    else:
        return False