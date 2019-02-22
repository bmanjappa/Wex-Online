from selenium import webdriver
import unittest
import time


class WexOnlineTest(unittest.TestCase):
    def setUp(self):

        # get base url for web portal
        web_url = "http://go.wexonline.com"
        #  get the path of chromedriver.exe file
        path = "C:\\Projects\\Drivers\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get(web_url)
        self.driver.implicitly_wait(10)


        # Maximize  browser
        self.driver.maximize_window()

    def test_download_file(self):
        driver = self.driver

        # input username and password
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("wtcleland")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("dQRbQSRq9gU4")

        # click login button
        driver.find_element_by_id("loginSubmit").click()

        # Click  Reports
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)

        # Click View My Reports
        driver.find_element_by_link_text("View My Reports").click()
        time.sleep(5)

        # Click select button
        driver.find_element_by_xpath("//*[@id='body']/main/div[2]/div/div[4]/table/tbody/tr[1]/td[9]/div/button").click()
        time.sleep(7)

        # Click Download
        driver.find_element_by_link_text("Download").click()
        time.sleep(12)

    def tearDown(self):
        # close the browser
        self.driver.quit()
