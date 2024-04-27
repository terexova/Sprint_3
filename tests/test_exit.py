import settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import UserLocators
from locators import LoginLocators
from locators import EntranceLocators

class TestExit:
    def test_personal_account(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        registration_button = driver.find_element(*LoginLocators.ENTER_REGISTRATION)
        registration_button.click()

        name_input = driver.find_element(*LoginLocators.LOGIN_NAME)
        name_input.send_keys('Olgaa')

        email_input = driver.find_element(*LoginLocators.LOGIN_EMAIL)
        email_input.send_keys('aaaaaaaaaaaаa@mail.ru')

        password_input = driver.find_element(*LoginLocators.LOGIN_PASSWORD)
        password_input.send_keys('123456789')

        button_registration = driver.find_element(*LoginLocators.BUTTON_REGISTRATION)
        button_registration.click()

        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        email_input = driver.find_element(*LoginLocators.LOGIN_EMAIL)
        email_input.send_keys('aaaaaaaaaaaаa@mail.ru')

        password_input = driver.find_element(*LoginLocators.LOGIN_PASSWORD)
        password_input.send_keys('123456789')

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        entrance_button.click()

        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.presence_of_element_located(LoginLocators.EXIT_TEXT)))

        exit_button = driver.find_element(*LoginLocators.EXIT_TEXT)
        exit_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.presence_of_element_located(LoginLocators.ENTRANCE_TEXT)))

        assert driver.current_url == settings.URL + '/login'

