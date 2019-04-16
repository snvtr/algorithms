def bracket_check(A):
    """
        single bracket type check
        >>> bracket_check('()')
        'Ok'
        >>> bracket_check(')')
        'Err'
    """

    cnt = 0
    for c in A:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return 'Err'

    return 'Ok'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
