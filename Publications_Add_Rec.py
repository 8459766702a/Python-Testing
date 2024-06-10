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
from selenium.webdriver.support.ui import Select


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
    time.sleep(25)
    
##########################################################################################################################################################################3

# All Events Tab
def Publications_menu(driver):
    # Wait for the menu to be present and clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[5]/li[1]/div[1]/div[1]/img[1]")) ).click()  
    time.sleep(10)
    
    # Wait for the "Add Record" button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]"))).click()
    time.sleep(5)
    
# Add Publications title page validation           
    actual_title_pg = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add Publications')]")))
    actual_title_pg.text
    if actual_title_pg:
            print(" 'Add Publications' page is visible")
    else:
            print("'Add Publications' page is not visible")
            
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

################################################################################################################################################         
# Book/ Journal Name Tab
    Book_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publicationtypebookjournal0")))
    Book_Name.click()
    Book_Name.send_keys("Title:biology_01")
    
    tab_name= driver.find_element(By.XPATH, "(//span[normalize-space()='Book or Journal'])[1]")                                          
    if tab_name:
            print("valid tab name as 'Book or Journal Name' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)   
                       
# Topic / subtopic Tab
    Pub_Type= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publicationtypes0")))
    Pub_Type.click()
    Pub_Type.send_keys("general")
    print("Name::",Pub_Type.get_attribute("placeholder"))
    time.sleep(2)             

    # Publication ID Tab
    Pub_ID = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publicationid0")))
    Pub_ID.click()
    Pub_ID.send_keys("general")
    print("Name::",Pub_ID.get_attribute("placeholder"))
    time.sleep(2)             

# Start Date Tab
    Start_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pubdate0")))
    Start_date.click()
    Start_date.send_keys("05/12/2024")
    print("Name::",Start_date.get_attribute("placeholder"))

# Publication Tab
    publication = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publication0")))
    publication.click()
    publication.send_keys("general")
    print("Name::",publication.get_attribute("placeholder"))
    time.sleep(2)  
    
# Publication Title Tab
    Pub_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publicationtypebookjournal0")))
    Pub_title.click()
    
    Pub_title.send_keys("Title:biology_01")
    
    Pub_title= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[6]")                                          
    if tab_name:
            print("valid tab name as 'Publications Title' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)                

# Publication Link Tab
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

def Publication_link(driver):

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "publicationlink0"))).click()
                                      
     # Enter the URL_1 into the input field
    url_input= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "publicationlink0")))
    url_input.send_keys("https://pubmed.ncbi.nlm.nih.gov/36748085/")
    print("Name::",url_input.get_attribute("placeholder"))
            
    # Validate the entered URL
    entered_url = url_input.get_attribute('value')
    if is_valid_url(entered_url):
        print(f"Entered URL is valid: {entered_url}")
    else:
        print(f"Entered URL is invalid: {entered_url}")
        time.sleep(4)
                         
# Topic Tab
    Topic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "topic0")))
    Topic.click()
    Topic.send_keys("Title:biology_01")
    
    Topic= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[8]")                                          
    if Topic:
            print("valid tab name as 'Topic' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
            
            
# Mest Term Tab
    MeSh_term = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "meshtermname0")))
    MeSh_term.click()
    MeSh_term.send_keys("Title:biology_01")
    
    MeSh_term= driver.find_element(By.XPATH, "(//span[normalize-space()='MeSH Terms'])[1]")                                          
    if MeSh_term:
            print("valid tab name as 'MeSh_Term' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 

# Name of Co- Author Tab
    Co_Author = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "coauthorname0")))
    Co_Author.click()
    Co_Author.send_keys("Title:biology_01")
    
    Co_Author= driver.find_element(By.XPATH, "(//span[normalize-space()='Name Of the Co-Authors'])[1]")                                          
    if Co_Author:
            print("valid tab name as 'MeSh_Term' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
                                    
# Keywords: Molecules ,others Tab
    Keywords = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "keywordsname0")))
    Keywords.click()
    Keywords.send_keys("Title:biology_01")
    
    Keywords= driver.find_element(By.XPATH, "(//span[normalize-space()='Keywords:Molecule or Others'])[1]")                                          
    if Keywords:
            print("valid tab name as 'Keywords: Molecules ,others' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
                            
# Condition or Indicator Tab
    Con_ind = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "indicationsname0")))
    Con_ind.click()
    Con_ind.send_keys("Title:biology_01")
    
    Con_ind= driver.find_element(By.XPATH, "(//span[normalize-space()='Condition OR Indication'])[1]")                                          
    if Con_ind:
            print("valid tab name as 'Condition or Indicator' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 

# Affilation Tab
    Affilation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "affiliationname0")))
    Affilation.click()
    Affilation.send_keys("Title:biology_01")
    
    Affilation= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[13]")                                          
    if Affilation:
            print("valid tab name as 'Affilation' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 

# Abstract Tab
    Abstract = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "abstract0")))
    Abstract.click()
    Abstract.send_keys("Title:biology_01")
    
    Abstract= driver.find_element(By.XPATH, "(//span[@class='p-0 m-0'])[14]")                                          
    if Abstract:
            print("valid tab name as 'Abstract' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
            
            
# Eigen or Inpact Factor Tab
    def enter_text(text):
        Eig_imp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "eigenfactorimpactfactor0")))
        Eig_imp.click()
        Eig_imp.send_keys("15")
        error_message = driver.find_element(By.ID, "error-message")


    # Test valid number input (integer)
        enter_text("123")
        assert error_message.text == "", f"Expected no error message, got: {error_message.text}"

    # Test valid number input (float)
        enter_text("123.45")
        assert error_message.text == "", f"Expected no error message, got: {error_message.text}"

    # Test invalid number input (alphabetic characters)
        enter_text("abc")
        assert error_message.text == "Please enter a valid number.", f"Expected error message, got: {error_message.text}"
      
     # title validation 
    Eig_imp= driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[15]/div[1]/label[1]/span[1]")                                          
    if Eig_imp:
            print("valid tab name as 'Eigen or Inpact Factor' visible")
    else:
            print("Invalid tab name")
            time.sleep(2)                 
            
