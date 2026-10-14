from itertools import product


def task1() -> int:
    """
    Олег составляет 4-буквенные кодовые слова из букв A, B, C, D, E, X, Z.
    Буквы X и Z встречаются только на двух первых позициях,
    буквы A, B, C, D, E — только на двух последних.
    """
    first = ['X', 'Z']              # позиции 1-2
    last = ['A', 'B', 'C', 'D', 'E']  # позиции 3-4

    words = product(first, first, last, last)  # перебор всех комбинаций
    return sum(1 for _ in words)                # считаем количество


if __name__ == '__main__':
    print(task1())  # 100