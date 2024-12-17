import os

def create_group_file(group_name, students):
    with open(f"{group_name}.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']}, {student['average_grade']}\n")


def write_to_file(group_name, student):
    with open(f"{group_name}.txt", "a") as file:
        file.write(f"{student['name']}, {student['average_grade']}\n")


def read_from_file(group_name):
    try:
        with open(f"{group_name}.txt", "r") as file:
            return [line.strip().split(", ") for line in file.readlines()]
    except FileNotFoundError:
        print(f"Файл {group_name}.txt не знайдено.")
        return []


def find_files_in_directory(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]


def search_student_in_file(group_name, student_name):
    data = read_from_file(group_name)
    for entry in data:
        if entry[0] == student_name:
            return entry
    return None


def sort_file_by_average_grade(group_name):
    data = read_from_file(group_name)

    sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=True)

    with open(f"{group_name}.txt", "w") as file:
        for entry in sorted_data:
            file.write(f"{entry[0]}, {entry[1]}\n")


def process_multiple_groups(groups):
    for group_name, students in groups.items():
        create_group_file(group_name, students)



if __name__ == "__main__":
    groups = {
        "Group_A": [
            {"name": "Alice", "average_grade": 85.5},
            {"name": "Bob", "average_grade": 92.0},
            {"name": "Charlie", "average_grade": 78.5}
        ],
        "Group_B": [
            {"name": "David", "average_grade": 90.0},
            {"name": "Eva", "average_grade": 88.5},
            {"name": "Frank", "average_grade": 83.0}
        ],
        "Group_C": [
            {"name": "Grace", "average_grade": 91.0},
            {"name": "Hannah", "average_grade": 86.0},
            {"name": "Isaac", "average_grade": 89.5}
        ]
    }

    process_multiple_groups(groups)

    new_student = {"name": "Jack", "average_grade": 87.0}
    write_to_file("Group_A", new_student)

    data_A = read_from_file("Group_A")
    print("Дані з файлу Group_A:", data_A)

    student_name = "Alice"
    found_student_A = search_student_in_file("Group_A", student_name)
    print(f"Знайдено студента {student_name} в Group_A: {found_student_A}")

    sort_file_by_average_grade("Group_A")
    print("Дані після сортування в Group_A:")
    print(read_from_file("Group_A"))

    files = find_files_in_directory('.')
    print("Файли у каталозі:", files)