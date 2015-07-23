list = [7, 2, 1, 6, 8, 5, 3, 4]

def swap(one, two):
    global list
    temp = list[one]
    list[one] = list[two]
    list[two] = temp

def quicksort(start, end):
    global list
    if(start >= end): return
    partition_idx = partition(start,end)
    quicksort(start, partition_idx-1)
    quicksort(partition_idx+1,end)

def partition(start, end):
    global list
    pivot = list[end]
    partition_idx = start
    for i in range(start,end):
        if(list[i] <= pivot):
            #swap list[i] and list[partition_idx]
            swap(i, partition_idx)
            partition_idx +=1
    #swap list[partition_idx] and list[end]
    swap(partition_idx,end)
    return partition_idx

print(list)
quicksort(0, len(list)-1)
print(list)
