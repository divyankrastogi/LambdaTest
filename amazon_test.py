import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# LambdaTest credentials
LT_USERNAME = 'rastogi.divyank739'
LT_ACCESS_KEY = '0bHl6G19qi83KdCstvuz9fBJ5YHhPIyl4bGsbpPH71mj5Thd26'

lt_browser_1 = {
    "build": 'AmazonPriceTest',
    "name": 'Test on Chrome',
    "platform": 'macOS Catalina',
    "browserName": 'chrome',
    "version": 'latest'
}
lt_browser_2 = {
    "build": 'AmazonPriceTest',
    "name": 'Test on Safari',
    "platform": 'macOS Catalina',
    "browserName": 'safari',
    "version": 'latest'
}
url = "https://www.amazon.com"

# Function to test the price of iPhone 13 on different browsers
def test_amazon_price_chrome():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    search_box = driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
    search_box.send_keys('iphone 13')
    search_box.submit()
    time.sleep(5)
    price_element = driver.find_element(By.CSS_SELECTOR,'.a-price')
    price = price_element.text if price_element else "Price not found"
    print(f"Price of iPhone 13 on Chrome: {price}")
    driver.quit()

# Function to test the price of iPhone 13 on different browsers
def test_amazon_price_safari():
    driver = webdriver.Safari()
    driver.get(url)
    time.sleep(5)
    search_box = driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
    search_box.send_keys('iphone 13')
    search_box.submit()
    time.sleep(5)
    price_element = driver.find_element(By.CSS_SELECTOR,'.a-price')
    price = price_element.text if price_element else "Price not found"
    print(f"Price of iPhone 13 on Safari: {price}")
    driver.quit()

# Running tests otest_amazon_price_chrome()
test_amazon_price_chrome()
test_amazon_price_safari()
