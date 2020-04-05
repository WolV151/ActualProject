# Project (25%) - Module Recording System
# Script by Marin Donchev
# SID: R00192936
# Group: COMP1B-Y

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


def module_select(module_code):  # returns info about students in a module in 4 lists
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


def update_attendance(module_code, student_name, days_present, days_absent, days_excused):  # updates the list based
    print(f"{module_code} - {len(student_name)} students\n"                                 # on user select
          f"=============================================")

    for i, x in enumerate(student_name):
        print(student_name[i])

        while True:
            student_option = mod.read_nonnegative_integer("Select an option:\n"
                                                          "1: Present\n"
                                                          "2: Absent\n"
                                                          "3: Excused\n"
                                                          "=====> ")

            if student_option == 1:  # update the list based on the 3 options and give an error otherwise
                days_present[i] += 1
                break
            elif student_option == 2:
                days_absent[i] += 1
                break
            elif student_option == 3:
                days_excused[i] += 1
                break
            else:
                print("Please select a valid option.")

    return days_present, days_absent, days_excused


def record_updates_file(module_file, student_name, days_present, days_absent, days_excused):
    with open(f"{module_file}_a.txt", "w") as writefile:
        for i, x in enumerate(student_name):
            print(f"{student_name[i]},{days_present[i]},{days_absent[i]},{days_excused[i]}", file=writefile)


def main():
    user_choice, option_flag = main_menu()
    module_codes, module_names = list_modules()
    selected_module = module_menu(option_flag, module_codes, module_names)
    student_name, days_present, days_absent, days_excused = module_select(selected_module)  # non updated lists to feed into update funciton
    days_present_updated, days_absent_updated, days_excused_updated = update_attendance(selected_module, student_name,
                                                                                        days_present, days_absent,
                                                                                        days_excused)  # updated

    record_updates_file(selected_module, student_name, days_present_updated, days_absent_updated, days_excused_updated) # record to file


main()
