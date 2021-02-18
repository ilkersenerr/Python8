from selenium.webdriver.common.by import By
from base.page_base import BaseClass

class AmazonProductPage:
    """
    Product Page Operations

    """

    ADD_TO_LIST = (By.CSS_SELECTOR, '.a-button-group-first')
    VIEW_YOUR_LIST = (By.LINK_TEXT, 'View Your List')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-title-word-break')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def add_product_to_list(self):
        """
        Adds Product to Wishlist

        """
        self.methods.wait_for_element(self.ADD_TO_LIST).click()
        assert self.methods.wait_for_element(self.PRODUCT_NAME).is_displayed(), "Product is not available on list"

    def navigate_to_your_list(self):
        """
        Navigates to wishlist

        """
        self.methods.wait_for_element(self.VIEW_YOUR_LIST).click()