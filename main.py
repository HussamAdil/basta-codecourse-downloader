from selenium import webdriver 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import click


@click.command(name= "download")
@click.option("--chrome-path", default="/home/hussamadil/Desktop/chromedriver", help="Chrome web driver for Seliunm. Download from here: https://chromedriver.chromium.org/downloads/")
@click.option("--course-url", help="Please enter the course url.")
@click.option("--number-of-videos", help= "Enter the number of videos to be downloaded.", default=1)
@click.option("--email", help="The email you used to sign up for Codecourse website")
@click.option("--password", help="The password you used to sign up for Codecourse website")
def main(chrome_path, course_url, number_of_videos, email, password):
    """A small script to help you download videos from CodeCourse"""
    
    driver = webdriver.Chrome(chrome_path)

    # go to login url  process
    driver.get("https://codecourse.com/auth/signin")
    
    web_email = driver.find_element_by_id("email")
    web_password = driver.find_element_by_id("password")
    
    #submit login form 
    web_email.send_keys(email)
    web_password.send_keys(password)
    driver.find_element_by_tag_name("button").click()
    
    # wait until login successful done
    WebDriverWait(driver, 10).until(EC.url_to_be("https://codecourse.com/dashboard"))
    
    driver.get(course_url)
    driver.implicitly_wait(10)
    
    # download
    for x in range(1, int(number_of_videos)):
        try:
            links = driver.find_elements_by_class_name('opacity-25')[x].find_element_by_tag_name('a')
            links.click()
            time.sleep(20)
        except NoSuchElementException:
            driver.close()
            print('videos are not downloadable sorry man :(  ')      
            break
            
if __name__ == "__main__":
    main()
              