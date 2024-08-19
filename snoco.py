from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.snoco.org/proptax/(S(twct4amugydns1c1d3pts1u2))/default.aspx"

# Set up the browser
driver = webdriver.Chrome()
driver.get(url)

# Find the input element and set its value
parcel_input = driver.find_element(By.ID, "mParcelID")
parcel_input.clear()  # Clear any existing value
parcel_input.send_keys("01106500001600")

# Find and click the search button
search_button = driver.find_element(By.ID, "mPayTaxes")
search_button.click()


# Once the results are loaded, you can extract the information you need
# For example, you could use BeautifulSoup to parse the HTML of the results
soup = BeautifulSoup(driver.page_source, 'html.parser')
# Now you can use BeautifulSoup to parse the results
print(soup.select('#mSitusAddressLabel')[0])
print(soup.select('#mSitusAddressLabel')[0])
# Don't forget to close the browser when you're done






address = soup.select('#mSitusAddress')[0]
a_href_click = soup.select('#mRealPropertyStructures tr td a')[0]
print("Address: ",address.text)
# Find the table with id "mParties"
table = soup.find('table', {'id': 'mParties'})

# Find all rows in the table
rows = table.find_all('tr')

# Skip the first row as it contains the header
for row in rows[1:]:
    # Find all cells in the row
    cells = row.find_all('td')
    # The role is in the first cell (index 0)
    role = cells[0].text.strip()
    # The name is in the third cell (index 2)
    name = cells[2].text.strip()
    if role == "Owner":
        print("Owner: ",name)


# Set up the browser
# print(a_href_click)
# driver = webdriver.Chrome()  # You'll need to have the Chrome WebDriver installed: https://sites.google.com/a/chromium.org/chromedriver/
# driver.get(a_href_click.search_button.click())

# Find and click the link using Selenium
# link = driver.find_element(By.XPATH, '//a[contains(@href, "PropInfo05-StructData.asp")]')
# link.click()

# Find and click the link using Selenium
link = driver.find_element(By.XPATH, '//a[contains(@href, "PropInfo05-StructData.asp")]')

# Open the link in a new tab (Ctrl+click)
ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Get the page source of the new tab
new_tab_html = driver.page_source

# Switch back to the original tab if needed
# driver.switch_to.window(driver.window_handles[0])

# Print or save the HTML content of the new tab
# print(new_tab_html)

# Assume 'html' contains the HTML content you provided
soup = BeautifulSoup(new_tab_html, 'html.parser')

# Find all rows in the table
rows = soup.find_all('tr')

# Search for the row containing the label "Heat"
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 2 and cells[1].text.strip() == "Heat":
        # The value is in the next cell
        heat_value = cells[2].text.strip()
        print("Heat Value:", heat_value)
        break


driver.quit()