import re
from tkinter import Button, Entry, Label, Tk
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
               
    # Fill in the username and password
        username_field.send_keys(username_entry.get())
        password_field.send_keys(password_entry.get())
        
        # Click the login button
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        time.sleep(25)
    
    
##############################################################################################################################################################################
# Award Tab
def Award_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[9]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(5)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add Awards')]")))
    if Title_Validation:
            print("Title 'Add Award' Tab open")
    else:
            print("Title 'Add Award'Tab Not open")
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

# Award or honor Name Tab
    honorname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "awardshonorsname0")))
    honorname.click()
    honorname.send_keys("Ramesh,rupesh sippi")
    institute_name_text = honorname.get_attribute('value')  

    institute_name_pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(institute_name_pattern, institute_name_text):
            print(f"Award or Honor name  is valid.")
    else:
            print(f"Award or Honor name is invalid.")
        
# Award or Honor By Tab
    honorBy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "awardshonorsby0")))
    honorBy.click()
    honorBy.send_keys("Mahesh" " ," "sippi")
    Degree_name_text = honorBy.get_attribute('value')  
    print("Name::",Degree_name_text )
    
    degree_pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(degree_pattern, Degree_name_text):
            print(f"Award or Honor By  is valid.")
    else:
            print(f"Award or Honor By is invalid.")        
        
# Year Name Tab
    year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "year0")))
    year.click()
    year.send_keys("2022")
    year_name_text = year.get_attribute('value')  
    print("Name::", year_name_text )
    
    speciality_pattern = r'^\d{4}$'
    if re.match(speciality_pattern, year_name_text):
            print(f"Year  is valid.")
    else:
            print(f"Year  is invalid.")        
                
        
##############################################################################################################################

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
        country_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "countryname0")))
        country_input.send_keys("United Kingdom")
        
        # Validate the entered country name
        entered_country = country_input.get_attribute('value')
        if entered_country in valid_countries:
            print(f"Entered country name is valid: {entered_country}")
        else:
            print(f"Entered country name is invalid: {entered_country}")
  
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
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[9]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Education" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Awards'])[1]")))
    if back_to_origin:
            print(" 'All Awards' title tab visible")
    else:
            print(" 'All Awards' title tab not visible")         



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
    Award_menu(driver)

    #select doctor dropdown
    dropdown_id = "doctor_select_field_id"
    index_to_select = 2  
    select_dropdown_by_index(driver, dropdown_id, index_to_select)  
    
 # Fetch the valid countries from the API
    valid_countries = fetch_valid_countries()

    if valid_countries:
        # Validate the countries tab and entered country name
            validate_country_name(driver, valid_countries)
    
    
    
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





