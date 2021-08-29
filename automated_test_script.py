from selenium import webdriver
from random import randint
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

# timeout declaration
wait = WebDriverWait(driver, 80)

# starting the driver with the web app
driver.get('https://www.americanas.com.br/categoria/celulares-e-smartphones?origem=blanca')

print("Test of adding products to a shopping basket with 10 products.")

for i in range (1, 10):

    #  this will click on the mobile model in random form
    random_model = randint(1, 12)
    celulares_model_choice = wait.until(EC.visibility_of_element_located((By.XPATH, \
    f'/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/section/div/div/div/ul/li[{random_model}]/a/img')))
    celulares_model_choice.click()
    print(f"  * Celular model clicked, in li position {random_model}")

    # this will randomly chose a mobile phone to click
    random_phone = randint(0, 4)
    celulares_choosen = wait.until(EC.visibility_of_element_located((By.XPATH, \
    f'/html/body/div[2]/div/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div/div/div[1]/div[{random_phone}]/div/div[2]/a/section/div[1]/div/div/picture/img')))
    celulares_choosen.click()
    print(f"  * Celular choosen clicked, in div position {random_phone}")

    # a click in the "Comprar" button
    comprar_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div[3]/a[1]/span')))
    comprar_button.clear()
    print("  * Comprar button clicked")

    try:
        # a click on the "Confirmar" pop up button that some times show up
        confirmation_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/a[2]')))
        confirmation_button.click()
        print("  * Confirmation button clicked")
    except:
        pass
    
    # a click on the "Continuar" button
    continue_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div/a')))
    continue_button.click()
    print("  * Continue button clicked")

    #  a click on the "adicionar mais produtos" link test
    add_more_link = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/a')))
    add_more_link.click()
    print("  * Add more products link clicked")

    print(f"Product added to basket. Number: {i}")