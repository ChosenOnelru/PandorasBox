from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

URL = 'https://openweathermap.org/'
MENU_INITIATIVES = (By.XPATH, '//*[@id="mobile-menu"]/li[8]/a')


def test_check_button_learn_more(driver):
    driver.get(URL)
    menu_initiatives = driver.find_element(*MENU_INITIATIVES)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(menu_initiatives)
    driver.execute_script("arguments[0].click();", menu_initiatives)
    actual_button = driver.find_element(By.XPATH, '//div[2]/div/div/div[2]/div/div[1]/center/a')
    expected_text_on_button = "Learn more"
    assert actual_button.text == expected_text_on_button
