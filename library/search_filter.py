from library.basic_functions import *
from constants.xpath.solution import *
from constants.xpath.timesheet import *

def searchts(driver):
    wait_until_element_is_visible(driver,search_n)
    click_element(driver,search_n)
    enter_text_in_element(driver,search_n,"Chiranth New")