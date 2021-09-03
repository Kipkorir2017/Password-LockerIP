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