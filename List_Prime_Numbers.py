# selecting prime numbers in a list from 0 to n
def listprime(n):
    from math import sqrt
    a = 1
    array = []
    prime = []
    while a < n:
        a += 1
        array.append(a)
    for ele in array:
        if ele == 2 or ele == 3:
            prime.append(ele)
        elif ele % 2 != 0 and ele % 3 != 0:
            prime.append(ele)
        else:
            pass
    return prime
