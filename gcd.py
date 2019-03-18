### functions() ###

def gcd(a,b):
    """ gcd(a,b) greatest common divisor through substraction """
    if a != b:
        if a > b:
            a = a - b
            return gcd(a,b)
        else:
            b = b - a
            return gcd(a,b)
    return a

def test():
    """ test function """
    print(gcd(13,17))
    print(gcd(44,8))



### main() ###


test()
