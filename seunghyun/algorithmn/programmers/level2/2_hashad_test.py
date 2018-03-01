from functools import reduce

def harshad(n):
    numArr= list(str(n))
    harshadNum = reduce(lambda x,y: int(x) + int(y), numArr)
    return n % harshadNum == 0

def test_hashad():
    assert harshad(10) == True
    assert harshad(12) == True
    assert harshad(18) == True
    assert harshad(11) == False
    assert harshad(13) == False
