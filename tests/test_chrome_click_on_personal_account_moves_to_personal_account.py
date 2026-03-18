from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators
import data

class TestStellarBurgersMovingToPersonalAcc:

    def test_login_on_the_main_page(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, locators.login_account_button).click() 
        browser.find_element(By.XPATH, locators.email_field).send_keys(data.reg_login) 
        browser.find_element(By.XPATH, locators.password_field).send_keys(data.reg_password) 
        browser.find_element(By.XPATH, locators.login_button).click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.order_button))) 

        browser.find_element(By.XPATH, locators.personal_account_button).click() 

        res = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_button))) 

        assert res.text == 'Профиль'
