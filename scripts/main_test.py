import sys
import os
import time
# sys.path.insert(0, '/Users/chiranth.c/Documents/tsSeleniumProject/constants/xpath')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from library.authmodule import login
from scripts.edit_time_sheet_for_current_date_tc import edit_time_sheet_for_current_date
from scripts.edit_time_sheet_and_add_all_activites_tc import edit_time_sheet_and_add_all_activites
from scripts.submit_ts_for_approval_tc import submit_ts_for_approval
from scripts.approve_the_time_sheet_tc import approve_the_time_sheet 
from scripts.reject_the_time_sheet_tc import reject_the_time_sheet 
from library.ts_actions import submit_ts
from constants.xpath.timesheet import *

def main():
    driver =  login("")
    time.sleep(10)

    # calling 1st test case to run


    # Tested
    # result = edit_time_sheet_for_current_date(driver)
    # result = edit_time_sheet_and_add_all_activites(driver,"Chiranth As Tech 4" , "Task", "07", "00" ,"09","00", long_duration_than_task_pop_up , False , True, "TSK000016")
    # result = edit_time_sheet_and_add_all_activites(driver , "Chiranth As Tech 4" , "Overtime", "01", "00" ,"02","00" ,time_range_conflict_pop_up, True)
    # result = edit_time_sheet_and_add_all_activites(driver, "Chiranth As Tech 4" , "Overtime", "01", "00" ,"02","00",inside_shift_range_conflict_pop_up,False)
    # result = submit_ts_for_approval(driver , "Chiranth As Tech 4")
    # result = approve_the_time_sheet(driver , "Chiranth As Tech 4")
    result = reject_the_time_sheet(driver , "Chiranth As Tech 4")

    result = True
    if(result):
        print("Successfully completed 1st test case automation")
    else:
        print("Sorry you are not lucky")
main()

