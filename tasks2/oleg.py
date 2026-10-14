from itertools import product


def task1() -> int:
    """
    Олег составляет 4-буквенные кодовые слова из букв A, B, C, D, E, X, Z.
    Буквы X и Z встречаются только на двух первых позициях,
    буквы A, B, C, D, E — только на двух последних.
    """
    first = ['X', 'Z']              
    last = ['A', 'B', 'C', 'D', 'E']  

    words = product(first, first, last, last)  
    return sum(1 for _ in words)                


if __name__ == '__main__':
    print(task1()) 