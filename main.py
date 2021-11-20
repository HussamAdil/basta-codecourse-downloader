from  selenium import webdriver 
import time
import sys

ChromeDriverPATH = "/home/hussamadil/Desktop/chromedriver" #change it base on your chromedriver path  

driver = webdriver.Chrome(ChromeDriverPATH)

#login 

driver.get("https://codecourse.com/auth/signin?redirect=%2Fcourses%2Frealtime-private-messages-with-laravel-livewire")

email = driver.find_element_by_id("email")

password = driver.find_element_by_id("password")

email.send_keys("me@hussamadil.com")

password.send_keys("mypassword")

driver.find_element_by_tag_name("button").click()

driver.implicitly_wait(10)

number_of_videos = sys.argv[1] #set loop scope for video to be download

for x in range(1, int(number_of_videos)):
        links = driver.find_elements_by_class_name('opacity-25')[x].find_element_by_tag_name('a')
        links.click()
        time.sleep(10)
              

                 


 