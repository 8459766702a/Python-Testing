import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests,json
from selenium import webdriver
import time


####################################### Utility functions #################################################

# Validate name
def is_valid_name(person_name):
     # Check if name contains any numerical digits
    if any(char.isdigit() for char in person_name):
        print("The name is invalid: Name contains numerical digits")
        return False

# Function to validate image link
def validate_image_link(image_link):
    for prefix in valid_prefixes:
        if image_link.startswith(prefix):
            print("The image link contains the required prefix")
            break
        else:
            print('Invalid image link(the prefix not present)')

# validate doctor specialities, sub specialities and suffix
def validate_specialities(spec_input, specialities):
    spec_present = False
    # for spec in specialities:
    if spec_input in specialities:
        spec_present = True
        print("The speciality is correct")
        return True
        
    if spec_present == False:
        print("The doctor speciality is not present")
        
def validate_subSpecialities(subSpec_input, sub_specialities):
    subSpec_present = False
    if subSpec_input in sub_specialities:
        subSpec_present = True
        print("The sub speciality is correct")
        return True
        
    if subSpec_present == False:
        print("The doctor sub speciality is not present")

def validate_suffix(suffix_input, doctor_suffix):
    suffix_present = False
    if suffix_input in doctor_suffix:
        suffix_present = True
        print("The suffix is correct")
        return True
        
    if suffix_present == False:
        print("The doctor suffix is not present")

# function to validate extension
def validate_image_extension(img_link):
    file_extension = img_link.rsplit('.', 1)[-1].lower()  # Get the last part of URL after the last '.'
    print("the extracted file extension is",file_extension)

    # Check if the extracted file extension is in the list of valid extensions
    if file_extension in valid_extension:
        print("The image link contains a valid extension.")
    else:
        print('Invalid image link extension')

# Validate domain names
def validate_domain_names(domain_name):
    dom_name = domain_name.split("/")[2] 
    print("the extracted domain name is",dom_name)
    
    domain_found = False
    for domain in domainNames:
        if domain == dom_name:
            domain_found=True
            print("the domain name is valid")
            break
        
    if not domain_found:
        print("The domain name is invalid")

# Validate email
def is_valid_email(email):
    
    # Check to see if the email is already registered
    email_present =False
    if email in email_id:
        email_present=True
        print("The email already exists")
    if email_present == False:
        pass
    
    # Regular expression pattern for validating an email address
    pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    if pattern.match(pattern, email):
        print("the email is valid")
        return True
    else:
        print("The emaile is invalid")
        return False

def is_valid_phoneNumber(p_number):
    print("the length of p number is",len(p_number))
    if len(p_number) == 10:
        print("The phone number is valid")
        return True
    else:
        print("The phone number is invalid")
  
def validate_areaOfInterest(interest, interest_list):
    print("the area of interest is",interest)
    interests_list = [interest.strip() for interest in interest.split(',')]  # Split interests by comma and remove whitespace
    valid_interests = [int.strip() for int in interest_list]  # Assuming areasOfInterest is a list of valid interests
    
    for interest in interests_list:
        if interest in valid_interests:
            print(f"The interest '{interest}' is valid")
        else:
            print(f"The interest '{interest}' is not valid")  

def validate_spouseName(spouse_name):
    print("Check for spouse name")
    if spouse_name ==  spouseName:
        print("The spouse name is valid")
    else:
        print("Invalid spouse name")
        
def validate_workPlace(wplace_name):
    print("check for workplace name")
    if wplace_name==workplace_name:
        print("the workplace name is valid")
    else:
        print("invalid workplace name")    
 
def validate_address(adress, address_list):
    print("check for address")
    address_status=False
    if adress in address_list:
        print('the address is valid')
        address_status=True
        return True
    if address_status==False:
        print("The address is invalid")
 
def validate_state_city(s_c_name,name, list):
    if name in list:
        print(f"The {s_c_name} is valid ")
    else:
        print(f"Invalid {s_c_name}") 
 
def validate_zipcode(zipcode):
    pattern = r'^[1-9][0-9]{5}$'
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Match the input ZIP code against the pattern
    if regex.match(zipcode):
        print("The zipcode is valid")
    else:
        print("The zipcode is invalid")
       
###################################### Utility function #######

valid_prefixes=['https://','http://'] 
valid_extension=['jpg','png']
domainNames=['facebook.com','linkedin.com','twitter.com','youtube.com']

