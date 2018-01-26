"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "browserName": "Safari",
                'platformName': 'iOS',
                'platformVersion': '11.1',
                'deviceName': 'iPhone 6'
            })

    def tearDown(self):
        self.driver.quit()

    def test_ui_website(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        div = self.driver.find_element_by_id('i_am_an_id')
        # check the text retrieved matches expected value
        self.assertEqual('I am a div', div.text)

        # populate the comments field by id
        self.driver.find_element_by_id('comments').send_keys('My comment')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
