import random

N = int(input("кількість чисел (N): "))
min_value = int(input("мінімальне значення для генерації чисел: "))
max_value = int(input("максимальне значення для генерації чисел: "))

random_numbers = [random.randint(min_value, max_value) for _ in range(N)]
print(f"Згенерований список: {random_numbers}")

average = sum(random_numbers) / len(random_numbers)
print(f"Середнє арифметичне: {average}")
