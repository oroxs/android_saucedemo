import os
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()

options.udid = '14191JEC207644'
options.platform_name = 'Android'
options.app_package = 'com.swaglabsmobileapp'
options.app_activity = 'MainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Login Page
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

# Product Page
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Toggle"]').click()
wait = WebDriverWait(driver, 10)

#Select Product
for i in range(3):
    el = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]'))
    )
    el.click()

driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Cart"]/android.view.ViewGroup').click()

# swipe to find button checkout
os.system("adb shell input swipe 500 1500 500 500")
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-CHECKOUT"]').click()

# Chekout Information Page
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-First Name"]').send_keys('Vedy')
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Last Name"]').send_keys('Aditya')
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Zip/Postal Code"]').send_keys('40227')
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-CONTINUE"]').click()

# Swipe to find button Finish
os.system("adb shell input swipe 500 1500 500 500")
# Checkout Overview Page
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-FINISH"]').click()

# Checkout Complete page
driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-BACK HOME"]').click()

