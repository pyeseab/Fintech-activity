#import functions to test 
import unittest
from routes.users import add_user, get_user_by_id
from routes.portfolio import add_portfolio, get_user_portfolios
from routes.advice import advice_for_user_portfolios

#define test class
class TestEndpoints(unittest.TestCase):

#test user creation
    def test_add_user(self):
        result = add_user("TestUser", "test@example.com")
        self.assertIn("added successfully", result)

    def test_get_user(self):
        user = get_user_by_id(1)
        self.assertIsNotNone(user)
        self.assertIn("username", user)
