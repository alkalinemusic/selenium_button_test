"""
This test will determine if the "OUR STORY" button on the landing page of showseeker.com 
will redirect to the "About Us" page when clicked.
The browser being accessed is Chrome.
The Chrome webdriver used is located locally. 

Classes imported
    webdriver   - for accessing the Chrome webdriver
    time        - python library module for pausing the script, for visual checks and permitting
                  the page load time before enacting a successive action
    
Test Case
    1. Open Chrome and maximize the window size
    2. Enter the url "showseeker.com"
    3. Ensure the correct title "ShowSeeker" is in the page title tag
    4. Locate the "OUR STORY" button using the xpath
    5. Click on the "OUR STORY" button 
    6. Ensure the correct title "About us | ShowSeeker" is in the page title tag (2 second pause before running this check)
    7. Close browser

"""


# import selenium webdriver
from selenium import webdriver
# import time module from Python library
import time

# set the url to be accessed
root_url = "https:www.showseeker.com"


# set the webdriver for chrome
chromeDriver = webdriver.Chrome(
    executable_path="/Users/admin/Documents/Coding/python_files/virtual_environments/virt01/drivers/chromedriver")

# maximize the window when open, wait 1sec., load the url var
chromeDriver.maximize_window()
chromeDriver.implicitly_wait(1)
chromeDriver.get(root_url)


# ensure the page name is in the title
assert "ShowSeeker" in chromeDriver.title

# set var to the element we are searching for... ID="yui_3_17_2_1_1603495020232_218"
target_element = chromeDriver.find_element_by_xpath(
    "/html/body/div[4]/div[2]/div/main/section[1]/div[2]/div/div/div/div[2]/div/div/a")

# click on the target_element
target_element.click()

# wait 2 seconds for the page to properly load before the next command
time.sleep(2)

# verify that the page title tag includes the About us page title
assert "About Us | ShowSeeker" in chromeDriver.title

# verify the correct page was loaded - ?? name of the button that was clicked

# wait 10 seconds - simply for visual confirmation tests
time.sleep(10)

# close the browser/webdriver
chromeDriver.close()
