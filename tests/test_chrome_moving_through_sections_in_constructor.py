from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import locators

class TestStellarBurgersMovingThroughSectionsInConstructor:

    def test_click_to_word_souses_moves_to_section_souses(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By. XPATH, locators.sauses_button).click()

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_sauses_button)))

        assert result.text == 'Соусы'

    def test_scroll_from_section_bread_moves_to_section_souses(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        element = browser.find_element(By.XPATH, locators.sauses_header)
        
        browser.execute_script("arguments[0].scrollIntoView();", element)

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_sauses_button)))

        assert result.text == 'Соусы'

    def test_click_to_word_bread_moves_to_section_bread(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By. XPATH, locators.sauses_button).click()
        browser.find_element(By. XPATH, locators.bread_button).click()

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_bread_button)))

        assert result.text == 'Булки'

    def test_scroll_from_section_souses_moves_to_section_bread(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By. XPATH, locators.sauses_button).click()

        element = browser.find_element(By.XPATH, locators.bread_header)
        browser.execute_script("arguments[0].scrollIntoView();", element)

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_bread_button)))

        assert result.text == 'Булки'

    def test_click_to_word_fillings_moves_to_section_fillings(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        browser.find_element(By. XPATH, locators.fillings_button).click()

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_fillings_button)))

        assert result.text == 'Начинки'

    def test_scroll_from_section_bread_moves_to_section_fillings(self, browser):
        
        browser.get(urls.url_stellar_burgers)

        
        element = browser.find_element(By.XPATH, locators.fillings_header)
        browser.execute_script("arguments[0].scrollIntoView();", element)

        result = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.selected_fillings_button)))

        assert result.text == 'Начинки'

        
