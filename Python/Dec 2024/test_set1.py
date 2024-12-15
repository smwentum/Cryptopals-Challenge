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


def test_convert_binary_to_base_64_0():
    '''doing 0 should get A'''
    b = convert_binary_str_to_base_64("000000")
    assert b == 'A'

def test_convert_binary_to_base_64_1():
    '''doing 1 should get B'''
    b = convert_binary_str_to_base_64("000001")
    assert b == 'B'

def test_convert_binary_to_base_64_2():
    '''doing 2 should get C'''
    b = convert_binary_str_to_base_64("000010")
    assert b == 'C'

def test_convert_binary_to_base_64_3():
    '''doing 3 should get D'''
    b = convert_binary_str_to_base_64("000011")
    assert b == 'D'


def test_convert_binary_to_base_64_4():
    '''doing 4 should get E'''
    b = convert_binary_str_to_base_64("000100")
    assert b == 'E'

def test_convert_binary_to_base_64_5():
    '''doing 5 should get F'''
    b = convert_binary_str_to_base_64("000101")
    assert b == 'F'

def test_convert_binary_to_base_64_6():
    '''doing 6 should get G'''
    b = convert_binary_str_to_base_64("000110")
    assert b == 'G'

def test_convert_binary_to_base_64_7():
    '''doing 7 should get H'''
    b = convert_binary_str_to_base_64("000111")
    assert b == 'H'




def test_convert_binary_to_base_64_8():
    '''doing 8 should get I'''
    b = convert_binary_str_to_base_64("001000")
    assert b == 'I'

def test_convert_binary_to_base_64_9():
    '''doing 9 should get J'''
    b = convert_binary_str_to_base_64("001001")
    assert b == 'J'

def test_convert_binary_to_base_64_10():
    '''doing 10 should get K'''
    b = convert_binary_str_to_base_64("001010")
    assert b == 'K'

def test_convert_binary_to_base_64_11():
    '''doing 11 should get L'''
    b = convert_binary_str_to_base_64("001011")
    assert b == 'L'


def test_convert_binary_to_base_64_12():
    '''doing 12 should get M'''
    b = convert_binary_str_to_base_64("001100")
    assert b == 'M'

def test_convert_binary_to_base_64_13():
    '''doing 5 should get N'''
    b = convert_binary_str_to_base_64("001101")
    assert b == 'N'

def test_convert_binary_to_base_64_14():
    '''doing 6 should get O'''
    b = convert_binary_str_to_base_64("001110")
    assert b == 'O'

def test_convert_binary_to_base_64_15():
    '''doing 15 should get P'''
    b = convert_binary_str_to_base_64("001111")
    assert b == 'P'



def test_convert_binary_to_base_64_16():
    '''doing 16 should get Q'''
    b = convert_binary_str_to_base_64("010000")
    assert b == 'Q'

def test_convert_binary_to_base_64_17():
    '''doing 17 should get R'''
    b = convert_binary_str_to_base_64("010001")
    assert b == 'R'

def test_convert_binary_to_base_64_18():
    '''doing 18 should get S'''
    b = convert_binary_str_to_base_64("010010")
    assert b == 'S'


def test_convert_binary_to_base_64_19():
    '''doing 19 should get T'''
    b = convert_binary_str_to_base_64("010011")
    assert b == 'T'


def test_convert_binary_to_base_64_20():
    '''doing 20 should get U'''
    b = convert_binary_str_to_base_64("010100")
    assert b == 'U'

def test_convert_binary_to_base_64_21():
    '''doing 21 should get V'''
    b = convert_binary_str_to_base_64("010101")
    assert b == 'V'

def test_convert_binary_to_base_64_22():
    '''doing 22 should get W'''
    b = convert_binary_str_to_base_64("010110")
    assert b == 'W'

def test_convert_binary_to_base_64_23():
    '''doing 23 should get X'''
    b = convert_binary_str_to_base_64("010111")
    assert b == 'X'


def test_convert_binary_to_base_64_24():
    '''doing 24 should get Y'''
    b = convert_binary_str_to_base_64("011000")
    assert b == 'Y'

def test_convert_binary_to_base_64_25():
    '''doing 25 should get Z'''
    b = convert_binary_str_to_base_64("011001")
    assert b == 'Z'

def test_convert_binary_to_base_64_26():
    '''doing 26 should get a'''
    b = convert_binary_str_to_base_64("011010")
    assert b == 'a'

def test_convert_binary_to_base_64_27():
    '''doing 27 should get b'''
    b = convert_binary_str_to_base_64("011011")
    assert b == 'b'


def test_convert_binary_to_base_64_28():
    '''doing 28 should get c'''
    b = convert_binary_str_to_base_64("011100")
    assert b == 'c'

def test_convert_binary_to_base_64_29():
    '''doing 29 should get d'''
    b = convert_binary_str_to_base_64("011101")
    assert b == 'd'

def test_convert_binary_to_base_64_30():
    '''doing 30 should get e'''
    b = convert_binary_str_to_base_64("011110")
    assert b == 'e'

def test_convert_binary_to_base_64_31():
    '''doing 31 should get f'''
    b = convert_binary_str_to_base_64("011111")
    assert b == 'f'


