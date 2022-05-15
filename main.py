# Написати функції:

# 1. Примає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.

pi = 3.1415

def circle_length(r):
    try:
        return 2 * pi * r
    except TypeError as e:
        return e


print(circle_length(2))


# 2 Примає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.

def circle_square(r):
    try:
        return pi * (r ** 2)

    except TypeError as e:
        return e


print(circle_square('df'))

# 3. Приймає число, повертає чи є число поліндромом. Тобто з права на ліво і з ліва на право читається однаково. 12321 - це поліндром, 1234 - не поліндром.

def palindrome(n):
    s = str(n)
    return s == s[::-1]


print(palindrome(1221))

# 4. Функція приймає число n яке більше 0. За допомогою рекурсії виводить всі числа що менші n але більші 0.


def smaller_int(n):
    if n == 1:
        return []

    return [n - 1] + smaller_int(n - 1)  # returns in descending order; smaller_int(n - 1) + [n-1] - in ascending order


print(smaller_int(45))

# 5. Написати функцію lambda що приймає x i y, а повертає x^2 + y^2

sum_of_squares = lambda x, y: x ** 2 + y ** 2

print(sum_of_squares(3, 2))

# 6. Написати функцію lambda що приймає слово і повертає його довжину.

word_length = lambda word: len(word)

print(word_length("hello"))

# 7. Написати map що перетворює всі числа в списку на строку.
l = [101, 215, 3, 324, 234]
l = list(map(str, l))
# l = " ".join(list(map(str, l))) return string of numbers separed with a space;
# l = list(map(str, l)) return list of strings of numbers
print(l)


# 8. Написати filter що залишає в списку тільки числа > 10

def num_exceed_10(n):
    return n > 10


lst = [10, -4, 34, 50, 1, 65]
lst = list(filter(num_exceed_10, lst))
print(lst)

# 9. Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd ) (2 способи з lambda і без ) ( підказка: викорисати метот replace )

l = ['dsadfdfaaaa', 'sdffftt', 'aaaa1df', 'aaaa']

# спосіб 1 з lambda

l_delete_a = list(map(lambda a: a.replace('a', ''), l))

print(l_delete_a)

# спосіб 2 без lambda

def delete_a(wlst):
    return [i.replace('a', '') for i in wlst]


print(delete_a(l))

# 10. Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4. (2 способи з lambda і без )

l = ['dsa', 'sdffftt', 'aaaa1df', 'aaaa']

# спосіб 1 з lambda

new_l = list(filter(lambda a: len(a) > 4, l))

print(new_l)

# спосіб 2 без lambda


def letter_count(word):
    return len(word) > 4


new_l = list(filter(letter_count, l))

print(new_l)
