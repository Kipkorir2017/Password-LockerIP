import unittest # Importing the unittest module
from user import User # Importing the User class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.

        '''
        self.new_user=User("kipkorirbenjamin","BenjamiN41")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"kipkorirbenjamin")
        self.assertEqual(self.new_user.password,"BenjamiN41")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    
    