#include <bits/stdc++.h>
using namespace std;
const int T[9][6]={{1,2,3,1,4,5},{1,6,7,1,1,1},{2,2,8,2,2,2},{3,8,3,3,3,3},{4,2,7,4,4,4},{5,6,3,5,5,5},{6,6,8,6,6,6},{7,8,7,7,7,7},{8,8,8,8,8,8}};
const int SIG[9]={0,0,4,1,16,32,8,2,0};
const vector<vector<int>> STEPS={{-1,-1},{1,2,-1,-2},{2,1,-2,-1},{3,1,1,-3},{1,-1},{2,-2}};
const map<int,set<int>> REQ={{2,{16,32}},{3,{16,32}},{4,{1,2,4,8}},{5,{16,32}},{6,{1,2,4,8}},{7,{1,2,4,8}},{8,{1,2,4,8}},{9,{16,32}}};
map<tuple<int,int,int>,uint32_t> masks;
int position6[6]={},key3[3]={};
long long words=0;
map<pair<int,int>,int> label_index;
void dfs(int depth,int n,int q){
    if(depth==n){
        auto it=REQ.find(n);
        if(it==REQ.end() || !it->second.count(SIG[q])) return;
        if(position6[0]!=2) return;
        for(int j=1;j<6;j++) if(position6[j]) return;
        masks[make_tuple(key3[0],key3[1],key3[2])]|=(1u<<label_index[{n,SIG[q]}]);
        ++words; return;
    }
    for(int a=0;a<6;a++){
        int qq=T[q][a]; if(qq==8)continue;
        for(int x:STEPS[a]){position6[abs(x)-1]+=x>0?1:-1; if(x>0)key3[x-1]++;}
        dfs(depth+1,n,qq);
        for(int x:STEPS[a]){position6[abs(x)-1]-=x>0?1:-1; if(x>0)key3[x-1]--;}
    }
}
int main(){
    int i=0;for(auto [n,sigs]:REQ)for(int s:sigs)label_index[{n,s}]=i++;
    for(auto [n,sigs]:REQ)dfs(0,n,0);
    if(words!=178850 || masks.size()!=94 || label_index.size()!=24)return 2;
    set<uint32_t> patterns;
    for(auto [key,mask]:masks)patterns.insert(mask);
    if(patterns.size()!=21)return 3;
    vector<pair<int,int>> sentinels={{2,16},{2,32},{3,16},{4,1},{7,1}};
    vector<vector<tuple<int,int,int>>> f(5);
    for(int j=0;j<5;j++)for(auto [key,mask]:masks)
        if((mask>>label_index[sentinels[j]])&1)f[j].push_back(key);
    if(f[0].size()!=1||f[1].size()!=1||f[2].size()!=2||f[3].size()!=7||f[4].size()!=34)return 4;
    for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)
        for(auto k:f[a])for(auto t:f[b])if(k==t)return 5;
    uint32_t ALL=(1u<<label_index.size())-1;
    set<set<tuple<int,int,int>>> solutions;
    for(auto k1:f[0])for(auto k2:f[1])for(auto k3:f[2])for(auto k4:f[3])for(auto k5:f[4])
        if((masks[k1]|masks[k2]|masks[k3]|masks[k4]|masks[k5])==ALL)
            solutions.insert({k1,k2,k3,k4,k5});
    if(solutions.size()!=16)return 6;
    cout<<"INDEPENDENT_BRUTE_ALL_WORDS "<<words<<" keys "<<masks.size()
        <<" labels "<<label_index.size()<<" patterns "<<patterns.size()<<"\n";
    cout<<"PACKS 1 1 2 7 34 EXACT_FIVE_KEY_SETS "<<solutions.size()<<"\n";
}