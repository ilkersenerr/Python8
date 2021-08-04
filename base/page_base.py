from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass(object):
    """
    The class we need to call all pages

    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_element(self, selector):
        """
        item to be selected

        """
        return self.wait.until(EC.element_to_be_clickable(selector))

    def presence_for_element(self, selector):
        """
        Showing the item

        """
        return self.wait.until(EC.presence_of_element_located(selector))

    def presence_for_all_elements(self, selector):
        """
        Where the selected directory is hosted

        """
        return self.wait.until(EC.presence_of_all_elements_located(selector))

    def wait_till_element_disappears(self, selector):
        """
        Where to find the item after the item disappears

        """
        return self.wait.until(EC.invisibility_of_element_located(selector))

    def exist_element(self, selector, multiple=False):
        """
        Returns "true" if the item was found. Returns "false" if the item was not found

        """
        if not multiple:
            try:
                self.wait.until(EC.presence_of_element_located(selector))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(EC.presence_of_all_elements_located(selector))
                return True
            except TimeoutException:
                return False