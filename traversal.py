import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def preord(arr,index):
    print(arr[index][0],end=' ')
    if(arr[index][1]>=0):
        preord(arr,arr[index][1])
    if(arr[index][2]>=0):
        preord(arr,arr[index][2])
        
def inord(arr,index):
    if(arr[index][1]>=0):
        inord(arr,arr[index][1])
    print(arr[index][0],end=' ')
    if(arr[index][2]>=0):
        inord(arr,arr[index][2])

def postord(arr,index):
    if(arr[index][1]>=0):
        postord(arr,arr[index][1])
    if(arr[index][2]>=0):
        postord(arr,arr[index][2])
    print(arr[index][0],end=' ')

def main():
    n=int(input())
    arr=[]
    for i in range(n):
        x=[int(i) for i in input().split()]
        arr.append(x)
    inord(arr,0)
    print('')
    preord(arr,0)
    print('')
    postord(arr,0)
threading.Thread(target=main).start()


