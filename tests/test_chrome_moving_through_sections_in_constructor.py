from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_click_to_word_souses_moves_to_section_souses(browser):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By. XPATH, "//span[text()='Соусы']").click()

    result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Соусы']]")))

    assert result.text == 'Соусы'

def test_scroll_from_section_bread_moves_to_section_souses(browser):
     
     browser.get("https://stellarburgers.education-services.ru/")

     element = browser.find_element(By.XPATH, "//section//h2[normalize-space()='Соусы']")
     
     browser.execute_script("arguments[0].scrollIntoView();", element)

     result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Соусы']]")))

     assert result.text == 'Соусы'

def test_click_to_word_bread_moves_to_section_bread(browser):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By. XPATH, "//span[text()='Соусы']").click()
    browser.find_element(By. XPATH, "//span[text()='Булки']").click()

    result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Булки']]")))

    assert result.text == 'Булки'

def test_scroll_from_section_souses_moves_to_section_bread(browser):
     
     browser.get("https://stellarburgers.education-services.ru/")

     browser.find_element(By. XPATH, "//span[text()='Соусы']").click()

     element = browser.find_element(By.XPATH, "//section//h2[normalize-space()='Булки']")
     browser.execute_script("arguments[0].scrollIntoView();", element)

     result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Булки']]")))

     assert result.text == 'Булки'

def test_click_to_word_fillings_moves_to_section_fillings(browser):
    
    browser.get("https://stellarburgers.education-services.ru/")

    browser.find_element(By. XPATH, "//span[text()='Начинки']").click()

    result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Начинки']]")))

    assert result.text == 'Начинки'

def test_scroll_from_section_bread_moves_to_section_fillings(browser):
     
     browser.get("https://stellarburgers.education-services.ru/")

    
     element = browser.find_element(By.XPATH, "//section//h2[normalize-space()='Начинки']")
     browser.execute_script("arguments[0].scrollIntoView();", element)

     result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Начинки']]")))

     assert result.text == 'Начинки'

     
