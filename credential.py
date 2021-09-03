class Credential:
    '''
    Class that generate new instances of credentials details
    '''
    credential_list=[]
     
    def __init__(self,account_name,username,password):

        self.account_name=account_name
        self.username=username
        self.password=password

    #save account
    def save_account(self):

        '''
        save_account method saves user account  into credential_list
        '''
        Credential.credential_list.append(self)

    #looping throught the list to check if the account exist
    @classmethod

    def account_exist(cls, account_name):
        '''
        Method that checks if account exist from the credential list.
        Args:
            String: account name to search if it exist
        Returns :
            Boolean: True or false depending if the account exist
        '''
        for account in cls.credential_list:
            if account.account_name == account_name:
                return True

        return False