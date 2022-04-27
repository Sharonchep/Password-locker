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

