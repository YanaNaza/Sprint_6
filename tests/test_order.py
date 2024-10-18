from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from helpers.data import YanScooterOrderHeaderBtn, YanScooterOrderMainBtn
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в шапке главной страницы')
    def test_create_order_header_btn(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.get_cookies(HomePageLocators.COOKIES_BUTTON)
        order_page.click_header_order_btn()
        order_page.create_order(YanScooterOrderHeaderBtn.first_name,
                                YanScooterOrderHeaderBtn.last_name,
                                YanScooterOrderHeaderBtn.address,
                                OrderPageLocators.STATION_1,
                                YanScooterOrderHeaderBtn.phone,
                                OrderPageLocators.DATE_1,
                                OrderPageLocators.TIME_1,
                                OrderPageLocators.BLACK_COLOR,
                                YanScooterOrderHeaderBtn.comment)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text


    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        order_page = OrderPage(driver)
        home_page.get_cookies(HomePageLocators.COOKIES_BUTTON)
        order_page.click_main_order_btn()
        order_page.create_order(YanScooterOrderMainBtn.first_name,
                                YanScooterOrderMainBtn.last_name,
                                YanScooterOrderMainBtn.address,
                                OrderPageLocators.STATION_2,
                                YanScooterOrderMainBtn.phone,
                                OrderPageLocators.DATE_2,
                                OrderPageLocators.TIME_2,
                                OrderPageLocators.GREY_COLOR,
                                YanScooterOrderMainBtn.comment)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text