### __defs__ ###

class Heap():

    def __init__(self):
        self.HeapList = [-999]

    def clear(self):
        self.HeapList = [-999]

    def add(self, new_val):
        """
        Добавляет новый элемент в дерево (в конец списка и потом
        запускает рекурсивно поиск места для элемента)
        """
        self.HeapList.append(new_val)
        if len(self.HeapList) > 2:
            self.swap_up(len(self.HeapList)-1)

    def delete(self, del_idx):
        """ Удаляет элемент из дерева по индексу в списке """
        if len(self.HeapList) == 1:
            return
        else:
            self.swap_down(del_idx)
            self.HeapList.pop()

    def swap_up(self, child_idx):
        """ перемещает элемент в списке вверх по дереву при добавлении """
        parent_idx = child_idx // 2
        if parent_idx == 0:
            return

        if self.HeapList[parent_idx] > self.HeapList[child_idx]:
            temp_val              = self.HeapList[child_idx]
            self.HeapList[child_idx]  = self.HeapList[parent_idx]
            self.HeapList[parent_idx] = temp_val
            self.swap_up(parent_idx)

    def swap_down(self, empty_idx):
        """ перемещает элемент по дереву вниз при удалении элемента """
        if empty_idx >= len(self.HeapList) // 2:
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
