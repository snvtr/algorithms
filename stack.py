
"""
>>> _clear(stack)
>>> _push(stack,1)
>>> _push(stack,2)
>>> _get_len(stack)
2
>>> _pop(stack)
2
>>> _pop(stack)
1
>>> _get_len(stack)
0
"""

stack = []

def _push(stack, val):
    """ добавляет значение в стек """
    stack.append(val)

def _pop(stack):
    """ вынимает из стека значение """
    return stack.pop()

def _clear(stack):
    stack = []

def _get_len(stack):
    return len(stack)

#_push(stack,'A')
#_push(stack,'B')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
