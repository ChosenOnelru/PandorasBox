from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
BUTTON_INITIATIVES = (By.XPATH, '//*[@id="mobile-menu"]/li[8]/a')
URL = 'https://openweathermap.org/'
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')


def test_check_open_page_our_initiative(driver):
    driver.get(URL)
    button_initiatives = driver.find_element(*BUTTON_INITIATIVES)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_initiatives)
    driver.execute_script("arguments[0].click();", button_initiatives)
    expected_title = "Our Initiatives"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title
