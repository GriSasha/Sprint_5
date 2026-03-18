from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators
import data

class TestStellarBurgersMovingToConstructor:

    def test_moving_from_personal_account_to_constructor_by_button_constructor(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.login_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(data.reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(data.reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        browser.find_element(By.XPATH, locators.personal_account_button).click() 

        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_button))) 

        browser.find_element(By.XPATH, locators.constructor_button).click()
        res = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_header))) 

        assert res.text == 'Соберите бургер'


    def test_moving_from_personal_account_to_constructor_by_logo_stellar_burgers(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.login_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(data.reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(data.reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        browser.find_element(By.XPATH, locators.personal_account_button).click() 

        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_button))) 

        browser.find_element(By.XPATH, locators.stellar_burgers_logo).click() 
        res = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_header)))

        assert res.text == 'Соберите бургер'

