

class Heap():

    def __init__(self):
        self.Heap = []
        self.size = 0

    def add(self, new_val):
        if len(self.Heap) == 0:
            self.Heap.append(new_val)
            self.size = len(self.Heap)
        else:
            pass

    def del(self, del_val):
        if len(self.Heap) == 1:
            self.Heap = []
            self.size = 0
        elif len(self.Heap) == 0:
            self.size = 0
            return None
        else:
            pass

    def swap_up(self, child):
        pass

    def swap_down(self, empty_idx):
        pass

heap = Heap()
