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

        if user_number == 1:  # return use choice
            return 1
        elif user_number == 2:
            return 2
        elif user_number == 3:
            exit("Main exited")
        else:  # validation
            print("Option out range, please select a valid option from the main")


def list_modules():  # module display
    module_codes = []
    module_names = []

    with open("modules.txt", "r") as readfile:
        for read_pointer in readfile:
            split_text = read_pointer.split(",")

            module_codes.append(split_text[0].strip())
            module_names.append(split_text[1].strip())

    return module_codes, module_names


def module_menu(module_codes, module_names):
    print("\nModule Record System (Attendance) - Choose a module\n"
          "===================================================")

    for i, x in enumerate(module_codes):
        print(f"{i+1}. {module_codes[i]} - {module_names[i]}")

    user_number = mod.read_nonnegative_integer("=====> ")


def main():
    user_choice = main_menu()
    module_codes, module_names = list_modules()
    module_menu(module_codes, module_names)




main()