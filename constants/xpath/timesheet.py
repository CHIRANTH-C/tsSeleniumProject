from constants.data.filter_data_set import month , date , year
# from library.search_filter import month , date
# selected_month = str(month)
# selected_date = str(date)
# selected_year = str(year)

# Xpaths for search component
search="//input[@type='search']"
search_n="//input[@placeholder='Start typing to search...']"
empty_msg="//p[contains(text(),'SORRY! YOUR SEARCH RESULTS CAME UP EMPTY')]"

# Xpaths for date filter component
from_date="//input[@id='fromDate']/following-sibling::input"
to_date="//input[@id='toDate']/following-sibling::input"
month_drop_down="//select[@class='flatpickr-monthDropdown-months']"
month_drop_down_2="(//select[@class='flatpickr-monthDropdown-months'])[{}]"
month_drop_down_selection="//select[@class='flatpickr-monthDropdown-months']/child::option[contains(text(),'{}')]"
# month_drop_down_selection_2="(//select[@class='flatpickr-monthDropdown-months']/child::option[contains(text(),'{}')])[2]"
month_drop_down_selection_2="(//select[@class='flatpickr-monthDropdown-months']/child::option[contains(text(),'{}')])[{}]"
txt_input_year="//input[@class='numInput cur-year']"
txt_input_year_2="(//input[@class='numInput cur-year'])[{}]"
# select_date="//span[@class='flatpickr-day today' and text()='" +selected_date+ "']"
select_date="//span[@class='flatpickr-day today' and text()='{}']"
select_date_2="(//span[@class='flatpickr-day today' and text()='{}'])[{}]"

# Xpaths for ts list
ts_name_row="//div[text()='Chiranth As Tech 4']"
ts_date_row="//div[text()='07-08-2023']"

# Xpaths for technician 
ts_tech_drop_down="//button[@type='button']//child::span[contains(text(),'All')]"
btn_clear_all="//button[contains(text(),'Clear All')]"
txt_input_search_tech="//input[@type='search' and @placeholder='Search']"
check_box_select="//label[text()='Chiranth As Tech 4']"
btn_apply="//button[contains(text(),'Apply')]"
edit_icon="//span[@class='icon-edit']"
txt_edit_timesheet="//div[contains(text(),'Edit Timesheet')]"

# Xpaths for adding activity
btn_add_new_activity="//button[@id='addNew']"
select_activity_drop_down="//select[@id='ActivityDropdown']"
select_specific_activity="//select[@id='ActivityDropdown']//child::option[text()='Overtime']"
activity_start_time="//input[@id='activityStartTime']"
activity_end_time="//input[@id='activityEndTime']"

txt_input_hrs="//input[@class='numInput flatpickr-hour' and @aria-label='Hour']"
txt_input_mins="//input[@class='numInput flatpickr-minute' and @aria-label='Minute']"
toggle_am_pm="//span[@title='Click to toggle' and contains(text(),'PM')]"


txt_input_hrs_2="(//input[@class='numInput flatpickr-hour' and @aria-label='Hour'])[2]"
txt_input_mins_2="(//input[@class='numInput flatpickr-minute' and @aria-label='Minute'])[2]"
toggle_am_pm_2="(//span[@title='Click to toggle'])[2]"

btn_save="//button[@id='Submit']"

activity_entry="//div[@class='tabledata styles_default__3REJC' and contains(text(),'Overtime')]"