import app

#test fonction 1
def test_answer1():
    assert app.inc(1) == 2

#test fonction 2
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "2003/09/11".split(""))   
    # When.
    age = app.get_age(yyyy, mm, dd)
    # Then.
    assert age == 20
    
#tset fonction 3
def test_answer2():
    assert app.deinc(3) == 2