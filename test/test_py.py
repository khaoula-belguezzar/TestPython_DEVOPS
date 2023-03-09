'''importer le fichier app'''
import app


def test_answer1():
    '''tset fonction 1'''
    assert app.inc(1) == 2
def test_answer2():
    '''tset fonction 2'''
    assert app.multiplication(5,2) == 10
def test_answer3():
    '''tset fonction 3'''
    assert app.soustraction(7) == 5
   