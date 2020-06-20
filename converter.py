def decimalToBinary(n):
    result = n
    binary = ''

    while (result > 0):
        binary += ('1' if not(result % 2 == 0) else '0')
        result //= 2

    return binary[::-1]

def binaryToDecimal(binary):
    result = 0
    b = str(binary)
    l = len(b) - 1
    for i in b:
        result += int(i) * (2 ** l)
        l -= 1
    return result
    # return result

def octalToDecimal(octal):
    num = map(int, str(octal)[::-1])
    decimal = 0
    for i, number in enumerate(num):
        decimal += number * (8 ** i)
    return decimal

def decimalToOctal(n):
    i = n
    octal = ''
    while (i > 0):
        octal += str(i % 8)
        i //= 8
    return octal[::-1]