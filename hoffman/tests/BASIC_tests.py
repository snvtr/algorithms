from nose.tools import *
import huffman.huffman

def setup():
    pass

def teardown():
    pass

def test_basic():
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
    result = huffman.huffman.decode(Code, input)
    assert_equal(result, 'TA\nZACECB\n')
    
