import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import *
from constants.xpath.solution import *
from constants.xpath.timesheet import *


# def hover_over_on_ts_entry(driver):
#     wait_until_element_is_visible(driver,ts_date_row)
#     hover_over_on_element(driver,ts_date_row)
#     time.sleep(10)

def edit_ts_entry(driver):
    wait_until_element_is_visible(driver,ts_date_row)
    hover_over_on_element(driver,ts_date_row)
    wait_until_element_is_visible(driver,edit_icon)
    click_element(driver,edit_icon)
    time.sleep(10)
    result = wait_until_element_is_visible(driver,txt_edit_timesheet)
    return result

def add_activity(driver):
    wait_until_element_is_visible(driver , btn_add_new_activity)
    click_element(driver , btn_add_new_activity)
    time.sleep(10)
    wait_until_element_is_visible(driver , select_activity_drop_down)
    click_element(driver , select_activity_drop_down)
    # time.sleep(5)
    wait_until_element_is_visible(driver , select_specific_activity)
    click_element(driver , select_specific_activity)
    # time.sleep(5)
    wait_until_element_is_visible(driver , activity_start_time)
    click_element(driver , activity_start_time)
    # time.sleep(5)
    wait_until_element_is_visible(driver , txt_input_hrs)
    click_element(driver , txt_input_hrs)
    enter_text_in_element(driver , txt_input_hrs , "01")
    # time.sleep(5)
    wait_until_element_is_visible(driver , txt_input_mins)
    click_element(driver, txt_input_mins)
    enter_text_in_element(driver , txt_input_mins , "00")
    # time.sleep(5)
    wait_until_element_is_visible(driver , toggle_am_pm)
    click_element(driver , toggle_am_pm)
    # time.sleep(5)
    wait_until_element_is_visible(driver , activity_end_time)
    click_element(driver , activity_end_time)
    time.sleep(5)
    wait_until_element_is_visible(driver , txt_input_hrs_2)
    click_element(driver , txt_input_hrs_2)
    enter_text_in_element(driver , txt_input_hrs_2 , "02")
    # time.sleep(5)
    wait_until_element_is_visible(driver , txt_input_mins_2)
    click_element(driver, txt_input_mins_2)
    enter_text_in_element(driver , txt_input_mins_2 , "00")
    # time.sleep(5)
    wait_until_element_is_visible(driver , toggle_am_pm_2)
    click_element(driver , toggle_am_pm_2)
    # time.sleep(5)
    wait_until_element_is_visible(driver , btn_save)
    click_element(driver , btn_save)
    # time.sleep(5)
    result=wait_until_element_is_visible(driver , activity_entry)
    return result


