# fonction 1
def inc(x):
    return x + 1

#test fonction 1
def test_answer():
    assert inc(3) == 5
    
#fonction 2
import datetime

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age

#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split(""))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 26 
    
#fonction 3
def inc(x):
    return x - 1

#tset fonction 3
def test_answer():
    assert inc(3) == 2