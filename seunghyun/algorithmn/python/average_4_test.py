def average(array):
    sum = 0
    for i in array:
        sum += i
    return sum / len(array)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
assert average([5, 3, 4]) == 4.0
assert average([1, 2, 3, 4, 5]) == 3.0
assert average([1, 3, 5]) == 3.0