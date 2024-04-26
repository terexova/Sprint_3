import settings
from locators import UserLocators

class TestTransitionConstructor:
    def test_transition_constructor(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        assert personal_account_button
        personal_account_button.click()

        constructor_button = driver.find_element(*UserLocators.ENTER_CONSTRUCTOR_BUTTON)
        assert constructor_button
        constructor_button.click()

    def test_transition_logo_Stellar_Burger(self, driver):
        driver.get(settings.URL)
        personal_account_button = driver.find_element(*UserLocators.ENTER_PERSONAL_ACCOUNT_BUTTON)
        assert personal_account_button
        personal_account_button.click()

        logo_Stellar_Burger_button = driver.find_element(*UserLocators.ENTER_LOGO_STELLAR_BURGER_BUTTON)
        assert logo_Stellar_Burger_button
        logo_Stellar_Burger_button.click()