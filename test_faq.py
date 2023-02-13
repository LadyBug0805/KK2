from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


PATH = "C:\Program Files\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://70000tons.com")
driver.maximize_window()

select_language = driver.find_element(By.LINK_TEXT, "English")
select_language.click()

faq = driver.find_element(By.ID, "umc-div-menu-faq")
faq.click()
faq =WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/ul/li[6]/a/div"))
#simple_assert(faq.text, "FREQUENTLY ASKED QUESTIONS") 
driver.close()