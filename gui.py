import os
import PySimpleGUI as sg
import subprocess
import sys
import numpy as np
import random

# Функція для отримання списку лабораторних робіт
def get_labs_list():
    labs_path = "labs"
    labs = []
    if os.path.exists(labs_path):
        for folder in os.listdir(labs_path):
            lab_path = os.path.join(labs_path, folder)
            if os.path.isdir(lab_path) and any(f.endswith(".py") for f in os.listdir(lab_path)):
                labs.append(folder)
    return labs

# Функція для читання опису лабораторної роботи
def get_lab_description(lab_name):
    readme_path = os.path.join("labs", lab_name, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Опис відсутній."

# Функція для запуску лабораторної роботи та отримання результату
def run_lab(lab_name, user_input):
    lab_dir = os.path.join("labs", lab_name)
    lab_files = [f for f in os.listdir(lab_dir) if f.endswith(".py")]
    if lab_files:
        lab_path = os.path.join(lab_dir, lab_files[0])
        try:
            # Обробка введення для роботи з numpy-масивом або випадковими числами
            processed_input = process_user_input(user_input)
            result = subprocess.run(
                [sys.executable, lab_path],
                input=processed_input,  # Передаємо оброблене введення користувача
                capture_output=True,
                text=True,
                encoding="utf-8"
            )
            if result.returncode != 0:
                return f"Помилка виконання:\n{result.stderr}"
            return result.stdout if result.stdout else "Результат відсутній."
        except Exception as e:
            return f"Помилка виконання: {str(e)}"
    else:
        return "Файл лабораторної роботи не знайдено."

# Функція для обробки введення користувача для numpy або випадкових чисел
def process_user_input(user_input):
    try:
        # Обробка введення для генерації випадкових чисел
        if "random" in user_input.lower():
            parts = user_input.split(",")
            if len(parts) == 3:
                N = safe_int_conversion(parts[0].strip())
                min_value = safe_int_conversion(parts[1].strip())
                max_value = safe_int_conversion(parts[2].strip())
                random_numbers = [random.randint(min_value, max_value) for _ in range(N)]
                processed_input = f"{N}\n" + "\n".join(map(str, random_numbers)) + "\n"
                return processed_input
        # Очікуємо, що користувач введе числа через кому або пробіл
        user_values = list(map(float, user_input.replace(",", " ").split()))
        N = len(user_values)
        processed_input = f"{N}\n" + "\n".join(map(str, user_values)) + "\n"
        return processed_input
    except ValueError:
        return ""

# Функція для безпечного конвертування у ціле число
def safe_int_conversion(value):
    while True:
        try:
            return int(float(value))  # Конвертація float у int
        except ValueError:
            print(f"Некоректне значення: {value}. Будь ласка, введіть коректне число.")
            value = input("Спробуйте ще раз: ")

# Головна функція для GUI
def main():
    # Отримати список лабораторних робіт
    labs = get_labs_list()

    # Оформлення вікна
    layout = [
        [sg.Text("Список лабораторних робіт", font=("Helvetica", 16))],
        [sg.Listbox(values=labs, size=(30, 10), key="-LAB_LIST-", enable_events=True)],
        [sg.Text("Опис роботи:", font=("Helvetica", 14))],
        [sg.Multiline(size=(50, 10), key="-DESCRIPTION-", disabled=True)],
        [sg.Text("Введіть дані для лабораторної роботи (якщо потрібно):", font=("Helvetica", 14))],
        [sg.Multiline(size=(50, 5), key="-USER_INPUT-")],
        [sg.Text("Результат виконання:", font=("Helvetica", 14))],
        [sg.Multiline(size=(50, 10), key="-OUTPUT-", disabled=True)],
        [sg.Button("Запустити", key="-RUN-"), sg.Button("Вийти", key="-EXIT-")]
    ]

    # Створення вікна
    window = sg.Window("GUI для лабораторних робіт", layout)

    while True:
        event, values = window.read()

        # Обробка закриття вікна
        if event in (sg.WINDOW_CLOSED, "-EXIT-"):
            break

        # Вибір лабораторної роботи
        if event == "-LAB_LIST-" and values["-LAB_LIST-"]:
            selected_lab = values["-LAB_LIST-"][0]
            description = get_lab_description(selected_lab)
            window["-DESCRIPTION-"].update(description)

        # Запуск лабораторної роботи
        if event == "-RUN-" and values["-LAB_LIST-"]:
            selected_lab = values["-LAB_LIST-"][0]
            user_input = values["-USER_INPUT-"]
            output = run_lab(selected_lab, user_input)
            window["-OUTPUT-"].update(output)

    window.close()

if __name__ == "__main__":
    main()
