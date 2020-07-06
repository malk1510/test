n=int(input())
dick={}
ar=[]
for i in range(n):
    x=input().split()
    if(x[0]=='add'):
        dick[x[1]]=x[2]
    elif(x[0]=='find'):
        try:
            ar.append(dick[x[1]])
        except(KeyError):
            ar.append('not found')
    elif(x[0]=='del'):
        try:
            del dick[x[1]]
        except(KeyError):
            continue
for i in ar:
    print(i)
    
