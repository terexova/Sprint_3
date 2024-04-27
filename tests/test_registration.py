
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import UserLocators
from locators import LoginLocators

fake = Faker()

class TestLogin:
    def test_personal_account(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        registration_button = driver.find_element(*LoginLocators.ENTER_REGISTRATION)
        registration_button.click()

        name_input = driver.find_element(*LoginLocators.LOGIN_NAME)
        name_input.send_keys(fake.name())

        email_input = driver.find_element(*LoginLocators.LOGIN_EMAIL)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*LoginLocators.LOGIN_PASSWORD)
        password_input.send_keys(fake.password())

        button_registration = driver.find_element(*LoginLocators.BUTTON_REGISTRATION)
        button_registration.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.presence_of_element_located(LoginLocators.ENTRANCE_TEXT)))


        wrong_password_input = driver.find_element(*LoginLocators.LOGIN_PASSWORD)
        wrong_password_input.send_keys('12345')

        assert driver.current_url == settings.URL + '/login'

