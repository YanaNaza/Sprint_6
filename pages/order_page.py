import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_FIELD, name)


    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)


    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)


    @allure.step('Выбор станции метро')
    def set_metro(self, station):
        self.find_element(OrderPageLocators.METRO_FIELD).click()
        self.click_to_element(station)


    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_NUMBER_FIELD, phone)


    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)


    @allure.step('Выбор даты доставки')
    def set_date(self, date):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(date)


    @allure.step('Выбор срока аренды')
    def set_term(self, term):
        self.click_to_element(OrderPageLocators.RENT_TIME_FIELD)
        self.click_to_element(term)


    @allure.step('Выбор цвета')
    def set_color(self, color):
        self.click_to_element(color)


    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.COMMENTS, comments)