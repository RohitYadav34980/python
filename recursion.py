# recursion is call a function in itself
'''
syntax of recurssion
def function_name(n):
    statement/body of function
    return function_name(some argument)
'''


# for example factorial function:::::
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Enter a number: "))
print(factorial(n))
