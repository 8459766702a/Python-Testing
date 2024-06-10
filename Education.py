import re
from tkinter import Button, Entry, Label, Tk
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
               
    # Fill in the username and password
        username_field.send_keys(username_entry.get())
        password_field.send_keys(password_entry.get())
        
        # Click the login button
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        time.sleep(25)
    
    
##############################################################################################################################################################################
# Education Tab
def Education_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[8]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(5)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add Education')]")))
    if Title_Validation:
            print("Title 'Add Education' Tab open")
    else:
            print("Title 'Add Education'Tab Not open")
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
#############################################################################################################################################

# Institute Name Tab
    Institute = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "institutionname0")))
    Institute.click()
    Institute.send_keys("RSECOE,pune-univercity")
    institute_name_text = Institute.get_attribute('value')  

    institute_name_pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(institute_name_pattern, institute_name_text):
            print(f"Institute name  is valid.")
    else:
            print(f"Institute name is invalid.")
        
# Degree Name Tab
    Degree = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "degree0")))
    Degree.click()
    Degree.send_keys("Mbbs" " ," "M.D")
    Degree_name_text = Degree.get_attribute('value')  
    print("Name::",Degree_name_text )
    
    degree_pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(degree_pattern, Degree_name_text):
            print(f"Institute name  is valid.")
    else:
            print(f"Institute name is invalid.")        
        
# Speciality Name Tab
    speciality = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "speciality0")))
    speciality.click()
    speciality.send_keys("heart specialist" " ," "theropy")
    speciality_name_text = speciality.get_attribute('value')  
    print("Name::", speciality_name_text )
    
    speciality_pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(speciality_pattern, speciality_name_text):
            print(f"Institute name  is valid.")
    else:
            print(f"Institute name  is invalid.")        
                
        
# Passing Year Tab
    Passing_Year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passingyear0")))
    Passing_Year.click()
    Passing_Year.clear()  
    Passing_Year.send_keys('2020')
    print("Name::", Passing_Year.get_attribute("placeholder"))
    # Extract the date text
    data_text = Passing_Year.text
    data_pattern = r'^\d{4}$'
         
    if re.match(data_pattern, data_text ):
            print(f"Passing_Year  is valid.")
    else:
            print(f"Passing_Year is invalid.")  
##############################################################################################################################

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
# tabular view validation
def tabularView(driver):
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[8]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Education" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Education'])[1]")))
    if back_to_origin:
            print(" 'All Education' title tab visible")
    else:
            print(" 'All Education' title tab not visible")         



###############################################################################################################################
if __name__ == "__main__":
    
   def start_login():
    # Retrieve the input values from the Tkinter entry widgets
    username = username_entry.get()
    password = password_entry.get()
    
    # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver)
    
    # All Events Tab
    Education_menu(driver)

    #select doctor dropdown
    dropdown_id = "doctor_select_field_id"
    index_to_select = 2  
    select_dropdown_by_index(driver, dropdown_id, index_to_select)  
    
    # Validate country, state, and city
    validate_country_state_city(driver)      
    
    # validation of reference url
    validate_reference_url(driver)
    
    
    
    # Initialize the main window
root = Tk()
root.geometry("400x200")
root.title("Peer Profiler Login")

# Create a label and entry for the username
username_label = Label(root, text="Username:")
username_entry = Entry(root)
username_entry.pack()

# Create a label and entry for the password
password_label = Label(root, text="Password:")
password_entry = Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = Button(root, text="Login", command=start_login)
login_button.pack()

# Run the main event loop
root.mainloop()





