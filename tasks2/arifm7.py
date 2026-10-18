'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-'''
def to_base(n, base):
    """Перевод натурального числа n в систему счисления с основанием base."""
    if n == 0:
        return '0'
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def task2():
    """
    Значение выражения 49^10 + 7^30 - 49 записали в 7-чной системе.
    """
    value = 49 ** 10 + 7 ** 30 - 49
    return to_base(value, 7).count('6')

print(task2())  