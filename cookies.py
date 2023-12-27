from auth_date import apollo_login, apollo_pass # создал файл auth_date, в нем находятся логин и пароль
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time

driver = webdriver.Chrome()


driver.get("https://app.apollo.io/#/settings/account/mailboxes")
driver.maximize_window()
time.sleep(10)

email_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div/div/input')
email_login.send_keys(apollo_login)
time.sleep(1)
	
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[6]/div/div[1]/div/input')
password.send_keys(apollo_pass)
time.sleep(1)
button_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[7]/button')
button_login.click()
time.sleep(40)

pickle.dump(driver.get_cookies(), open(f"{apollo_login}_cookies", "wb")) # сохранение куки


	#Авторизация с куки

driver.get("https://app.apollo.io/#/companies?finderViewId=5a205be49a57e40c095e1d60")
driver.maximize_window()
time.sleep(5)


for cookie in pickle.load(open(f"{apollo_login}_cookies", "rb")):
	driver.add_cookie(cookie)
	
print("Куки подгружены")