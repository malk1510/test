#python3
class Trie:
    def __init__(self):
        self.childrenchar=[[]]
        self.childrenindex=[[]]
        self.parents=[]
        self.flags=[False]
    def depth(self,currentIndex):
        if(currentIndex==0):
            return 0
        return (self.depth(self.parents[currentIndex-1][0])+1)
    def insertTrie(self,s):
        currentIndex=0
        while(s[0] in self.childrenchar[currentIndex]):
            currentIndex=self.childrenindex[currentIndex][self.childrenchar[currentIndex].index(s.pop(0))]
            if(len(s)==0):
                self.flags[currentIndex]=True
                break
        for i in s:
            self.parents.append([currentIndex,i])
            self.childrenindex[currentIndex].append(len(self.parents))
            self.childrenchar[currentIndex].append(i)
            self.flags.append(False)
            currentIndex=len(self.parents)
            self.childrenindex.append([])
            self.childrenchar.append([])
        self.flags[currentIndex]=True
ob=Trie()
s=list(input())
n=int(input())
for i in range(n):
    ob.insertTrie(list(input()))
for i in range(len(s)):
    currentIndex=0
    j=i
    k=False
    while(s[j] in ob.childrenchar[currentIndex]):
        currentIndex=ob.childrenindex[currentIndex][ob.childrenchar[currentIndex].index(s[j])]
        j+=1
        k=ob.flags[currentIndex] and j-i==ob.depth(currentIndex)
        if(k):
            break
        if(j>=len(s)):
            break
    if(ob.childrenindex[currentIndex]==[] or k):
        print(str(i),end=' ')
        
            
        
