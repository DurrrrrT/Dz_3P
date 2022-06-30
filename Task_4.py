# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]
unique = []

for number in numbers:
    if number in unique:
        continue
    else:
        unique.append(number)

print(unique)
