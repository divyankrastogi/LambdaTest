import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions

# LambdaTest credentials
LT_USERNAME = 'rastogi.divyank739'
LT_ACCESS_KEY = '0bHl6G19qi83KdCstvuz9fBJ5YHhPIyl4bGsbpPH71mj5Thd26'

lt_browser_1 = {
    "build": 'AmazonPriceTest',
    "name": 'Test on Chrome',
    "platform": 'macOS Catalina',
    "browserName": 'chrome',
    "version": 'latest',
    "user": LT_USERNAME,
    "accessKey": LT_ACCESS_KEY
}
lt_browser_2 = {
    "build": 'AmazonPriceTest',
    "name": 'Test on Safari',
    "platform": 'macOS Catalina',
    "browserName": 'safari',
    "version": 'latest',
    "user": LT_USERNAME,
    "accessKey": LT_ACCESS_KEY
}
url = "https://www.amazon.com"

# Function to test the price of iPhone 13 on different browsers
def test_amazon_price_chrome():
    chrome_options = ChromeOptions()
    capabilities = lt_browser_1
    driver = webdriver.Remote(
        command_executor='https://hub.lambdatest.com/wd/hub',
        options=chrome_options,
        desired_capabilities=capabilities
    )
    driver.get(url)
    time.sleep(10)
    search_box = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
    search_box.send_keys('iphone 13')
    search_box.submit()
    time.sleep(5)
    price_element = driver.find_element(By.CSS_SELECTOR, '.a-price')
    price = price_element.text if price_element else "Price not found"
    print(f"Price of iPhone 13 on Chrome: {price}")
    driver.quit()

# Function to test the price of iPhone 13 on different browsers
def test_amazon_price_safari():
    safari_options = SafariOptions()
    capabilities = lt_browser_2
    driver = webdriver.Remote(
        command_executor='https://hub.lambdatest.com/wd/hub',
        options=safari_options,
        desired_capabilities=capabilities
    )
    driver.get(url)
    time.sleep(5)
    search_box = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
    search_box.send_keys('iphone 13')
    search_box.submit()
    time.sleep(5)
    price_element = driver.find_element(By.CSS_SELECTOR, '.a-price')
    price = price_element.text if price_element else "Price not found"
    print(f"Price of iPhone 13 on Safari: {price}")
    driver.quit()

# Running tests
if __name__ == '__main__':
    pytest.main()
