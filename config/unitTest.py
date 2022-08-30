import random
import string
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        chrome_options = Options()
        chrome_options.add_argument('--disable-warnings')
        chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://stage.outreach.sloovi.com/login')

    def randomizeName(self, name):
        name = name + "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return name
