from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'https://openweathermap.org/'
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')

def test_switching_temperature_measuring_system_on_F(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(load_div))
    driver.find_element(By.CSS_SELECTOR, "button.stick-footer-panel__link").click()
    driver.find_element(By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]").click()
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(load_div))
    driver.find_element(By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]").click()
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(load_div))
    current_temp = driver.find_element(By.CSS_SELECTOR, "div.current-temp span.heading")
    assert "°F" in current_temp.text