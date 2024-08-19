import time
import csv
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize colorama
init(autoreset=True)

file_path = 'data/search_people_free.csv'

# Record the start time
start_time = time.time()

# Specify the path to Slimjet's user profile directory
slimjet_user_data_dir = "C:/Users/FA/AppData/Local/Slimjet/User Data"  # Update this path if needed

# Set up Chrome options to use Slimjet's user profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={slimjet_user_data_dir}")

# Set the binary location for Slimjet
chrome_options.binary_location = "C:/Program Files/Slimjet/slimjet.exe"  # Update this path to where Slimjet is installed

# Add headless mode and disable GPU
chrome_options.add_argument("--headless")  # Optional: Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU

# Set up the Chrome driver service with the Slimjet user profile options
s = Service("E:/python_projects/FirstProject/chromedriver_slimjet.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

# Record the time after starting the driver
driver_start_time = time.time()

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        url = row[0]
        if not url:
            continue
        number = row[0]
        driver.get(url)

        # Add a delay to allow the webpage to load
        time.sleep(5)  # Adjust the delay as needed

        try:
            input_element = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div")
            input_value = input_element.get_attribute("value")

            if input_value == "Yes":
                print(Fore.GREEN + f"Parcel Number: {number} {input_value}")
            else:
                print(Fore.RED + f"Parcel Number: {number} {input_value}")
        except NoSuchElementException:
            print(Fore.YELLOW + "Input element not found on the page.")

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
