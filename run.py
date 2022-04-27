#!/usr/bin/env python3.8
from password import User, Credential
import random #Generate random numbers for various distributions including integer and floats.
import string #string module allows you to create and customize your own string
import getpass #The getpass module provides a secure way to handle the password prompts where programs interact with the users via the terminal.

def create_user(name, user_password):
    new_user = User(name, user_password)
    return new_user
def generate_password(user):
    return user.generate_random_password()
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def create_credential(account, account_username, account_password):
    new_credential = Credential(account, account_username, account_password)
    return new_credential
def save_credential(credential):
    credential.save_credential()
def delete_credential(credential):
    credential.delete_credential()
def find_credential(account_username):
    return Credential.find_by_account_username(account_username)
def check_existing_credential(account_username):
    return Credential.find_by_account_username(account_username)
def display_credential():
    return Credential.display_all_credential()
    
def main():
    user_name = input("Enter your name >")
    print(f"Hello {user_name}, Welcome to password locker")
    print("\n")
    ask = input(f"Hello {user_name}. Do you have an account? YES/NO >").lower()
    if ask == "no":
        print("Sign up with password locker to get signed")
        user_name = input("Enter your User name >")
        create = input(
            f"Hello{user_name}.Do you want a generated password? YES/NO >"
        )
        if create == "no":
            print("_"*167)
            print("|Passwords may not be visible coz they are secured|")
            print(""*67)
            getpass.getpass()
            print("You are logged in")
            while True:

                       print("Use these short codes : cc - create a new credential, dc - display credential, fc - find credential, dl - delete credential, gp - generate random password, ex - exit the credential list")
                       short_code = input().lower()
                       if short_code == 'cc':
                           print("create account")
                           print("_"*10)
                           
                           print("Account.....")
                           account = input(">")

                           print("usename....")
                           account_username = input(">")

                           print("Enter password")
                           account_password = input(">")

                           save_credential(create_credential(account, account_username, account_password))

                           print("\n")
                           print(f"New Credential {account} {account_username} {account_password} has been created")
                           print("\n")

