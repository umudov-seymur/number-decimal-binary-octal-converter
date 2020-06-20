# number-decimal-binary-octal-converter
number to decimal,binary,octal converter for practice

## USAGE
```python
from converter import *

# usage
try:
    number = int(input('Enter number: '))
     
    print("Decimal to binary: ", decimalToBinary(number))
    print("Binary to decimal: ", binaryToDecimal(number))

    print("Decimal to octal: ", decimalToOctal(number))
    print("Octal to decimal: ", octalToDecimal(number))

except ValueError:
    print('Please, enter valid number!')
```
