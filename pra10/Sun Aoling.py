
import doctest
from prac6.car import Car


def run_tests():
    """Functions Test."""
    assert repeat_string("Python", 1) == "print:Python"
    assert repeat_string("hi", 2) == "print:hi hi"
    test_car = Car()
    assert test_car.odometer == 0, "Note: The car’s odometer is not set"
    test_car = Car()
    assert test_car.fuel == 0"Note: The car’s fuel has run out"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

def repeat_string(s, n):
    return " ".join([s] * n)    "Repeat  's', 'n' times, with spaces in between."
def is_long_word(word, length=5):"Defined length is at most 5"
    return len(word) >= length

def phrase_to_sentence(phrase):
    sentence = phrase.capitalize()
    if sentence[-1] !='.':
        sentence+='.'
    return sentence
run_tests()

doctest.testmod()


