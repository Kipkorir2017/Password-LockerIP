class User:
    '''
    class that generate new instances of users details

    '''
    def __init__(self,username,password):
        user_list=[]

        self.username=username
        self.password=password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
     #looping through to check if  user exist in the list

