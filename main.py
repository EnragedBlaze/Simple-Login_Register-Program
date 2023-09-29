import string
from string import punctuation
import time
import random

pass_choice = []
choices = [1, 2, 3]
choices_2 = [1, 2]
numbers = list("1234567890")
Letters = list(string.ascii_letters)
special_char = list(punctuation)
file_read = open('Accounts.txt', 'r')
read = file_read.readlines()
read_mod = []
for line in read:
    a = line.strip()
    split = a.split(" ")
    read_mod.extend(split)
password_list = read_mod[1::2]
username_list = read_mod[::2]
file_read.close()
Password_Gen = ""


def start():
    print("What would you like to do? Type the selected option's number\n1. Login\n2. Register\n3. Exit")
    try:
        choice = int(input(">>>"))
        if choice in choices:
            if choice == 1:
                time.sleep(0.5)
                login()
            if choice == 2:
                time.sleep(0.5)
                register()
            if choice == 3:
                print("Goodbye")
                time.sleep(0.5)
                exit()
        elif choice not in choices:
            time.sleep(0.4)
            print("Please only input '1', '2', or '3' for your respective choice\n")
            time.sleep(1)
            start()
    except ValueError:  # Provides a solution for the instance of a value error
        print("An incorrect value has been entered\nOnly enter '1', '2' or '3'\n")
        time.sleep(1.5)  # Slows next command execution by 2 seconds, respective for each time.sleep
        start()


def login():
    admin_rights = "admin"
    log_file = open('Accounts.txt', 'r')
    log_read = log_file.readlines()
    log = []
    for phrase in log_read:
        log.append(phrase.strip())
    log_file.close()

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username and password in admin_rights:
        admin_login()
    else:
        key = username + " " + password
        if key in log:
            print("You have successfully logged in")
            time.sleep(2)
        else:
            print("You have entered an incorrect username or password\nPlease try again\n")
            time.sleep(1)
            start()


def admin_login():
    time.sleep(0.5)
    print("\nYou have successfully logged in\n")
    choice = int(input("1. View all account's information\n2. Exit\n"))
    try:
        if choice in choices_2:
            if choice == 1:
                admin = open('Accounts.txt', 'r')
                admin_read = admin.readlines()
                admin_view = []
                for acc in admin_read:
                    admin_view.append(acc.strip())
                print(admin_view)
                time.sleep(2)
            elif choice == 2:
                print("Goodbye")
                time.sleep(2)
                exit()
        elif choice not in choices_2:
            time.sleep(0.4)
            print("Please only input '1', '2', or '3' for your respective choice\n")
            time.sleep(1)
            admin_login()
    except ValueError:  # Provides a solution for the instance of a value error
        print("An incorrect value has been entered\nOnly enter '1', '2' or '3'\n")
        time.sleep(1.5)  # Slows next command execution by 2 seconds, respective for each time.sleep
        admin_login()


def register():
    username = input("Enter Username: ")
    if username in username_list:
        print("Username already exists please enter a new username\n")
        time.sleep(1)
        register()
    prompt = int(input("1. Create your own password\n2. Ask computer to generate one for you\n"))
    try:
        if prompt in choices_2:
            if prompt == 1:
                password = input('Enter Password: ')
                confirm_password = input('Confirm Password: ')
                if password == confirm_password:
                    if password in password_list:
                        print("Password already exists please try again\n")
                        time.sleep(0.5)
                        register()
                    elif username or password not in read_mod:
                        file_write = open('Accounts.txt', 'a')
                        file_write.write(f'\n{username} {confirm_password}')
                        file_write.close()
                        print("\nCongratulations you have successfully registered!\n")
                        time.sleep(1)
                        start()
                elif password != confirm_password:
                    print("Passwords do not match please try again\n")
                    time.sleep(0.5)
                    register()
                else:
                    print("Unexpected error has occurred please try again\n")
                time.sleep(2)
            elif prompt == 2:
                password_gen()
                file_write = open('Accounts.txt', 'a')
                file_write.write(f'\n{username} {Password_Gen}')
                file_write.close()

                time.sleep(1)
                print(f'\nHere is Your generated password {Password_Gen}')
                time.sleep(2)
                print("\nCongratulations you have successfully registered!\n")
                time.sleep(1)
                start()

        elif prompt not in choices_2:
            time.sleep(0.4)
            print("Please only input '1' or '2' for your respective choice\n")
            time.sleep(1)
            admin_login()
    except ValueError:  # Provides a solution for the instance of a value error
        print("An incorrect value has been entered\nOnly enter '1' or '2'\n")
        time.sleep(1.5)  # Slows next command execution by 2 seconds, respective for each time.sleep
        register()


def password_gen():
    pass_choice_ = int(input("1. Use default password length of 8\n2. Choose Password Length\n"))

    def disp_pass():
        global Password_Gen
        while True:
            Password_Gen = "".join(random.sample(pass_choice, pass_length))
            if Password_Gen not in password_list:
                break

            elif Password_Gen in password_list:
                continue

    try:
        if pass_choice_ in choices_2:
            if pass_choice_ == 1:
                pass_length = 8
                pass_gen_choice()
                random.shuffle(pass_choice)
                disp_pass()

            elif pass_choice_ == 2:
                pass_length = int(input("Enter the number of digits in your password:\n"))
                pass_gen_choice()
                random.shuffle(pass_choice)
                disp_pass()

        elif pass_choice_ not in choices_2:
            time.sleep(0.4)
            print("Please only input '1' or '2' for your respective choice\n")
            time.sleep(1)
            password_gen()
    except ValueError:  # Provides a solution for the instance of a value error
        print("An incorrect value has been entered\nOnly enter '1' or '2'\n")
        time.sleep(1.5)  # Slows next command execution by 2 seconds, respective for each time.sleep
        password_gen()


def pass_gen_choice() -> None:
    try:
        number_ = int(input("Do you want numbers in your password\n1. Yes\n2. No\n"))
        character_ = int(input("Do you want characters in your password\n1. Yes\n2. No\n"))
        letters_ = int(input("Do you want letters in your password\n1. Yes\n2. No\n"))
        if number_ in choices_2:
            if number_ == 1:
                pass_choice.extend(numbers)
                print("Generating Password...")
                time.sleep(1)
        if character_ in choices_2:
            if character_ == 1:
                pass_choice.extend(special_char)
                print("Generating Password...")
                time.sleep(1)
        if letters_ in choices_2:
            if letters_ == 1:
                pass_choice.extend(Letters)
                print("Generating Password...")
                time.sleep(1)
        elif number_ or character_ or letters_ not in choices_2:
            time.sleep(0.4)
            print("Please only input '1' or '2' for your respective choice for each prompt\n")
            time.sleep(1)
            pass_gen_choice()

    except ValueError:  # Provides a solution for the instance of a value error
        print("An incorrect value has been entered\nOnly enter '1' or '2' mate\n")
        time.sleep(1.5)  # Slows next command execution by 2 seconds, respective for each time.sleep
        pass_gen_choice()


start()
