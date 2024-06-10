from time import sleep
import time
from tkinter import Button, Entry, Label, Tk
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
############################################################################################################################3
def add_Interaction(driver):

        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Interaction']")))
        button.click()
        time.sleep(5)
        
        Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[1]/p[1]")))
        if Title_Validation:
            print("Title 'Add Interaction' Tab open")
        else:
            print("Title 'Add Interaction' Tab not open")
            time.sleep(2)
        
    # Doctor Name field and its validation
            doctor_Name = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]")))
            doctor_Name.click
            doctor_Name.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN,Keys.ENTER)  # Navigate and select an option
            time.sleep(10)
# Get the placeholder text of the doctor name input field
            title_name = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiBox-root css-8rvwlv'][normalize-space()='Doctor(s) Name'])[2]")))
            print("placeholder Name:",title_name.text)
    
    # Check if the placeholder text contains the expected value
            if title_name == "Doctor(s) Name":
                print("Placeholder text validation successful.")
            else:
                print("Placeholder text validation failed.")
            
########################################################################################################################################
def doctorsname_from_dropdown(driver):
    # Locate the doctor name input field using XPath directly
    doctor_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='tags-outlined'])[1]")))
    doctor_name_input.click()
    try:
        # Wait for the dropdown options to load
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAutocomplete-popper")))
    except TimeoutException:
        print("Dropdown options did not appear within the timeout period.")
        return
    time.sleep(5)
    # Initialize an empty list to store doctor names
    doctor_names = []
    
    # Loop through the dropdown options
    while True:
        # Retrieve the text of the highlighted option
        highlighted_option_text = doctor_name_input.get_attribute("aria-activedescendant")
        doctor_names.append(highlighted_option_text)
        
        # Hover over the highlighted option to move the cursor (sometimes necessary for dropdowns)
        ActionChains(driver).move_to_element(doctor_name_input).perform()
        # Send DOWN arrow key to navigate to the next option
        doctor_name_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        
        # Retrieve the current option text again to check if we've looped back to the beginning
        current_option_text = doctor_name_input.get_attribute("aria-activedescendant")
        
        # Break the loop if we've reached the beginning of the dropdown options again
        if current_option_text == doctor_names[-1]:  # Compare with the last element of the list
            break
        
# Print the list of doctor names
    print("Doctor Names in Dropdown:")
    for name in doctor_names:
        print("Names::", name)
        time.sleep(5)    
#########################################################################################################################

# Add-new_doctor field
def Add_new_doc(driver):
    Add_doc = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall PrivateSwitchBase-root MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall MuiCheckbox-root MuiCheckbox-colorPrimary MuiCheckbox-sizeSmall css-1bix3s6']//input[@type='checkbox']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", Add_doc[0])  # Scroll into view
    Add_doc[0].click()
    time.sleep(2) 
    
# Wait for the name input field to be present, click it, and enter the name
    Add_doc_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type name']")))
    Add_doc_name.click()
    Add_doc_name.send_keys("Sara P","@123")      
     
    title_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Add doctor(s), not present in PROFILER.']")))
    if title_field:
        print("Add doc title is visible")
    else:
        print(f"Add doc title not visible")

##################################################################################################################################################

# Date Tab
def Date_tab(driver):
    
    click_date_tab = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")))
    click_date_tab.click()
    time.sleep(4)
    
    click_date_tab.send_keys("05/17/2024")
    # validate the field name
    title_name= click_date_tab.get_attribute("placeholder")
    print("title name:", title_name)
    # validate the words limit no.
    title_name = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]")))
    print("Title of field::" ,title_name.text)
    
####################################################################################################################################################################    
# Mode, Location, Location in detail Tabs

def mode_location(driver):
        # Click to activate the dropdown
        mode_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]")))
        mode_tab.click()
        
        # Read the dropdown options and print them
        DD_read = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[6]/div[3]/ul[1]")
        for option in DD_read:
            time.sleep(2)
            print(f"Option: {option.text}")
            
            option_click= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[3]/ul[1]/li[2]"))) 
            option_click.click()
            print("clicked option::" ,option_click.text) 
            
    # VAalidate the mode totle
        mode_title = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Mode']")))  
        print("Title of field::" ,mode_title.text)
        time.sleep(2)        
        
        
 # Click to activate the location dropdown
        location_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]")))
        location_tab.click()
        # Read the dropdown options and print them
        Loc_DD_read = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[6]/div[3]/ul[1]")
        for option in Loc_DD_read:
            time.sleep(2)
            print(f"Option: {option.text}")
            option_click= WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[3]/ul[1]/li[3]"))) 
            option_click.click()
            print("clicked option::" ,option_click.text) 
            
    # VAalidate the mode totle
        location_title = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Location']")))  
        print("Title of field::" ,location_title.text)   
        
        
    # location in detail
        
        location_indetail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/input[1]")))                    
        location_indetail.click()
        location_indetail.send_keys("Marriot Hotell,pune")
        print("placeholder text::" ,location_indetail.text)
################################################################################################################################
        
# Category Tab: Brands, CME, Support tabs
def brand_CME_Support(driver):
    
    categoty_title = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]")))        
    print("placeholder text::", categoty_title.text)  
    
# Brand_tab validation
    brand_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")))
    brand_tab.click()
    
# dropdow _check box validation
    brand_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
    for option in brand_list:
        print(f"Option: {option.text}")
        if option.text.strip() == "ADIPRIN":
            option.click()
            print("Clicked option.")
            break
        
    # check box selection validation        
    click_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[1]/div[1]/div[1]/div[6]/div[1]/div[1]")))
    click_box.click()
    print("placeholder text::",click_box.get_attribute("value") )  

# CMEs_tab validation
    CMEs_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]")))
    CMEs_tab.click()
    
# dropdow _check box validation
    CMEs_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
    for option in CMEs_list:
        print(f"Option: {option.text}")
        if option.text.strip() == "On-Line":
            option.click()
            print("Clicked option.")
            break
    # check box selection validation        
    click_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]/input[1]")))
    click_box.click()
    print("placeholder text::", click_box.get_attribute("value"))  


# Support_tab validation
    support_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]")))
    support_tab.click()
    
# dropdow _check box validation
    support_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    for option in support_list:
        print(f"Option: {option.text}")
        if option.text.strip() == "Science":
            option.click()
            print("Clicked option.")
            break
        
    # check box selection validation        
    support_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/label[1]/span[1]/input[1]")))
    support_box.click()
    print("placeholder text::", support_box.get_attribute("value"))     
##################################################################################################################################################    
# Title/subject and details tab

def subject_det(driver):
    
    subject_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/textarea[1]")))
    subject_tab.click()
    subject_tab.send_keys("this is for testing/demo")  
    print("name of title::" ,subject_tab.text)       
    
    tab_limit = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[2]/p[1]")))
    print("name of title::",tab_limit.text)

if __name__ == "__main__":
    
   
        
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # Add Interaction button click and field validation 
        add_Interaction(driver) 
        
        # doctor name field
        doctorsname_from_dropdown(driver)
        
        # Add-new_docytor field
        Add_new_doc(driver)
        
        # Date Tab
        Date_tab(driver)
        
        # Mode, Location, Location in detail Tabs
        mode_location(driver)
        
        # Category Tab: Brands, CME, Support tabs
        brand_CME_Support(driver)
        
        # Title/subject and details tab
        subject_det(driver)
        
        #close the window
        driver.quit()
    
    