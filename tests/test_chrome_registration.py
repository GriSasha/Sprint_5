from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_with_valid_name_email_password(browser, login, password):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By.XPATH, "//a[@href='/account']").click() 
    browser.find_element(By.XPATH, "//a[@href='/register']").click() 
    browser.find_element(By.XPATH, "//div[label[text()='Имя']]//input[@type='text']").send_keys(login) 
    browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(login) 
    browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(password) 
    browser.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() 


    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main/div/h2[text()='Вход']"))) 

    assert browser.find_element(By.XPATH, "//main/div/h2[text()='Вход']").text == 'Вход'


def test_registration_with_invalid_password(browser, login, bad_password):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By.XPATH, "//a[@href='/account']").click()
    browser.find_element(By.XPATH, "//a[@href='/register']").click()
    browser.find_element(By.XPATH, "//div[label[text()='Имя']]//input[@type='text']").send_keys(login)
    browser.find_element(By.XPATH, "//div[label[text()='Email']]//input[@type='text']").send_keys(login)
    browser.find_element(By.XPATH, "//div[label[text()='Пароль']]//input[@type='password']").send_keys(bad_password)
    browser.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    error = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//fieldset/div/p")))

    assert error.text == 'Некорректный пароль'