def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

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

items = [54,26,93,17,77,31,44,55,20]
merge_sort(items)
print(items)



def quickSort(items):
   quickSortHelper(items,0,len(items)-1)

def quickSortHelper(items,first,last):
   if first<last:

       splitpoint = partition(items,first,last)

       quickSortHelper(items,first,splitpoint-1)
       quickSortHelper(items,splitpoint+1,last)


def partition(items,first,last):
   pivotvalue = items[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and items[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while items[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = items[leftmark]
           items[leftmark] = items[rightmark]
           items[rightmark] = temp

   temp = items[first]
   items[first] = items[rightmark]
   items[rightmark] = temp


   return rightmark

items = [54,26,93,17,77,31,44,55,20, 100, 107]
quickSort(items)
print(items)
