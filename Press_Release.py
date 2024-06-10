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
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(20)
    
    
##########################################################################################################################################################################3

# Press_Release Tab
def Press_Release(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[6]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(5)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/ol[1]/li[3]/button[1]/span[1]")))
    if Title_Validation:
            print("Title 'Add Press Releaase' Tab open")
    else:
            print("Title 'Add Press Release'Tab Not open")
            time.sleep(2)
            
# Doctor Name tilte validation           
    doctor_name = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='Doctor Name'])[1]")))
    if doctor_name:
            print(" 'Doctor Name' page is visible")
    else:
            print("'Doctor Name' page is not visible")
            
            
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

               
# Publications Tab

    publication = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publication0")))
    publication.click()
    publication.send_keys("PharmaStar")
    
    tab_name= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Publications' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)  
            
# Press Release Title Tab
    pre_rel_tit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pressreleasetitle0")))
    pre_rel_tit.click()
    pre_rel_tit.send_keys("PharmaStar")
    
    tab_name= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Press Release Title' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)  
            
# Type Tab
    type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pressreleasetype0")))
    type.click()
    type.send_keys("class-1")
    
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Type'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Type' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)               
                
# Start Date Tab
    Start_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "date0")))
    Start_date.click()
    Start_date.send_keys("05/12/2024")
    print("Name::",Start_date.get_attribute("placeholder"))
    # Extract the date text
    date_text = Start_date.text

# Define the date pattern (example: MM/DD/YYYY)
    date_pattern = r"^\d{2}/\d{2}/\d{4}$"

# Validate the date pattern using regex
    if re.match(date_pattern, date_text):
        print(f"Date '{date_text}' is valid.")
    else:
        print(f"Date '{date_text}' is invalid.")
    
# indications Tab
    indication = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "indicationsname0")))
    indication.click()
    indication.send_keys("05/25/2024") 
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Indication'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Indication' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
   
   
    
# Company Name Tab
    company_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "companyname0")))
    company_name.click()
    company_name.send_keys("TCS")
    print("Name::",company_name.get_attribute("placeholder"))
    time.sleep(5)

    
# Product Name Tab
    product_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "productname0")))
    product_name.click()
    product_name.send_keys("demo") 
    print("Name::",product_name.get_attribute("placeholder"))
       
    time.sleep(4)

# Name of Co-Author Tab
    co_author = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nameofcoauthors0")))
    co_author.click()
    co_author.send_keys("RAmesh", " ,", "Suresh") 
    
    tab_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Name of the Co-Authors'])[1]")))
    if tab_name:
            print("valid tab name as 'Name of Co-Author' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
        
# KeyTerm Tab
    keyterm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "keywords0")))
    keyterm.click()
    keyterm.send_keys("ABAcd123", " ,", "asdfff") 
    tab_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Key Terms'])[1]")))
    if tab_name:
            print("valid tab name as 'Key Term' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)    

# Abstract Tab
    abstract = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "abstract0")))
    abstract.click()
    abstract.send_keys("muscle pain", "A34@#", "Covid-19") 
    
   
            
# Topic tab
    
    topic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "topic0")))
    topic.click()
    topic.send_keys("biological study") 
    tab_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-0 m-0'])[11]")))
    if tab_name:
            print("valid tab name as 'Topic' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)            
                 
####################################################################################################################################################        

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
        countries_tab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "countryname0")))
        countries_tab.click()
        print("Name::",countries_tab.get_attribute("placeholder"))


        # Enter the country name into the input field
        country_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "countryname0")))
        country_input.send_keys("United Kingdom")
        
        # Validate the entered country name
        entered_country = country_input.get_attribute('value')
        if entered_country in valid_countries:
            print(f"Entered country name is valid: {entered_country}")
        else:
            print(f"Entered country name is invalid: {entered_country}")
 
########################################################################################################################################################            
 
# Refrence UrL
def Refrence_url(driver):

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reflink10"))).click()
                                      
     # Enter the URL_1 into the input field
    url_input= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "reflink10")))
    url_input.send_keys("https://example.com")
    print("Name::",url_input.get_attribute("placeholder"))
            
    # Validate the entered URL
    entered_url = url_input.get_attribute('value')
    if is_valid_url(entered_url):
        print(f"Entered URL is valid: {entered_url}")
    else:
        print(f"Entered URL is invalid: {entered_url}")
        time.sleep(4)    

########################################################################################################################################            

# tabular view validation
def tabularView(driver):
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[6]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Press Release" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Press Releases'])[1]")))
    if back_to_origin:
            print("'All Press Release' title tab visible")
    else:
            print("'All Press Release' title tab not visible")    
        
                   
########################################################################################################################################            
        
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # clinical trial Tab
        Press_Release(driver)
        
        #select doctor dropdown
        dropdown_id = "doctor_select_field_id"
        index_to_select = 1  
        select_dropdown_by_index(driver, dropdown_id, index_to_select)
        
        # Validation of refrence URl links
        validate_reference_url(driver)
        
        # Fetch the valid countries from the API
        valid_countries = fetch_valid_countries()

        if valid_countries:
        # Validate the countries tab and entered country name
            validate_country_name(driver, valid_countries)
    
        # Refrence UrL
        Refrence_url(driver)
                
        # tabular view validation
        tabularView(driver)       

        #close the window
        #driver.quit()
    
        