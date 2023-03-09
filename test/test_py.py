import app

#test fonction 1
def test_answer1():
    assert app.inc(1) == 2

#test fonction 2
def test_answer2():
    assert app.multiplication(5,2) == 10
    
#tset fonction 3
def test_answer3():
    assert app.soustraction(7) == 5