def convert_hex_to_binary(hex:str)->str:
    '''takes a hex string and converts it to a binary string'''
    # following the hint i am going to convert the hex string to base 2
    # then convert base 2 to base 64
    s = ""
    for h in hex:
        s += hex_to_binary(h)
    return s




def hex_to_binary(h):
    '''Converts a hexidecimal string to a binary string'''
    h = h.capitalize()
    s = ""
    match h:
        case "0":
            s = "0000"
        case "1":
            s = "0001"
        case "2":
            s = "0010"
        case "3":
            s = "0011"
        case "4":
            s = "0100"
        case "5":
            s = "0101"
        case "6":
            s = "0110"
        case "7":
            s = "0111"
        case "8":
            s = "1000"
        case "9":
            s = "1001"
        case "A":
            s = "1010"
        case "B":
            s = "1011"
        case "C":
            s = "1100"
        case "D":
            s = "1101"
        case "E":
            s = "1110"
        case "F":
            s = "1111"
    #print(s)
    return s


def convert_binary_to_base_64(b:str)-> str:
    s = ""
    while len(b) % 6 != 0:
        b = "0"+b
    for i in range(0,len(b),6):
        s = convert_binary_str_to_base_64(s[i:i+6])
    return ""

# Index	Binary	Char.		Index	Binary	Char.		Index	Binary	Char.		Index	Binary	Char.
# 0	000000	A	16	010000	Q	32	100000	g	48	110000	w
# 1	000001	B	17	010001	R	33	100001	h	49	110001	x
# 2	000010	C	18	010010	S	34	100010	i	50	110010	y
# 3	000011	D	19	010011	T	35	100011	j	51	110011	z
# 4	000100	E	20	010100	U	36	100100	k	52	110100	0
# 5	000101	F	21	010101	V	37	100101	l	53	110101	1
# 6	000110	G	22	010110	W	38	100110	m	54	110110	2
# 7	000111	H	23	010111	X	39	100111	n	55	110111	3
# 8	001000	I	24	011000	Y	40	101000	o	56	111000	4
# 9	001001	J	25	011001	Z	41	101001	p	57	111001	5
# 10	001010	K	26	011010	a	42	101010	q	58	111010	6
# 11	001011	L	27	011011	b	43	101011	r	59	111011	7
# 12	001100	M	28	011100	c	44	101100	s	60	111100	8
# 13	001101	N	29	011101	d	45	101101	t	61	111101	9
# 14	001110	O	30	011110	e	46	101110	u	62	111110	+
# 15	001111	P	31	011111	f	47	101111	v	63	111111	/


def convert_binary_str_to_base_64(b:str)->str:
    b = b.upper()
    s = ""
    match b:
        case "000000":
            s = "A"
        case "000001":
            s = "B"
        case "000010":
            s = "C"
        case "000011":
            s = "D"
        case "000100":
            s = "E"
        case "000101":
            s = "F"
        case "000110":
            s = "G"
        case "000111":
            s = "H"
        case "001000":
            s = "I"
        case "001001":
            s = "J"
        case "001010":
            s = "K"
        case "001011":
            s = "L"
        case "001100":
            s = "M"
        case "001101":
            s = "N"
        case "001110":
            s = "O"
        case "001111":
            s = "P"
        case "010000":
            s = "Q"
        case "010001":
            s = "R"
        case "010010":
            s = "S"
        case "010011":
            s = "T"
        case "010100":
            s = "U"
        case "010101":
            s = "V"
        case "010110":
            s = "W"
        case "010111":
            s = "X"
        case "011000":
            s = "Y"
        case "011001":
            s = "Z"
        case "011010":
            s = "a"
        case "011011":
            s = "b"
        case "011100":
            s = "c"
        case "011101":
            s = "d"
        case "011110":
            s = "e"
        case "011111":
            s = "f"

        case "100000":
            s = "g"
        case "100001":
            s = "h"
        case "100010":
            s = "i"
        case "100011":
            s = "j"
        case "100100":
            s = "k"
        case "100101":
            s = "l"
        case "100110":
            s = "m"
        case "100111":
            s = "n"
        case "101000":
            s = "o"
        case "101001":
            s = "p"
        case "101010":
            s = "q"
        case "101011":
            s = "r"
        case "101100":
            s = "s"
        case "101101":
            s = "t"
        case "101110":
            s = "u"
        case "101111":
            s = "v"
        case "110000":
            s = "w"
        case "110001":
            s = "x"
        case "110010":
            s = "y"
        case "110011":
            s = "z"
        case "110100":
            s = "0"
        case "110101":
            s = "1"
        case "110110":
            s = "2"
        case "110111":
            s = "3"
        case "111000":
            s = "4"
        case "111001":
            s = "5"
        case "111010":
            s = "6"
        case "111011":
            s = "7"
        case "111100":
            s = "8"
        case "111101":
            s = "9"
        case "111110":
            s = "+"
        case "111111":
            s = "/"


    return s