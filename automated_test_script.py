from selenium import webdriver
from random import randint,choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from xvfbwrapper import Xvfb
from time import sleep

# to hidde the windows if you wish
# display = Xvfb()
# display.start()

users_exmaples = ["eu", "nos"]
users_info = ["Seja benvindo ao nosso estabelecimento", "Mindelo", "Cabo verde"]

# location of the chromedriver file and the google-chrome
driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)

# timeout taken to send values to the input boxes
wait = WebDriverWait(driver, 60)

driver.get('https://rgtest.casacelestina.cv/')

# send values to the full password input box
passwd_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user_pass"]')))
passwd_field.clear()
passwd_field.send_keys("fNbmS534%1@Z$yHSW^")
print("  * Password input box filled")
# click on the log now button
log_now_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wp-submit"]')))
log_now_button.click()
print("  * Log now input box clicked")