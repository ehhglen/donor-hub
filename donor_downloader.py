from selenium import webdriver
from selenium.webdriver.common.by import By
import secrets


DONORBOX_LOGIN_URL = "https://donorbox.org/org_session/new"
USERNAME = secrets.username
PASSWORD = secrets.password

driver = webdriver.Firefox()
driver.get(DONORBOX_LOGIN_URL)

username_input_field = driver.find_element(By.ID, "org_user_session_email")
password_input_field = driver.find_element(By.ID, "org_user_session_password")

username_input_field.send_keys(USERNAME)
password_input_field.send_keys(PASSWORD)



