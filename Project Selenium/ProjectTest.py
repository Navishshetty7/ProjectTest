from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def testlogin():
    driver = webdriver.Firefox()
    actions = ActionChains(driver)
    driver.get("https://www.myntra.com/home-furnishing?src=bc")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    time.sleep(3)
    element_search = driver.find_element(By.XPATH, '//input[@class="desktop-searchBar"]')
    element_search.send_keys("Dream Weaverz")
    element_search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    value = driver.find_element(By.PARTIAL_LINK_TEXT, 'DREAM WEAVERZ').is_displayed();
    assert value == True, "DREAM WEAVERZ not found"
    driver.find_element(By.XPATH, '//a[@class ="desktop-main" and @href="/shop/men"]').click()
    verificationPage="https://www.myntra.com/shop/men"
    newPage = driver.current_url
    assert newPage == verificationPage, "Page Not traversed"
    driver.get("https://www.myntra.com/home-furnishing?src=bc")
    parent_element = driver.find_element(By.XPATH, '//div[@class="sort-sortBy"]')
    actions.move_to_element(parent_element).perform()
    driver.find_element(By.XPATH, '//label[@class="sort-label " and text()="Popularity"]').click()
    value = driver.find_element(By.PARTIAL_LINK_TEXT, 'DREAM WEAVERZ').is_displayed();
    assert value == True, "DREAM WEAVERZ not found"
    driver.get("https://www.myntra.com/home-furnishing?src=bc")
    driver.find_element(By.XPATH, '//label[@class="common-customCheckbox" and text()="White"]').click()
    value = driver.find_element(By.PARTIAL_LINK_TEXT, 'Stylespace by Isha').is_displayed();
    assert value == True, "Required Data Not found"
    value = driver.find_element(By.XPATH, '//span[@class="filter-summary-colourBox" and @data-colorhex="white"]').is_displayed();
    assert value == True, "Required Data Not found"
    driver.get("https://www.myntra.com/home-furnishing?src=bc")

    parent_element = driver.find_element(By.XPATH, '//span[@class="desktop-userTitle" and text()="Profile"]')
    actions.move_to_element(parent_element).perform()
    driver.find_element(By.XPATH, '//a[@class="desktop-linkButton" and text()="login / Signup"]').click()
    driver.implicitly_wait(10)
    value = driver.find_element(By.XPATH, '//div[@class="mobileInputContainer"]').is_displayed();
    assert value == True, "Required Data Not found"

    driver.close()

testlogin()