from selenium.webdriver.common.by import By
from base.page_base import BaseClass

class AmazonLogin:
    """
    Login Page

    """

    email = "orcuxtl@maxresistance.com"
    password = "T123ester"
    TXT_EMAIL = (By.ID, 'ap_email')
    BUTTON_CONTINUE = (By.ID, 'continue')
    TXT_PASSWORD = (By.ID, 'ap_password')
    SUBMIT_SIGNIN = (By.ID, 'signInSubmit')


    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login(self):
        """
        login processes

        """
        self.methods.wait_for_element(self.TXT_EMAIL).send_keys(self.email)
        self.methods.wait_for_element(self.BUTTON_CONTINUE).click()
        self.methods.wait_for_element(self.TXT_PASSWORD).send_keys(self.password)
        self.methods.wait_for_element(self.SUBMIT_SIGNIN).click()