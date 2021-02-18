from selenium.webdriver.common.by import By
from base.page_base import BaseClass

class AmazonWishListPage:
    """
     Wishlist Page Operations

    """

    DELETE_ITEM_BY_NAME = (By.NAME, 'submit.deleteItem')
    IS_PRODUCT_DELETED = (By.CSS_SELECTOR, '.a-alert-inline-success')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def delete_item(self):
        """
        Delete Selected Item from Wishlist

        """
        self.methods.wait_for_element(self.DELETE_ITEM_BY_NAME).click()
        assert self.methods.exist_element(self.IS_PRODUCT_DELETED), "Product cannot deleted successfully"