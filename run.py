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

#function to create new account
def create_account(account_name,username, password):
    '''
    function to create new account
    '''
    new_account=Credential(account_name,username,password)
    return new_account

#function to save new account details
def save_account(credential):
    '''
    function to save new created account details
    '''
    credential.save_account()

#function to find account by acc name
def find_account(account_name):
    '''
    Function to find account by account name and return account
    '''
    return Credential.find_account_by_name(account_name)

#function to find account if exist and return boolean
def check_existing_account(account_name):
    '''
    Function to check if account exist and return boolean value
    '''
    return Credential.account_exist(account_name)

#function to delete account
def delete_account(credential):
    '''
    Function to delete a account
    '''
    credential.delete_account()




