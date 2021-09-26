"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


def count_subs(string: str) -> int:
    l = len(string)
    counter = set()
    for i in range(l):
        for j in range(i+1, l+1):
            counter.add(hash(string[i:j]))

    counter.remove(hash(string))
    return len(counter)


if __name__ == '__main__':
    print(count_subs('literal'))
    print(count_subs('algorithms'))
    print(count_subs('python'))
