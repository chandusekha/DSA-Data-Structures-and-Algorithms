def bobbleSort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1

print(bobbleSort([4,2,6,5,3,1]))