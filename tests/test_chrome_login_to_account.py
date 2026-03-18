from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersLogin:

    def test_login_on_the_main_page(self, browser, reg_login, reg_password):
        
        browser.get("https://stellarburgers.education-services.ru/")

        browser.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() 
        browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
        browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
        browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_personal_account_button(self, browser, reg_login, reg_password):

        browser.get("https://stellarburgers.education-services.ru/")

        browser.find_element(By.XPATH, "//a[@href='/account']").click() 
        browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
        browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
        browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_registration_form(self, browser, reg_login, reg_password):

        browser.get("https://stellarburgers.education-services.ru/")

        browser.find_element(By.XPATH, "//a[@href='/account']").click() 
        browser.find_element(By.XPATH, "//a[@href='/register']").click() 
        browser.find_element(By.XPATH, "//a[@href='/login']").click() 
        browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
        browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
        browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

        assert registr.text == 'Оформить заказ'

    def test_login_by_password_recovery_form(self, browser, reg_login, reg_password):
    
        browser.get("https://stellarburgers.education-services.ru/")

        browser.find_element(By.XPATH, "//a[@href='/account']").click() 
        browser.find_element(By.XPATH, "//a[@href='/forgot-password']").click() 
        browser.find_element(By.XPATH, "//a[@href='/login']").click() 
        browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
        browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
        browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


        registr = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

        assert registr.text == 'Оформить заказ'