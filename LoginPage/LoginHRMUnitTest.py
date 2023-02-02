import time
import unittest
from selenium import webdriver

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..","..")) # Three dots denotes the heirarchy where the file(that need to tun) is kept. 3 dots could be 2,1 or 4 depend upon hierarchy.

from Demo.POM.Tests.LoginWindow import Login
from Demo.POM.Tests.HomeScreen import HomePage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.drive = webdriver.Chrome("F:\Selenium Learning\Drivers\chromedriver.exe")
        cls.drive.maximize_window()
        cls.drive.implicitly_wait(10)

    def test_mmfs(self):
        self.drive.get("https://wealthelite.in/client-login")
        Log_in = Login(self.drive)
        Log_in.enter_username("dubey.rounak@gmail.com")
        Log_in.enter_password("695480")
        Log_in.login_button()

        Home_p = HomePage(self.drive)
        Home_p.profile_click()
        Home_p.logout()
        Home_p.confirm_logout()

        # self.driver.find_element_by_name("username").send_keys("dubey.rounak@gmail.com")
        # self.driver.find_element_by_name("password").send_keys("695480")
        # self.driver.find_element_by_class_name("btn.btn-primary.nc-lf-btn").click()
        # self.driver.find_element_by_class_name()
        # self.driver.find_element_by_class_name()
        print(self.drive.title)
        time.sleep(2)

    # def test_orangehrm(self):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     self.driver.find_element_by_name("username").send_keys("Admin")
    #     self.driver.find_element_by_name("password").send_keys("admin123")
    #     self.driver.find_element_by_class_name("oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
    #     print(self.driver.title)
    #     time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.drive.close()
        cls.drive.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