# Indexed Tab
    index = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "indexeduseu0")))
    index.click()
    index.send_keys("Title:biology_01")
    
    index= driver.find_element(By.XPATH, "(//span[normalize-space()='Indexed (US/EU)'])[1]")                                          
    if index:
            print("valid tab name as 'Indexed' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
            
                        
 # Indexed Other Tab
    Indexed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "indexedothers0")))
    Indexed.click()
    Indexed.send_keys("Title:biology_01")
    
    Indexed= driver.find_element(By.XPATH, "(//span[normalize-space()='Indexed Others'])[1]")                                          
    if Indexed:
            print("valid tab name as 'Indexed Other' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
            
            
 # Non-Index Tab
    nonindex = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nonindex0")))
    nonindex.click()
    nonindex.send_keys("Title:biology_01")
    
    nonindex= driver.find_element(By.XPATH, "(//span[normalize-space()='Non-Index'])[1]")                                          
    if nonindex:
            print("valid tab name as 'Non-Index' visible")
    else:
            print("Invalid tab name")
            time.sleep(2) 
                                  
###############################################################################################################################################################            
 
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
        
###############################################################################################################################################################        
# tabular view validation
def tabularView(driver):
  
    back_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[5]/li[1]/div[1]/div[1]/img[1]")))
    back_menu.click()   
    time.sleep(5)
        
 # Validate return to "All Clinical Trials" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='All Publications']")))
    if back_to_origin:
            print("'All Publications' title tab visible")
    else:
            print("'All Publications' title tab not visible")   
    print("##############################################################################################")               
        
##############################################################################################################################################################
# validating Registration,refrence URL

def UrL_href(driver):
    # Locate the table by its XPATH
    table = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]")

    # Locate all rows in the table
    rows = table.find_elements(By.XPATH, ".//tr")
    column_index = 8 

    # Iterate through each row and get the links in the specified column
    for row in rows:
        try:
            # Get all cells in the row
            cells = row.find_elements(By.XPATH, ".//td")

            # Check if the row has enough cells (i.e., it's not a header or malformed row)
            if len(cells) > column_index:
                # Get the cell in the specified column
                cell = cells[column_index]

                # Find all links in the cell
                links = cell.find_elements(By.TAG_NAME, "a")

                # Print the href attribute of each link
                for link in links:
                    print("Link:", link.get_attribute("href"))

        except Exception as e:
            print(f"Error finding cells in row: {e}")
###############################################################################################################################################################        
                
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # clinical trial Tab
        Publications_menu(driver)
        
        #select doctor dropdown
        dropdown_id = "doctor_select_field_id"
        index_to_select = 2  
        select_dropdown_by_index(driver, dropdown_id, index_to_select)   
        
        # Publication Link
        Publication_link(driver) 
        
        # Refrence UrL
        Refrence_url(driver)
        
        # tabular view validation
        tabularView(driver)
        
        # validating Registration,refrence URL
        UrL_href(driver)