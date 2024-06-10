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
    time.sleep(15)
    
##########################################################################################################################################################################3
# Survey Tab
def survey_menu(driver):
    # Wait for the menu to be present and clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/a[30]/li[1]/div[1]/div[1]/img[1]")) ).click()  
    time.sleep(10)
    Title_Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'justify-content-center align-items-center text-center')][normalize-space()='Survey Mgmt.'])[1]")))
    if Title_Name:
        print("TITLE NAME IS VISIBLE")
    else:
        print("Title not visible")
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]"))).click( )
    time.sleep(5)
    
    # Topic Tab
    topic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "survey_topic")))
    topic.send_keys("revolution in medical science")
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "survey_topic"))).send_keys("revolution in medical science")
        
            
            








                
if __name__ == "__main__":
            
        # Setup WebDriver
        driver = setup_driver()

        # Navigate to login page
        navigate_to_login(driver)   
        
        # Fill login credentials
        fill_login_credentials(driver) 
        
        # Survey Tab
        survey_menu(driver)












