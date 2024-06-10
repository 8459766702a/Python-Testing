import re
import traceback
import requests
from selenium.webdriver.support.ui import WebDriverWait, Select
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
def Payment_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[11]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(10)
        
    Title_Validation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/ol[1]/li[3]/button[1]/span[1]")))
    if Title_Validation:
            print("Title 'Add Payment' Tab open")
    else:
            print("Title 'Add Payment' Tab Not open")
            

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
        dropdown = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, dropdown_id)))
        
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
        time.sleep(10)
        
        # Validate that the correct option is selected
        selected_option = DD.first_selected_option
        selected_text = selected_option.text

        print(f"Selected option is: {selected_text}")
        print("Validation Successful!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
#############################################################################################################################################            
# Payment Tab
    publication = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "paymentstype0")))
    publication.click()
    publication.send_keys("General")
    
    tab_name= publication.get_attribute("value")                                         
    pattern = r'^[A-Za-z]+$'
    if re.match(pattern, tab_name):
            print(f"Payment Type  is valid.")
    else:
            print(f" Payment Type is invalid.")             
            
            
# Payment Amaount Tab
    payamount = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "paymentsamount0")))
    payamount.click()
    payamount.send_keys("Rs.10" "," "$0.8")
    
    tab_name= payamount.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Payment Amount  is valid.")
    else:
            print(f" Payment Amount is invalid.") 
            
# NAture of Payment Tab
    Nature_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "natureofpayments0")))
    Nature_pay.click()
    Nature_pay.send_keys("Gpay")
    
    tab_name= Nature_pay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f" Nature of Payment  is valid.")
    else:
            print(f" Nature of Payment is invalid.")             
            
            
# Form of Payment Tab
    Form_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "formofpayments0")))
    Form_pay.click()
    Form_pay.send_keys("Rs.10" "," "$0.8")
    
    tab_name= Form_pay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f" Form Payment  is valid.")
    else:
            print(f" Form Payment is invalid.")             

# Date of Payment Tab
    date_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dateofpayments0")))
    date_pay.click()
    date_pay.send_keys("05/12/2024")
    print("Name::",date_pay.get_attribute("placeholder"))
    # Extract the date text
    date_text = date_pay.text

# Define the date pattern (example: MM/DD/YYYY)
    date_pattern = r"^\d{2}/\d{2}/\d{4}$"

# Validate the date pattern using regex
    if re.match(date_pattern, date_text):
        print(f"Date is valid.")
    else:
        print(f"Date is invalid.")            
               
# company making Payment Tab
    comp_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "companymakingpayments0")))
    comp_pay.click()
    comp_pay.send_keys("Rs.10" "," "$0.8")
    
    tab_name= comp_pay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"company making Payment  is valid.")
    else:
            print(f" company making Payment is invalid.") 
            
            
# Reporting Year Tab
    repo_Year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "reportingyear0")))
    repo_Year.click()
    repo_Year.clear()  
    repo_Year.send_keys("2020")
    print("Name::", repo_Year.get_attribute("placeholder"))
    # Extract the date text
    data_text = repo_Year.text
    data_pattern = r'^\d{4}$'
         
    if re.match(data_pattern, data_text ):
            print(f"Reporting Year  is valid.")
    else:
            print(f"Reporting Year is invalid.")  
            
# Physician Profile Id Tab
    physician_id = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "physicianprofileids0")))
    physician_id.click()
    physician_id.clear()  
    physician_id.send_keys("165745")
    print("Name::", physician_id.get_attribute("placeholder"))
    # Extract the date text
    data_text = physician_id.text
    data_pattern = r'^\d+$'
         
    if re.match(data_pattern, data_text ):
            print(f"Physician Profile Id  is valid.")
    else:
            print(f"Physician Profile Id is invalid.")  
            
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

# Function to fetch valid cities for a given country from the API with retry logic
def fetch_valid_cities(country_name):
    url = 'https://countriesnow.space/api/v0.1/countries/cities'
    try:
        response = requests.post(url, json={"country": country_name}, timeout=20)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cities for {country_name}: {e}")
    raise Exception(f"Failed to fetch valid cities for {country_name}.")

# Function to validate entered country and city using API data
def validate_country_and_city(driver):
    try:
        # Fetch valid countries
        valid_countries = fetch_valid_countries()

        # Locate and click the Countries tab
        countries_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='countryoftravel0'])[1]")))
        countries_tab.click()
        print("Name::", countries_tab.get_attribute("placeholder"))

        # Enter the country name into the input field
        country_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "countryoftravel0")))
        country_input.send_keys("India")
        
        # Validate the entered country name
        entered_country = country_input.get_attribute('value')
        if entered_country in valid_countries:
            print(f"Entered country name is valid: {entered_country}")
        else:
            print(f"Entered country name is invalid: {entered_country}")
            return

        # Fetch valid cities for the entered country
        valid_cities = fetch_valid_cities(entered_country)

        # Enter the city name into the input field
        city_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cityoftravel0")))
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
# Recepient Type Tab
    recept_type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recepienttype0")))
    recept_type.click()
    recept_type.send_keys("Covered Recipient Physician")
    
    tab_name= recept_type.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Recepient Type  is valid.")
    else:
            print(f"Recepient Type is invalid.") 

