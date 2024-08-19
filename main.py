from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
from colorama import Fore, Back, Style, init
import time

file_path = 'data/dataLinks.csv'



start_time = time.time()

# Set up the Chrome driver service
s = Service("E:/python_projects/FirstProject/chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver.get("https://plia.tfaforms.net/64?ownerfn=%25GENEVIEVE%25&ownerln=%25YEE%25&tadd=%257307%2033RD%20AVE%20NE%25&tcity=%25SEATTLE%25&tzip=%2598115%25&pnumber=3290800050")
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
            print(Fore.GREEN + f"Parcel Number: {number} {input_value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Parcel Number: {number} {input_value}" + Style.RESET_ALL)

loop_end_time = time.time()

# Close the browser
driver.quit()
quit_time = time.time()

# Calculate the time taken for each part
driver_startup_time = driver_start_time - start_time
loop_time = loop_end_time - driver_start_time
quit_driver_time = quit_time - loop_end_time

print(f"Time taken to start the driver: {driver_startup_time} seconds")
print(f"Time taken for looping through the CSV file: {loop_time} seconds")
print(f"Time taken to quit the driver: {quit_driver_time} seconds")

# /html/body/div/div/div[2]/div/form/div[1]/div[1]/div/input

#for java script enabled pages we have to use the Selenium library
