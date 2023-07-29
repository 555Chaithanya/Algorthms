import timeit    
def Partition(L,R,arr):
    p_idx=L
    pivot=arr[p_idx]
    while L<R:
        while L<len(arr) and arr[L]<=pivot:
            L=L+1
        while arr[R]>pivot:
            R=R-1
        if L<R:
            arr[L],arr[R]=arr[R],arr[L]
    arr[p_idx],arr[R]=arr[R],arr[p_idx]
    return R

def quick_sort(L,R,arr):
    if L<R:
        p=Partition(L,R,arr)
        quick_sort(L,p-1,arr)
        quick_sort(p+1,R,arr)

if __name__=='__main__':
    arr=[]
    n=int(input("Enter size of the array:"))
    for i in range(n):
        l=int(input("~"))
        arr.append(l)
   
    print("Array elements before sorting:")
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
    print("Array elements after sorting:")
    b=timeit.timeit()
    quick_sort(0,len(arr)-1,arr)
    e=timeit.timeit()
    print(arr,end=" ")
    print()
    
    print(e-b)
            
