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
            print('true')
            return True
        else:
            print('false')
            return False
    else:
        ans = num2 % num1
        if ans == 0:
            print('true')
            return True
        else:
            print('false')
            return False
