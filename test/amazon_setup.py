from selenium import webdriver
from base.page_base import BaseClass
from page.wishlist_page import AmazonWishListPage
from page.category_page import AmazonCategoryPage
from page.login_page import AmazonLogin
from page.main_page import AmazonMainPage
from page.product_page import AmazonProductPage

class Setup:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.amazon_main = AmazonMainPage(self.driver)
        self.amazon_login = AmazonLogin(self.driver)
        self.amazon_category = AmazonCategoryPage(self.driver)
        self.amazon_product = AmazonProductPage(self.driver)
        self.amazon_wishlist = AmazonWishListPage(self.driver)