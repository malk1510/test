import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
def sksks(parents,heights,i):
    if(parents[i]==-1):
        heights[i]=1
    elif(heights[parents[i]]==0):
        heights[i]=sksks(parents,heights,parents[i])+1
    else:
        heights[i]=heights[parents[i]]+1
    return heights[i]

n=input()
arr=[int(i) for i in input().split()]
heights=[]
for i in range(int(n)):
    heights.append(0)
for i in range(int(n)):
    heights[i]=sksks(arr,heights,i)
print(max(heights))
