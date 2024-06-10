
import re
from requests import options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def navigate_to_login(driver):
    # Navigate to the login page
    driver.get("https://beta.peerprofiler.com/login")
    time.sleep(5)

def fill_login_credentials(driver):     
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        time.sleep(10)
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        username_field.send_keys("Pgadmin2020")
        password_field.send_keys("PG@AdminKoLsNew")
        
        # Click the login button
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        time.sleep(20)
        
##############################################################################################################################################################################
# Manage Permission Tab
def mangepermission_menu(driver):
    
    click_menu = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[32]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    
    WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]"))).click()
    # Module Name Tab
    topic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "modulename")))
    topic.send_keys("revolution in medical science")
    
    Order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "orders")))
    Order.send_keys("2")
    tab_name= Order.get_attribute("placeholder")                                         
    pattern = r'^\d+$'
    if re.match(pattern, tab_name):
            print(f" Orders  is valid.")
    else:
            print(f" Orders is invalid.") 
####################################################################################################            
    
    # Function to check if a URL is valid
def is_valid_url(url):
    regex = re.compile(
        r'^(https?|ftp):\/\/'  # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def External_link(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "url"))).click()
                                      
     # Enter the URL_1 into the input field
    url_input= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "url")))
    url_input.send_keys("https://pubmed.ncbi.nlm.nih.gov/36748085/")
    print("Name::",url_input.get_attribute("placeholder"))
            
    # Validate the entered URL
    entered_url = url_input.get_attribute('value')
    if is_valid_url(entered_url):
        print(f"Entered URL is valid: {entered_url}")
    else:
        print(f"Entered URL is invalid: {entered_url}")  
        
    time.sleep(5)
    close_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/button[1]/span[1]/i[1]")))
    close_tab.click()
###########################################################################################################################################################
# create sub module  
def Manage_submodule(driver):
    click_menu = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]")))
    click_menu.click()   
    time.sleep(10)
    
    create_menu = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]")))
    create_menu.click()   
    time.sleep(10)
##############################################################################################################################################
    
def select_dropdown_by_index(driver, dropdown_id, index):
    try:
        # Wait for the dropdown to be present
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, dropdown_id)))
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
        
# sub-Module Tab
    submodule = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "formname")))
    submodule.send_keys("asdfrggbnh")

# order tab    
    Order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "orders")))
    Order.send_keys("2")
    tab_name= Order.get_attribute("placeholder")                                         
    pattern = r'^\d+$'
    if re.match(pattern, tab_name):
            print(f" Orders  is valid.")
    else:
            print(f" Orders is invalid.") 
####################################################################################################            
# Module allocation
def Module_allocation(driver):
    click_menu = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]")))
    click_menu.click()   
    time.sleep(10)
    
    create_menu = WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]")))
    create_menu.click()   
    time.sleep(10)  
    
    
# Company Name tab   
def select_dropdown_by_index(driver, dropdown_id, index):
    try:
        # Wait for the dropdown to be present
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, dropdown_id)))
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
        
# Company Name tab   
def select_dropdown_by_index(driver, dropdown_id, index):
    try:
        # Wait for the dropdown to be present
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, dropdown_id)))
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
        
#####################################################################################################################            

                
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # manage module Tab
        mangepermission_menu(driver)
        
        #External Url
        External_link(driver)  
        
        # manage sub module
        Manage_submodule(driver)   
            
         #select doctor dropdown
        dropdown_id = "modulename"
        index_to_select = 2  
        select_dropdown_by_index(driver, dropdown_id, index_to_select)   
        
        # Module allocation
        Module_allocation(driver)
        
        #select doctor dropdown
        dropdown_id = "companyid"
        index_to_select = 5 
        select_dropdown_by_index(driver, dropdown_id, index_to_select)     