'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-'''
def divisors(n):
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    result.sort()
    return result
def task3(start = 312614, end = 312651):
    found = []
    for n in range(start, end + 1):
        d = divisors(n)
        if len(d) == 6:
            found.append((n, d))
    return found
for number, d in task3():
    print(' '.join(str(x) for x in d))