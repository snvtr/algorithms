from nose.tools import *
import heap2.heap2

def setup():
    pass

def teardown():
    pass

def test_heap():

    my_heap = heap2.heap2.Heap()
    my_heap.add(10)
    my_heap.add(9)
    my_heap.add(8)
    my_heap.add(7)
    my_heap.add(6)
    my_heap.add(5)
    my_heap.add(4)
    my_heap.add(3)
    my_heap.add(2)
    my_heap.add(1)
    my_heap.add(0)

    assert_equal(str(my_heap), '0; 1; 2; 5; 4; 3; 9; 6; 10; 7; 8; ')

    rc = my_heap.pop()
    rc = my_heap.pop()
    rc = my_heap.pop()
    rc = my_heap.pop()

    assert_equal(str(my_heap), '4; 5; 8; 6; 7; 10; 9; ')

    rc = my_heap.pop()
    rc = my_heap.pop()
    rc = my_heap.pop()
    rc = my_heap.pop()

    assert_equal(str(my_heap), '8; 9; 10; ')