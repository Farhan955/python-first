import time
import csv
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize colorama
init(autoreset=True)

file_path = 'data/dataLinks.csv'

# Record the start time
start_time = time.time()

# Specify the path to Chrome's user profile directory
chrome_user_data_dir = "C:/Users/FA/AppData/Local/Google/Chrome/User Data"  # Update this path

# Set up Chrome options to use Chrome's user profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")

# Set the binary location for Chrome
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Update this path to where Chrome is installed

# Set up the Chrome driver service with Chrome's user profile options
s = Service("E:/python_projects/FirstProject/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

# Record the time after starting the driver
driver_start_time = time.time()

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        url = row[7]
        if not url:
            continue
        number = row[0]
        driver.get(url)

        input_element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[1]/div[1]/div/input")
        input_value = input_element.get_attribute("value")

        if input_value == "Yes":
            print(Fore.GREEN + f"Parcel Number: {number} {input_value}")
        else:
            print(Fore.RED + f"Parcel Number: {number} {input_value}")

# Record the time after looping through the CSV file
loop_end_time = time.time()

# Close the browser
driver.quit()

# Record the time after quitting the driver
quit_time = time.time()

# Calculate the time taken for each part
driver_startup_time = driver_start_time - start_time
loop_time = loop_end_time - driver_start_time
quit_driver_time = quit_time - loop_end_time

print(f"Time taken to start the driver: {driver_startup_time} seconds")
print(f"Time taken for looping through the CSV file: {loop_time} seconds")
print(f"Time taken to quit the driver: {quit_driver_time} seconds")
