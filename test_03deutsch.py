
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver import get_webdriver


class Test():
    def setup_method(self, method):
        self.driver = get_webdriver()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_deutsch(self):
        self.driver.get("https://70000tons.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "English").click()
        self.driver.find_element(By.LINK_TEXT, "English").click()

        #Waiting for language drop-down to click on German
        el = self.driver.find_element(By.ID, "mega-menu-item-wpml-ls-18-en")
        ActionChains(self.driver).move_to_element(el).perform()
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.LINK_TEXT, "Deutsch"))
        self.driver.find_element(By.LINK_TEXT, "Deutsch").click()
        #Waiting for German page to load
        WebDriverWait(self.driver, timeout=20).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/div/section/section[1]/h1"))
        assert self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/section[1]/h1").text == "DAS ORIGINAL, DIE WELTGRÖSSTE HEAVY-METAL-KREUZFAHRT"
        assert self.driver.current_url == "https://70000tons.com/home/?lang=de"