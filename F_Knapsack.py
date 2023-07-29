
wts=list(map(int,input("Enter the weights:").split()))
vls=list(map(int,input("Enter the values:").split()))
W=int(input("Enter max capacity of Knapsack:"))
def Knapsack(W,wts,vls):
    rats=[]
    for i in range(len(wts)):
        R=float(vls[i]/wts[i])
        rats.append(R)
    print(rats)
    SelecSort(rats,wts,vls)
    print(rats)
    max_vl=0
    frac=[0]*len(wts)
    for i in range(len(wts)):
        if wts[i]<=W:
            max_vl+=vls[i]
            W-=wts[i]
            frac[i]=1
        else:
            frac[i]=W/wts[i]
            max_vl+=vls[i]*frac[i]
            break
    return max_vl

def SelecSort(arr,arr1,arr2):
    for i in range(len(arr)):
        max_idx=i
        for j in range(i+1,len(arr)):
            if arr[max_idx]<arr[j]:
                max_idx=j
        arr[i],arr[max_idx]=arr[max_idx],arr[i]
        arr1[i],arr1[max_idx]=arr1[max_idx],arr1[i]
        arr2[i],arr2[max_idx]=arr2[max_idx],arr2[i]
            
print("The maximum optimal value is:",Knapsack(W,wts,vls))
    
