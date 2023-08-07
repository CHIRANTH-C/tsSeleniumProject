import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.basic_functions import *
from constants.xpath.solution import *
from constants.xpath.timesheet import *
from constants.xpath.xpath_dynamic import create_dynamic_xpath , create_dynamic_xpath_2

def searchts(driver):
    wait_until_element_is_visible(driver,search_n)
    click_element(driver,search_n)
    enter_text_in_element(driver,search_n,"Chiranth New")

def filter_from_date(driver):
    wait_until_element_is_visible(driver,from_date)
    click_element(driver,from_date)
    wait_until_element_is_visible(driver,create_dynamic_xpath_2(month_drop_down_selection_2 , "August" , 1))
    click_element(driver,create_dynamic_xpath_2(month_drop_down_selection_2 , "August" ,1))
    click_element(driver,create_dynamic_xpath(txt_input_year_2,1))
    enter_text_in_element(driver,create_dynamic_xpath(txt_input_year_2,1),year)
    wait_until_element_is_visible(driver,create_dynamic_xpath_2(select_date_2 , "7" , 1))
    click_element(driver,create_dynamic_xpath_2(select_date_2 , "7" , 1))

# def filter_from_date(driver):
#     wait_until_element_is_visible(driver,from_date)
#     click_element(driver,from_date)
#     wait_until_element_is_visible(driver,create_dynamic_xpath(month_drop_down_selection, "August"))
#     click_element(driver,create_dynamic_xpath(month_drop_down_selection, "August"))
#     click_element(driver,txt_input_year)
#     enter_text_in_element(driver,txt_input_year,"2023")
#     wait_until_element_is_visible(driver,create_dynamic_xpath(select_date, "7"))
#     click_element(driver,create_dynamic_xpath(select_date, "7"))


def filter_to_date(driver):
    wait_until_element_is_visible(driver,to_date)
    click_element(driver,to_date)
    wait_until_element_is_visible(driver,create_dynamic_xpath_2(month_drop_down_selection_2 , "August" , 2))
    click_element(driver,create_dynamic_xpath_2(month_drop_down_selection_2 , "August" , 2))
    click_element(driver,create_dynamic_xpath(txt_input_year_2,2))
    enter_text_in_element(driver,create_dynamic_xpath(txt_input_year_2,2),year)
    wait_until_element_is_visible(driver,create_dynamic_xpath_2(select_date_2 , "7" , 2))
    click_element(driver,create_dynamic_xpath_2(select_date_2 , "7" , 2))


def drop_down(driver):
    wait_until_element_is_visible(driver,ts_tech_drop_down)
    click_element(driver , ts_tech_drop_down)
    wait_until_element_is_visible(driver,btn_clear_all)
    click_element(driver, btn_clear_all)
    wait_until_element_is_visible(driver,txt_input_search_tech)
    click_element(driver,txt_input_search_tech)
    enter_text_in_element(driver,txt_input_search_tech,'Chiranth As Tech 4')
    wait_until_element_is_visible(driver,check_box_select)
    click_element(driver,check_box_select)
    result = wait_until_element_is_visible(driver,btn_apply)
    click_element(driver,btn_apply)
    time.sleep(5)
    return result
