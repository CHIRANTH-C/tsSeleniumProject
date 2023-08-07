import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import *
from constants.xpath.solution import *
from constants.xpath.timesheet import *
# from constants.data.filter_data_set import *

def searchts(driver):
    wait_until_element_is_visible(driver,search_n)
    click_element(driver,search_n)
    enter_text_in_element(driver,search_n,"Chiranth New")

def filter_from_date(driver):
    wait_until_element_is_visible(driver,from_date)
    click_element(driver,from_date)
    wait_until_element_is_visible(driver,month_drop_down_selection)
    click_element(driver,month_drop_down_selection)
    click_element(driver,txt_input_year)
    enter_text_in_element(driver,txt_input_year,year)
    wait_until_element_is_visible(driver,select_date)
    click_element(driver,select_date)
    # result_name_selected = wait_until_element_is_visible(driver,ts_name_row)
    # print(result_name_selected)
    # result_date_selected = wait_until_element_is_visible(driver,ts_date_row)
    # print(result_date_selected)


def filter_to_date(driver):
    wait_until_element_is_visible(driver,to_date)
    click_element(driver,to_date)
    wait_until_element_is_visible(driver,month_drop_down_selection_2)
    click_element(driver,month_drop_down_selection_2)
    click_element(driver,txt_input_year_2)
    enter_text_in_element(driver,txt_input_year_2,year)
    wait_until_element_is_visible(driver,select_date_2)
    click_element(driver,select_date_2)
#    result_name_selected = wait_until_element_is_visible(driver,ts_name_row)
#    print(result_name_selected)
#    result_date_selected = wait_until_element_is_visible(driver,ts_date_row)
#    print(result_date_selected)

def drop_down(driver):
    wait_until_element_is_visible(driver,ts_tech_drop_down)
    click_element(driver , ts_tech_drop_down)
    wait_until_element_is_visible(driver,btn_clear_all)
    click_element(driver, btn_clear_all)
    wait_until_element_is_visible(driver,txt_input_search_tech)
    click_element(driver,txt_input_search_tech)
    enter_text_in_element(driver,txt_input_search_tech,'Chiranth As Tech 4')
    # time.sleep(10)
    wait_until_element_is_visible(driver,check_box_select)
    click_element(driver,check_box_select)
    result = wait_until_element_is_visible(driver,btn_apply)
    click_element(driver,btn_apply)
    time.sleep(5)
    return result
