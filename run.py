#!/usr/bin/env python3.8
from user import User
from credential import Credential
import random
import string


#User class Functions

#Function to create user
def create_user(username, password):
    '''
    Function to create new account
    '''
    new_user=User(username,password)
    return new_user

#Function to save user 
def save_user(user):
    '''
    Function to save newly crated user
    '''
    user.save_user()

#Function to find user
def find_user(cls,username,password):
    '''
    function to find user if it exist return account
    '''
    return User.find_user_by_name(cls,username,password)

#function to check if user exist and return boolean value

def check_existing_user(username,password):
    '''
    Function to check if a user exist with username and password and returns a Boolean
    '''
    return User.user_exist(username,password)

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

#function to display account
def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Credential.display_account()

#Main Function

def response_none(question):
    '''
    Users response on whether to generate password or not
    '''
    response = None
    while response not in ("Y", "N"):
     response = input(question).lower()
    return response




def main():
    print("----------------")
    print('\n')
    print(f"Welcome to Password Locker, save and remember your passwords.")
    print('\n')
    print(" ---------------")
    print('\n')
    print("Please create Account:")
    print('\n')



    print("Enter your New username")
    username = input()
    print("Enter your New password")
    password = input()
    save_user(create_user(username, password))
    print('\n')
    

    print("             ")
    print('\n')
    print(f"Hello {username}, Thank you for creating an account.")
    print('\n')
    print("--------------")

    print("Proceed to Login")
    print('\n')

    print("Enter your Username:")
    user_name = input()

    print("Enter your Password:")
    pass_word = input()
    print('\n')






