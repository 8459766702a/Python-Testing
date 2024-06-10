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
def Event_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[4]/li[1]/div[1]/div[1]")))
    click_menu.click()   
    time.sleep(10)
    
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]")))
    Add_record.click()
    time.sleep(5)
        
            
# Add Event title page validation           
    actual_title_pg = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add Events')]")))
    actual_title_pg.text
    if actual_title_pg:
            print(" 'Add Event' page is visible")
    else:
            print("'Add Event' page is not visible")
            
#######################################################################################################################################################            
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

        DD.select_by_index(index)
        time.sleep(3)
        
        # Validate that the correct option is selected
        selected_option = DD.first_selected_option
        selected_text = selected_option.text

        print(f"Selected option is: {selected_text}")
        print("Validation Successful!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

        time.sleep(2)   
            
# Event Name Tab
    Event_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "eventname0")))
    Event_Name.click()
    Event_Name.send_keys("Title:biology_01")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Event_Name):
        print(' Event Name validation successful and matches the date pattern.')
    else:
        print(' Event Name  validation failed or does not match the date pattern.')
    
    tab_name= driver.find_element(By.XPATH, "//span[normalize-space()='Event Name']")                                          
    if tab_name:
            print("valid tab name as 'Event Name' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)              
# Topic / subtopic Tab
    Top_sub = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "topicsubtopic0")))
    Top_sub.click()
    Top_sub.send_keys("general")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Top_sub):
        print(' Topic / subtopic validation successful and matches the date pattern.')
    else:
        print(' Topic / subtopic  validation failed or does not match the date pattern.')
    
    print("Name::",Top_sub.get_attribute("placeholder"))
    time.sleep(2)             


            
# Event Type Tab
    Event_type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "eventtype0")))
    Event_type.click()
    Event_type.send_keys("general")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Event_type):
        print(' Event Type validation successful and matches the date pattern.')
    else:
        print(' Event Type  validation failed or does not match the date pattern.')
    print("Name::",Event_type.get_attribute("placeholder"))
    time.sleep(2)             

# Role Tab
    Role = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "role0")))
    Role.click()
    Role.send_keys("general")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Role):
        print(' Role validation successful and matches the date pattern.')
    else:
        print(' Role validation failed or does not match the date pattern.')
    print("Name::",Event_type.get_attribute("placeholder"))
    time.sleep(2)
    print("Name::",Role.get_attribute("placeholder"))
    time.sleep(2)             

# Start Date Tab
    Start_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"startdate0")))
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
    End_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "enddate0")))
    End_date.click()
    End_date.send_keys("05/20/2024") 
    print("Name::",End_date.get_attribute("placeholder"))
                       
            
# Other participant Tab
    Other_part = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "participantsname0")))
    Other_part.click()
    Other_part.send_keys("N/a" " ," "sbshj")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Other_part):
        print(' Other participant validation successful and matches the date pattern.')
    else:
        print(' Other participant validation failed or does not match the date pattern.')
    print("Name::",Other_part.get_attribute("placeholder"))
    
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Other Participants'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Other Participant' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)   
    time.sleep(2)  
    
# Sponsors Tab
    sponsors = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sponsorname0")))
    sponsors.click()
    sponsors.send_keys("N/a" "," "sbshj")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, sponsors):
        print('sponsors validation successful and matches the date pattern.')
    else:
        print('sponsors validation failed or does not match the date pattern.')
        
    print("Name::",sponsors.get_attribute("placeholder"))
    
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Sponsor'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Sponsors  ' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)   
    time.sleep(2)     
               
     
# Keywords Tab
    Keywords = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "themename0")))
    Keywords.click()
    Keywords.send_keys("N/a" "," "covid-19")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Keywords):
        print('Keywords validation successful and matches the date pattern.')
    else:
        print('Keywords validation failed or does not match the date pattern.')
        
    print("Name::",Keywords.get_attribute("placeholder"))
    
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Key Words'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Keyword' visible")
    else:
            print("Invalid tab name")
    time.sleep(2)        
                                            
# Product NAme Tab
    Product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "productname0")))
    Product.click()
    Product.send_keys("N/a" "," "Machine")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, Product):
        print('Product validation successful and matches the date pattern.')
    else:
        print('Product validation failed or does not match the date pattern.')
        
    print("Name::",Keywords.get_attribute("placeholder"))
    print("Name::",Product.get_attribute("placeholder"))
                         
                                            
