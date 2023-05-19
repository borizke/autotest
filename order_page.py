from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Order_page(Base):




    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)

     # locators
    confirm_order = "//input[@name='order_go']"
    cancel_order = "/html/body/div[5]/div[3]/div/button[1]"
    clear_cart = "//*[@id='formTrash']/div[3]/div/div[1]/button[2]"
    confirm_cancel = "//button[@id='popup_msg_ok']"
    price_number = "//*[@id='formTrash']/div[2]/table/tfoot/tr/td[2]/div"

    #getters

    def get_confirm_order(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_order)))

    def get_cancel_order(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_order)))

    def get_clear_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart)))
    #
    def get_confirm_cancel(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_cancel)))
    #
    def get_price_number(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_number)))


    # Actions
    def click_confirm_order(self):
        self.get_confirm_order().click()
        print("Click confirm order")

    def click_cancel_order(self):
        self.get_cancel_order().click()
        print("Click cancel order")

    def click_clear_cart(self):
        self.get_clear_cart().click()
        print("Click clear cart")
    #
    def click_confirm_cancel(self):
        self.get_confirm_cancel().click()
        print("Click cancel order")


     # Methods

    def confirmation(self):

        self.get_current_url()
        self.assert_price(self.get_price_number(), "30 560,00")
        self.click_confirm_order()
        self.click_cancel_order()
        self.click_clear_cart()
        self.click_confirm_cancel()












