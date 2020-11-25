# Liam Barry
# CSCI-141: hw1
# Conditionals

"""
determining whether the greater of the two numbers are divisible by each other
return True if numbers are divisible
returns False if the numbers are not
"""
def divisible(num1, num2):

    if num1 > num2:
        ans = num1 % num2
        if ans == 0:
            print(str(num1) + ' is evenly divisible by ' + str(num2))
            return True
        else:
            return False
    else:
        ans = num2 % num1
        if ans == 0:
            print(str(num2) + ' is evenly divisible by ' + str(num1))
            return True
        else:
            return False

def main():
    num1 = int(input("enter a number greater than 0: "))
    num2 = int(input("enter a number greater than 0: "))

    if num1 <= 0 or num2 <= 0:
        print('none')

    if num1 == num2:
        print('both numbers are equal!')
    divisible(num1, num2)


main()