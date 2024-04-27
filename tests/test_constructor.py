import settings
from locators import ConstructorLocatorsSauce

class TestConstructorSauce:
    def test_constructor_filling(self, driver):
        driver.get(settings.URL)
        filling = driver.find_element(*ConstructorLocatorsSauce.FILLING)
        filling.click()
        assert 'tab_tab_type_current' in filling.get_attribute('class')

    def test_constructor_bread(self, driver):
        driver.get(settings.URL)
        filling = driver.find_element(*ConstructorLocatorsSauce.FILLING)
        filling.click()
        bread = driver.find_element(*ConstructorLocatorsSauce.BREAD)
        bread.click()
        assert 'tab_tab_type_current' in bread.get_attribute('class')

    def test_constructor_sauce(self, driver):
        driver.get(settings.URL)
        sauce = driver.find_element(*ConstructorLocatorsSauce.SAUCE)
        sauce.click()
        assert 'tab_tab_type_current' in sauce.get_attribute('class')

