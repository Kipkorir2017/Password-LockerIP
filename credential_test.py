import unittest # Importing the unittest module
from credential import Credential # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credential("Facebook", "kipkorirbenjamin", "BenjamiN41")# create credential object
