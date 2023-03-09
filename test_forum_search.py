from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestForumSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_forum_search(self):
        driver = self.driver
        driver.get("https://70000tons.com/forum/")
        driver.maximize_window()

        search = driver.find_element(By.CLASS_NAME, "form-control")
        search.click()
        search.clear()
        search.send_keys("slayer")
        search.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div/span[1]"))
        assert self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div/span[1]").text == "Searched query: slayer"
