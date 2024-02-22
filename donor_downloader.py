from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import secrets


DONORBOX_LOGIN_URL = "https://donorbox.org/org_session/new"
USERNAME = secrets.username
PASSWORD = secrets.password

driver = webdriver.Firefox()
driver.get(DONORBOX_LOGIN_URL)

username_input_field = driver.find_element(By.ID, "org_user_session_email")
password_input_field = driver.find_element(By.ID, "org_user_session_password")
login_button = driver.find_element(By.NAME, "commit")

username_input_field.send_keys(USERNAME)
password_input_field.send_keys(PASSWORD)
login_button.click()

'''
looks like captcha doesnt pop-up everytime
wait to see if captcha frame appears before trying to solve
'''  
#TODO: fix below; it doesnt click on the captcha checkbox 
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"g-recaptcha")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

# solve the captcha
#solver = RecaptchaSolver(driver=driver)
#recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title=reCAPTCHA"]')
#solver.click_recaptcha_v2(iframe=recaptcha_iframe)


