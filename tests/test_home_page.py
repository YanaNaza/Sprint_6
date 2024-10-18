from conftest import driver
from pages.home_page import HomePage
from helpers.urls import Urls
import allure

class TestPageLogo:
    @allure.title('Клик на лого Самоката в шапке ведет на главную страницу')
    def test_click_on_samokat_logo_return_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_header_order_btn()  # Вызов метода, который работает с локатором
        home_page.click_on_samokat_logo()
        home_page.wait_navigating_url(Urls.HOME_PAGE)
        assert home_page.get_current_url() == Urls.HOME_PAGE


    @allure.title('Клик на Яндекс  лого шапки возвращает на Dzen.ru')
    def test_click_on_yandex_logo_return_dzen_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_yandex_logo()
        home_page.tab_switch()
        home_page.wait_navigating_url(Urls.DZEN_HOME_PAGE)
        assert home_page.get_current_url() == Urls.DZEN_HOME_PAGE