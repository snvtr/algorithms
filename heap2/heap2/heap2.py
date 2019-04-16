#!/usr/bin/python3

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

        if self.size == 0:
            return None
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
        
        if index > self.size // 2:
            return

        # если да, значит есть две ветки 
        if index * 2 + 2 < self.size:
            if self.List[index*2+1] < self.List[index*2+2] and self.List[index*2+1] < self.List[index]:
                # тут поменять местами
                self.List[index*2+1], self.List[index] = self.List[index], self.List[index*2+1]
                self.go_down(index*2+1)
                return
            if self.List[index*2+2] < self.List[index*2+1] and self.List[index*2+2] < self.List[index]:
                # тут поменять местами
                self.List[index*2+2], self.List[index] = self.List[index], self.List[index*2+2]
                self.go_down(index*2+2)
                return

        # если да, значит есть только левая ветка и она последняя
        if index * 2 + 1 < self.size:
            if self.List[index*2+1] < self.List[index]:
                # тут поменять местами и возвращаемся наверх
                self.List[index*2+1], self.List[index] = self.List[index], self.List[index*2+1]
                return

        # больше ничего не остаётся
        return
        
