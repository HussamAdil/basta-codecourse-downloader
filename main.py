from  selenium import webdriver 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ChromeDriverPATH = "/home/hussamadil/Desktop/chromedriver" #change it base on your chromedriver path  

driver = webdriver.Chrome(ChromeDriverPATH)

#config

course_url = input('course url ? ')

number_of_videos = input('How videos do you want to download ? ')

user_email = "hussam0683@gmail.com"

user_password = "5b9ebe7e6d1e49ea951bff40a3323b0d6c66d650de0e2497fc42ce2d22ada645"

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
        time.sleep(60)