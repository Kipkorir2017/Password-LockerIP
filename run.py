#!/usr/bin/env python3.8
from user import User
from credential import Credential
import random
import string


#User class Functions

def create_user():
    '''
    Function to create new account
    '''
    new_user=User("username","password")
    return new_user

