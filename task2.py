"""
Задача 2: Напишите программу, которая сортирует список чисел методом сортировки слиянием.

Сортировка слиянием - это эффективный алгоритм сортировки, который разбивает список на две половины,
сортирует их отдельно, а затем объединяет в отсортированный список.
Задача состоит в том, чтобы написать программу,
которая будет сортировать список чисел методом сортировки слиянием.

Пример решения:

Программа принимает на вход список чисел, который нужно отсортировать.
Если список состоит из одного элемента или пуст, он считается уже отсортированным.
В противном случае список разделяется на две половины.
Рекурсивно вызывается сортировка слиянием для каждой половины.
Затем отсортированные половины сливаются в один отсортированный список.
Конечный отсортированный список возвращается.
"""
import random
from typing import List


def merge_sorting(numbers: List[int]) -> list:  # Метод сортировки слиянием

    if not isinstance(numbers, list):
        numbers = list(numbers)

    length = len(numbers)
    if length <= 1:
        return numbers

    middle = length // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    left_half = merge_sorting(left_half)
    right_half = merge_sorting(right_half)

    return connect_lists(left_half, right_half)


def connect_lists(left: list, right: list) -> list:  # Метод для соединения двух списков
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


array_numbers = []
for num in range(10):  # Заполнить пустой массив 10 случайными числами
    array_numbers.append(random.randint(1, 30))  # В радиусе от 1 до 30

print(f"Массив случайных чисел до сортировки -> {array_numbers}")
print(f"Массив случайных чисел после сортировки -> {merge_sorting(array_numbers)}")
