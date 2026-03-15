from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_moving_from_personal_account_to_constructor_by_button_constructor(browser, reg_login, reg_password):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() 
    browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
    browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

    browser.find_element(By.XPATH, "//a[@href='/account']").click() 

    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']"))) 

    browser.find_element(By.XPATH, "//a[.//p[normalize-space()='Конструктор']]").click()
    res = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/h1"))) 

    assert res.text == 'Соберите бургер'

def test_moving_from_personal_account_to_constructor_by_logo_stellar_burgers(browser, reg_login, reg_password):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() 
    browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(reg_login) 
    browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(reg_password) 
    browser.find_element(By.XPATH, ".//button[text()='Войти']").click() 


    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']"))) 

    browser.find_element(By.XPATH, "//a[@href='/account']").click() 

    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']"))) 

    browser.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div").click() 
    res = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/h1")))

    assert res.text == 'Соберите бургер'
