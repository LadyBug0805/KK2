from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Testfaq():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_faq(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://70000tons.com")
        self.driver.maximize_window()

        select_language = self.driver.find_element(By.LINK_TEXT, "English")
        select_language.click()

        faq = self.driver.find_element(By.ID, "umc-div-menu-faq")
        faq.click()
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.XPATH, "//*[@id=\"main\"]/article/section/h2[1]"))
        assert self.driver.find_element(
            By.XPATH, "//*[@id=\"main\"]/article/section/h2[1]").text == "FREQUENTLY ASKED QUESTIONS"
