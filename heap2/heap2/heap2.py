#!/usr/bin/python3

class Heap():

    def __init__(self):

        self.List = []
        self.size = 0

    def __str__(self):

        to_str = ''

        for i in self.List:
            to_str += str(i) + '; '

        return to_str
        
    def add(self, item):
        """ adds an element to the end and then pushes it up: """
        self.List.append(item)
        self.size += 1
        
        if self.size == 1:
            return True

        self.go_up(self.size-1)
        return True
    
    def pop(self):
        """ returns the very first element: """
        if self.size == 0:
            return None

        rc, self.List[0] = self.List[0], self.List[-1]
        self.List.pop(-1)
        self.size -= 1 
        self.go_down(0)

        return rc
        
    def go_up(self, index):
        """ to push an elements upwards """
        if index == 0:
            return True
            
        if self.List[index] < self.List[index // 2]:
            self.List[index], self.List[index // 2] = self.List[index // 2], self.List[index]
            self.go_up(index // 2)
            
        return True
        
    def go_down(self, index):
        """ reshuffles the tree when the first element is popped """

        # border case. We have reached the end of the tree:
        if index > self.size // 2:
            return True

        # border case. If it is the last subtree and the parent has two children:
        if index * 2 + 2 < self.size:
            if self.List[index*2+1] < self.List[index*2+2] and self.List[index*2+1] < self.List[index]:
                self.List[index*2+1], self.List[index] = self.List[index], self.List[index*2+1]
                self.go_down(index*2+1)
                return True
            if self.List[index*2+2] < self.List[index*2+1] and self.List[index*2+2] < self.List[index]:
                self.List[index*2+2], self.List[index] = self.List[index], self.List[index*2+2]
                self.go_down(index*2+2)
                return True

        # border case. If it is the last subtree and the parent has only one child:
        if index * 2 + 1 < self.size:
            if self.List[index*2+1] < self.List[index]:
                self.List[index*2+1], self.List[index] = self.List[index], self.List[index*2+1]
                return True

        # nothing is left: 
        return True
