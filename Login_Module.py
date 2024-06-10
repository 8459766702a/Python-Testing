from lib2to3.pgen2.driver import Driver
from time import sleep
import time
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
    # Create a Chrome WebDriver instance and maximize the window
    driver = webdriver.Chrome(options=chrome_options)
    return driver
##############################################################################################################
def navigate_to_login(driver):
    # Navigate to the login page
    driver.get("https://beta.peerprofiler.com/login")
    time.sleep(10)
    
    
####################################################################################################################3
def validate_logo(driver):
    # Validate company Logo
    Logo = driver.find_element(By.XPATH, "//img[@alt='Logo']")
    if Logo:
        print("Logo is present and visible")
    else:
        print("Logo is not visible and present")
        
###############################################################################################################################
def fill_login_credentials(driver):
    # Fill in the username and password fields
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    # Fill in the username and password
    username = "Pgadmin2020"
    password = "PG@AdminKoLsNew"
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(10)

######################################################################################################################################
def validate_eye_button(driver):
    # Validate the eye button in the password field
    eye_button = driver.find_elements(By.XPATH, "//span[@class='material-icons-round notranslate MuiIcon-root MuiIcon-fontSizeSmall d-flex align-items-center css-mbs4uh']//*[name()='svg']")
    if eye_button:
        print("Eye button is present in the password field.")
    else:
        print("Eye button is not present in the password field.")
    time.sleep(1)
############################################################################################################################################

def select_dashboard(driver):
    # Select 'Dashboard' from the dropdown
    dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"demo-simple-select")))
    dropdown.click()
    DD = Select(dropdown)
    DD.select_by_visible_text("Dashboard")
    time.sleep(3)
    
    # Validate that 'Dashboard' is selected by default
    selected_option_text = "Dashboard"  
    selected_text = DD.first_selected_option.text
    if selected_text == selected_option_text:
        print(f"Selected option is: {selected_text}")
        print("Validation Successful!")
    else:
        print("Validation Failed!")

#############################################################################################################################################

def submit_login_form(driver):
    # Submit the login form
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    print("Login successful and credentials verified.")

####################################################################################################################################

def validate_dashboard_page(driver):
    # Validate dashboard page
    Default_pg = driver.find_element(By.XPATH,"//span[normalize-space()='Dashboard']")
    if Default_pg:
        print("Dashboard page is visible")
    else:
        print("Dashboard page is not visible")

#####################################################################################################################################

def validate_header_data(driver):
    # Validate header data presence
    header_Elements = driver.find_elements(By.XPATH, "//div[@class=' flex-wrap d-flex w-100 jc-end al-center css-1l0086i']")  
    # Iterate through the tabs and print their names
    for tab in header_Elements:
        print("Tab names:" ,tab.text)
        time.sleep(10)

##################################################################################################################################################
def validate_tab_titles(driver):
    # Validate tab titles
    tabs = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(7) > div:nth-child(1)")
    tab_titles = [tab.text for tab in tabs]
    expected_titles = ["Top 30 Doctors by Activities", "Directory", "Latest Engagement","Latest Interactions","Prominent Digital Platforms","Recently Viewed", "Top Associations", "Recommendation", "Top Doctors by no. of Events", "Top Interest Areas" , "Top Educational Institutions"]  

    for i, title in enumerate(tab_titles):
        if title == expected_titles[i]:
            print(f"Tab {i+1} title is correct: {title}")
        else:
            print(f"Tab {i+1} title is incorrect. Expected: {expected_titles[i]}, Actual: {title}")
    time.sleep(5)   
        
##################################################################################################################################     
#  Directory Tab_ Search _button_list reading
def directory_search_button(driver):
    dir_ser_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@title='Name']")))

    dir_ser_button.click()
    DD = Select(dir_ser_button)
    DD.select_by_visible_text("Name")
    time.sleep(3)
    # Read all available options using a for loop
    all_options = DD.options
    print("Available options:****************8")
    for option in all_options:
     print("List::" , option.text)
    
    # Validate that 'search_button' is selected by default
    selected_option_text = "Name"  
    Default_selected_text = DD.first_selected_option.text
    if Default_selected_text == selected_option_text:
        print(f"Selected option is: {Default_selected_text}")
        print("Validation Successful!")
    else:
        print("Validation Failed!")
        
#########################################################################################################################################################       
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
        venuename = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='engagementvenue']")))
        venuename.click()
        venuename.send_keys("Pune","@123")
        
        #validate the tilte
        title_venue= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/fieldset[1]/legend[1]/span[1]/div[1]")))
        title_venue.get_attribute("placeholder") 
        print("Venue_title_Name::", title_venue.text)     
        
