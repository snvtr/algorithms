import sys

# 4doctest:

class Stack():
    """
        реализует имитацию стека
    """

    Stack = []

    def __init__(self):
        self.Stack = []

    def clear(self):
        self.Stack = []

    def append(self, item):
        self.Stack.append(item)

    def pop(self):
        if len(self.Stack) > 0:
            return self.Stack.pop()
        else:
            return None

    def debug(self):
        print(self.Stack)

def is_int(x):
    try:
        rc = int(x)
        return True
    except:
        return False

def doctest_stub_func():
    """
    >>> is_int(0)
    True
    >>> is_int('A')
    False
    >>> my_stack = Stack()
    >>> my_stack.append(0)
    >>> my_stack.append(1)
    >>> my_stack.clear()
    >>> my_stack.debug()
    []
    """
    pass

#A = [2,2,'+']
#A = [2,3,4,'+','*'] # (3+4)*2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    A = [1,2,3,'-',4,'+','*'] # (3-2+4)*1
    my_stack = Stack()

    for c in A:
        if c in ['+','-','*','/']: # basic arithmetic operands
            x = my_stack.pop()     # pity, no checks for None
            y = my_stack.pop()     # here either
            if x is not None and y is not None:
                cmd = str(x) + c + str(y)
                val = eval(cmd) # I know, eval() is evil
                my_stack.append(val)
            else:
                print('Something wrong with the stack')
                sys.exit()
        elif is_int(c):
            my_stack.append(c)

    my_stack.debug()
