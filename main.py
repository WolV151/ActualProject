# Project (25%) - Module Recording System

import mod


def main_menu():
    while True:
        user_number = mod.read_nonnegative_integer("Module Record System - Main Menu\n"
                                                   "=----------------------------------=\n"
                                                   "1. Record Attendance\n"
                                                   "2. Generate Statistics\n"
                                                   "3. Exit\n"
                                                   "=====> ")

        if user_number == 1:
            print("Record attendance")
            break
        elif user_number == 2:
            print("Generate stats")
            break
        elif user_number == 3:
            exit("Main exited")
        else:
            print("Option out range, please select a valid option from the main")




def main():
    main_menu()

main()