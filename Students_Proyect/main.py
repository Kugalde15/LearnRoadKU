from menu import main_menu


def run_program():
    students_data = []
    try:

        if students_data:
            print("Data already loaded")
        else:
            print("\n\nNo data loaded, please add or import data\n")
            input("*"*10)
        main_menu(students_data)

    except Exception as ex:
        print("Unexpected error: " ,ex)


run_program()
