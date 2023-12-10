import pytest_html
import requests
import pytest
import json
from datetime import datetime
from appium import webdriver
from selenium.webdriver.common.by import By
import os

from pytest_html.html_report import HTMLReport

from Appium.CommonFunction import takeScreenShot


class TestAPI:
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5556",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def test_api_get_request(self):
        response = requests.get('https://gorest.co.in/public/v2/users/1830460/posts')
        assert response.status_code == 200
        assert 'successful' in response.text

    def test_api_post_request(self):
        url = "https://gorest.co.in/public/v2/users"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer 3507b1c48738f8767ab6b44db07b47d51a5cab536c59b0eff1e3e510817984b0"
        }
        data = {
            "name": "Tenali Ramakrishna",
            "gender": "male",
            "email": "tenali.ramakrishna@15ce.com",
            "status": "active"
        }

        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 422
        assert '"has already been taken' in response.text

    def test_api_get_request2(self):
        response = requests.get('https://gorest.co.in/public/v2/posts')
        assert response.status_code == 200
        assert 'user_id' in response.text

    def test_chromeApp(self):
        url = "https://m.taobao.com"
        # 手机淘宝H5
        driver = self.driver
        #   driver.implicitly_wait(10)

        driver.implicitly_wait(30)
        driver.find_element(By.ID, 'com.android.chrome:id/terms_accept').click()
        driver.implicitly_wait(20)
        driver.find_element(By.ID, 'com.android.chrome:id/negative_button').click()
        driver.implicitly_wait(50)
        driver.find_element(By.ID, 'com.android.chrome:id/negative_button').click()
        driver.implicitly_wait(20)
        # Navigate to a URL
        driver.get(url)
        takeScreenShot(driver, name="ScreenShot")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(os.getcwd() + "\\report", f"Appium_test_report_{now}.html")
    pytest.main(['-v', '-s', 'TestAPI.py', '--html=' + report_path])
