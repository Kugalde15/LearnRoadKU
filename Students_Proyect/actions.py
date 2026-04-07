

import re


def add_student(students_data):

    student_name = is_valid_name("Enter the student's full name: ")
    section = is_valid_section("Enter the student section (07A / 11C): ")

    if student_exists(students_data, student_name, section):

        print("\nThe enrolled student already exists, enter a new student\n")
        input("*"*20)
        return

    spanish_note = validation("Spanish note", "Spanish note: ")
    english_note = validation("English note", "English note: ")
    social_note = validation("Social note", "Social note: ")
    science_note = validation("Science note", "Science note: ")

    data = {
        "Student name" : student_name,
        "Section" : section,
        "Spanish note" : spanish_note,
        "English note" : english_note,
        "Social note" : social_note,
        "Science note" : science_note
        }

    students_data.append(data)
    data["Average"] = (data["Spanish note"] + data["English note"] + data["Social note"] + data["Science note"]) / 4
    print("Student added successfully ✅")
    add_other_student(students_data)


def add_other_student(students_data):

    print("Do you need to add another student? Yes[Y] / No[AnyKey]: ")
    other_student = input("\u27A4 ").upper()
    if other_student == "Y":
        add_student(students_data)
    else:
        return

def validation(str_name, show_str):

    while True:
        try:

            data = int(input(show_str))
            if data < 0:
                print("The number must be higher than 0\n")
            elif data > 100:
                print("The number must be lower than 100\n")
            else:
                return data

        except ValueError:
            print(f"{str_name} need to be a number (0 - 100): \n")


def see_all_students(students_data):

    for val in students_data:
        print(
            f"Full name: {val['Student name']}\n"
            f"Section: {val['Section']}\n"
            f"Spanish note: {val['Spanish note']}\n"
            f"English note: {val['English note']}\n"
            f"Social note: {val['Social note']}\n"
            f"Science note: {val['Science note']}\n"
            f"Average: {val['Average']}"
            )
        print("-" * 20)

    print("Any key to return to menu")
    input("*"*20)
    return

def top_3_average(students_data):

    top3 = []
    count = 0
    for top in students_data:
        top3.append(top)
    top3 = sorted(students_data, key=lambda x: x["Average"], reverse=True)[:3]
    print(">> Best Students <<")

    for i in top3:
        count += 1
        print(f'Top {count}: \nName: {i["Student name"]}\nSection: {i["Section"]}\nAverage: {i["Average"]}')
        print("-"*15)
    print("Any key to return to menu")
    input("*"*20)
    return

def get_global_avg(students_data):

    sum_all_avg = 0
    for val in students_data:
        sum_all_avg += val["Average"]
    global_avg = sum_all_avg / len(students_data)
    print(f"\nThe average of all students is \u27A4  {round(global_avg, 2)}\n")
    print("Any key to return to menu")
    input("*"*20)
    return

def del_student(students_data):

    student_to_delete = is_valid_name("Student's name to deleted: \n")
    section_del = is_valid_section("Section of the student: \n")
    for student in students_data:
        if student["Student name"].lower().strip() == student_to_delete.lower().strip() and student["Section"].lower().strip() == section_del.lower().strip():
            sure_del = input(f"You sure to delete '{student['Student name']}' Yes [Y] / No [AnyKey]: \n").upper()
            if sure_del == "Y":
                students_data.remove(student)
                print("Student successfully removed \u2705\n")
            break
    else:
        print("Student not found \u274c")

    opc = input("Press [ Y ] to search another student, press [ R ] to return to menu or [ AnyKey ] to exit: \n").upper()
    if opc == "Y" :
        del_student(students_data)
    if opc == "R" :
        return
    else:
        exit()


def failed_students(students_data):

    fail_students = []
    note = 60
    for fail in students_data:
        if note > fail["Spanish note"]:
            fail_students.append(fail)
        elif note > fail["English note"]:
            fail_students.append(fail)
        elif note > fail["Social note"]:
            fail_students.append(fail)
        elif note > fail["Science note"]:
            fail_students.append(fail)
    print("Students failed: \n")

    for show in fail_students:
        print(f'Name: {show["Student name"]} \nSection: {show["Section"]}')
        if note > show["Spanish note"]:
            print(f'Spanish note: {show["Spanish note"]}')
        if note > show["English note"]:
            print(f'English note: {show["English note"]}')
        if note > show["Social note"]:
            print(f'Social note: {show["Social note"]}')
        if note > show["Science note"]:
            print(f'Science note: {show["Science note"]}')
        print("-"*20)

    print("Any key to return to menu")
    input("*"*20)
    return

def is_valid_name(show_str):

    while True:
        data = input(show_str).title()

        if data.isdigit():
            print("Name cannot be a number, please enter a valid name\n")
            continue

        if len(data) <= 3:
            print("Enter a valid full name\n")
            continue

        return data


def is_valid_section(show_str):

    valid_sections = (
        "07A","07B", "07C",
        "08A", "08B", "08C",
        "09A","09B","09C",
        "10A" , "10B", "10C",
        "11A", "11B", "11C"
        )

    while True:

        data = input(show_str).upper()

        if data not in valid_sections:
            print("Enter a valid section (07A / 11C)\n")
            continue

        return data


def student_exists(students_data, name, section):

    for val in students_data:
        if val["Student name"].strip().lower() == name.strip().lower() and val["Section"].strip().lower() == section.strip().lower():
            return True
    return False
