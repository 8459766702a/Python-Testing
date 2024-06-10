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
# Bio detail_ Add record Tab
def biodetail_menu(driver):
    
    click_menu = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[2]/li[1]/div[1]/div[1]/img[1]")))
    click_menu.click()   
    time.sleep(10)
    Add_record= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")))
    Add_record.click()
    time.sleep(10)

# Speciality tab
def fetch_and_validate_specialty(driver, expected_specialty):

    speciality = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "specialityname")))
    speciality.click()
    speciality.send_keys(expected_specialty)
    
    # Define the list of specialties( used collection Array-list)
    specialties =["Acupuncture And Acupressure", "Allergy & Immunology", "Anatomy", "Anesthesia", 
                   "Aviation Medicine", "Ayurveda", "Ayush", "BDS Student", "Biochemistry", "Biophysics", 
                   "Biostatistics", "Blood Banking & Tranfusion Medicine", "Cardiology", "Colon & Rectal Surgery", 
                   "Community Medical Services And Ed", "Community Medicine/ Psm", "Dentistry", "Dermatology", 
                   "Dietician/ Nutrition", "Electropathy", "Embryology", "Emergency Medicine", "Endocrinology", 
                   "Family Medicine", "Forensic Medicine", "Gastroenterology", "General Practice", "General Surgery", 
                   "Geriatric Medicine", "Health Journalism", "Hematology", "Homeopathy", "Infectious Disease", 
                   "Integrative Medicine", "Intensive Care Specialist", "Internal Medicine", "Lab Technician", 
                   "Medical Administration", "Medical Genetics", "Medical Oncology", "Medico-Legal Expert", 
                   "Microbiology", "Multipurpose Health Worker", "Naturopathy", "Neonatology", "Nephrology", 
                   "Neurology", "Neurosurgery", "Nuclear Medicine", "Nursing", "Obstetrics & Gynecology", 
                   "Occupational Medicine", "Ophthalmology", "Oral & Maxillofacial Surgery", "Orthopaedic Surgery", 
                   "Otolaryngology (Ent)", "Palliative Medicine", "Pathology", "Pediatrics", "Pharmacology", 
                   "Physical Medicine And Rehabilitation", "Physiology", "Physiotherapy", "Plastic Surgery", 
                   "Preventive Medicine", "Psychiatry", "Pulmonology", "Radiation Oncology", "Radiology", 
                   "Radiology Imaging Technician", "Research", "Resident Physician", "Rheumatology", "Siddha Medicine", 
                   "Speech Therapist", "Surgical Oncology", "Thoracic Surgery", "Unani Medicine", "Undergraduate Student", 
                   "Urology", "Vascular Surgery", "Veterinary", "Yoga"]
    
    # Validate the specialty
    if expected_specialty in specialties:
        print(f"Specialty '{expected_specialty}' found in the  list.")
    else:
        print(f"Specialty '{expected_specialty}' not found in the  list.")
    print("All Specilty::", specialties)    
    print("################################################################################################################")    
    
##################################################################################################################################################

 # Sub- Specality tab
