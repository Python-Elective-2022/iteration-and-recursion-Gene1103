'''
in this function, iterativePower, base, exponent
    result = 1
    every exponent value
        result = timexbase
    return result
print the iterativePower base 2,3
'''
def iterativePower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterativePower(2,3))
'''
in this function, recursivePower, base, exponent
    if exp=1
        return base
    else
        return the base time the result from function
print the recursivePower function base 2,3s
'''
base = 0
exp = 0
def recursivePower(base, exp):
    if exp == 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(2,3))


