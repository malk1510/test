#include<bits/stdc++.h>
using namespace std;

class Disjoint_Set{
    private: int n;
    private: vector<int> parent;
public:
    Disjoint_Set(int n){
        this->n = n;
        for(int i=0;i<n;i++)
            parent.push_back(i);
    }
    int find(int i){
        if(parent[i]==i)
            return i;
        else
            return find(parent[i]);
    }
    void Union(int a, int b){
        int a_par = find(a), b_par = find(b);
        if(a_par == b_par)
            return;
        else
            parent[a_par] = b_par;
        return;
    }
};

int main(){
	return 0;}