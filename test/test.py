# fonction 1
def inc(x):
    return x + 1

#fonction 2
import datetime

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age

#fonction 3
def deinc(x):
    return x - 1

#test fonction 1
def test_answer1():
    assert inc(1) == 2
    
#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "2002/09/11".split(""))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 25 
    

#tset fonction 3
def test_answer2():
    assert deinc(3) == 2