import time
def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        Printarr(arr)
def Printarr(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
if __name__=="__main__":
    arr=[]
    n=int(input("Enter size of arr:"))
    for i in range(n):
        l=float(input())
        arr.append(l)
    b=time.time()
    print("Array elements before sorting:")
    Printarr(arr)
    print("Array elements after sorting(at each iteration):")
    SelectionSort(arr)
    
    e=time.time()
    print(e-b)
