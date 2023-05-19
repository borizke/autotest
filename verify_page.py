from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class Verify_page(Base):




    def __init__(self, driver_g):
        self.driver_g = driver_g
        super().__init__(driver_g)


    def verify(self):
        self.get_screenshot()
        self.assert_url("http://zip69.ru/cart?removeMarked")

        # self.get_current_url()












