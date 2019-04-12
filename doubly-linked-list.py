#!/usr/bin/python3

### __defs__() ###

class DoublyLinkedList():

    def __init__(self):
        self.List =[[None, [], []]]

    def __str__(self):
    
        temp_str = ''

        for i in self.List:
            temp_str = ''.join([temp_str,str(i[0]),'::',str(i[1]),'::',str(i[2]),'\n'])
            
        return temp_str

    def push(self, item):

        if self.List[0][0] is None:
            self.List[0][0] = item
        else:
            self.List.append([item,self.List[-1],[]])
            self.List[-2][2] = self.List[-1]

        return # None
    
    def pop(self):
        
        temp_val, temp_lst1, temp_lst2 = self.List.pop()
        self.List[-1][2][:] = []

        return temp_val

    def search_by_value(self, value):

        for i in range(len(self.List)-1):
            if value == self.List[i][0]:
                return index

        return

    def delete_by_value(self, value):

        return True


### __main__() ###

A = DoublyLinkedList()
A.push(1)
A.push(2)
A.push(3)
A.push(4)

print(str(A))

my_val = A.pop()

print(str(A))

