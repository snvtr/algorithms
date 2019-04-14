#!/usr/bin/python3

import sys

Code = {'A': '01',
        'B': '001',
        'C': '100',
        'T': '110011',
        'D': '110',
        'E': '1010',
        'F': '1011',
        'Z': '11101',
        '\n': '11111'}

#                 T       A    \n       Z       C     E      C     B     \n   
input = ''.join(['110011','01','11111','11101','01','100','1010','100','001','11111'])
output = []

def decode(Code, input):
    """
    >>> decode(Code, input)
    'TA\nZACECB\n'
    """
    pos = 0
    while pos < len(input):
        for c in Code.keys():
            temp = input[pos:pos+len(Code[c])]
    #        print('current temp %s, current pos: %d' % (temp, pos))
            if temp.find(Code[c]) >= 0:
    #            print('debug. symbol %s found in string %s' % (c, input))
                output.append(c)
    #            input = input.replace(Code[c], '0'*len(Code[c]), 1)
                pos += len(Code[c])
    #            print('debug. current string: %s' % input)

    return ''.join(output)

#print('%r.' % decode(Code, input))
