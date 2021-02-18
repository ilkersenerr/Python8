from selenium.webdriver.common.by import By
from base.page_base import BaseClass

class AmazonMainPage:

    searched_text = "samsung"
    SIGN_IN = (By.PARTIAL_LINK_TEXT, 'Sign in')
    TXT_SEARCH = (By.ID, 'twotabsearchtextbox')
    BUTTON_SEARCH = (By.ID, 'nav-search-submit-text')
    IS_ON_MAIN_PAGE = (By.CLASS_NAME, 'a-carousel-row')
    IS_ANY_PRODUCT_ON_CAT_PAGE = (By.CLASS_NAME, 's-result-item')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_home_page(self):
        self.driver.get('https://www.amazon.com')
        home_page_loaded = self.methods.exist_element(self.IS_ON_MAIN_PAGE)
        assert home_page_loaded, True

    def navigate_to_sign_in(self):
        self.methods.wait_for_element(self.SIGN_IN).click()

    def navigate_to_search_product(self):
        self.methods.wait_for_element(self.TXT_SEARCH).send_keys(self.searched_text)
        self.methods.wait_for_element(self.BUTTON_SEARCH).click()
        assert self.methods.wait_for_element(self.IS_ANY_PRODUCT_ON_CAT_PAGE).is_displayed(),"Search Results are not Available"