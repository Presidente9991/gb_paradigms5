"""
Задача 1: Напишите программу, которая находит все простые числа в заданном диапазоне.

Простые числа - это числа больше 1, которые не имеют делителей, кроме 1 и самих себя.
Задача состоит в том, чтобы написать программу,
которая будет находить и выводить все простые числа в заданном диапазоне.

Пример решения:

Программа принимает на вход начальное и конечное числа диапазона.
Для каждого числа в диапазоне проверяется, является ли оно простым.
Если число простое, оно добавляется в список простых чисел.
В конце программа выводит список найденных простых чисел.
"""


def prime_number(numbers: int, divisor: int = 2) -> bool:  # Метод для проверки, является ли число простым
    if not isinstance(numbers, int):
        numbers = int(numbers)

    if not isinstance(divisor, int):
        divisor = int(divisor)

    if numbers < 2:
        return False
    if numbers == 2:
        return True
    if numbers % divisor == 0:
        return False
    if divisor * divisor > numbers:
        return True
    return prime_number(numbers, divisor + 1)


input_request = int(input('Введите число, которым должен заканчиваться список: '))
if input_request <= 1:
    raise ValueError('Число должно быть не меньше, чем 2!')

array_prime_numbers = []
for number in range(1, input_request + 1):
    if prime_number(number):
        array_prime_numbers.append(number)

print(f"Следующие числа являются простыми: {array_prime_numbers}")
