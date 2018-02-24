from functools import reduce

def sum_divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    print(f"result: {divisors}")
    return reduce(lambda x,y:x+y, divisors)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
def test_sum_divisor():
    assert sum_divisor(3) == 4
    assert sum_divisor(12) == 28
    assert sum_divisor(20) == 42
    