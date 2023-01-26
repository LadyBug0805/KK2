from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://70000tons.com/forum/")
print(driver.title)

search =  driver.find_element(By.CLASS_NAME, "form-control")
search.send_keys("Slayer")
search.send_keys(Keys.RETURN)
time.sleep(5)