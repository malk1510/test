#python3
def graphscrap(arr,index,a):
    a.append(index)
    for i in arr[index]:
        if(i not in a):
            graphscrap(arr,i,a)
    
                
[n,m]=[int(i) for i in input().split()]
arr=[[] for i in range(n)]
for i in range(m):
    [x,y]=[int(i) for i in input().split()]
    if(x!=y):
        if((y-1) not in arr[x-1]):
            arr[x-1].append(y-1)
            arr[y-1].append(x-1)
a=[]
k=0
for i in range(n):
    if(i not in a):
        k+=1
        graphscrap(arr,i,a)
print(k)


        
    

    
