from set1 import *

def test_set1_0():
    '''Make sure the 0 works correctly'''
    bin = hex_to_binary("0")
    assert bin == "0000"