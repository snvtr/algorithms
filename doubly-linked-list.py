#!/usr/bin/python3

class DoublyLinkedList():

    def __init__(self):
        self.List =[[None, [], []]]

    def push(self, item):
        if self.List[0][0] is None:
            self.List[0][0] = item
        else:
            self.List.append([item,self.List[-1],[]])
            self.List[-2][2] = self.List[-1]
    
    def pop(self):
        
        temp_val, temp_lst1, temp_lst2 = self.List.pop()
        self.List[-1][2][:] = []
        return temp_val
        

    def __str__(self):
    
        temp_str = ''

        for i in self.List:
            temp_str = ''.join([temp_str,str(i[0]),'::',str(i[1]),'::',str(i[2]),'\n'])
            
        return temp_str
            

A = DoublyLinkedList()
A.push(1)
A.push(2)
A.push(3)
A.push(4)

print(str(A))

my_val = A.pop()

print(str(A))

