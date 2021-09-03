#!/usr/bin/env python3.8
from user import User
from credential import Credential
import random
import string


#User class Functions

#Function to create user
def create_user():
    '''
    Function to create new account
    '''
    new_user=User("username","password")
    return new_user

#Function to save user 
def save_user(user):
    '''
    Function to save newly crated user
    '''
    user.save_user()