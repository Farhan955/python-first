from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
from colorama import Fore, Back, Style, init
import time

file_path = 'data/plia/snoco/snoco_data20Links.csv'
output_file_path = 'data/plia/snoco/snoco_data20Links_checked.csv'

# file_path = 'data/plia/king/data63Links.csv'
# output_file_path = 'data/plia/king/data63Links_checked.csv'

start_time = time.time()

# Set up the Chrome driver service
s = Service("E:/python_projects/FirstProject/chromedriver.exe")
driver = webdriver.Chrome(service=s)

with open(file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    for row in csv_reader:
        if len(row) > 7:  # Check if the row has at least 8 elements
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

            # Add the input_value to the row
            row.append(input_value)

        # Write the updated row to the new CSV file
        csv_writer.writerow(row)

loop_end_time = time.time()
# Close the browser
driver.quit()

loop_time = loop_end_time - start_time
print(f"Time taken for looping through the CSV file: {loop_time} seconds")
