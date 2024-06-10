import re
from tkinter.tix import Select
import traceback
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

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
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        username_field.send_keys("Pgadmin2020")
        password_field.send_keys("PG@AdminKoLsNew")
        
        # Click the login button
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        time.sleep(25)
        
##############################################################################################################################################################################
# Press_Release Tab
def Associations_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[7]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(5)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/ol[1]/li[3]/button[1]/span[1]")))
    if Title_Validation:
            print("Title 'Add Association' Tab open")
    else:
            print("Title 'Add Association'Tab Not open")
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
    publication = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "associationname0")))
    publication.click()
    publication.send_keys("PharmaStar")
    
    tab_name= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Association' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 

# Department Tab
    Pub_Type= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "department0")))
    Pub_Type.click()
    Pub_Type.send_keys("general")
    print("Name::",Pub_Type.get_attribute("placeholder"))
    time.sleep(2)  
    

# Department Tab
    Pub_Type= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "position0")))
    Pub_Type.click()
    Pub_Type.send_keys("Sub-general")
    print("Name::",Pub_Type.get_attribute("placeholder"))
    time.sleep(2)  
    
#########################################################################################################################################################            

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
        
        
# Address line-1 field Tab
    address_element  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addressline10")))
    address_element.click()
    address_element.send_keys("choice amby smruti", " ,", "A1/2001") 
    address_text = address_element.get_attribute('value')    
    
    address_pattern = r'^[0-9a-zA-Z\s,.-]+$'
        
    if re.match(address_pattern, address_text ):
            print(f"Address  is valid.")
    else:
            print(f"Address is invalid.")  
                            
# Address line-2 field Tab
    address_element  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addressline20")))
    address_element.click()
    address_element.send_keys("rEESR", " ,", "RASAYANI") 
    address_text = address_element.get_attribute('value') 
    address_pattern = r'^[0-9a-zA-Z\s,.-]+$'  
        
    if re.match(address_pattern, address_text ):
            print(f"Address  is valid.")
    else:
            print(f"Address is invalid.")
            
            
# Pin Code field Tab
    pincode  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pincode0")))
    pincode.click()
    pincode.send_keys("411017") 
    pincode_text = address_element.get_attribute('value') 
    pincode_pattern = r'^\d{6}$'
        
    if re.match(address_pattern, address_text ):
            print(f"pincode  is valid.")
    else:
            print(f"pincode is invalid.")   
            
            
# tenurefrom Tab
    tenurefrom = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tenurefrom0")))
    tenurefrom.click()
    tenurefrom.send_keys("2022")
    print("Name::",tenurefrom.get_attribute("placeholder"))
    # Extract the date text
    date_text = tenurefrom.text
    date_pattern = r'^\d{4}$'
         
    if re.match(date_pattern, date_text ):
            print(f"tenurefrom  is valid.")
    else:
            print(f"tenurefrom is invalid.")   
                       
# tenureto Tab
    tenureto0 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tenureto0")))
    tenureto0.click()
    tenureto0.send_keys("2024")
    print("Name::",tenureto0.get_attribute("placeholder"))
    # Extract the date text
    date_text = tenurefrom.text
    date_pattern = r'^\d{4}$'
         
    if re.match(date_pattern, date_text ):
            print(f"tenureto  is valid.")
    else:
            print(f"tenureto is invalid.")               

# Socity Type Tab
    socity_type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "typeassociations0")))
    socity_type.click()
    socity_type.send_keys("class-1")
    print("Name::",socity_type.get_attribute("placeholder"))
    time.sleep(5)

# National/ International Tab
    Nat_Inter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]")))
    Nat_Inter.click()
    Nat_Inter.send_keys("class-1")
    print("Name::",Nat_Inter.get_attribute("placeholder"))
    time.sleep(5)

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
    
    
# validation of reference url
def validate_reference_url(driver):

        # Refrence Link Tab
        Ref_url_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reflink10")))
        Ref_url_tab.click()

        # Enter the URL into the input field
        url_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "reflink10")))
        url_to_enter = "https://example.com" 
        url_input.clear()
        url_input.send_keys(url_to_enter)
        print("Name::",url_input.get_attribute("placeholder"))

#  check box validation           
        check_box = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[16]")))
        
        if check_box:
            print(" 'check_box Name' page is visible")
        else:
            print("'check_box Name' page is not visible")
         
        check_box_1 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[16]/label[1]")))
        check_box_1 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[16]/label[1]/input[1]"))).click()

########################################################################################################################################            

# tabular view validation
def tabularView(driver):
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[7]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Press Release" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Associations'])[1]")))
    if back_to_origin:
            print(" 'All Associations' title tab visible")
    else:
            print(" 'All Associations' title tab not visible")            
                
###############################################################################################################################

if __name__ == "__main__":
    # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver)
    
    # All Events Tab
    Associations_menu(driver)

    #select doctor dropdown
    dropdown_id = "doctor_select_field_id"
    index_to_select = 2  
    select_dropdown_by_index(driver, dropdown_id, index_to_select)
    
   # Validate country, state, and city
    validate_country_state_city(driver)
    
    # validation of reference url
    validate_reference_url(driver)
    
    # Optionally, close the driver
    driver.quit()
       
            
            


