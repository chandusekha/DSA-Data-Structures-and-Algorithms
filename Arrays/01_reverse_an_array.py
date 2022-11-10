def swap(arr,l,h):
    arr[l],arr[h]=arr[h],arr[l]
    return arr
def reverse(arr):
    low = 0
    high = len(arr)-1
    while low<=high:
        revarr = swap(arr,low,high)
        low+=1
        high-=1
    return revarr
sum = reverse([2,5,10,1,3,8])
print(sum)