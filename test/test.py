from app import inc
from app import get_age

#test fonction 1
def test_answer():
    assert inc(3) == 5
    
#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split(""))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 26 
    

#tset fonction 3
def test_answer():
    assert inc(3) == 2