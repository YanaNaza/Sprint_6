from conftest import driver
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from helpers.urls import Urls
import allure


class TestPageLogo:
    @allure.title('Клик на лого Самоката в шапке ведет на главную страницу')
    def test_click_on_samokat_logo_return_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_to_element(HomePageLocators.ORDER_BUTTON_HEADER)
        home_page.click_on_samokat_logo()
        home_page.wait_navigating_url(Urls.HOME_PAGE)
        home_page_url = Urls.HOME_PAGE
        assert home_page_url == home_page.get_current_url()


    @allure.title('Клик на Яндекс  лого шапки возвращает на Dzen.ru')
    def test_click_on_yandex_logo_return_dzen_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_yandex_logo()
        home_page.tab_switch()
        home_page.wait_navigating_url(HomePageLocators.DZEN_HOME_PAGE)
        dzen_home_page_url = Urls.DZEN_HOME_PAGE
        assert dzen_home_page_url == home_page.get_current_url()