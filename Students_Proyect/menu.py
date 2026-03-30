import actions
import data
from actions import students_data
from data import students_headers

def main_menu():

    print("\n>> Student Control System <<\n")
    print("Select an option: ")
    print(
        "[1] - Add new student\n"
        "[2] - Show all students\n"
        "[3] - Top 3 average note\n"
        "[4] - Global average note\n"
        "[5] - Export file\n"
        "[6] - Import file\n"
        "[7] - Delete student\n"
        "[8] - Failed students\n"
        "[9] - Exit"
        )

    while True:
        try:

            opt = int(input("[Select 1 - 9] ==> "))
            if opt not in [1,2,3,4,5,6,7,8,9]:
                print("Enter a valid option, number between 1 - 9\n")
            elif opt == 1:
                actions.add_student()
            elif opt == 2:
                actions.see_all_students()
            elif opt == 3:
                actions.top_3_average()
            elif opt == 4:
                actions.get_global_avg()
            elif opt == 5:
                data.export_students("student_test.csv", students_data, students_headers)
            elif opt == 6:
                data.import_students("student_test.csv")
            elif opt == 7:
                actions.del_student()
            elif opt == 8:
                actions.failed_students()
            else:
                exit()

        except ValueError:
            print("Need to be a number between 1 - 9\n")
