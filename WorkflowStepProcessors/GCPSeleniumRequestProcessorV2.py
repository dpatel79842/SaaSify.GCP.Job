import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def run_selenium_script2():
    options = Options()
    options.add_experimental_option("detach", True)

    # Load configuration from JSON file
    with open('config.json') as config_file:
        config = json.load(config_file)

    with open('SeleniumSettings.json') as ss_file:
        seleniumsetting = json.load(ss_file)

    driver = webdriver.Chrome(options=options)
    driver.get(config['url'])

    driver.maximize_window()

    ByXPathFillValue(driver, "//*[@id='identifierId']", config['username'])

    ByXPathClick(driver, "//*[@id='identifierNext']/div/button")

    ByXPathFillValue(driver, "//*[@id='password']/div[1]/div/div[1]/input", config['password'])

    time.sleep(config['timeout'])

    ByXPathClick(driver, "//*[@id='passwordNext']/div/button")

    time.sleep(config['timeout'])

    ByXPathClick(driver, seleniumsetting['create offer'])

    time.sleep(config['timeout'])

    ByXPathClick(driver, "//span[text()=' Edit All ']")

    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "contact-information-form"))
    )

    elements = WebDriverWait(input_element, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
    )

    for element in elements:
        attribute_value = element.get_attribute("formcontrolname").lower()
        if attribute_value == "customerorganization":
            element.send_keys("Test Org")
        elif attribute_value == "customercontactname":
            element.send_keys("Dhaval Patel")
        elif attribute_value == "salescontactname":
            element.send_keys("Syed")
        elif attribute_value == "salescontactemail":
            element.send_keys("Syed@test.com")

    FindParentAndFillChildControl(driver,"billing-account-input", "input", "01320A-E6C8C4-111111")

    time.sleep(5)

    ByNameClick(driver, "productData")

    ByXPathClick(driver, "//mat-option[contains(., '{}')]".format('fourth-coffee-training-courses'))

    time.sleep(config['timeout'])

    ByNameClick(driver, "flavorData")

    time.sleep(config['timeout'])

    ByXPathClick(driver, "//mat-option[contains(., '{}')]".format('Standard'))

    time.sleep(config['timeout'])

    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "offer-pricing-details-display"))
    )

    input_element = WebDriverWait(input_element, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "button"))
    )

    input_element.click()

    time.sleep(config['timeout'])

    ByNameClick(driver, "paymentRecurrence")

    time.sleep(config['timeout'])

    ByXPathClick(driver, "//mat-option[contains(., '{}')]".format('Monthly'))

    time.sleep(config['timeout'])

    FindParentAndFillChildControl(driver, "purchase-deadline-input", "input", "5/6/24")

    time.sleep(config['timeout'])

    FindParentAndFillChildControl(driver, "fixed-price-field", "input", "1")

    time.sleep(config['timeout'])

    FindParentAndFillChildControl(driver, "usage-discount-field", "input", "2")

    time.sleep(config['timeout'])

    FindParentAndFillChildControl(driver, "contract-duration-input", "input", "4")

    time.sleep(config['timeout'])

    SelectOfferAcceptanceRadioButton(driver, 1)

    SaveButtonClick(driver)

    time.sleep(config['timeout'])

    ByXPathClick(driver,"//span[text()=' Save All ']")

    time.sleep(config['timeout'])

    '''
    driver.quit()
    '''

def SelectOfferAcceptanceRadioButton(driver, rbOfferStart):
    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "offer-term-section"))
    )

    elements = WebDriverWait(input_element, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "mat-radio-group"))
    )

    for element in elements:
        offertemCtn = 0
        innerelements = WebDriverWait(element, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "mat-radio-button"))
        )
        for innerelement in innerelements:
            if offertemCtn == rbOfferStart:
                innerattribute_value = innerelement.get_attribute("id").lower()
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, innerattribute_value))
                ).click()
                break
            offertemCtn = offertemCtn + 1

def ByXPathClick(driver, value):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, value))
    ).click()

def ByXPathFillValue(driver, xpath ,value):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    ).send_keys(value)

def ByNameClick(driver, value):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, value))
    ).click()

def FindParentAndFillChildControl(driver, parentelement, childelement, value):
    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, parentelement))
    )

    input_element = WebDriverWait(input_element, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, childelement))
    )
    input_element.send_keys(value)

def SaveButtonClick(driver):
    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "pricing-subtask"))
    )

    input_element = WebDriverWait(input_element, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "cfc-panel-footer"))
    )

    elements = WebDriverWait(input_element, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "button"))
    )

    for element in elements:
        attribute_value = element.text.lower()
        if attribute_value == "save":
            element.click()
            break