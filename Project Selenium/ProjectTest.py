from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

def testlogin():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("Iphone 14")
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "Apple iPhone 14 (128 GB) - Midnight").click()
    time.sleep(3)
    driver.implicitly_wait(10)
    #driver.find_element(By.LINK_TEXT, "//img[@class ='imgSwatch'][@ alt='Midnight']").click()
    value = driver.find_element(By.XPATH, '//span[@class ="selection" and text()="128 GB"]').is_displayed()
    assert value == True, "128 GB Not found"
    valuetwo = driver.find_element(By.XPATH, '//span[@class ="selection" and text()="Midnight"]').is_displayed()
    assert valuetwo == True, "Midnight Not found"
    valuethree = driver.find_element(By.XPATH, '//span[@class ="a-size-base po-break-word" and text()="Apple"]').is_displayed()
    assert valuethree == True, "Brand Apple Not found"
    driver.close()

testlogin()