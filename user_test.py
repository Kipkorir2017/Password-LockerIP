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

    