import csv
from actions import students_data


students_headers = (
    'Student name',
    'Section',
    'Spanish note',
    'English note',
    'Social note',
    'Science note',
    'Average'
)


def export_students(file_path, data, headers):

    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

    print("\nExport successful \u2705\n")
    print("Any key to return to menu")
    input("*"*10)


def import_students(file_path):

    students_data.clear()

    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Spanish note"] = int(row["Spanish note"])
                row["English note"] = int(row["English note"])
                row["Social note"] = int(row["Social note"])
                row["Science note"] = int(row["Science note"])
                row["Average"] = float(row["Average"])
                students_data.append(row)
        print("\nImport successful \u2705\n")
        print("Any key to return to menu")
        input("*"*10)

    except FileNotFoundError:
        print("File not found \u274c")

    return students_data