#  Country tab
       # country_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]")))
       # country_tab.click()
        #country_tab.send_keys("India")
        
    ############################################################################3
      # Locate the country input field and enter the text
        country_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]")))
        country_input.click()
        country_input.clear()
        country_input.send_keys("india")
    
    # Wait for the suggestions to appear
        time.sleep(2)  # Adjust sleep time as necessary for suggestions to load
    
    # Capture the suggestions
        suggestions = driver.execute_script("""
        var suggestions = document.querySelectorAll('ul.suggestions li');
        var suggestionText = [];
        suggestions.forEach(function(suggestion) {
            suggestionText.push(suggestion.textContent.trim());
        });
        return suggestionText;
        """)
    
        print("Available suggestions:", suggestions)
    
    # Validate if the entered text matches any of the suggestions
        if "india" in suggestions:
         print(f"'{"india"}' is available in the suggestions.")
        else:
         print(f"'{"india"}' is NOT available in the suggestions.")
    
    # Optionally, select the matching suggestion
        for suggestion in suggestions:
            if suggestion == "india":
             driver.find_element(By.XPATH, f"//li[text()='{"india"}']").click()
            break
    #############################################################################    
        
        #validate the title name
        country_title_Name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/label[1]")))
        country_title_Name.get_attribute("placeholder")
        print("title name of field::" , country_title_Name.text)    
        
           
        # Iterate all available options
        country_list = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]")     
        for index, country_options in enumerate(country_list):
            print(f"country_options {index + 1}: {country_options.text}")
                

        
#################################################################################################################
         # State Tab
        state_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[5]//form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]")))
        state_tab.click()
        actions = ActionChains(driver)
        actions.move_to_element(state_tab).send_keys("maha", Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    
        state_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//li")))
        for index, state_option in enumerate(state_list):
           print(f"state_options {index + 1}: {state_option.text}")
    
    # Validate the state title name
        state_title_Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[5]/div[3]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/label[1]")))
        print("title name of field::", state_title_Name.text)
    
    # City Tab
        city_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]")))
        city_tab.click()
        actions = ActionChains(driver)
        actions.move_to_element(city_tab).send_keys("pun", Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        city_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//li")))
        for index, city_option in enumerate(city_list):
         print(f"city_options {index + 1}: {city_option.text}")
    
    # Validate the city title name
        city_title_Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[5]/div[3]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/label[1]")))
        print("title name of field::", city_title_Name.text)



######################################################################################################################33       
        
        

# Details Tab   

        detail_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[6]/div[1]/div[1]/textarea[1]")))
        detail_tab.click()
        detail_tab.send_keys("This is for testing purpose ", "123","@#$")
        
        
    # validate the words limit no.
        limit_no = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[6]/p[1]")))
        print("limit no::" ,limit_no.text)
        
      #validate the Details title name
        Detail_title_Name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[5]/div[3]/div[2]/form[1]/div[1]/div[6]/div[1]/label[1]")))
        Detail_title_Name.get_attribute("placeholder")
        print("title name of field::" , Detail_title_Name.text)   
        
        
     # Tag User(s) Tab
     
        taguser_tab = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[9]/div[3]/div[2]/form[1]/div[1]/div[7]/div[1]/div[1]")))
        taguser_tab.click()
        time.sleep(4)
        actions = ActionChains(driver)
        actions.move_to_element(taguser_tab).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        #taguser_tab.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN,Keys.ENTER)
        
    
    #validate the tag user title name
        taguser_title_Name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[9]/div[3]/div[2]/form[1]/div[1]/div[7]/div[1]/div[1]/label")))
        taguser_title_Name.get_attribute("placeholder")                                                  
        print("title name of field::" , taguser_title_Name.text)   
      
    
    
########################################################################################################################################################                 
if __name__ == "__main__":
    # Setup WebDriver
    driver = setup_driver()
    
    # login(driver)
    # Navigate to login page
    navigate_to_login(driver)

    # Validate company Logo
    validate_logo(driver)

    # Fill in login credentials
    fill_login_credentials(driver)

    # Validate eye button in password field
    validate_eye_button(driver)

    # Select 'Dashboard' from dropdown
    select_dashboard(driver)

    # Submit login form
    submit_login_form(driver)

    # Wait for the dashboard page to load
    WebDriverWait(driver, 10).until(EC.url_to_be("https://beta.peerprofiler.com/dashboard"))

    # Validate dashboard page
    validate_dashboard_page(driver)

    # Validate header data presence
    validate_header_data(driver)

    # Validate tab titles
    validate_tab_titles(driver)
    
    # Validation directory_Tab_search button list validatio
    directory_search_button(driver)
    
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


    # Close browser
    #driver.quit()
