from operator import index
import re
from time import sleep
import time
from tkinter import Button, Entry, Label, Tk
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import traceback


def setup_driver():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Create a Chrome WebDriver instance and maximize the window
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def navigate_to_login(driver):
    # Navigate to the login page
    driver.get("https://beta.peerprofiler.com/login")
    time.sleep(5)

def fill_login_credentials(driver):
    # Fill in the username and password fields
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    username_field.send_keys("Pgadmin2020")
    password_field.send_keys("PG@AdminKoLsNew")
    
    # Click the login button
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(20)
    
##########################################################################################################################################################################3

# clinical trial Tab
def clinical_trial(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[3]/li[1]/div[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(5)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[2]")))
    if Title_Validation:
            print("Title 'Add clinical trial' Tab open")
    else:
            print("Title 'Add clinical trial'Tab Not open")
            time.sleep(2)
            
# title page validation           
    actual_title_pg = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Add Clinical Trials')])[1]")))
    if actual_title_pg:
            print(" 'Add clinical trials' page is visible")
    else:
            print("'Add clinical trials' page is not visible")
            
            
# Doctor Name tab(DD)
def select_dropdown_by_index(driver, dropdown_id, index):
    try:
        # Wait for the dropdown to be present
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, dropdown_id)))
        
        # Create a Select object from the dropdown element
        DD = Select(dropdown)
        
        # Validate the index
        options_count = len(DD.options)
        if index >= options_count:
            print(f"Index {index} is out of range. The dropdown has {options_count} options.")
            return

        # Select the option by index
        DD.select_by_index(index)
        
        # Wait for the selection to be processed (if necessary)
        time.sleep(3)
        
        # Validate that the correct option is selected
        selected_option = DD.first_selected_option
        selected_text = selected_option.text

        print(f"Selected option is: {selected_text}")
        print("Validation Successful!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
 # Title Tab
    title_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "title0")))
    title_tab.click()
    title_tab.send_keys("Biology")
    
    title_name= driver.find_element(By.XPATH, "(//span[contains(@class,'p-0 m-0')])[1]")                                          
    if title_name:
            print("valid tab name as 'title' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)   
        
# Trial ID Tab

    trialID_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='Trial_ID0'])[1]")))
    trialID_tab.click()
    trialID_tab.send_keys("TC_120ac")
    
    tab_name= driver.find_element(By.XPATH, "//span[normalize-space()='Trial ID']")                                          
    if title_name:
            print("valid tab name as 'Trial ID' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)   
        
# Start Date Tab
    Start_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='startdate0']")))
    Start_date.click()
    Start_date.send_keys("05/12/2024")
    
    date_patterns = {
    "YYYY-MM-DD": r'^\d{4}-\d{2}-\d{2}$',
    "MM/DD/YYYY": r'^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/(\d{4})$',
    "DD-MM-YYYY": r'^([0-2][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$',
    "YYYY/MM/DD": r'^\d{4}/\d{2}/\d{2}$',
    "DD/MM/YYYY": r'^([0-2][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$',
    "MM-DD-YYYY": r'^(0[1-9]|1[0-2])-([0-2][0-9]|3[01])-(\d{4})$' ,
    "MM-Jun-YY" : r'^\d{1,2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2}$'
}
    print("Name::",Start_date.get_attribute("placeholder"))
    # Check the input date against all patterns and find a match
    matched_pattern = None
    for pattern_name, pattern in date_patterns.items():
        if re.match(pattern, Start_date):
            matched_pattern = pattern_name
        break

    if matched_pattern:
        print(f'Date input validation successful and matches the pattern: {matched_pattern}.')
    else:
        print('Date input validation failed or does not match any pattern.')

    
# End Date Tab
    End_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='enddate0']")))
    End_date.click()
    End_date.send_keys("05/25/2024") 
    print("Name::",End_date.get_attribute("placeholder"))

    time.sleep(3)
   
    
# Status Tab
    Status_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='trialstatus0']")))
    Status_tab.click()
    Status_tab.send_keys("Not Completed")
    print("Name::",Status_tab.get_attribute("placeholder"))

    time.sleep(5)

    
# Trial Type Tab
    trial_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='trialtype0']")))
    trial_tab.click()
    trial_tab.send_keys("demo") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, trial_tab):
        print('Trial- Type validation successful and matches the date pattern.')
    else:
        print('Trial -Type validation failed or does not match the date pattern.')

    print("Name::",trial_tab.get_attribute("placeholder"))
       
    time.sleep(4)

# Sponsor Tab
    sponsor_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='selectbyidsponser1name0']")))
    sponsor_tab.click()
    sponsor_tab.send_keys("ABAcd123", " ,", "asdfff") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, sponsor_tab):
        print('Sponsor validation successful and matches the date pattern.')
    else:
        print('Sponsor validation failed or does not match the date pattern.')

    print("Name::",sponsor_tab.get_attribute("placeholder"))
    Title_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sponsor']")))
    print("Name::",Title_name)

    time.sleep(4)
        
# Product Name Tab
    product_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='productname0'])[1]")))
    product_tab.click()
    product_tab.send_keys("ABAcd123", " ,", "asdfff") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, product_tab):
        print('Product Name validation successful and matches the date pattern.')
    else:
        print('Product Name validation failed or does not match the date pattern.')

    print("Name::",product_tab.get_attribute("placeholder"))
    time.sleep(4)    

# Indicator Name Tab
    indicator_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='selectbyidindicators1name0'])[1]")))
    indicator_tab.click()
    indicator_tab.send_keys("muscle pain", " ,", "Covid-19") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, sponsor_tab):
        print('Indicator validation successful and matches the date pattern.')
    else:
        print('indicator validation failed or does not match the date pattern.')

    print("Name::",indicator_tab.get_attribute("value"))
    Title_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Indicators']")))
    print("Name::",Title_name)

    
    time.sleep(4)    
        

