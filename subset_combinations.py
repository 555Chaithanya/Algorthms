from itertools import combinations  
def subsetSum(n, arr, s):
    for i in range(n+1):
        for subset in combinations(arr, i):
            if sum(subset) == s:
                print(list(subset))
def foundSubset(arr,n,s):
    if(s==0):
        return True
    if(n==0 and s!=0):
        return False
    if(arr[n-1]>s):
        return foundSubset(arr,n-1,s)
    return foundSubset(arr,n-1,s) or foundSubset(arr,n-1,s-arr[n-1])

arr=[]
n=int(input("Enter size of the array:"))
print("Enter array elements:")
for i in range(n):
    l=int(input())
    arr.append(l)
s=int(input("Enter sum upto where you need subsets:"))
print(arr,end=" ")
print()
if(foundSubset(arr,n,s)==True):
    print("Subsets are found for given sum")
    subsetSum(n, arr, s)
else:
    print("No subset is found for given sum")
   
