import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_visit_google(self):
        self.driver.get('https://www.google.com/')

    def test_hello_world(self):
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-worl-report'))