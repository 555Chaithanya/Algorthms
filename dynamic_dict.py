dict={}
n=int(input("Enter no of nodes:"))
for i in range(n):
    key=input("Enter key:")
    value=[]
    m=int(input("Enter no of values:"))
    for i in range(m):
        l=input("Enter the values:")
        value.append(l)
    dict[key]=value
print(dict)
