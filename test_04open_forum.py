
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver import get_webdriver

class TestUntitled():
  def setup_method(self, method):
    self.driver = get_webdriver()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_open_forum(self):
    self.driver.get("https://70000tons.com/")
    self.driver.set_window_size(1936, 1048)
    self.driver.maximize_window()
    self.driver.find_element(By.LINK_TEXT, "English").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#sidebar > #text-14 a:nth-child(7) > img").click()
    self.vars["win1262"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win1262"])
    assert self.driver.current_url == "https://70000tons.com/forum/"
    assert self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div[1]/ol/li[2]").text == "70000TONS OF METAL OFFICIAL FORUM"
  