specialities = ['General Surgery','Neurology','Orthopaedic Surgery', 'Pathology']
sub_specialities = ['child neurology','gynecologic oncology','pediatric orthopaedics','hematology']
doctor_suffix = ['MD','ENT','DMD','DPT','GP']
email_id = ['rodri.ash@gmail.com', 'josh.dsouza@outlook.com']
areasOfInterest = ['Oncologist','Surgeon','immunology','Neurology']
otherAreaOfInterest = ['Urology','pathology', 'Cardiology']
spouseName = 'roger'
workplace_name='TATA',
addressLine_1 = ['123 Main St, Springfield, IL 12345', '456 Oak St, Springfield, IL 12345']
state = ['California','Maharashtra','Gujarat']
city = ['New york', 'Mumbai','Pune']
 

# Set Chrome driver path
chrome_driver_path = "C://chrome_driver//chromedriver-win64//chromedriver.exe"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Create a Chrome WebDriver instance and maximize the window
driver = webdriver.Chrome(options=chrome_options)
#return driver

# Navigate to the login page
driver.get("https://beta.peerprofiler.com/login")

# Find username and password fields and login button
# username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Enter credentials and click login button
username.send_keys("Pgadmin2020")
password.send_keys("PG@AdminKoLsNew")
login_button.click()


# Click on Bio Details menu
# Define the XPath of the element
xpath = "//*[@id='root']/div[2]/div/div[2]/ul/a[2]"

# Add WebDriverWait
# click the bio details option from menu
wait = WebDriverWait(driver, 15)  # 15 seconds timeout
bio_details_menu = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
bio_details_menu.click()


# direct to the bio details form
bio_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[6]/div[1]/div/div/div[1]/a')))
bio_details.click()

# enter the first name,middle name and last name
# First Name
input_firstName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstname"]')))
firstName_input = 'Ashton8'
input_firstName.send_keys(firstName_input)
entered_firstName = input_firstName.get_attribute('value')

# validate the name
is_valid_name(entered_firstName)

# middle Name
input_middleName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="middlename"]')))
middleName_input = 'Rodri'
input_middleName.send_keys(middleName_input)
entered_middleName = input_middleName.get_attribute('value')

# Last Name
input_lastName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lastname"]')))
lastName_input = 'Fernandes'
input_lastName.send_keys(lastName_input)
entered_lastName = input_lastName.get_attribute('value')


# Enter the image link
input_imgLink = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Image_link"]')))
img_link='https://arpannewborncare.com/wp-content/uploads/2019/07/dr-ashish.jpg'
input_imgLink.send_keys(img_link)

entered_imgLink = input_imgLink.get_attribute('value')

# validate image link
validate_image_link(entered_imgLink)

# validate image link extension
validate_image_extension(entered_imgLink)

# Enter image source link
input_imgSourceLink = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="source_link"]')))
imgSource_link='https://arpannewborncare.com/team/'
input_imgSourceLink.send_keys(imgSource_link)

entered_imgSourceLink = input_imgSourceLink.get_attribute('value')

# validate image source link
print("Validation for image source link")
validate_image_link(entered_imgSourceLink)

# Enter the specialities of doctors
input_speciality = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="specialityname"]')))
doc_speciality='Neurology'
input_speciality.send_keys(doc_speciality)

entered_docSpeciality = input_speciality.get_attribute('value')

# Validate doctor speciality
validate_specialities(entered_docSpeciality,specialities)

# Enter the sub-speciality of doctor
input_subSpeciality = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subspecialityname"]')))
doc_subSpeciality='child neurology'
input_subSpeciality.send_keys(doc_subSpeciality)

entered_docSubSpeciality = input_subSpeciality.get_attribute('value')

validate_subSpecialities(entered_docSubSpeciality, sub_specialities)

# Enter the Doctor suffix
input_docSuffix = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="suffixname"]')))
doc_suffix='MD'
input_docSuffix.send_keys(doc_suffix)

entered_docSuffix = input_docSuffix.get_attribute('value')

validate_suffix(entered_docSuffix,doctor_suffix)

# Enter area of interest
input_areaOfInterest = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="areaofinterestname"]')))
areaofInterstInput="Oncologist, def, dwdw"
input_areaOfInterest.send_keys(areaofInterstInput)

entered_areaOfInterest = input_areaOfInterest.get_attribute('value')
validate_areaOfInterest(entered_areaOfInterest,areasOfInterest)

# Enter other area of interest
input_otherAreaOfInterest = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otherinterestareasnonclinical"]')))
otherAreaofInterstInput="Oncologist, Urology, dwdw"
input_otherAreaOfInterest.send_keys(otherAreaofInterstInput)

entered_otherAreaOfInterest = input_otherAreaOfInterest.get_attribute('value')
validate_areaOfInterest(entered_otherAreaOfInterest,otherAreaOfInterest)


# Work phone number
print("Check for work phone number:")
input_workPhoneNum = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="workphone1"]')))
workPhone_num=92345674
input_workPhoneNum.send_keys(workPhone_num)

