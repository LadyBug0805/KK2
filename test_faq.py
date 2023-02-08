from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://70000tons.com")
driver.maximize_window()

select_language = driver.find_element(By.LINK_TEXT, "English")
select_language.click()

faq = driver.find_element(By.ID, "umc-div-menu-faq")
faq.click()
time.sleep(3)
driver.close()