from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service #не было ранее
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import pickle
from auth_date import apollo_login, apollo_pass



options = webdriver.ChromeOptions()
# options.add_argument('user-agent=Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')

options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome()


try:


	# driver.get("https://app.apollo.io/#/settings/account/mailboxes")
	# driver.maximize_window()
	# time.sleep(10)

	# email_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div/div/input')
	# email_login.send_keys(apollo_login)
	# time.sleep(1)

	# password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[6]/div/div[1]/div/input')
	# password.send_keys(apollo_pass)
	# time.sleep(1)
	# button_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[7]/button')
	# button_login.click()
	# time.sleep(40)

	# pickle.dump(driver.get_cookies(), open(f"{apollo_login}_cookies", "wb")) # сохранение куки


	#Авторизация с куки

	driver.get("https://app.apollo.io/#/companies?finderViewId=5a205be49a57e40c095e1d60")
	driver.maximize_window()
	time.sleep(5)


	for cookie in pickle.load(open(f"{apollo_login}_cookies", "rb")):
		driver.add_cookie(cookie)
	
	print("Куки подгружены")


	time.sleep(2)
	driver.refresh()
	
	print("Страницу перезагрузил, входим в аккаунт")
	time.sleep(3)


	button_company = driver.find_element(By.XPATH, '//*[@id="main-app"]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[4]/div[2]/div/span/div[1]')
	button_company.click()
	time.sleep(1)

	send_company = str(input("Введи название компании: "))


	select_name_company = driver.find_element(By.XPATH, '//*[@id="main-app"]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[1]/input') # ебать! едва нашел!
	select_name_company.send_keys(send_company)
	time.sleep(2)
	select_name_company.send_keys(Keys.ENTER)
	time.sleep(5)

	company_singl_link = driver.find_element(By.CLASS_NAME, 'zp_J1j17')
	print(company_singl_link.text)
	company_singl_link.click()
	time.sleep(5)	


	empl = driver.find_element(By.XPATH, '//*[@id="location_detail_card"]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/a')
	empl.click()
	time.sleep(3)
	
	# with open(f'{send_company}.csv', 'w', encoding='utf-8') as file:
	# 	writer = csv.writer(file)
	# 	writer.writerow(['Persones', 'Jobs'])


	def persUrl():

		blocks = driver.find_elements(By.CLASS_NAME, 'zp_xVJ20')

		num = 0
		previous_url = driver.current_url  # сохраняем URL текущей страницы
		links = []
		for block in blocks:
			num += 1
			link = block.find_element(By.TAG_NAME, 'a')
			href = link.get_attribute('href')
			print(f'{num}.', href)
			links.append(href)

		for href in links:
			driver.get(href)
			
			try:
				name_persone = driver.find_element(By.XPATH, '//*[@id="general_information_card"]/div/div/div/div/div[1]/div[1]/div[1]/div/span')
				print("Имя: ", name_persone.text)
			except:
				print("Блок с именем не найден")


			try:
				jobs = driver.find_element(By.CLASS_NAME, 'zp_Y6y8d')
				print("Должность: ", jobs.text)
			except:
				print("Должность не найдена")

					# Локация
			try:
				location = driver.find_element(By.XPATH, '//*[@id="location_detail_card"]/div/div/div/div/div[2]/div/div/form/div/div/div[2]/div/div/div[1]/div[2]')
				print("Локация: ", location.text)
			except:
				print("Локация не определа")

			try:
				linkedin_link = driver.find_element(By.XPATH, '//a[contains(@href, "linkedin.com")]')
				linkedin_url = linkedin_link.get_attribute("href")
				print("Ссылка на Linkedin: ", linkedin_url)
			except:
				print("Ссылка на Linkedin не найдена")


					# Это для кнопки на персональной странице сотрудника. Нажмаем на нее - там показываются емейлы
			try:	
				button_emails = driver.find_element(By.XPATH, '//*[@id="general_information_card"]/div/div/div/div[1]/div/div[2]/div/button')
				button_emails.click()
				time.sleep(2)
			except:
				print("Все норм, кнопки нет")

			try:
				number_person = driver.find_element(By.XPATH, '//*[@id="general_information_card"]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/a/span')
				print(number_person.text)
			except:
				print("Ошибка")


			try:
				emails_one = driver.find_element(By.XPATH, '//*[@id="general_information_card"]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/a')
				email_one = emails_one.text.strip()  
				print("Email: ", email_one)
			except:
				print("Email не найден")

			try:
				emails_two = driver.find_element(By.CLASS_NAME, 'zp_RIH0H zp_dAPkM zp_Iu6Pf')
				email_two = emails_two.text.strip()
				print("Email: ", email_two)
			except:
				print("Email не найден")

				time.sleep(2)
			print("\n")

			# Кнопка для перехода по страницам компании
			# button_next = driver.find_element(By.XPATH, '//*[@id="panel-content-container"]/div/div[2]/div/div[2]/div/div/div/div/div/div[4]/div/div/div/div/div[3]/div/div[2]/button[2]')
			# button_next.click()
			# time.sleep(5)

	persUrl()


	# Условие цикла
	# while True:
	# 	persInfo()


except Exception as ex:
	print(ex)
# finally:
# 	driver.close()
# 	driver.quit()









