import re
import traceback
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
        
        
 # Find all tab elements
def All_tabs(drive): 
    tabs = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(7) > div:nth-child(1)") #list of element

# Extract tab titles
    tab_titles = [tab.text for tab in tabs]

# Define expected tab titles
    expected_titles = ["Top 30 Doctors by Activities", "Directory", "Latest Engagement","Latest Interactions","Prominent Digital Platforms","Recently Viewed", "Top Associations", "Recommendation", "Top Doctors by no. of Events", "Top Interest Areas" , "Top Educational Institutions"]  

# Validate tab titles
    for i, title in enumerate(tab_titles):
        if title == expected_titles[i]:
            print(f"Tab {i+1} title is correct: {title}")
    else:
        print(f"Tab {i+1} title is incorrect. Expected: {expected_titles[i]}, Actual: {title}")

        time.sleep(20)
       
        pass  # Placeholder for further actions
    #finally:
    
    # Doctor Name list from dropdown 
def doctor_DD(driver):          
    name_DD = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='path'])[827]"))).click()
    #name_DD.send_keys(Keys.ARROW_DOWN)

    
    # Retrieve the options from the dropdown
    doctor_options = Select(name_DD).options
    
    # Print the list of doctors
    print("List of Doctors:")
    for option in doctor_options:
        print(option.text)
    time.sleep(10)
    # Close the dropdown
    name_DD.click()  # Assuming clicking again closes the dropdown
    
# Activity title Name field validation
    Activity_title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id=':r5k:'])[1]"))) 
    Activity_title.click()
    time.sleep(2)
    
# start date
# Wait for the date input field to be present and visible
    date_input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='engagementdatetimepicker2']")))
    date_input_field.clear()

# Enter the date into the input field
    date_input_field.send_keys("05/08/2024")  # format is MM/DD/YYYY
    
    
    
def read_doctors_from_dropdown(driver):
    # Locate the doctor name input field using XPath directly
    doctor_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='tags-outlined'])[1]")))
    
    # Click on the input field to open the dropdown
    doctor_name_input.click()
    
    # Wait for the dropdown options to load
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAutocomplete-popper")))
    
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
        doctor_name_input.send_keys(Keys.ARROW_DOWN)
        
        # Retrieve the current option text again to check if we've looped back to the beginning
        current_option_text = doctor_name_input.get_attribute("aria-activedescendant")
        
        # Break the loop if we've reached the beginning of the dropdown options again
        if current_option_text == doctor_names[0]:
            break
    
    # Print the list of doctor names
    print("Doctor Names in Dropdown:")
    for name in doctor_names:
        print("Names::", name)
        
 # Add Engagement Tab: Catagory Tab: title validation
    Category_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiTypography-root MuiTypography-body1 css-12j5849")))
    if Category_title:     
        print("Add enegagement tab: category field title present" )
    else:
        print("Add enegagement tab: category field title not present")

# Activities dropdown chesk box validation
    #Activities_tab = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[2]"))).click()


#  Latest Engagement Tab: Add engagement: Avtivites_buttonDD list
    activities_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Activites')]")))
    activities_button.click()

    # Locate the dropdown and select "Articles"
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']")))
    dropdown.click()

    # Find the option for "Articles" and click on it
    articles_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and text()='Article']")))
    articles_option.click()

    # Read and print all available options
    all_options = driver.find_elements(By.XPATH, "//div[@role='option']")
    print("Available options:")
    for option in all_options:
        print("Option:", option.text)

    # Validate that "Articles" is selected
    selected_option_text = articles_option.text
    if selected_option_text == "Article":
        print("Selected option is:", selected_option_text)
        print("Validation Successful!")
    else:
        print("Validation Failed!")
        
        
        
        
        

if __name__ == "__main__":
    # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver)
    
     # Find all tab elements
    All_tabs(driver)
    
    # All search doctor name Tab
    doctor_DD(driver)  
    
    read_doctors_from_dropdown(driver)