def subspecality(driver, expected_Sub_specialty):

    Sub_speciality = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "subspecialityname")))
    Sub_speciality.click()
    Sub_speciality.send_keys(expected_Sub_specialty)
    
    # in this used collections: - Dictonary{key: value}
    specialties_SubSpecialty = {
    "Acupuncture And Acupressure": ["Traditional Acupuncture", "Medical Acupuncture"],
    "Allergy & Immunology": ["Pediatric Allergy", "Clinical Immunology"],
    "Anatomy": ["Gross Anatomy", "Neuroanatomy"],
    "Anesthesia": ["Cardiac Anesthesia", "Pediatric Anesthesia", "Neuroanesthesia"],
    "Aviation Medicine": ["Flight Surgeon", "Aerospace Medicine"],
    "Ayurveda": ["Panchakarma", "Kayachikitsa"],
    "Ayush": ["Yoga Therapy", "Naturopathy"],
    "BDS Student": ["Orthodontics", "Periodontics"],
    "Biochemistry": ["Clinical Biochemistry", "Molecular Biochemistry"],
    "Biophysics": ["Medical Biophysics", "Structural Biophysics"],
    "Biostatistics": ["Epidemiology", "Genetic Statistics"],
    "Blood Banking & Tranfusion Medicine": ["Clinical Transfusion", "Apheresis"],
    "Cardiology": ["Interventional Cardiology", "Pediatric Cardiology", "Electrophysiology"],
    "Colon & Rectal Surgery": ["Proctology", "Colorectal Oncology"],
    "Community Medical Services And Ed": ["Public Health", "Epidemiology"],
    "Community Medicine/ Psm": ["Preventive Medicine", "Occupational Health"],
    "Dentistry": ["Endodontics", "Prosthodontics"],
    "Dermatology": ["Cosmetic Dermatology", "Dermatopathology"],
    "Dietician/ Nutrition": ["Clinical Nutrition", "Sports Nutrition"],
    "Electropathy": ["Electro Homeopathy", "Electro Acupuncture"],
    "Embryology": ["Clinical Embryology", "Reproductive Biology"],
    "Emergency Medicine": ["Trauma Medicine", "Pediatric Emergency Medicine"],
    "Endocrinology": ["Diabetes", "Thyroid Disorders"],
    "Family Medicine": ["Geriatric Medicine", "Adolescent Medicine"],
    "Forensic Medicine": ["Forensic Pathology", "Forensic Toxicology"],
    "Gastroenterology": ["Hepatology", "Pediatric Gastroenterology"],
    "General Practice": ["Primary Care", "Family Planning"],
    "General Surgery": ["Minimally Invasive Surgery", "Trauma Surgery"],
    "Geriatric Medicine": ["Geriatric Psychiatry", "Geriatric Rehabilitation"],
    "Health Journalism": ["Medical Writing", "Health Communication"],
    "Hematology": ["Hematologic Oncology", "Transfusion Medicine"],
    "Homeopathy": ["Clinical Homeopathy", "Homeopathic Pediatrics"],
    "Infectious Disease": ["HIV/AIDS", "Tropical Medicine"],
    "Integrative Medicine": ["Holistic Medicine", "Complementary Medicine"],
    "Intensive Care Specialist": ["Critical Care Medicine", "Pediatric Intensive Care"],
    "Internal Medicine": ["Pulmonology", "Rheumatology"],
    "Lab Technician": ["Clinical Laboratory Science", "Histotechnology"],
    "Medical Administration": ["Healthcare Management", "Hospital Administration"],
    "Medical Genetics": ["Clinical Genetics", "Genetic Counseling"],
    "Medical Oncology": ["Radiation Oncology", "Surgical Oncology"],
    "Medico-Legal Expert": ["Forensic Medicine", "Legal Medicine"],
    "Microbiology": ["Clinical Microbiology", "Immunology"],
    "Multipurpose Health Worker": ["Community Health Worker", "Public Health Worker"],
    "Naturopathy": ["Hydrotherapy", "Botanical Medicine"],
    "Neonatology": ["Perinatal Medicine", "Neonatal Intensive Care"],
    "Nephrology": ["Dialysis Medicine", "Renal Transplantation"],
    "Neurology": ["Neurocritical Care", "Pediatric Neurology"],
    "Neurosurgery": ["Spine Surgery", "Neuro-oncology"],
    "Nuclear Medicine": ["Radiopharmacy", "Therapeutic Nuclear Medicine"],
    "Nursing": ["Critical Care Nursing", "Pediatric Nursing"],
    "Obstetrics & Gynecology": ["Maternal-Fetal Medicine", "Gynecologic Oncology"],
    "Occupational Medicine": ["Industrial Medicine", "Occupational Health Psychology"],
    "Ophthalmology": ["Retina Specialist", "Pediatric Ophthalmology"],
    "Oral & Maxillofacial Surgery": ["Craniofacial Surgery", "Oral Oncology"],
    "Orthopaedic Surgery": ["Sports Medicine", "Joint Replacement Surgery"],
    "Otolaryngology (ENT)": ["Head and Neck Surgery", "Otology"],
    "Palliative Medicine": ["Hospice Care", "Pain Management"],
    "Pathology": ["Cytopathology", "Forensic Pathology"],
    "Pediatrics": ["Neonatology", "Pediatric Cardiology"],
    "Pharmacology": ["Clinical Pharmacology", "Pharmacogenomics"],
    "Physical Medicine And Rehabilitation": ["Spinal Cord Injury Medicine", "Pediatric Rehabilitation"],
    "Physiology": ["Cardiovascular Physiology", "Neurophysiology"],
    "Physiotherapy": ["Orthopedic Physiotherapy", "Neurological Physiotherapy"],
    "Plastic Surgery": ["Reconstructive Surgery", "Cosmetic Surgery"],
    "Preventive Medicine": ["Public Health", "Occupational Medicine"],
    "Psychiatry": ["Child and Adolescent Psychiatry", "Forensic Psychiatry"],
    "Pulmonology": ["Sleep Medicine", "Interstitial Lung Disease"],
    "Radiation Oncology": ["Brachytherapy", "Radiobiology"],
    "Radiology": ["Interventional Radiology", "Diagnostic Radiology"],
    "Radiology Imaging Technician": ["CT Technician", "MRI Technician"],
    "Research": ["Clinical Research", "Translational Research"],
    "Resident Physician": ["Internal Medicine Residency", "Surgical Residency"],
    "Rheumatology": ["Pediatric Rheumatology", "Autoimmune Diseases"],
    "Siddha Medicine": ["Siddha Pharmacology", "Siddha Internal Medicine"],
    "Speech Therapist": ["Pediatric Speech Therapy", "Voice Therapy"],
    "Surgical Oncology": ["Breast Surgical Oncology", "Colorectal Surgical Oncology"],
    "Thoracic Surgery": ["Cardiothoracic Surgery", "Thoracic Oncology"],
    "Unani Medicine": ["Ilaj Bit Tadbeer", "Unani Pharmacology"],
    "Undergraduate Student": ["Pre-medical Studies", "Biomedical Sciences"],
    "Urology": ["Pediatric Urology", "Urologic Oncology"],
    "Vascular Surgery": ["Endovascular Surgery", "Peripheral Vascular Surgery"],
    "Veterinary": ["Veterinary Surgery", "Veterinary Pathology"],
    "Yoga": ["Therapeutic Yoga", "Yoga Research"]
    }  
     
