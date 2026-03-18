from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators

class TestStellarBurgersLogout:

    def test_logout_from_account_opens_login_page(self, browser, reg_login, reg_password):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.login_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        browser.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_button)))
        browser.find_element(By.XPATH, locators.logout_button).click()

        result =  WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button)))

        assert result.text == 'Войти'
        
