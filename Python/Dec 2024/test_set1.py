from set1 import *

def test_set1_0():
    '''Make sure the 0 works correctly'''
    b = hex_to_binary("0")
    assert b == "0000"

def test_set1_1():
    '''Make sure the 1 works correctly'''
    b = hex_to_binary("1")
    assert b == "0001"

def test_set1_2():
    '''Make sure the 2 works correctly'''
    b = hex_to_binary("2")
    assert b == "0010"

def test_set1_3():
    '''Make sure the 3 works correctly'''
    b = hex_to_binary("3")
    assert b == "0011"

def test_set1_4():
    '''Make sure the 4 works correctly'''
    b = hex_to_binary("4")
    assert b == "0100"

def test_set1_5():
    '''Make sure the 5 works correctly'''
    b = hex_to_binary("5")
    assert b == "0101"

def test_set1_6():
    '''Make sure the 6 works correctly'''
    b = hex_to_binary("6")
    assert b == "0110"

def test_set1_7():
    '''Make sure the 6 works correctly'''
    b = hex_to_binary("7")
    assert b == "0111"

def test_set1_8():
    '''Make sure the 8 works correctly'''
    b = hex_to_binary("8")
    assert b == "1000"

def test_set1_9():
    '''Make sure the 9 works correctly'''
    b = hex_to_binary("9")
    assert b == "1001"

def test_set1_10():
    '''Make sure the A works correctly'''
    b = hex_to_binary("A")
    assert b == "1010"

def test_set1_10_lower():
    '''Make sure the A works correctly'''
    b = hex_to_binary("a")
    assert b == "1010"

def test_set1_11_lower():
    '''Make sure the b works correctly'''
    b = hex_to_binary("b")
    assert b == "1011"

def test_set1_11():
    '''Make sure the B works correctly'''
    b = hex_to_binary("B")
    assert b == "1011"

def test_set1_12_lower():
    '''Make sure the c works correctly'''
    b = hex_to_binary("c")
    assert b == "1100"

def test_set1_12():
    '''Make sure the C works correctly'''
    b = hex_to_binary("C")
    assert b == "1100"

def test_set1_13_lower():
    '''Make sure the d works correctly'''
    b = hex_to_binary("d")
    assert b == "1101"

def test_set1_13():
    '''Make sure the D works correctly'''
    b = hex_to_binary("D")
    assert b == "1101"

def test_set1_14_lower():
    '''Make sure the e works correctly'''
    b = hex_to_binary("e")
    assert b == "1110"

def test_set1_14():
    '''Make sure the E works correctly'''
    b = hex_to_binary("E")
    assert b == "1110"

def test_set1_15_lower():
    '''Make sure the f works correctly'''
    b = hex_to_binary("f")
    assert b == "1111"

def test_set1_15():
    '''Make sure the F works correctly'''
    b = hex_to_binary("F")
    assert b == "1111"

def test_convert_hex_to_binary():
    '''Doing half the challenge'''
    b = convert_hex_to_binary("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    assert "010010010010011101101101001000000110101101101001011011000110110001101001011011100110011100100000011110010110111101110101011100100010000001100010011100100110000101101001011011100010000001101100011010010110101101100101001000000110000100100000011100000110111101101001011100110110111101101110011011110111010101110011001000000110110101110101011100110110100001110010011011110110111101101101" ==b
