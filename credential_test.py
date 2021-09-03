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

    #second Test, to test if account credentials are already saved
    def test_save_account(self):
        '''
        test if new credentials has  been saved to new credential list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credential.credential_list))

    #Third Test, to test if multiple account credentials are saved
    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save multiple accounts
        objects to our credential_list
        '''
        self.new_account.save_account()
        test_account = Credential("Facebook","kipkorirbenjamin","BenjamiN41") # new account
        test_account.save_account()
        self.assertEqual(len(Credential.credential_list),2)

    #Fourth Test, test to check if  can find a account by account name and display information
    def test_find_account_by_name(self):
        '''
        test to check if  can find a account by account name 
        '''
        self.new_account.save_account()
        test_account = Credential("Facebook", "Kipkorirbenjamin", "BenjamiN41")  # new account
        test_account.save_account()

        found_account = Credential.find_by_account_name("Facebook")
        self.assertEqual(found_account.username, test_account.username)


    #Fifth Test, to test if we can remove account  credentials
    def test_delete_contact(self):
        '''
        test_delete_account credentials to test if we can remove a credentials from our credential list
        '''
        self.new_account.save_account()
        test_account = Credential("Test","username","password") # new credentials
        test_account.save_account()

        self.new_account.delete_account()# Deleting account credentials
        self.assertEqual(len(Credential.credential_list),1)

 