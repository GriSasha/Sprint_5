import pytest  
import random
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def fox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@ pytest.fixture
def login():
    number = random.randint(100000, 999999)
    domains = ["mail.ru", "yandex.ru", "gmail.ru"]
    domain = random.choice(domains)
    return f"user{number}@{domain}"

@pytest.fixture
def password():
    number = random.randint(100000, 999999)
    return f"Pass{number}!"

@pytest.fixture
def bad_password():
    number = random.randint(100, 999)
    return f"P{number}"

@pytest.fixture
def reg_login():
    reg_login = "san_41@mail.ru"
    return reg_login

@pytest.fixture
def reg_password():
    reg_password = "123456"
    return reg_password



