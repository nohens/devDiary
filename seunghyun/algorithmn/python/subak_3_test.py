def water_melon(n):
    words = ["수", "박"]
    result = ""
    for i in range(n):
        result += words[i % 2]
    return result

def test_water_melon():
    assert water_melon(0) ==  ""
    assert water_melon(1) ==  "수"
    assert water_melon(2) ==  "수박"
    assert water_melon(3) ==  "수박수"
    assert water_melon(4) ==  "수박수박"
    assert water_melon(5) ==  "수박수박수"
