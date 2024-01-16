import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

common = webdriver.ChromeOptions()
common.add_experimental_option("detach",True)
my_email = os.environ["EMAIL"]
my_pass = os.environ["PASSWORD"]

URL = "https://myaccount.uscis.gov/"
driver = webdriver.Chrome(options=common)
driver.get(url=URL)

email = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/form/div[1]/input")
email.send_keys(my_email)

password = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/form/div[2]/input")
password.send_keys(my_pass,Keys.ENTER)