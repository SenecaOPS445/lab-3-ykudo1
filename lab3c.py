#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: ykudo

def operate(number1, number2, operator):
    # Place logic in this function

    if operator == 'add':
#       return int(number1) + int(number2) + operator
        return int(number1) + int(number2)

    elif operator == 'subtract':
        return int(number1) - int(number2)

    elif operator == 'multiply':
        return int(number1) * int(number2)

#   elif operator == 'divide':
#       return int(number1) / int(number2)

    else:
#       print('Error: function operator can be "add", "subtract", or "multiply" ')
        return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
#   print(operate_add(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))


