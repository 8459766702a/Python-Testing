
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




#from Login_Module import select_dashboard
def setup_driver():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
########################################################################################################
    # Create a Chrome WebDriver instance and maximize the window
    driver = webdriver.Chrome(options=chrome_options)
    return driver
##############################################################################################################
def navigate_to_login(driver):
    # Navigate to the login page
    driver.get("https://beta.peerprofiler.com/login")
    time.sleep(5)
    
################################################################################################################
def fill_login_credentials(driver):
    # Fill in the username and password fields
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    # Fill in the username and password

    # Fill in the username and password
    username_field.send_keys(username_entry.get())
    password_field.send_keys(password_entry.get())
    
    # Click the login button
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(10)
#########################################################################################################################
# Add engagement Button Validation
def add_engagement(driver):
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Engagement']")))
    button.click()
    Title_Validation = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[contains(text(), 'Add Engagement')]"), "Add Engagement"))
    if Title_Validation:
        print("Title 'Add Engagement 'Tab open")
        
    else:
        print("Title 'Add Engagement' Tab not open")
        time.sleep(2)
        
# Doctor Name field and its validation
    doctor_Name = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"tags-outlined")))
    doctor_Name.click
    doctor_Name.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN,Keys.ENTER)  # Navigate and select an option
    time.sleep(10)
    
# Get the placeholder text of the doctor name input field
    placeholder_text = doctor_Name.get_attribute("placeholder")
    
    # Check if the placeholder text contains the expected value
    if placeholder_text == "Doctor(s) Name":
        print("Placeholder text validation successful.")
    else:
        print("Placeholder text validation failed.")
        
        
########################################################################################################################################
def read_doctors_from_dropdown(driver):
    # Locate the doctor name input field using XPath directly
    doctor_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='tags-outlined'])[1]")))
    doctor_name_input.click()
    try:
        # Wait for the dropdown options to load
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAutocomplete-popper")))
    except TimeoutException:
        print("Dropdown options did not appear within the timeout period.")
        return
    time.sleep(10)
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
        time.sleep(10)

        
###############################################################################################################################        
def Add_doctors(driver):

        # Wait for the checkbox to be present and click it
        Add_doc = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "(//input[@type='checkbox'])[1]")))

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

# Activity title
def Activity_title(driver):
    
    click_activity_title = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/textarea[1]")))
    click_activity_title.click()
    time.sleep(4)
    click_activity_title.send_keys("Testing Demo123***")
    # validate the field name
    title_tag= click_activity_title.get_attribute("placeholder")
    print("title name:", title_tag)
    # validate the words limit no.
    limit_no = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/p[1]")))
    print("limit no::" ,limit_no.text)
####################################################################################################################################################################    

 # Add Engagement Tab: Catagory Tab: title validation
def Activites_button(driver): 
    Category_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[2]")))
    #print("category title name:" ,Category_title.text)
    if Category_title:     
        print("Category tab: category field title present" )
    else:
        print("category tab: category field title not present")   
time.sleep(5)


def read_activities_options(driver):
                   
        activities_dropdown = driver.find_element(By.XPATH, "//p[normalize-space()='Activites']").click()
        activities_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div")
        
        # iterate the list
        for index, containt_data in enumerate(activities_list):
            print(f"containt_data {index + 1}: {containt_data.text}")         
        select_checkbox = driver.find_element(By.XPATH, "//input[@value='20']")
        select_checkbox.click()
        #validate the clicked element
        Article= WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/p[1]")))
        print("selected checkbox_Name::" , Article.text)
        
        
        Event_dropdown = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]").click()
        #validate the clicked Element
        
        event_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div")
        
        # iterate the list
        for index, event_options in enumerate(event_list):
            print(f"event_options {index + 1}: {event_options.text}")
            
        # clickind check box    
        select_checkbox = driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/input[1]").click()
        # validate the clicked element
        Advosary_board = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Advisory Board']")))  
        print("selected check box Name::" , Advosary_board.text)

#############################################################################################################################################################
 
#Venue and country state city tab validation
def venue_Name(driver):
        venuename = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "engagementvenue")))
        venuename.click()
        venuename.send_keys("Pune ,hijewadi-412412 ")

        pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$'
        if re.match(pattern, venuename):
            print('venuename validation successful and matches the date pattern.')
        else:
            print('venuename validation failed or does not match the date pattern.')
        
        #validate the tilte
        title_venue= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/fieldset[1]/legend[1]/span[1]/div[1]")))
        title_venue.get_attribute("placeholder") 
        print("Venue_title_Name::", title_venue)     
#########################################################################################################################################
 

#####################################################################################################################################################3333    
# Country TAB
        city_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")))
        city_tab.click()
        #city_tab.send_keys("pune", Keys.ARROW_DOWN, Keys.ENTER)
        actions = ActionChains(driver)
        actions.move_to_element(city_tab).send_keys("India" ,Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        city_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[9]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]")     
        for index, city_options in enumerate(city_list):
            print(f"city_options {index + 1}: {city_options.text}")


# State TAB
        state_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//div[5]//form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]")))
        state_tab.click()
        actions = ActionChains(driver)
        actions.move_to_element(state_tab).send_keys("maha" ,Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        
        state_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[9]/div[3]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]")     
        for index, state_options in enumerate(state_list):
            print(f"state_options {index + 1}: {state_options.text}")
                
    
#validate the state title name
        state_title_Name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/label[1]")))
        state_title_Name.get_attribute("placeholder")
        print("title name of field::" , state_title_Name.text)  

    
# City TAB
        city_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")))
        city_tab.click()
        #city_tab.send_keys("pune", Keys.ARROW_DOWN, Keys.ENTER)
        actions = ActionChains(driver)
        actions.move_to_element(city_tab).send_keys("pun" ,Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        city_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[9]/div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")     
        for index, city_options in enumerate(city_list):
            print(f"city_options {index + 1}: {city_options.text}")
            
#validate the city title name
        city_title_Name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/label[1]")))
        city_title_Name.get_attribute("placeholder")
        print("title name of field::" , city_title_Name.text)  
        
        time.sleep(10)


####################################################################################################################


if __name__ == "__main__":
    
  def on_login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    
    # Setup WebDriver
     # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver) 
    
    # Add Engagement button click and field validation 
    add_engagement(driver)
    
    # Example usage:
    read_doctors_from_dropdown(driver)
    
    # Add Dcoctor field
    Add_doctors(driver)
    
    # Activity title validation
    Activity_title(driver)
        
    # Latest Engagement Tab: Add engagement: Avtivites_buttonDD list
    Activites_button(driver)
   
    # Read activites -options
    read_activities_options(driver)
    
    #Venue and country state city tab validation
    venue_Name(driver)
    
    # Validate country, state, and city
    #validate_country_state_city(driver)


    # Close browser
    #driver.quit()

    # Close the browser
    driver.quit()

# Initialize the main window
root = Tk()
root.geometry("400x200")
root.title("Peer Profiler Login")

# Create a label and entry for the username
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for the password
password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the login button
login_button = Button(root, text="Login", command=on_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()






