from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json



@given('Browser is launched and logged using super admin')
def launchbrowser(context):

    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.get("https://alpha-postgres.curbwaste.com/login")
    context.driver.find_element(By.NAME, 'email').send_keys("dev@curbwaste.com")
    context.driver.find_element(By.XPATH, '//button[text()="Request OTP" and contains(@class, "btn-dark")]').click()
    context.driver.find_element(By.XPATH, '//*[@data-id="0"]').send_keys("7")
    context.driver.find_element(By.XPATH, '//*[@data-id="1"]').send_keys("9")
    context.driver.find_element(By.XPATH, '//*[@data-id="2"]').send_keys("0")
    context.driver.find_element(By.XPATH, '//*[@data-id="3"]').send_keys("6")
    context.driver.find_element(By.XPATH, "//button[text()='Login' and contains(@class, 'btn-dark')]").click()
    context.driver.maximize_window()
    context.driver.delete_all_cookies()

@when('I select a company of company id "{value}"')
def selectCompany(context, value):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, f"//a[@href='/company/{value}']").click()
    time.sleep(5)

@when('I impersonate a user')
def impersonateUser(context):
    context.driver.implicitly_wait(10)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div[5]/div/div[2]/table/tbody/tr[1]/td[6]/button").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/aside/div/ul/li[3]").click()

@when('I Select create "{value}" order')
def createorder(context, value):
    context.driver.implicitly_wait(10)
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//div[text() = 'Create Order']").click()
    time.sleep(5)
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, f"//li[@role='option' and text() = '{value}']").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//input[@type='text' and @class='ant-input ant-select-search__field']").send_keys("Adrain McDonald")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//li[@role='option' and text()='Adrain McDonald']").click()
    context.driver.find_element(By.XPATH, "//input[@placeholder='MM/DD/YY']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//a[text()='Today']").click()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(13) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.cno-product-section-wrapper > div:nth-child(1) > div:nth-child(3) > div").click()
    context.driver.find_element(By.XPATH, "//li[ @ role = 'option' and text() = '10 Yard Dumpster']").click()
    #context.driver.execute_script("window.scrollTo(0, 1080)")
    context.driver.find_element(By.XPATH, "//div[@class='ant-modal-wrap ' and @role='dialog']").send_keys(Keys.END)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//div[@class='ant-modal-wrap ' and @role='dialog']").send_keys(Keys.END)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//div[@class='ant-modal-wrap ' and @role='dialog']").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//div[@class='ant-modal-wrap ' and @role='dialog']").send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    context.elements = context.driver.find_elements(By.XPATH, "//input[@type='text' and @class='ant-input ant-select-search__field']")
    if len(context.elements) >= 8:
        # Click on the 8th element (index 7, as indexing starts from 0)
        context.elements[7].click()
        print("Clicked on the 8th element.")
    else:
        print("There are less than 8 elements matching the XPath.")
    #context.driver.find_element(By.XPATH, "//div[text() = 'Select Price List & SKU']").click()
    context.driver.find_element(By.XPATH, "//li[ @role = 'option' and @text = 'Standard Pricing | 10 yard']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "// button[ @class ='ant-btn submit-order']").click()
    time.sleep(5)
    context.target_element = context.driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div/main/div[1]/div[2]/div[2]/div/table/tbody[1]/tr/td[2]/span" )
    # Get the text value of the element
    context.text_value = context.target_element.text




@when('I go to billing tab and search for the above order in invoices')
def billinginvo(context):
    context.driver.implicitly_wait(10)
    text_value = context.text_value
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/aside/div/ul/li[5]").click()
    time.sleep(7)
    context.driver.find_element(By.XPATH, "//span[text() = 'Invoices']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@class='ant-input' and @placeholder='Search by Order #, Service Address, or PO #...']").send_keys(text_value)




# @then('I Verify data is available')
# def Verifypageloaded(context):
#     context.driver.implicitly_wait(10)
#     context.value = context.driver.find_element(By.PARTIAL_LINK_TEXT, 'DREAM WEAVERZ').is_displayed()
#     assert context.value == True, "Value not found"

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
