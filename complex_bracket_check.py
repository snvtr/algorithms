def complex_bracket_check(A):
    """
        проверяет на корректность скобочную последовательность
        с двумя видами скобок

        >>> complex_bracket_check('(])')
        'Err'
        >>> complex_bracket_check('([])')
        'Ok'
    """

    return 'Ok'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
