def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def test_even_or_odd():
    assert even_or_odd(2) == 'Even'
    assert even_or_odd(3) == 'Odd'
    assert even_or_odd(4) == 'Even'