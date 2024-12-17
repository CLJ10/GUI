import numpy as np

N = int(input("Введіть розмір масиву N: "))
array = []

print("Введіть елементи масиву:")
for _ in range(N):
    array.append(float(input()))

array = np.array(array)

negative_elements = array[array < 0]
if negative_elements.size > 0:
    min_negative = negative_elements.min()
    print(f"Мінімальний від'ємний елемент: {min_negative}")
else:
    print("В масиві немає від'ємних елементів.")

positive_elements = array[array > 0]
if positive_elements.size > 0:
    mean_positive = positive_elements.mean()
    print(f"Середнє арифметичне додатних елементів: {mean_positive}")
else:
    print("В масиві немає додатних елементів.")

if positive_elements.size > 0:
    print("Додатні елементи масиву:")
    print(positive_elements)
else:
    print("Додатні елементи відсутні.")
