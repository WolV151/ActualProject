# Functions I've been collecting
# also includes classes

import datetime


class bcolors:  # color menu
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def read_nonnegative_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                break
            print(bcolors.WARNING + "\n Please enter a positive number!" + bcolors.ENDC)
        except ValueError:
            print(bcolors.WARNING + "\n Please enter a number!" + bcolors.ENDC)
    return user_input


def read_nonnegative_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                break
            print(bcolors.WARNING + "\n Please enter a positive number!" + bcolors.ENDC)
        except ValueError:
            print(bcolors.WARNING + "\n Please enter a number!" + bcolors.ENDC)
    return user_input


def read_string(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) != 0:
            break
        print(bcolors.WARNING + "\nMust be non-empty" + bcolors.ENDC)
    return user_input


def yes_no(message):
    while True:
        user_input = input(message).lower()
        if user_input == "y" or user_input == "yes":
            user_input = True
            break
        elif user_input == "n" or user_input == "no":
            user_input = False
            break
        else:
            print(bcolors.WARNING + "Please answer yes or no, or y or n." + bcolors.ENDC)
    return user_input


def print_date_now():
    today = datetime.date.today()
    print(bcolors.OKBLUE + f"Date {today.day}/{today.month}/{today.year}" + bcolors.ENDC)


def return_date():
    today = datetime.date.today()
    return f"{today.day}_{today.month}_{today.year}"


def calculate_average(num):  # array purposes
    return float(sum(num)) / max(len(num), 1)

