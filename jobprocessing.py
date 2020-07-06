def extractMin(arr):
    ans=arr[0]
    arr[0]=arr[len(arr)-1]
    arr[len(arr)-1]=ans
    del arr[len(arr)-1]
    index=0
    while(index<int(len(arr)/2)):
        max_index=index
        if(2*index+2==len(arr)):
            if(arr[2*index+1][1]<arr[index][1]):
                max_index=2*index+1
            if(arr[2*index+1][1]==arr[index][1] and arr[2*index+1][0]<arr[index][0]):
                max_index=2*index+1
        else:
            if(arr[max_index][1]>arr[2*index+2][1]):
                max_index=2*index+2
            if(arr[max_index][1]==arr[2*index+2][1] and arr[max_index][0]>arr[2*index+2][0]):
                max_index=2*index+2
            if(arr[max_index][1]>arr[2*index+1][1]):
                max_index=2*index+1
            if(arr[max_index][1]==arr[2*index+1][1] and arr[max_index][0]>arr[2*index+1][0]):
                max_index=2*index+1
        if(index==max_index):
            break
        t=arr[max_index]
        arr[max_index]=arr[index]
        arr[index]=t
        index=max_index
    return ans

def insert(arr,i):
    arr.append(i)
    index=len(arr)-1
    while(index>0):
        max_index=index
        if(index==1):
            if(arr[0][1]>arr[1][1]):
                max_index=0
        elif(index%2==0):
            max_index=int((index-2)/2)
            if(arr[index][1]>=arr[max_index][1]):
                max_index=index
        else:
            max_index=int((index-1)/2)
            if(arr[index][1]>=arr[max_index][1]):
                max_index=index
        if(max_index==index):
            break
        t=arr[max_index]
        arr[max_index]=arr[index]
        arr[index]=t
        index=max_index


def threads(n,arr):
    time=[]
    ans=[]
    for i in range(n):
        time.append([i,0])
    for i in arr:
        job=(extractMin(time))
        ans.append(job)
        insert(time,[job[0],i+job[1]])
    return ans
[n,m]=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
for i in threads(n,arr):
    x=[str(j) for j in i]
    print(' '.join(x))
        
