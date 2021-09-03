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

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.username,"kipkorirbenjamin")
        self.assertEqual(self.new_account.password,"BenjamiN41")


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    
    def test_save_account(self):
        '''
        test if new credential account has  been saved to new credential list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credential.credential_list))