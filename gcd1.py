def gcd(a, b):
    """ greatest common divider through division """
    if b != 0:
        if a > b:
            return gcd(b, a % b)
        elif a < b:
            return gcd(a, b % a)
    return a


#a = int(input())
#b = int(input())

print(gcb(44, 8))