# Function to check if a URL is valid
def is_valid_url(url):
    regex = re.compile(
        r'^(https?|ftp):\/\/'  # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def validate_reference_url(driver):

        # Refrence Link Tab
        Ref_url_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='reflink10'])[1]")))
        Ref_url_tab.click()

        # Enter the URL into the input field
        url_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@id='reflink10'])[1]")))
        url_to_enter = "https://example.com" 
        url_input.clear()
        url_input.send_keys(url_to_enter)
        print("Name::",url_input.get_attribute("placeholder"))

        
        # Validate the entered URL
        entered_url = url_input.get_attribute('value')
        if is_valid_url(entered_url):
            print(f"Entered URL is valid: {entered_url}")
            print("Validation Successful!")
        else:
            print(f"Entered URL is invalid: {entered_url}")
            print("Validation Failed!")
            time.sleep(4)     
########################################################################################################################

# Sceientific title tab
def scientific_study(driver):
    
    Sci_title_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='scientifictitle0']")))
    Sci_title_tab.click()
    Sci_title_tab.send_keys("biological study") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Sci_title_tab):
        print('Scientific Study validation successful and matches the date pattern.')
    else:
        print('Scientific Study validation failed or does not match the date pattern.')

    print("Name::",Sci_title_tab.get_attribute("placeholder"))
    time.sleep(4)   

# Phase title tab   
    Phase_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='phase0'])[1]")))
    Phase_tab.click()
    Phase_tab.send_keys("phase 2",",","phase 3") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Sci_title_tab):
        print('Phase title validation successful and matches the date pattern.')
    else:
        print('Phase title validation failed or does not match the date pattern.')
    print("Name::",Phase_tab.get_attribute("placeholder"))
    time.sleep(4)   
    

# Role tab   
    role_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='role0'])[1]")))
    role_tab.click()
    role_tab.send_keys("Investigator") 
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, role_tab):
        print('Role validation successful and matches the date pattern.')
    else:
        print('Role validation failed or does not match the date pattern.')
        
    print("Name::",role_tab.get_attribute("placeholder"))
    time.sleep(4)   
 
####################################################################################################################
# Function to fetch valid countries from an API
def fetch_valid_countries():
    response = requests.get('https://restcountries.com/v3.1/all', timeout=30)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    countries = response.json()
    country_names = [country['name']['common'] for country in countries]
    return country_names
    

# Function to validate the entered country name
def validate_country_name(driver, valid_countries):
        # Locate and click the Countries tab
        countries_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='selectbyidcountries1name0']")))
        countries_tab.click()
        print("Name::",countries_tab.get_attribute("placeholder"))


        # Enter the country name into the input field
        country_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "selectbyidcountries1name0")))
        country_input.send_keys("United Kingdom")
        
        # Validate the entered country name
        entered_country = country_input.get_attribute('value')
        if entered_country in valid_countries:
            print(f"Entered country name is valid: {entered_country}")
        else:
            print(f"Entered country name is invalid: {entered_country}")
    
# Title Description tab   
        title_des_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='trialdescription0']")))
        title_des_tab.click()
        title_des_tab.send_keys("biological study: in Covid -19 micro-viruses") 
        
        
        print("Name::",title_des_tab.get_attribute("placeholder"))
        time.sleep(4)   
 
        
# Title Colabrator or Investigator tab   
        title_des_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='selectbyidcollaboratorsorcoinvestigators1name0']")))
        title_des_tab.click()
        title_des_tab.send_keys("Abcd123",",","fgdFCF") 
        
        pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
        if re.match(pattern, title_des_tab):
            print('Title Colabrator or Investigator validation successful and matches the date pattern.')
        else:
             print('Title Colabrator or Investigator validation failed or does not match the date pattern.')
             
        Title_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Collaborators or Co-Investigators'])[1]")))
        print("Name::",Title_name)
        time.sleep(4)   
        
# Keywords Tab
        keywords_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectbyidkeywordsclinicaltrials1name0")))
        keywords_tab.click()
        keywords_tab.send_keys("MST", " ,", "dcid") 
        
        pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
        if re.match(pattern, title_des_tab):
            print('Keywords validation successful and matches the date pattern.')
        else:
             print('Keywords validation failed or does not match the date pattern.')
             
        print("Name::",keywords_tab.get_attribute("value"))
        Title_name = driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[16]")
        print("Name::",Title_name)
        time.sleep(10)
########################################################################################################################################################
# tabular view validation
def tabularView(driver):
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[3]/li[1]/div[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Clinical Trials" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Clinical Trials'])[1]")))
    if back_to_origin:
            print("'All clinical Trials' title tab visible")
    else:
            print("'All clinical Trials' title tab not visible")    
        
        
   
########################################################################################################################################            
        
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # clinical trial Tab
        clinical_trial(driver)
        
        #select doctor dropdown
        dropdown_id = "doctor_select_field_id"
        index_to_select = 1  
        select_dropdown_by_index(driver, dropdown_id, index_to_select)
        
        # Validation of refrence URl links
        validate_reference_url(driver)
        
        # Sceientific title tab
        scientific_study(driver)
        
    # Fetch the valid countries from the API
        valid_countries = fetch_valid_countries()

        if valid_countries:
        # Validate the countries tab and entered country name
            validate_country_name(driver, valid_countries)
            
     # tabular view validation
        tabularView(driver)       

        #close the window
        #driver.quit()
    
        