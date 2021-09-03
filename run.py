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

#Function to find user
def find_user(username, password):
    '''
    function to find user if it exist return account
    '''
    return User.find_by_name(username,password)

#function to check if user exist and return boolean value

def check_existing_user(username, password):
    '''
    Function to check if a user exist with username and password and returns a Boolean
    '''
    return User.user_exist(username, password)

#Credential Functions

