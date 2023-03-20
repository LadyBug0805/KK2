
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver import get_webdriver


class TestFaqtravel():
    def setup_method(self, method):
        self.driver = get_webdriver()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_faqtravel(self):
        self.driver.get("https://70000tons.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "English").click()

        #wait for page to load and click on FAQ
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/header/nav/div/ul/li[6]"))
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/header/nav/div/ul/li[6]").click()

        #Wait for Travel Questions to load
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/div/section/article/section/div[1]/div[2]/div/div[1]/a"))
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/article/section/div[1]/div[2]/div/div[1]/a").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".su-accordion:nth-child(4) .su-spoiler-icon").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(
            By.LINK_TEXT, "US State Department website").click()
        self.vars["win9655"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win9655"])
        assert self.driver.current_url == "https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wizard.html"