# or /for loop iterating dictonary use loop 
    # for   iterate_list in specialties_SubSpecialty.values() :   # values() enterd for reading value.if not written it will print only key data
    #     print("List oiption:" , iterate_list)
         
# Validate the Sub_specialty
    if expected_Sub_specialty in specialties_SubSpecialty:
        print(f"Sub-Specialty '{expected_Sub_specialty}' found in the list.")
    else:
        print(f"Sub-Specialty '{expected_Sub_specialty}' not found in  list.")

    print("All Specilty::", specialties_SubSpecialty)    
    print("################################################################################################################")    

#####################################################################################################################
def suffix_qualification(driver, expected_suffix_qual_list):
    suffix_qual = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "suffixname")))
    suffix_qual.click()
    suffix_qual.send_keys(expected_suffix_qual_list)
    
    suffix_qual_list = ["MD", "DO", "MBBS", "MBChB", "MBBS-MD", "PhD", "DSc", "MS", "MSc", "MPH", "MBA(HM)", "MPAS", "DPT", 
    "DNP", "DDS", "DMD", "PharmD", "DC", "DVM", "PsyD", "FAAN", "APN", "RN", "MN", "ET", "WOCN"]
    
    # Validate the suffix qualification
    if expected_suffix_qual_list in suffix_qual_list:
        print(f"Suffix qualification '{expected_suffix_qual_list}' found in the list.")
    else:
        print(f"Suffix qualification '{expected_suffix_qual_list}' not found in the list.")

    print("All Suffix Qualifications:", suffix_qual_list)
    print("################################################################################################################")    

    
    
    
########################################################################################################################    
if __name__ == "__main__":
    
    # Setup WebDriver
    driver = setup_driver()

    # Navigate to login page
    navigate_to_login(driver)   
    
    # Fill login credentials
    fill_login_credentials(driver)
    
    # All Events Tab
    biodetail_menu(driver) 
    
    # speciality tab
    #url = "https://curofy.com/doctors-directory"
    expected_specialty = "Cardiology"
    fetch_and_validate_specialty(driver, expected_specialty)    
    
    # Sub- Specality tab
    expected_Sub_specialty = "HIV/AIDS"
    subspecality(driver, expected_Sub_specialty)
     
   # Suffix_qualification tab
    expected_suffix_qual_list = "MD"
    suffix_qualification(driver, expected_suffix_qual_list)
