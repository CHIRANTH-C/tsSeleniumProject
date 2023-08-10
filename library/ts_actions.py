import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from constants.xpath.xpath_dynamic import create_new_dynamic_xpath
from library.basic_functions import *
from constants.xpath.solution import *
from constants.xpath.timesheet import *

def edit_ts_entry(driver , tech_name):
    wait_until_element_is_visible(driver,create_new_dynamic_xpath(ts_date_row ,tech_name))
    hover_over_on_element(driver,create_new_dynamic_xpath(ts_date_row ,tech_name))
    wait_until_element_is_visible(driver,edit_icon)
    click_element(driver,edit_icon)
    time.sleep(10)
    result = wait_until_element_is_visible(driver,txt_edit_timesheet)
    return result

      
def handel_override_pop_up(driver, conflict_pop_up):
    wait_until_element_is_visible(driver , conflict_pop_up)
    wait_until_element_is_visible(driver , btn_override)
    click_element(driver , btn_override)

def add_activity(driver, start_hrs , start_mins , end_hrs , end_mins):
    wait_until_element_is_visible(driver , btn_add_new_activity)
    click_element(driver , btn_add_new_activity)
    time.sleep(10)
    wait_until_element_is_visible(driver , select_activity_drop_down)
    click_element(driver , select_activity_drop_down)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(select_specific_activity,"Overtime"))
    click_element(driver , create_new_dynamic_xpath(select_specific_activity,"Overtime"))
   
    wait_until_element_is_visible(driver , activity_start_time)
    click_element(driver , activity_start_time)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_hrs,1))
    click_element(driver , create_new_dynamic_xpath(txt_input_hrs,1))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_hrs,1) , start_hrs)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_mins,1))
    click_element(driver, create_new_dynamic_xpath(txt_input_mins,1))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_mins,1) , start_mins)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(toggle_am_pm,1))
    click_element(driver , create_new_dynamic_xpath(toggle_am_pm,1))
   
    wait_until_element_is_visible(driver , activity_end_time)
    click_element(driver , activity_end_time)
    time.sleep(5)
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_hrs,2))
    click_element(driver , create_new_dynamic_xpath(txt_input_hrs,2))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_hrs,2) , end_hrs)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_mins,2))
    click_element(driver, create_new_dynamic_xpath(txt_input_mins,2))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_mins,2) , end_mins)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(toggle_am_pm,2))
    click_element(driver , create_new_dynamic_xpath(toggle_am_pm,2))
   
    wait_until_element_is_visible(driver , btn_save)
    click_element(driver , btn_save)
   
    time.sleep(5)

    handel_override_pop_up(driver, time_range_conflict_pop_up)    

    result=wait_until_element_is_visible(driver , create_new_dynamic_xpath(activity_entry,"Overtime"))
    return result

def add_activity_and_handle_conflict(driver,activity_name, start_hrs , start_mins , end_hrs , end_mins , conflict_pop_up , isAM , isTaskType, task_id):
    
    # click on add new activity button
    wait_until_element_is_visible(driver , btn_add_new_activity)
    click_element(driver , btn_add_new_activity)
    time.sleep(10)

    # Click on activity drop down
    wait_until_element_is_visible(driver , select_activity_drop_down)
    click_element(driver , select_activity_drop_down)
   

    # Choose the <activity_name> from the drop down
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(select_specific_activity,activity_name))
    click_element(driver , create_new_dynamic_xpath(select_specific_activity,activity_name))
   

    if(isTaskType==True):
          wait_until_element_is_visible(driver,task_id_drop_down)
          click_element(driver,task_id_drop_down)
          wait_until_element_is_visible(driver,create_new_dynamic_xpath(select_specific_task_id,task_id))
          click_element(driver , create_new_dynamic_xpath(select_specific_task_id,task_id))

    # set the start time 
    wait_until_element_is_visible(driver , activity_start_time)
    click_element(driver , activity_start_time)
   

    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_hrs,1))
    click_element(driver , create_new_dynamic_xpath(txt_input_hrs,1))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_hrs,1) , start_hrs)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_mins,1))
    click_element(driver, create_new_dynamic_xpath(txt_input_mins,1))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_mins,1) , start_mins)
   

    if(isAM == True):
            wait_until_element_is_visible(driver , create_new_dynamic_xpath(toggle_am_pm,1))
            click_element(driver , create_new_dynamic_xpath(toggle_am_pm,1))

   

    # set the start time 
    wait_until_element_is_visible(driver , activity_end_time)
    click_element(driver , activity_end_time)
    time.sleep(5)
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_hrs,2))
    click_element(driver , create_new_dynamic_xpath(txt_input_hrs,2))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_hrs,2) , end_hrs)
   
    wait_until_element_is_visible(driver , create_new_dynamic_xpath(txt_input_mins,2))
    click_element(driver, create_new_dynamic_xpath(txt_input_mins,2))
    enter_text_in_element(driver , create_new_dynamic_xpath(txt_input_mins,2) , end_mins)
   
    if(isAM == True):
            wait_until_element_is_visible(driver , create_new_dynamic_xpath(toggle_am_pm,2))
            click_element(driver , create_new_dynamic_xpath(toggle_am_pm,2))
   
    # Save the activity
    wait_until_element_is_visible(driver , btn_save)
    click_element(driver , btn_save)

    time.sleep(5)

    # handle over ride pop up
    handel_override_pop_up(driver, conflict_pop_up)    

    result=wait_until_element_is_visible(driver , create_new_dynamic_xpath(activity_entry,activity_name))
    return result

def submit_ts(driver):
     wait_until_element_is_visible(driver,btn_save)
     click_element(driver,btn_save)
     time.sleep(5)
     wait_until_element_is_visible(driver,btn_continue)
     click_element(driver,btn_continue)
     return True

def navigate_to_page(driver, ts_page_xpath):
     wait_until_element_is_visible(driver,ts_page_xpath)
     click_element(driver,ts_page_xpath)

def approve_ts(driver):
     wait_until_element_is_visible(driver,approve_reject_drop_down)
     click_element(driver,approve_reject_drop_down)
     wait_until_element_is_visible(driver,approve_reject_drop_down_approve)
     click_element(driver,approve_reject_drop_down_approve)
     wait_until_element_is_visible(driver,btn_approve_pending)
     click_element(driver,btn_approve_pending)

def reject_ts(driver):
     wait_until_element_is_visible(driver,approve_reject_drop_down)
     click_element(driver,approve_reject_drop_down)
     wait_until_element_is_visible(driver,approve_reject_drop_down_reject)
     click_element(driver,approve_reject_drop_down_reject)
     wait_until_element_is_visible(driver,txt_area_reject_reason)
     click_element(driver,txt_area_reject_reason)
     enter_text_in_element(driver,txt_area_reject_reason,"Rejected")
     wait_until_element_is_visible(driver,btn_reject_pending)
     click_element(driver,btn_reject_pending)
