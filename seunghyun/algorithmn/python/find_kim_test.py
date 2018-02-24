def find_kim(seoul):
    for idx, name in enumerate(seoul):
        if name == "Kim":
            return idx

def test_find_kim():
    seoul = ["Queen", "Tod", "Kim"]
    assert find_kim(seoul) == 2
    seoul = ["Kim", "Tod", "Choi", "James"]
    assert find_kim(seoul) == 0
    seoul = ["Queen", "Tod", ""]
    assert find_kim(seoul) == None

