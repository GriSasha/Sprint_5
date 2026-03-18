from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators


class TestStellarBurgersLogin:

    def test_login_on_the_main_page(self, browser, reg_login, reg_password):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.login_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click() 


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_personal_account_button(self, browser, reg_login, reg_password):

        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.personal_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click()


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_registration_form(self, browser, reg_login, reg_password):

        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.personal_account_button).click() 
        browser.find_element(By.XPATH, locators.registration_link).click() 
        browser.find_element(By.XPATH, locators.login_link).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click()



        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_password_recovery_form(self, browser, reg_login, reg_password):
    
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.personal_account_button).click() 
        browser.find_element(By.XPATH, locators.password_recover_button).click() 
        browser.find_element(By.XPATH, locators.login_link).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click()


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        assert registr.text == 'Оформить заказ'