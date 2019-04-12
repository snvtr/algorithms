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
            # only unique values, to make it possible to search them by value and return their index.
            if self.search(item) == -1:
                self.List.append([item,self.List[-1],[]])
                self.List[-2][2] = self.List[-1]
            else:
                return False

        return True
    
    def pop(self):
        
        temp_val, temp_lst1, temp_lst2 = self.List.pop()
        self.List[-1][2][:] = []

        return temp_val

    def search(self, value): # search by value

        for i in range(len(self.List)-1):
            if value == self.List[i][0]:
                return i

        return -1

    def delete(self, index): # delete by index

        if len(self.List) == 0:
            return False

        if index > 0:
            if index != len(self.List):
                self.List[index-1][2][:] = self.List[index+1]
                self.List[index+1][1][:] = self.List[index-1]
            else:
                self.List[index-1][2][:] = []
            self.List.pop(index)
        elif index == 0:
            self.List.pop(0)
            if len(self.List) > 0:
                self.List[0][1][:] = []
        else:
            return False

        return True


### __main__() ###

A = DoublyLinkedList()
A.push(1)
A.push(2)
A.push(3)
A.push(4)
A.push(5)

#print(A.search(3))
A.delete(3)
print(A)

