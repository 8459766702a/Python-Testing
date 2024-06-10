import time
import time
from tkinter import Button, Entry, Label, Tk
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



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
    
##########################################################################################################################################################################
def comp_intel_mang(driver):
     # Wait for the menu to be present and clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[23]/li[1]/div[1]/div[1]/img[1]"))).click()  
    time.sleep(10)
    Comp_intel= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]")))
    Comp_intel.click()
    time.sleep(10)

    tab= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[5]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")))
    tab.click()
    tab.send_keys("sara p")
    print("title name:" , tab.get_attribute('value'))
    time.sleep(10)

    




##############################################################################################################################################################        
                
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # clinical trial Tab
        comp_intel_mang(driver)    