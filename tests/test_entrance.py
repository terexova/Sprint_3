
from faker import Faker

import settings
from locators import EntranceLocators

fake = Faker()

class TestMestoEntrance:
    def test_entrance_in_account(self, driver):
        driver.get(settings.URL)
        entrance_in_account_button = driver.find_element(*EntranceLocators.ENTRANCE_IN_ACCOUNT)
        assert entrance_in_account_button
        entrance_in_account_button.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        assert email_input
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        assert password_input
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        assert entrance_button
        entrance_button.click()

    def test_entrance_personal_account(self, driver):
        driver.get(settings.URL)
        entrance_personal_account = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        assert entrance_personal_account
        entrance_personal_account.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        assert email_input
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        assert password_input
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        assert entrance_button
        entrance_button.click()

    def test_entrance_in_registration(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        assert personal_account_button
        personal_account_button.click()

        button_registration = driver.find_element(*EntranceLocators.ENTRANCE_REGISTRATION)
        assert button_registration
        button_registration.click()

        entrance_registration = driver.find_element(*EntranceLocators.ENTRANCE_TEXT)
        assert entrance_registration
        entrance_registration.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        assert email_input
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        assert password_input
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        assert entrance_button
        entrance_button.click()

    def test_entrance_in_password_recovery(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*EntranceLocators.ENTRANCE_PERSONAL_ACCOUNT)
        assert personal_account_button
        personal_account_button.click()

        password_recovery_button = driver.find_element(*EntranceLocators.PASSWORD_RECOVERY_BUTTON)
        assert password_recovery_button
        password_recovery_button.click()

        password_recovery_entrance = driver.find_element(*EntranceLocators.PASSWORD_RECOVERY_ENTRANCE_TEXT)
        assert password_recovery_entrance
        password_recovery_entrance.click()

        email_input = driver.find_element(*EntranceLocators.LOGIN_EMAIL)
        assert email_input
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*EntranceLocators.LOGIN_PASSWORD)
        assert password_input
        password_input.send_keys(fake.password())

        entrance_button = driver.find_element(*EntranceLocators.ENTRANCE_BUTTON)
        assert entrance_button
        entrance_button.click()

        assert driver.current_url == settings.URL + '/login'