from functools import reduce

def sum_divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return reduce(lambda x,y:x+y, divisors)

def test_sum_divisor():
    assert sum_divisor(3) == 4
    assert sum_divisor(12) == 28
    assert sum_divisor(20) == 42
    