# Recepient Type Tab
    recept_type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recepienttype0")))
    recept_type.click()
    recept_type.send_keys("Covered Recipient Physician")
    
    tab_name= recept_type.get_attribute("value")                                         
    pattern = r'^[a-zA-Z0-9\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Recepient Type  is valid.")
    else:
            print(f"Recepient Type is invalid.") 

# Speciality Tab
    speciality = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recepienttype0")))
    speciality.click()
    speciality.send_keys("Physician")
    
    tab_name= speciality.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Speciality  is valid.")
    else:
            print(f"Speciality is invalid.") 

# Third Party Received this Payment ? Tab
    tirdparty_recPay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recepienttype0")))
    tirdparty_recPay.click()
    tirdparty_recPay.send_keys("Physician")
    
    tab_name= tirdparty_recPay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Third Party Received this Payment ?  is valid.")
    else:
            print(f"Third Party Received this Payment ? is invalid.") 

# Third Party Receiving Payment Tab
    tirdparty_recevingPay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "thirdpartyreceivingpayment0")))
    tirdparty_recevingPay.click()
    tirdparty_recevingPay.send_keys("Not")
    
    tab_name= tirdparty_recevingPay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Third Party Receiving Payment is valid.")
    else:
            print(f"Third Party Receiving Payment is invalid.") 
            
# Type of Product Asociated with Payment Tab
    Prod_asso_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "producttypeassociatedwithpayments0")))
    Prod_asso_pay.click()
    Prod_asso_pay.send_keys("Physician")
    
    tab_name= Prod_asso_pay.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Type of Product Asociated with Payment  is valid.")
    else:
            print(f"Type of Product Asociated with Payment is invalid.") 
            
            
# Associated Drug(s) or Biologicals or Device or Medical Supply - Product Name Tab
    product_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sasorbordormsorpname0")))
    product_name.click()
    product_name.send_keys("Physician")
    
    tab_name= product_name.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Associated Drug(s) or Biologicals or Device or Medical Supply - Product Name  is valid.")
    else:
            print(f"Associated Drug(s) or Biologicals or Device or Medical Supply - Product Name is invalid.") 
            
# Preclinical Research Tab
    preclinical_res = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "preclinicalresearch0")))
    preclinical_res.click()
    preclinical_res.send_keys("Physician")
    
    tab_name= preclinical_res.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Preclinical Research  is valid.")
    else:
            print(f"Preclinical Research is invalid.")                                     
            
            
# Expenditure category Tab
    Expend_cat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "expenditurecategory0")))
    Expend_cat.click()
    Expend_cat.send_keys("Physician")
    
    tab_name= Expend_cat.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Expenditure category  is valid.")
    else:
            print(f"Expenditure category is invalid.")  
            
            
# Name of study Tab
    name_study= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nameofstudy0")))
    name_study.click()
    name_study.send_keys("Physician")
    
    tab_name= name_study.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Name of study  is valid.")
    else:
            print(f"Name of study is invalid.")  
            
            
# Clinical trail gov identifier Tab
    preclinical_res = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clinicaltrailgovidentifier0")))
    preclinical_res.click()
    preclinical_res.send_keys("Physician")
    
    tab_name= preclinical_res.get_attribute("value")                                         
    pattern = r'^[a-zA-Z\s,.\'-]+$'
    if re.match(pattern, tab_name):
            print(f"Clinical trail gov identifier  is valid.")
    else:
            print(f"Clinical trail gov identifier is invalid.")              

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
#############################################################################################################################    
    
# validation of research information link
def validate_reference_url(driver):

        # Refrence Link Tab
        Ref_url_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "researchinformationlink0")))
        Ref_url_tab.click()

        # Enter the URL into the input field
        url_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "researchinformationlink0")))
        url_to_enter = "https://example.com" 
        url_input.clear()
        url_input.send_keys(url_to_enter)
        print("Name::",url_input.get_attribute("placeholder"))
        
        
# tabular view validation
def tabularView(driver):
  
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[11]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
        
 # Validate return to "All Payments" page
    back_to_origin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='All Payments'])[1]")))
    if back_to_origin:
            print(" 'All Payments' title tab visible")
    else:
            print(" 'All Payments' title tab not visible")                     
                                    
############################################################################################################################

if __name__ == "__main__":
    
    # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver)
    
    # All Events Tab
    Payment_menu(driver)  
    
    #select doctor dropdown
    dropdown_id = "doctor_select_field_id"
    index_to_select = 2  
    select_dropdown_by_index(driver, dropdown_id, index_to_select) 
    
    # Validate country and city inputs
    validate_country_and_city(driver)    
    
    # validation of reference url
    validate_reference_url(driver)  
    
    # tabular view validation
    tabularView(driver)    