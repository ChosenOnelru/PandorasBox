import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_open_page():
    driver.get('https://openweathermap.org/') # открыть url
    driver.maximize_window() # сделать полноэкранный режим
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_weathermap_search():
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div'))) # ожидание загрузки элементов
    driver.find_element(By.XPATH, '//a[contains(@href, "weathermap?zoom")]').click()
    window_mainpage = driver.window_handles[0] # дескриптор главной страницы
    window_weathermap_zoom = driver.window_handles[1] # возвращаем дескриптор новой странице
    driver.switch_to.window(window_weathermap_zoom) # переключаем на новою страницу
    assert driver.title == 'Interactive weather maps - OpenWeatherMap'
    driver.find_element(By.XPATH, '//a[@title="Nominatim Search"]').click()
    search_city = driver.find_element(By.XPATH, '//div[@class="leaflet-bar leaflet-control"]/form/input')
    search_city.send_keys('Moskow')
    search_city.send_keys(Keys.ENTER) # нажатие Enter
    driver.find_element(By.XPATH, '//span[text()="Moscow"]').click()




def test_open_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    temp_change = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]')
    time.sleep(10)
    ActionChains(driver).drag_and_drop_by_offset(temp_change, 72, 0).perform()
    time.sleep(5)

def test_conflickt():
    print("sd")
    pr


