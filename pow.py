
def simple_pow(x, y):
    
    result = 1
    for i in range(y):
        result *= x
    return result

def quik_pow(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x * x * quik_pow(x, y-2)

def test_pow(function, x, y, result):
    tested = function(x,y)
    if result == tested:
        print("Correct result %d for x=%d, y=%d" % (result, x, y))
    else:
        print("Incorrect result %d for x=%d, y=%d" % (tested, x, y))



test_pow(simple_pow, 2, 5, 32)
test_pow(quik_pow, 2, 5, 32)
test_pow(quik_pow, 10, 3, 1000)
test_pow(quik_pow, 10, 5, 100000)
test_pow(quik_pow, 2, 9, 512)
