def selectionSort(mylist):
    for i in range(len(mylist)-1):
        min_index = i;
        for j in range(i+1,len(mylist)):
            if mylist[j]<mylist[min_index]:
                min_index=j
        if i!=min_index:
            temp=mylist[i]
            mylist[i]=mylist[min_index]
            mylist[min_index]=temp
    return mylist
print(selectionSort([4,2,6,5,3,1]))