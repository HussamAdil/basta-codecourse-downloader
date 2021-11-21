from  selenium import webdriver 
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ChromeDriverPATH = "/home/hussamadil/Desktop/chromedriver" #change it base on your chromedriver path  

driver = webdriver.Chrome(ChromeDriverPATH)

#config

course_url = input('course url ? ')

number_of_videos = input('How videos do you want to download ? ')

user_email = input(' Your email ? ')

user_password = input(' Your password ? ')

# login process

driver.get("https://codecourse.com/auth/signin")

email = driver.find_element_by_id("email")

password = driver.find_element_by_id("password")

email.send_keys(user_email)

password.send_keys(user_password)

driver.find_element_by_tag_name("button").click()

WebDriverWait(driver, 10).until(EC.url_to_be("https://codecourse.com/dashboard"))

driver.implicitly_wait(5)

driver.get(course_url)

#download

for x in range(0, int(number_of_videos)):
        links = driver.find_elements_by_class_name('opacity-25')[x].find_element_by_tag_name('a')
        links.click()
        time.sleep(10)