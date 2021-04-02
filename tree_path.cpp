#include<bits/stdc++.h>
using namespace std;

class Node{
    public: int val;
    Node* left;
    Node* right;
    Node(int val){
        this->val = val;
        left = NULL;
        right = NULL;
    }
};

class BinTree{
    Node* root;
    public: void insert(int n){
        if(root == NULL){
            root = new Node(n);
            return;
        }
        Node* curr_node = root;
        while(curr_node->left && curr_node->right){
            if((float)(rand())/RAND_MAX > 0.5)
                curr_node = curr_node->right;
            else
                curr_node = curr_node->left;
        }
        if(curr_node->left)
            curr_node -> right = new Node(n);
        else
            curr_node -> left = new Node(n);
        return;
    }
    int max_path(Node* node, vector<int>& max_paths){
        if(node==NULL)
            return 0;
        int p1 = max_path(node->left, max_paths);
        int p2 = max_path(node->right, max_paths);
        max_paths.push_back(p1+p2+node->val);
        return (node->val + max(p1,p2));
    }

    int max_tree_sum(){
        vector<int> max_paths;
        max_path(this->root, max_paths);
        int mx = max_paths[0];
        for(int i: max_paths){
            if(mx<i)
                mx = i;
        }
        return mx;
    }
};
int main(){
    vector<int> t = {1,2,42,1,4,43,1,332};
    BinTree tr;
    for(int i: t)
        tr.insert(i);
    cout<<tr.max_tree_sum();
    return 0;
}