# Project (25%) - Module Recording System
# Script by Marin Donchev
# SID: R00192936
# Group: COMP1B-Y

import mod


def login_check(login_file):
    user_input_username = mod.read_string("Username: ")
    user_input_password = mod.read_string("Password: ")
    usernames = []
    passwords = []
    with open(f"{login_file}.txt", "r") as readfile:
        while True:
            line = readfile.readline().rstrip()
            if line == "":
                break
            usernames.append(line)
            line = readfile.readline().rstrip()
            if line == "":
                break
            passwords.append(line)

    for i, x in enumerate(usernames):  # if they match - continue, if not then try again
        while True:
            if user_input_username == usernames[i] and user_input_password == passwords[i]:
                print("Welcome", usernames[i], "\n")
                break
            else:
                print(mod.bcolors.FAIL + "Login Failed!" + mod.bcolors.ENDC)
                user_input_username = mod.read_string("Username: ")
                user_input_password = mod.read_string("Password: ")


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
    print(f"{module_code} - {len(student_name)} students\n"  # on user select
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


def record_updates_file(module_file, student_name, days_present, days_absent, days_excused):  # save to a file function
    with open(f"{module_file}.txt", "w") as writefile:
        for i, x in enumerate(student_name):
            print(f"{student_name[i]}, {days_present[i]}, {days_absent[i]}, {days_excused[i]}", file=writefile)


def stat_calculator(module_code, student_name, days_present, days_absent, days_excused):
    non_attenders = ""  # accumulators
    low_attenders = ""
    best_attenders = ""
    best_attendance_number = 0
    average_sum = 0

    filename = module_code + "_" + mod.return_date()  # file to write to

    total_students = len(student_name)  # total number of students
    total_classes = days_present[0] + days_absent[0] + days_excused[0]  # get number of classes by summing all days

    for i, x in enumerate(student_name):
        average_student_attendance = (days_present[i] / total_classes) * 10  # average attendance days per student
        average_sum = average_sum + average_student_attendance  # sum the average attendance per student

        if days_present[i] == max(days_present):
            best_attenders = best_attenders + "\n" + student_name[i]
            best_attendance_number = days_present[i]

        if days_present[i] == 0:
            non_attenders = non_attenders + "\n" + student_name[i]

        if (average_student_attendance * 10) < 70 and days_present[i] != 0:
            low_attenders = low_attenders + "\n" + student_name[i]

    average_overall = average_sum // total_students  # overall average attendance

    if non_attenders == "":  # so it does not stay empty
        non_attenders = "None"

    if low_attenders == "":
        low_attenders = "None"

    print(f"Module: {module_code}\n"
          f"Number of Students: {total_students}\n"
          f"Number of Classes: {total_classes}\n"
          f"Average Attendance: {average_overall} days\n"
          f"\nLow Attender(s) - Under 70%:{low_attenders}\n"
          f"\nNon Attender(s): {non_attenders}\n"
          f"\nBest Attender(s): {best_attenders}\n"
          f"- with an attendance of {best_attendance_number}/{total_classes} days")

    try:  # write to a file
        with open(f"{filename}.txt", "x") as writefile:
            print(f"Module: {module_code}\n"
                  f"Number of Students: {total_students}\n"
                  f"Number of Classes: {total_classes}\n"
                  f"Average Attendance: {average_overall}\n"
                  f"\nLow Attender(s) - Under 70%:{low_attenders}\n"
                  f"\nNon Attender(s): {non_attenders}\n"
                  f"\nBest Attender(s): {best_attenders}\n"
                  f"- with an attendance of {best_attendance_number}/{total_classes} days", file=writefile)
    except FileExistsError:
        overwrite = mod.yes_no(
            mod.bcolors.WARNING + "Warning: A file with today's statistics already exist. Overwrite?: "
            + mod.bcolors.ENDC)

        if overwrite:  # if it exists overwrite it or not
            with open(f"{filename}.txt", "w") as writefile:
                print(f"Module: {module_code}\n"
                      f"Number of Students: {total_students}\n"
                      f"Number of Classes: {total_classes}\n"
                      f"Average Attendance: {average_overall}\n"
                      f"\nLow Attender(s) - Under 70%:{low_attenders}\n"
                      f"\nNon Attender(s): {non_attenders}\n"
                      f"\nBest Attender(s): {best_attenders}\n"
                      f"- with an attendance of {best_attendance_number}/{total_classes} days", file=writefile)
            print(mod.bcolors.OKBLUE + f"File {filename}.txt overwritten." + mod.bcolors.ENDC)
        else:
            print(mod.bcolors.OKBLUE + f"File {filename}.txt not overwritten." + mod.bcolors.ENDC)


def main():
    login_check("login_details")
    while True:  # show the main menu until the user chooses EXIT
        user_choice, option_flag = main_menu()
        module_codes, module_names = list_modules()
        selected_module = module_menu(option_flag, module_codes, module_names)
        student_name, days_present, days_absent, days_excused = module_select(selected_module)  # non updated lists
        # to feed into update function

        # option 1 - update attendance
        if user_choice == 1:
            days_present_updated, days_absent_updated, days_excused_updated = update_attendance(selected_module,
                                                                                                student_name,
                                                                                                days_present,
                                                                                                days_absent,
                                                                                                days_excused)  # updated

            record_updates_file(selected_module, student_name, days_present_updated, days_absent_updated,
                                days_excused_updated)  # record to file

        # option 2 - generate stats
        elif user_choice == 2:
            stat_calculator(selected_module, student_name, days_present, days_absent, days_excused)


main()
