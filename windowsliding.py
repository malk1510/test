def logang(arr,m):
    max1=0
    max1time=m
    max2=0
    max2time=m
    ar=[]
    if(m==1):
        return arr
    for i in range(len(arr)):
        if(arr[i]>=max1):
            max1=arr[i]
            max1time=m
            max2=0
            max2time=m
        elif(arr[i]>=max2):
            max2=arr[i]
            max2time=m
        if(max1time<=0):
            max1=max2
            max1time=max2time
            max2=arr[i]
            max2time=m
        if(i>=m-1):
            ar.append(max1)
        max1time-=1
        max2time-=1
    return ar
n=input()
arr=[int(i) for i in input().split()]
m=int(input())
print(' '.join([str(i) for i in logang(arr,m)]))
    
