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
            return 1, True  # true stands for attendance
        elif user_number == 2:
            return 2, False  # false is for statistics
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


def module_menu(option_flag, module_codes, module_names):
    if option_flag:
        text = "Attendance"
    else:
        text = "Statistics"

    print(f"\nModule Record System ({text}) - Choose a module\n"
          "===================================================")

    for i, x in enumerate(module_codes):
        print(f"{i + 1}. {module_codes[i]} - {module_names[i]}")  # i + 1 so it does not display 0, 1 but 1, 2

    while True:
        user_number = mod.read_nonnegative_integer("=====> ")
        if 0 < user_number < len(module_codes) + 1:  # I disallow the number to be 0 so I have to add +1 to the range
            break
        print("Please select for the modules available.")

    return module_codes[user_number - 1]  # returns the module code specified by the user


def module_select(module_code):
    student_name = []
    days_present = []
    days_absent = []
    days_excused = []

    with open(f"{module_code}.txt", "r") as readfile:
        for read_pointer in readfile:
            split_text = read_pointer.split(",")

            student_name.append(split_text[0])
            days_present.append(int(split_text[1]))
            days_absent.append(int(split_text[2]))
            days_excused.append(int(split_text[3]))

    return student_name, days_present, days_absent, days_excused


def main():
    user_choice, option_flag = main_menu()
    module_codes, module_names = list_modules()
    selected_module = module_menu(option_flag, module_codes, module_names)

    print(module_select(selected_module))


main()
