import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Catalogi_page(Base):




    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)

     # locators
    continental_checkbox = "//*[@id='catalog-form']/div[1]/div/div/ul/li[1]/label/span"
    radius_checkbox = "//*[@id='catalog-form']/div[6]/div[2]/ul/li[6]/label/span"
    show_choice_button = "//*[@id='catalog-form']/div[8]/button[1]"
    cart = "//*[@id='CONTINENTAL0358417']/div[2]/div[2]/div/div/div/button"
    final_cart = "//span[@class='cart']"



    #getters

    def get_checkbox_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.continental_checkbox)))

    def get_checkbox_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.radius_checkbox)))

    def get_final_choice(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_choice_button)))

    def get_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_final_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_cart)))




    # Actions
    def choose_checkbox_1(self,driver_g):
        self.get_checkbox_1().click()
        print("Click checkbox 1")
        self.driver_g.execute_script("window.scrollTo(0,700)")
        super().__init__(driver_g)
        print("scrolled down")

    def choose_checkbox_2(self):
        self.get_checkbox_2().click()
        print("Click checkbox 2")
    #
    def click_final_choice(self):
        self.get_final_choice().click()
        print("Click final tire choice")
    #
    def add_to_cart(self):
        self.get_cart().click()
        print("Click cart")
    #
    def click_cart(self):
        self.get_final_cart().click()
        print("Click menu")



     # Methods

    def click_checkbox(self):

        self.get_current_url()
        self.choose_checkbox_1(driver_g="window.scrollTo(0,700)")
        self.choose_checkbox_2()
        time.sleep(5)
        self.click_final_choice()
        self.add_to_cart()
        self.click_cart()











