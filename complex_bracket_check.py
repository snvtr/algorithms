def complex_bracket_check(A):
    """
        проверяет на корректность скобочную последовательность
        с двумя видами скобок

        >>> complex_bracket_check('(])')
        'Err'
        >>> complex_bracket_check('[[]]')
        'Ok'
        >>> complex_bracket_check('(([(]))())')
        'Err'
    """
    cnt_r = 0
    cnt_s = 0
    prev = A[0]
#    print('r: %i, s: %i' % (cnt_r, cnt_s))
    for c in A:
        if c == ')' and prev == '[': # некорректно
            return 'Err'
        if c == ']' and prev == '(': # некорректно
            return 'Err'
				
        if c == '(':
            cnt_r += 1
        if c == '[':
            cnt_s += 1
        if c == ')':
            cnt_r -= 1
        if c == ']':
            cnt_s -= 1

        prev = c
 #       print('r: %i, s: %i' % (cnt_r, cnt_s))

    if cnt_r + cnt_s != 0:        # некорректно
        return 'Err'

    return 'Ok'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
#    print(complex_bracket_check('(([(]))())'))
