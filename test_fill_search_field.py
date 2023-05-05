import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'https://openweathermap.org/'
cities = ['Dallas', 'Chicago', 'Houston']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')


@pytest.mark.parametrize('city', cities)
def test_fill_city_field(driver, city):
    driver.get(URL)
    wait_act = WebDriverWait(driver, 15)
    wait_act.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait_act.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait_act.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city


def test_fill_city_field_in_russian(driver):
    driver.get(URL)
    wait_act = WebDriverWait(driver, 15)
    wait_act.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys('Кишинев')
    driver.find_element(*search_button).click()
    wait_act.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = 'Chisinau, MD'
    wait_act.until(EC.text_to_be_present_in_element(displayed_city, 'Chisinau'))
    actual_city = driver.find_element(*displayed_city)
    assert expected_city == actual_city.text