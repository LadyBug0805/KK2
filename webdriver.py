from selenium import webdriver


def get_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    return webdriver.Chrome(options=options)
