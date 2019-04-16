### __defs__ ###

class Heap():

    def __init__(self):
        self.HeapList = [-999]

    def clear(self):
        self.HeapList = [-999]

    def add(self, new_val):
        """
        Adds a new element to the end of the list and then moves it recursively up into the proper place.
        """
        self.HeapList.append(new_val)
        if len(self.HeapList) > 2:
            self.swap_up(len(self.HeapList)-1)

    def delete(self, del_idx):
        """ Deletes an element from the tree """
        if len(self.HeapList) == 1:
            return
        else:
            self.swap_down(del_idx)
            self.HeapList.pop()

    def swap_up(self, child_idx):
        """ moves up an elements """
        parent_idx = child_idx // 2
        if parent_idx == 0:
            return

        if self.HeapList[parent_idx] > self.HeapList[child_idx]:
            temp_val              = self.HeapList[child_idx]
            self.HeapList[child_idx]  = self.HeapList[parent_idx]
            self.HeapList[parent_idx] = temp_val
            self.swap_up(parent_idx)

    def swap_down(self, empty_idx):
        """
        This implementation is actually wrong. It does not replace a removed element with the last element.
        It just replaces the deleted element with a special value
        """
        if empty_idx >= len(self.HeapList) // 2:
            self.HeapList[empty_idx] = -999
            return

        child_idx1 = empty_idx * 2
        child_idx2 = empty_idx * 2 + 1
        if self.HeapList[child_idx1] < self.HeapList[child_idx2]:
            self.HeapList[empty_idx] = self.HeapList[child_idx1]
            self.swap_down(child_idx1)
        else:
            self.HeapList[empty_idx] = self.HeapList[child_idx2]
            self.swap_down(child_idx2)


### __main__() ###

my_heap = Heap()
my_heap.add(2)
my_heap.add(4)
my_heap.add(6)
my_heap.add(3)
my_heap.add(5)
my_heap.add(7)
my_heap.add(1)

print(my_heap.HeapList)

my_heap.delete(2)

print(my_heap.HeapList)