def test_convert_binary_to_base_64_32():
    '''doing 0 should get g'''
    b = convert_binary_str_to_base_64("100000")
    assert b == 'g'

def test_convert_binary_to_base_64_33():
    '''doing 33 should get h'''
    b = convert_binary_str_to_base_64("100001")
    assert b == 'h'

def test_convert_binary_to_base_64_34():
    '''doing 34 should get i'''
    b = convert_binary_str_to_base_64("100010")
    assert b == 'i'

def test_convert_binary_to_base_64_35():
    '''doing 35 should get j'''
    b = convert_binary_str_to_base_64("100011")
    assert b == 'j'


def test_convert_binary_to_base_64_36():
    '''doing 36 should get k'''
    b = convert_binary_str_to_base_64("100100")
    assert b == 'k'

def test_convert_binary_to_base_64_37():
    '''doing 37 should get l'''
    b = convert_binary_str_to_base_64("100101")
    assert b == 'l'

def test_convert_binary_to_base_64_38():
    '''doing 38 should get m'''
    b = convert_binary_str_to_base_64("100110")
    assert b == 'm'

def test_convert_binary_to_base_64_39():
    '''doing 39 should get n'''
    b = convert_binary_str_to_base_64("100111")
    assert b == 'n'




def test_convert_binary_to_base_64_40():
    '''doing 40 should get o'''
    b = convert_binary_str_to_base_64("101000")
    assert b == 'o'

def test_convert_binary_to_base_64_41():
    '''doing 41 should get p'''
    b = convert_binary_str_to_base_64("101001")
    assert b == 'p'

def test_convert_binary_to_base_64_42():
    '''doing 42 should get q'''
    b = convert_binary_str_to_base_64("101010")
    assert b == 'q'

def test_convert_binary_to_base_64_43():
    '''doing 43 should get r'''
    b = convert_binary_str_to_base_64("101011")
    assert b == 'r'


def test_convert_binary_to_base_64_44():
    '''doing 44 should get s'''
    b = convert_binary_str_to_base_64("101100")
    assert b == 's'

def test_convert_binary_to_base_64_45():
    '''doing 45 should get t'''
    b = convert_binary_str_to_base_64("101101")
    assert b == 't'

def test_convert_binary_to_base_64_46():
    '''doing 46 should get u'''
    b = convert_binary_str_to_base_64("101110")
    assert b == 'u'

def test_convert_binary_to_base_64_47():
    '''doing 47 should get v'''
    b = convert_binary_str_to_base_64("101111")
    assert b == 'v'



def test_convert_binary_to_base_64_48():
    '''doing 48 should get w'''
    b = convert_binary_str_to_base_64("110000")
    assert b == 'w'

def test_convert_binary_to_base_64_49():
    '''doing 49  should get x'''
    b = convert_binary_str_to_base_64("110001")
    assert b == 'x'

def test_convert_binary_to_base_64_50():
    '''doing 50 should get y'''
    b = convert_binary_str_to_base_64("110010")
    assert b == 'y'


def test_convert_binary_to_base_64_51():
    '''doing 51 should get z'''
    b = convert_binary_str_to_base_64("110011")
    assert b == 'z'


def test_convert_binary_to_base_64_52():
    '''doing 52 should get 0'''
    b = convert_binary_str_to_base_64("110100")
    assert b == '0'

def test_convert_binary_to_base_64_53():
    '''doing 53 should get 1'''
    b = convert_binary_str_to_base_64("110101")
    assert b == '1'

def test_convert_binary_to_base_64_54():
    '''doing 54 should get 2'''
    b = convert_binary_str_to_base_64("110110")
    assert b == '2'

def test_convert_binary_to_base_64_55():
    '''doing 55 should get 3'''
    b = convert_binary_str_to_base_64("110111")
    assert b == '3'


def test_convert_binary_to_base_64_56():
    '''doing 56 should get 4'''
    b = convert_binary_str_to_base_64("111000")
    assert b == '4'

def test_convert_binary_to_base_64_57():
    '''doing 57 should get 5'''
    b = convert_binary_str_to_base_64("111001")
    assert b == '5'

def test_convert_binary_to_base_64_58():
    '''doing 58 should get 6'''
    b = convert_binary_str_to_base_64("111010")
    assert b == '6'

def test_convert_binary_to_base_64_59():
    '''doing 59 should get 7'''
    b = convert_binary_str_to_base_64("111011")
    assert b == '7'


def test_convert_binary_to_base_64_60():
    '''doing 60 should get 8'''
    b = convert_binary_str_to_base_64("111100")
    assert b == '8'

def test_convert_binary_to_base_64_61():
    '''doing 61 should get 9'''
    b = convert_binary_str_to_base_64("111101")
    assert b == '9'

def test_convert_binary_to_base_64_62():
    '''doing 62 should get +'''
    b = convert_binary_str_to_base_64("111110")
    assert b == '+'

def test_convert_binary_to_base_64_63():
    '''doing 63 should get /'''
    b = convert_binary_str_to_base_64("111111")
    assert b == '/'


def test_convert_hex_to_base_64():
  b64=   convert_hex_to_base_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
  assert b64 == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"