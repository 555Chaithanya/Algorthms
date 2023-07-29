from math import sqrt
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)
dataset=[[4,3,0],[6,7,1],[7,8,1],[5,5,0],[8,8,1]]
n=len(dataset)

k=int(input("Enter the K value: "))
print("Enter the values to test the data:")
test=[6,8]
count_pos = 0
count_neg = 0
distances=[]
for train_row in dataset:
    dist=euclidean_distance(test, train_row)
    distances.append(dist)
print(distances)
def Sort(dataset,distances,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if distances[j]<distances[min]:
                min=j
        distances[i],distances[min]=distances[min],distances[i]
        
        dataset[i],dataset[min]=dataset[min],dataset[i]
for i in range(k):
    if(dataset[i][2]==0):
        count_neg=count_neg+1
    if(dataset[i][2]==1):
        count_pos=count_pos+1

def KNN(dataset):
    for i in range(k):
        print(dataset[k])

if(count_pos>count_neg):
    print("Test data neighbours are:")
    KNN(dataset)
    print("test data belongs to cluster 1")
    test.append(1)
    print(test)
else:
    print("test data belongs to cluster 0")
    test.append(0)
    print(test)




    
    
