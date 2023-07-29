import time
def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1
    

def Printarr(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__=='__main__':
    n=int(input('Enter Size of Arr:'))
    arr=[]
    for i in range(n):
        l=int(input())
        arr.append(l)
    print('Array elemnets before sorting:')
    Printarr(arr)

    
    p=time.time()
    mergeSort(arr)
    q=time.time()
    print('Array elemnets after sorting:')
    Printarr(arr)
    print("time is",q-p)

    
        
