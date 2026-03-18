from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls

class TestStellarBurgersRegistration:

    def test_registration_with_valid_name_email_password(self, browser, login, password):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.personal_account_button).click() 
        browser.find_element(By.XPATH, locators.registration_link).click() 
        browser.find_element(By.XPATH, locators.name_field).send_keys(login) 
        browser.find_element(By.XPATH, locators.email_field).send_keys(login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(password) 
        browser.find_element(By.XPATH, locators.registration_button).click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))) 

        assert browser.find_element(By.XPATH, locators.login_header).text == 'Вход'


    def test_registration_with_invalid_password(self, browser, login, bad_password):
    
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.personal_account_button).click()
        browser.find_element(By.XPATH, locators.registration_link).click()
        browser.find_element(By.XPATH, locators.name_field).send_keys(login)
        browser.find_element(By.XPATH, locators.email_field).send_keys(login)
        browser.find_element(By.XPATH, locators.password_field).send_keys(bad_password)
        browser.find_element(By.XPATH, locators.registration_button).click()

        error = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.validation_error)))

        assert error.text == 'Некорректный пароль'

