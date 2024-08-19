import csv
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore, Style, init

file_path = 'data/dataLinks.csv'

# Initialize colorama
init()

# Set up the Chrome driver service path
driver_path = "E:/python_projects/FirstProject/chromedriver.exe"


# Function to process a single URL
def process_url(number, url, driver_path):
    # Initialize the WebDriver for this thread
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.get(url)

    try:
        # Find the input element using the correct locator strategy
        input_element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[1]/div[1]/div/input")
        input_value = input_element.get_attribute("value")

        if input_value == "Yes":
            print(Fore.GREEN + f"Parcel Number: {number} {input_value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Parcel Number: {number} {input_value}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.YELLOW + f"Error processing Parcel Number: {number} - {e}" + Style.RESET_ALL)

    finally:
        driver.quit()


# Read the CSV file and start processing
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    threads = []
    for row in csv_reader:
        url = row[7]
        if not url:
            continue
        number = row[0]

        # Create a new thread for each URL
        thread = threading.Thread(target=process_url, args=(number, url, driver_path))
        threads.append(thread)

        # Start the thread
        thread.start()

        # If we have 5 threads running, wait for them to finish before starting new ones
        if len(threads) >= 10:
            for t in threads:
                t.join()
            threads = []

    # Ensure all remaining threads are finished
    for t in threads:
        t.join()