# Description Tab
    description = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Description0")))
    description.click()
    description.send_keys("N/a" "," "covid-19")
    
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
    if re.match(pattern, description):
        print('description validation successful and matches the date pattern.')
    else:
        print('description validation failed or does not match the date pattern.')
    print("Name::",description.get_attribute("placeholder"))
                
 # Region Tab
    Region = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "region0")))
    Region.click()
    Region.send_keys("navi-mumbai")
    print("Name::",Region.get_attribute("placeholder"))
    time.sleep(5)
                           
 # Location Tab
    location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "location0")))
    location.click()
    location.send_keys("Mumbai")
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Key Words'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Location' visible")
    else:
            print("Invalid tab name")   
            time.sleep(5)
    
############################################################################################################################

# Function to fetch valid countries from an API with retry logic
def fetch_valid_countries():
    urls = ['https://restcountries.com/v3.1/all', 'https://countriesnow.space/api/v0.1/countries']
    for url in urls:
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            if 'restcountries' in url:
                countries = response.json()
                country_names = [country['name']['common'] for country in countries]
            else:
                countries = response.json().get('data', [])
                country_names = [country['country'] for country in countries]
            return country_names
        except requests.exceptions.RequestException as e:
            print(f"Error fetching countries from {url}: {e}")
    raise Exception("Failed to fetch valid countries from all sources.")

# Function to fetch valid states for a given country from the API with retry logic
def fetch_valid_states(country_name):
    url = 'https://countriesnow.space/api/v0.1/countries/states'
    try:
        response = requests.post(url, json={"country": country_name}, timeout=20)
        response.raise_for_status()
        states = response.json().get('data', {}).get('states', [])
        return [state['name'] for state in states]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching states for {country_name}: {e}")
    raise Exception(f"Failed to fetch valid states for {country_name}.")

# Function to fetch valid cities for a given state and country from the API with retry logic
def fetch_valid_cities(country_name, state_name):
    url = 'https://countriesnow.space/api/v0.1/countries/state/cities'
    try:
        response = requests.post(url, json={"country": country_name, "state": state_name}, timeout=20)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cities for {state_name}, {country_name}: {e}")
    raise Exception(f"Failed to fetch valid cities for {state_name}, {country_name}.")

# Function to validate entered country, state, and city using API data
def validate_country_state_city(driver):
    try:
        # Fetch valid countries
        valid_countries = fetch_valid_countries()

        # Locate and click the Countries tab
        countries_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='countryname0'])[1]")))
        countries_tab.click()
        print("Name::", countries_tab.get_attribute("placeholder"))

        # Enter the country name into the input field
        country_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "countryname0")))
        country_input.send_keys("India")
        
        # Validate the entered country name
        entered_country = country_input.get_attribute('value')
        if entered_country in valid_countries:
            print(f"Entered country name is valid: {entered_country}")
        else:
            print(f"Entered country name is invalid: {entered_country}")
            return

        # Fetch valid states for the entered country
        valid_states = fetch_valid_states(entered_country)
        
        # Enter the state name into the input field
        state_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "statename0")))
        state_input.send_keys("Karnataka")

        # Validate the entered state name
        entered_state = state_input.get_attribute('value')
        if entered_state in valid_states:
            print(f"Entered state name is valid: {entered_state}")
        else:
            print(f"Entered state name is invalid: {entered_state}")
            return

        # Fetch valid cities for the entered state
        valid_cities = fetch_valid_cities(entered_country, entered_state)

        # Enter the city name into the input field
        city_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cityname0")))
        city_input.send_keys("Bangalore")

        # Validate the entered city name
        entered_city = city_input.get_attribute('value')
        if entered_city in valid_cities:
            print(f"Entered city name is valid: {entered_city}")
        else:
            print(f"Entered city name is invalid: {entered_city}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
###############################################################################################################################
 
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
        Ref_url_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reflink10")))
        Ref_url_tab.click()

        # Enter the URL_1 into the input field
        url_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "reflink10")))
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
            
         # Regestration Link Tab
        Ref_url_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "registrationurl0")))
        Ref_url_tab.click()
    
        # Enter the registration URL_1 into the input field
        url_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "registrationurl0")))
        url_to_enter = "example.com" 
        url_input.clear()
        url_input.send_keys(url_to_enter)
        print("Name::",url_input.get_attribute("placeholder"))    
         # Validate the entered Reg. URL
        entered_url = url_input.get_attribute('value')
        if is_valid_url(entered_url):
            print(f"Entered Reg.URL is valid: {entered_url}")
            print("Validation Successful!")
        else:
            print(f"Entered Reg.URL is invalid: {entered_url}")
            print("Validation Failed!")
            time.sleep(4)                                                                                  
                
            
            
            
            
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # clinical trial Tab
        Event_menu(driver) 
        
         #select doctor dropdown
        dropdown_id = "doctor_select_field_id"
        index_to_select = 2  
        select_dropdown_by_index(driver, dropdown_id, index_to_select)    
                        
        # Validate country, state, and city
        validate_country_state_city(driver)
        
        # Refrence Link Tab
        validate_reference_url(driver)
        