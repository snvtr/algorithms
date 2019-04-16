
# simple heap without classes, wrong way #2

### --- subs() --- ###

def add(heap, new_val):
    """ add an element """
    heap.append(new_val)
    swap_up(heap, len(heap)-1)

def swap_up(heap, new_idx):
    """ push the element upwards """
    if new_idx == 0:
        return

    parent_id = new_idx // 2
    if heap[parent_id] > heap[new_idx]:
        tmp = heap[parent_id]
        heap[parent_id] = heap[new_idx]
        heap[new_idx] = tmp
        swap_up(heap, parent_id)

def delete(heap, del_idx):
    """ delete an element and replace it from below - this is WRONG """ 
    swap_down(heap, del_idx)
    x = heap.pop()


def swap_down(heap, del_idx):
    """ push the element downwards """
    if del_idx >= len(heap) // 2:
        return

    if heap[del_idx*2] < heap[del_idx*2+1]:
        heap[del_idx] = heap[del_idx*2]
        swap_down(heap, del_idx*2)
    else:
        heap[del_idx] = heap[del_idx*2+1]
        swap_down(heap, del_idx*2+1)

### --- main() --- ###

my_heap = [-1]

add(my_heap, 2)
add(my_heap, 6)
add(my_heap, 4)
add(my_heap, 3)
add(my_heap, 5)
add(my_heap, 1)
add(my_heap, 0)

print(my_heap)

delete(my_heap,1)
delete(my_heap,3)

print(my_heap)
