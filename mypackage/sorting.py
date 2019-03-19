def bubble_sort(items):

    # '''Return array of items, sorted in ascending order'''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
        return items

items = [54,26,93,17,77,31,44,55,20]
bubble_sort(items)
print(items)

def merge_sort(items):
    print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",items)
    return items

items = [54,26,93,17,77,31,44,55,20]
merge_sort(items)
print(items)



def quicksort(items):
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quicksort(items[:i])
        second_part = quicksort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
