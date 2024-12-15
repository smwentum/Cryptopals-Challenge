def convert_hex_to_binary(hex:str)->str:
    '''takes a hex string and converts it to a binary string'''
    # following the hint i am going to convert the hex string to base 2
    # then convert base 2 to base 64
    s = ""
    for h in hex:
        s += hex_to_binary(h)
    return s

def convert_binary_to_base_64(b:str)-> str:
    return ""


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
