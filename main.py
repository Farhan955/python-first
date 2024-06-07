
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Chrome driver service
s = Service("E:/python_projects/FirstProject/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open the target URL
# driver.get("https://plia.tfaforms.net/64?ownerfn=%25GENEVIEVE%25&ownerln=%25YEE%25&tadd=%257307%2033RD%20AVE%20NE%25&tcity=%25SEATTLE%25&tzip=%2598115%25&pnumber=3290800050")
driver.get("https://plia.tfaforms.net/64?ownerfn=%25SALLY%20HOLMES%25&ownerln=%25REED%25&tadd=%257325%2033RD%20AVE%20NE%25&tcity=%25SEATTLE%25&tzip=%2598115%25&pnumber=3290800030")

# Find the input element using the correct locator strategy
input_element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[1]/div[1]/div/input")

input_value = input_element.get_attribute("value")

print(f"The value of the input field is: {input_value}")

# Close the browser
driver.quit()


# /html/body/div/div/div[2]/div/form/div[1]/div[1]/div/input

#for java script enabled pages we have to use the Selenium library