entered_workPhoneNumber = input_workPhoneNum.get_attribute('value')
is_valid_phoneNumber(entered_workPhoneNumber)

# Alternate phone number
print("Check for alternate phone number:")
input_altPhoneNum = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="workphone2"]')))
altPhone_num=923456745633
input_altPhoneNum.send_keys(workPhone_num)

entered_altPhoneNumber = input_altPhoneNum.get_attribute('value')
is_valid_phoneNumber(entered_altPhoneNumber)


# Cell Phone number
print("Check for cell phone number:")
input_cellPhone = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cellphone"]')))
cell_num=9234567456
input_cellPhone.send_keys(cell_num)

entered_cellNumber = input_cellPhone.get_attribute('value')
is_valid_phoneNumber(entered_cellNumber)

# Email validation
print("Check for Email Id:")
input_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
email = 'rodri.ash@gmail.com'
input_email.send_keys(email)

entered_email = input_email.get_attribute('value')

is_valid_email(entered_email)

# Alternate email
print("check for alternate email")
input_altEmail = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email2"]')))
altEmail = 'tom.brady@gmail.com'
input_altEmail.send_keys(altEmail)

entered_altEmail = input_altEmail.get_attribute('value')

is_valid_email(entered_altEmail)


# enter spouse name
print("check for spouse name")
input_spouseName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="spousename"]')))
spouseName = 'roger'
input_spouseName.send_keys(spouseName)

entered_spouseName = input_spouseName.get_attribute('value')

validate_spouseName(entered_spouseName)


# Work place details

# work place name
input_workplaceName = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='primaryinstitutionorganisation']")))
workplace_name='TATA'
input_workplaceName.send_keys(workplace_name)
entered_workplaceName = input_workplaceName.get_attribute('value')
validate_workPlace(entered_workplaceName)


# Addess input 1
input_address_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='residentialaddressline1']")))
address_1='456 Oak St, Springfield, IL 12345'
input_address_1.send_keys(address_1)
entered_address1 = input_address_1.get_attribute('value')
validate_workPlace(entered_address1)

# Addess input 2
input_address_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='residentialaddressline2']")))
address_2='123 Main St, Springfield, IL 12345'
input_address_2.send_keys(address_2)
entered_address2 = input_address_2.get_attribute('value')
validate_workPlace(entered_address2)

# Enter the country input
# input_country=driver.find_element(By.XPATH, "//*[@id='resicountryname']")
input_country = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@placeholder='Country']")))
country_name='United States'
input_country.send_keys(country_name)

# get the value of input in country
entered_country = input_country.get_attribute('value')
print("Entered country name is:", entered_country)


# enter the state name
s_name='state name'
input_state = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='resistatename']")))
state_name='California'
input_state.send_keys(state_name)

# get the value of input in country
entered_state = input_state.get_attribute('value')
print("Entered state name is:", entered_state)
validate_state_city(s_name,entered_state,state)

# enter the city name
c_name='city name'
input_city = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='resicityname']")))
city_name='New york'
input_city.send_keys(city_name)
entered_city = input_city.get_attribute('value')
validate_state_city(c_name,entered_city,city)

# enter zip code

input_zipCode = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='residentialpostalcode']")))
zip_code='50007'
input_zipCode.send_keys(zip_code)
entered_zipCode = input_zipCode.get_attribute('value')

validate_zipcode(entered_zipCode)

# get the value of input in country
entered_city = input_city.get_attribute('value')
print("Entered city name is:", entered_city)
validate_state_city(c_name,entered_city,city)

# digital presence
input_digitalPresence = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[6]/div[1]/div/div/form/div[2]/div[1]/div[2]/div/div[8]/div/div/div[1]/div/div/input")))
socialmediaId_name='https://twitter.com/tejopratap'
# input_digitalPresence.send_keys(socialmediaId_name)
driver.execute_script("arguments[0].value = arguments[1];", input_digitalPresence, socialmediaId_name)

# get the value of input in country
entered_socialMediaAccount = input_digitalPresence.get_attribute('value')
print("Entered social media account is:", entered_socialMediaAccount)

# validate social media account
print("Validation of social media account url")
validate_image_link(entered_socialMediaAccount)

# validate domain name
validate_domain_names(entered_socialMediaAccount)


# API testing
response = requests.get('http://api.zippopotam.us/us/90210')
data = json.loads(response.text)
print("the api data is",data)

# name = data["query"]["city"]
print("The name is:", data['country'])
countryName_api=data['country']

if countryName_api == country_name:
    print("The country name is correct")
else:
    print("Incorrect country name")


# add wait time before the web app shuts down
time.sleep(10) 


