# 1. Вивести квадрати чисел від 1 до 10.

i = 1

while i <= 10:
    print(i ** 2)
    i += 1

# 2. Вивести квадрати чисел від 10 до 1.

i = 10

while i >= 1:
    print(i ** 2)
    i -= 1

# 3.
# 3.1 Знайти максимальне число в списку але не більше 100

lst = [13, 300, 320, 81, 940, 1002, 23, 96]

max_number = lst[0]

i = 0

while i < len(lst):
    if lst[i] <= 100:
        max_number = lst[i]
        break

    i += 1

if max_number > 100:
    print("All numbers are greater than 100")

else:
    k = 0

    while k < len(lst):
        if max_number < lst[k] <= 100:
            max_number = lst[k]

        k += 1

    print(max_number)

# 3.2 Знайти суму всіх чисел в списку що діляться на 3

sum_div3 = 0

k = 0

while k < len(lst):
    if lst[k] % 3 == 0:
        sum_div3 += lst[k]

    k += 1

print(sum_div3)

# 3.3. Вивести квадрати чисел від 10 до 30

i = 10

while i <= 30:
    print(i ** 2)
    i += 1

# 3.4 Є список слів, знайти слово в якому к-ть букв найбільша.

word_lst = ["one", "two", "three", "four", "five", "eleven", "twczzxelve"]

word_max = []

letter_count = 0

i = 0

while i < len(word_lst):
    if len(word_lst[i]) > letter_count:
        letter_count = len(word_lst[i])
        word_max = word_lst[i]

    i += 1

print(f"The longest word - '{word_max}' with {letter_count} letters")

# 3.5. Порахувати і вивести на екран окремо суму парних і непарних чисел списку

# I use the list "lst" from the first task

sum_even = 0

sum_odd = 0

i = 0

while i < len(lst):
    if lst[i] % 2 == 0:
        sum_even += lst[i]

    else:
        sum_odd += lst[i]

    i += 1

print(f"Sum of even numbers: {sum_even}; Sum of odd numbers: {sum_odd}")


#  Задачі на функції

# 1. Створити функцію що приймає масив і повертає суму його елементів.

def iterable_sum(iterable):
    sum_of_elements = 0
    for j in iterable:
        sum_of_elements += j

    return sum_of_elements


lst_1 = [1, 23, 3]

print(iterable_sum(lst_1))


# 2. Створити функцію яка приймає два аргумента перший список, другий число k. Знайти найбільше число в списку індекс якого менший числа k.
# Якщо список містить менше елементів ніж число k то повернути 0.

def list_max_index(lst, k):
    if len(lst) >= k:
        max_element = lst[0]
        j = 0

        while j < k:
            if lst[j] > max_element:
                max_element = lst[j]

            j += 1

        return max_element

    else:
        return 0


lst_2 = [1, 7, 8, -2]

print(iterable_max_index(lst_2, 3))
