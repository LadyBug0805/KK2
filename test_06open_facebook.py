
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver import get_webdriver


class TestTestopenfacebook():
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

    def test_testopenfacebook(self):
        self.driver.get("https://70000tons.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "English").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(
            By.CSS_SELECTOR, "#sidebar > #text-14 a:nth-child(1) > img").click()
        self.vars["win3036"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win3036"])
        assert self.driver.current_url == "https://www.facebook.com/70000tons"
