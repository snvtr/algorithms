
_stack = []

def _stack_push(_stack, _value):
    """ добавляет значение в стек """
    _stack.append(_value)

def _stack_pop(_stack):
    """ вынимает из стека значение """
    return _stack.pop()

def _stack_clear(_stack):
    _stack = []

def _stack_check(_stack):
    return len(_stack)

_stack_push(_stack,'A')
_stack_push(_stack,'B')
print(_stack_check(_stack))
print(_stack_pop(_stack))
print(_stack_pop(_stack))
print(_stack_check(_stack))
