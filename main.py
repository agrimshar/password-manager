from getpass import getpass
import os
from hashlib import sha256
import json

def __init__() -> bool:
    '''Checks if this is the first time running the program
    Pulls up the config file to configure stuff
    '''
    config_file_name = "config.txt"

    if os.path.exists(config_file_name):
        with open('config.txt', 'r') as f:
            data = json.load(f)
            username = data['name']
            print(f'Welcome back {username}. It\'s great to see you again!')
        f.close()
        return False
    else:
        print('Hello. It looks like this is your first time using me. I\'m happy you\'re here.')
        name = input('What should I call you? ')
        print(f'Hello {name}. ')
        master_password = getpass('Please enter your master password: ')
        hashed_master_password = sha256(master_password.encode('utf-8')).hexdigest()
        master_password = None
        f = open(config_file_name, 'w')
        f.write(json.dumps({'name': name, 'password': hashed_master_password}, indent=4))
        f.close()
        return True


if __name__ == '__main__':
    first_time_start_up = __init__()
    if first_time_start_up:
        print('I\'ve set up everything for you. You can now start using me.')
        print('I\'ll be here to help you out with your passwords. Just let me know what you need.')
    else:
        master_password = getpass('Please enter your master password: ')
        hashed_master_password = sha256(master_password.encode('utf-8')).hexdigest()
        master_password = None
        
        with open('config.txt', 'r') as f:
            data = json.load(f)
            username = data['name']

            while hashed_master_password != data["password"]:
                print('Sorry, the password you entered is incorrect. Please try again.')
                master_password = getpass('Please enter your master password: ')
                hashed_master_password = sha256(master_password.encode('utf-8')).hexdigest()
                master_password = None

            print(f'Welcome back {username}! How can I help you today?')