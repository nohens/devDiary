def collatz(num):
    count = 0
    while(count < 500):
        count += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        if num == 1:
            break

    return count if num == 1 else -1

def test_collatz():
    assert collatz(6) == 8