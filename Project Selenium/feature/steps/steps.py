from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


@given('Browser is launched')
def launchbrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.myntra.com/home-furnishing?src=bc")
    context.driver.maximize_window()
    context.driver.delete_all_cookies()


@when('I search for required data "{value}"')
def searchValue(context, value):
    context.driver.implicitly_wait(10)
    context.element_search = context.driver.find_element(By.XPATH, '//input[@class="desktop-searchBar"]')
    context.element_search.send_keys(value)
    context.element_search.send_keys(Keys.ENTER)

@then('I Verify data is available')
def Verifypageloaded(context):
    context.driver.implicitly_wait(10)
    context.value = context.driver.find_element(By.PARTIAL_LINK_TEXT, 'DREAM WEAVERZ').is_displayed()
    assert context.value == True, "Value not found"

@when('I select Men from the dropdown')
def selectMen(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, '//a[@class ="desktop-main" and @href="/shop/men"]').click()

@then('I validate whether proper Page is loaded')
def validateMen(context):
    context.driver.implicitly_wait(10)
    context.verificationPage="https://www.myntra.com/shop/men"
    context.newPage = context.driver.current_url
    assert context.newPage == context.verificationPage, "Page Not traversed"

@when('I sort by using popularity')
def sortPopularity(context):
    context.driver.implicitly_wait(10)
    context.actions = ActionChains(context.driver)
    context.driver.implicitly_wait(10)
    context.parent_element = context.driver.find_element(By.XPATH, '//div[@class="sort-sortBy"]')
    context.actions.move_to_element(context.parent_element).perform()
    context.driver.find_element(By.XPATH, '//label[@class="sort-label " and text()="Popularity"]').click()

@when('I filter by white colour')
def filterBy(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, '//label[@class="common-customCheckbox" and text()="White"]').click()

@then('I validate page is filtered by white colour')
def validatefilterBy(context):
    context.driver.implicitly_wait(10)
    context.value = context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Stylespace by Isha').is_displayed();
    assert context.value == True, "Required Data Not found"
    context.value = context.driver.find_element(By.XPATH, '//span[@class="filter-summary-colourBox" and @data-colorhex="white"]').is_displayed();
    assert context.value == True, "Required Data Not found"

@when('I move to login page via landing page')
def profileLogin(context):
    context.driver.implicitly_wait(10)
    context.actions = ActionChains(context.driver)
    context.parent_element = context.driver.find_element(By.XPATH, '//span[@class="desktop-userTitle" and text()="Profile"]')
    context.actions.move_to_element(context.parent_element).perform()
    context.driver.find_element(By.XPATH, '//a[@class="desktop-linkButton" and text()="login / Signup"]').click()

@then('I validate login page asks for phone number')
def profileLoginvalidate(context):
    context.driver.implicitly_wait(10)
    context.value = context.driver.find_element(By.XPATH, '//div[@class="mobileInputContainer"]').is_displayed();
    assert context.value == True, "Required Data Not found"


@then('Close browser')
def closeBrowser(context):
    context.driver.close()
