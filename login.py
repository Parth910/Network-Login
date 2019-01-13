from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynotify import pynotify
import time
import sys

connected = False

def Login():
    try:
        options = Options()
        options.add_argument('--headless')
        chromedriver = "/Users/adarshpunj/Desktop/chromedriver"
        driver = webdriver.Chrome(chromedriver,chrome_options=options)
        pynotify("Network Login","Trying to establish connection with 172.22.2.6").push()
        driver.get("https://172.22.2.6/connect/PortalMain")
        username = driver.find_element_by_id("LoginUserPassword_auth_username")
        username.send_keys("ENTER_YOUR_ID_HERE")
        password = driver.find_element_by_id("LoginUserPassword_auth_password")
        password.send_keys("ENTER_YOUR_PASSWORD_HERE")
        submit = driver.find_element_by_id("UserCheck_Login_Button_span").click()
        pynotify("Network Login","You are now connected to the internet")
        time.sleep(3)
        driver.quit()
        pynotify("Network Login","You are now connected to the internet").push()
        return True
    except:
        pynotify("Network Login","Attempt to login failed. Please try again").push()
        return False

def checkTime():
    timeout = time.time()+6
    while True:
        if time.time()>timeout:
            pynotify("Network Login","172.22.2.6 is taking too long to connect.").push()
            sys.exit()

connection = Login()
if connection == False:
	checkTime()
