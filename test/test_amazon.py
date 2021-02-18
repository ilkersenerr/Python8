import unittest
from amazon_setup import Setup

class AmazonTestCase(unittest.TestCase, Setup):
    """ TEST CASE
    1- Go to http://www.amazon.com and confirm the opening of the homepage with assertion
    2- Opening the login screen and logging in with a user (if there is a previous site subscription, it can be)
    3- Type 'samsung' in the Search field at the top of the screen and click the search button
    4- It will confirm that the result is found for samsung on the incoming page
    5- Click on page 2 from the search results and confirm that page 2 is currently displayed on the page that opens
    6- Click the 'Add to List' button in the 3rd product from the top
    7- It will click on the 'List' link at the top of the screen and select the Wish list from within
    8- Confirm that there is a product watched on the previous page
    9- By pressing the 'Delete' button next to this favorite product, it will be removed from my favorites
    10- The page will confirm that this product is no longer favorites

    """

    def setUp(self):
        Setup.__init__(self)

    def test_amazon(self):
        self.amazon_main.navigate_to_home_page()
        self.amazon_main.navigate_to_sign_in()
        self.amazon_login.login()
        self.amazon_main.navigate_to_search_product()
        self.amazon_category.navigate_to_second_page()
        self.amazon_category.click_product()
        self.amazon_product.add_product_to_list()
        self.amazon_product.navigate_to_your_list()
        self.amazon_wishlist.delete_item()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()