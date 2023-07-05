
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

@given('Browser is launched')
def launchbrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.in/")
    context.driver.maximize_window()
    context.driver.delete_all_cookies()


@when('I search for required data and select the device')
def loginportal(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("Iphone 14")
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()
    time.sleep(3)
    context.driver.find_element(By.LINK_TEXT, "Apple iPhone 14 (128 GB) - Midnight").click()


@then('I Verify data is available')
def Verifypageloaded(context):
    context.driver.implicitly_wait(10)
    context.driver.implicitly_wait(10)
    value = context.driver.find_element(By.XPATH, '//span[@class ="selection" and text()="128 GB"]').is_displayed()
    assert value == True, "128 GB Not found"
    valuetwo = context.driver.find_element(By.XPATH, '//span[@class ="selection" and text()="Midnight"]').is_displayed()
    assert valuetwo == True, "Midnight Not found"
    valuethree = context.driver.find_element(By.XPATH, '//span[@class ="a-size-base po-break-word" and text()="Apple"]').is_displayed()
    assert valuethree == True, "Brand Apple Not found"

@then('Close browser')
def closeBrowser(context):
    context.driver.close()
