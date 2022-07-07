import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest(unittest.TestCase):
    base_url = 'http://www.amazon.com/'

    def setUp(self):
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)

    def TearDown(self):
        self.driver.quit()


