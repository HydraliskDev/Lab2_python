def to_base(n: int, base: int) -> str:
    """Перевод натурального числа n в систему счисления с основанием base."""
    if n == 0:
        return '0'
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def task2() -> int:
    """
    Значение выражения 49^10 + 7^30 - 49 записали в 7-чной системе.
    Сколько цифр 6 содержится в записи?
    """
    value = 202
    return to_base(value, 7).count('6')

if __name__ == '__main__':
    print(task2())  # 18