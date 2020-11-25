# Liam Barry
# CSCI-141: hw1
# Conditionals

def is_triangle(num1, num2, num3):
    if num1 < 0 or num2 < 0 or num3 < 0:
        print('this triangle requires positive (+) integers only!')
        return None
    if (num1 + num2) < num3:
        print('num1, num2, num3 cannot form a triangle: ' + str(num3) + ' is too large!')
        return False
    if (num2 + num3) < num1:
        print('num1, num2, num3 cannot form a triangle: ' + str(num1) + ' is too large!')
        return False
    if (num3 + num1) < num2:
        print('num1, num2, num3 cannot form a triangle: ' + str(num2) + ' is too large!')
        return False
    else:
        print('num1, num2, num3 can all form a triangle together')
        return True


def main():
    num1 = int(input('please enter num1: '))
    num2 = int(input('please enter num2: '))
    num3 = int(input('please enter num3: '))

    is_triangle(num1, num2, num3)


main()