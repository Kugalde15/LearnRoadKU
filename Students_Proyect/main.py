import menu
import actions


def run_program():
    try:

        if actions.students_data:
            print("Data already loaded")
        else:
            print("\n\nNo data loaded, please add or import data\n")
            input("*"*10)
        menu.main_menu()

    except Exception as ex:
        print("Unexpected error: " ,ex)


run_program()
