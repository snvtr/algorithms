#!/usr/bin/python3

#import os

class Heap():

    def __init__(self):

        self.List = []
        self.size = 0

    def __str__(self):

        temp = ''

        for i in self.List:
            temp += str(i) + '; '

        return temp
        
    def add(self, item):

        self.List.append(item)
        self.size += 1
        
        if self.size == 1:
            return True

        self.go_up(self.size-1)
    
    def pop(self):

        rc, self.List[0] = self.List[0], self.List[-1]
        self.List.pop(-1)
        self.size -= 1 
        self.go_down(0)
        return rc
        
    def go_up(self, index):
        
        if index == 0:
            return
            
        if self.List[index] < self.List[index // 2]:
            self.List[index], self.List[index // 2] = self.List[index // 2], self.List[index]
            self.go_up(index // 2)
            
        return
        
    def go_down(self, index):
        
        if self.size // 2 > index:
            return

...

            self.go_down(index*2+2)

        else:

            return

            
my_heap = Heap()
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

print(my_heap)

rc = my_heap.pop()
print(my_heap)
rc = my_heap.pop()
print(my_heap)
rc = my_heap.pop()
print(my_heap)
rc = my_heap.pop()
print(my_heap)
rc = my_heap.pop()
print(my_heap)
rc = my_heap.pop()
print(my_heap)
