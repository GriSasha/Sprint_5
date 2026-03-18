from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
class TestStellarBurgersLogout:

    def test_logout_from_account_opens_login_page(self, browser, reg_login, reg_password):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() 
        browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
        browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
        browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

        browser.find_element(By.XPATH, "//a[@href='/account']").click()
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']")))
        browser.find_element(By.XPATH, "//button[text()='Выход']").click()

        result =  WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        assert result.text == 'Войти'
        
