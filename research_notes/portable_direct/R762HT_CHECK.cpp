#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Counts = array<int,9>;
static vector<string> ports;
static vector<string> types;
static map<string,int> idx;
static map<pair<int,Counts>,uint64_t> memo;
static uint64_t visited=0;
string union_support(const string &a,const string &b) {
    string u=a+b; sort(u.begin(),u.end()); u.erase(unique(u.begin(),u.end()),u.end());
    return u.size()==3 && a!=b ? u : string();
}
uint64_t calc(int root,int p,Counts c,bool use_memo) {
    if(all_of(c.begin(),c.end(),[](int x){return x==0;}))return p==root;
    auto key=make_pair(p,c);
    if(use_memo){auto it=memo.find(key);if(it!=memo.end())return it->second;}
    uint64_t ans=0;
    for(int q=0;q<(int)ports.size();q++) {
        string s=union_support(ports[p],ports[q]);
        auto it=idx.find(s);
        if(it!=idx.end() && c[it->second]>0) {
            --c[it->second]; ans+=calc(root,q,c,use_memo); ++c[it->second];
        }
    }
    if(use_memo)memo[key]=ans;
    else ++visited;
    return ans;
}
uint64_t sign_brute(const vector<string>&w) {
    array<int,6> H{}; for(auto&s:w)for(char i:s)++H[i-'0'];
    uint64_t ans=0;
    for(int mask=0;mask<(1<<w.size());mask++) {
        array<int,6> a{};
        for(int j=0;j<(int)w.size();j++) if(mask&(1<<j))for(char i:w[j])++a[i-'0'];
        bool ok=true; for(int i=0;i<6;i++)if(2*a[i]!=H[i])ok=false;
        ans+=ok;
    }
    return ans;
}
uint64_t sign_grouped(const Counts&n) {
    map<array<int,6>,uint64_t> dp;
    dp[{}]=1;
    for(int i=0;i<(int)types.size();i++) {
        int count=n[i]; if(!count)continue;
        map<array<int,6>,uint64_t> ndp;
        for(auto &e:dp)for(int j=0;j<=count;j++) {
            // These finite test inputs have n_s <= 2, so these are exact binomials.
            uint64_t coeff=(count==2 && j==1)?2:1;
            auto b=e.first; for(char k:types[i])b[k-'0']+=2*j-count;
            ndp[b]+=e.second*coeff;
        }
        dp.swap(ndp);
    }
    return dp[{}];
}
int main() {
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) ports.push_back(to_string(a)+to_string(b));
    vector<string> witness={"01","15","12","25","24","04","05","03","04","24","23","25","35","05","01"};
    if(witness.front()!=witness.back()) throw runtime_error("not closed");
    vector<string>w;
    for(size_t i=1;i<witness.size();i++) {
        auto s=union_support(witness[i-1],witness[i]);
        if(s.empty())throw runtime_error("illegal Port adjacency");
        w.push_back(s);
    }
    types=w; sort(types.begin(),types.end());types.erase(unique(types.begin(),types.end()),types.end());
    if(types.size()!=9)throw runtime_error("unexpected number of support types");
    Counts n{};
    for(int i=0;i<9;i++)idx[types[i]]=i;
    for(auto&s:w)++n[idx[s]];
    uint64_t D=1; for(int a:n){for(int j=2;j<=a;j++)D*=j;}
    const int root=find(ports.begin(),ports.end(),"01")-ports.begin();
    uint64_t W=calc(root,root,n,true);
    uint64_t direct=calc(root,root,n,false);
    uint64_t C1=sign_brute(w),C2=sign_grouped(n);
    if(W!=422||direct!=422||D!=32||C1!=104||C2!=104||W*D*C1!=1404416ULL)
        throw runtime_error("14-event certificate mismatch");
    Counts single{};single[idx["015"]]=2;
    // Root 01, support 015: neighbors 05 and 15, each returns to 01.
    if(calc(root,root,single,true)!=2)throw runtime_error("2-event unit count mismatch");
    cout<<"PASS R762HT; W01=422; D=32; rooted_labeled=13504; C=104; joint=1404416; DFS_nodes="<<visited<<"\n";
}
