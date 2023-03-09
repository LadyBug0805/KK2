# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_deutsch(self):
        self.driver.get("https://70000tons.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "English").click()
        self.driver.find_element(By.LINK_TEXT, "English").click()

        el = self.driver.find_element(By.ID, "mega-menu-item-wpml-ls-18-en")
        ActionChains(self.driver).move_to_element(el).perform()
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.LINK_TEXT, "Deutsch"))
        self.driver.find_element(By.LINK_TEXT, "Deutsch").click()
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(
            By.XPATH, "//*[@id=\"intro-message\"]/h1"))
        assert self.driver.find_element(
            By.XPATH, "//*[@id=\"intro-message\"]/h1").text == "DAS ORIGINAL, DIE WELTGRÖSSTE HEAVY-METAL-KREUZFAHRT"
