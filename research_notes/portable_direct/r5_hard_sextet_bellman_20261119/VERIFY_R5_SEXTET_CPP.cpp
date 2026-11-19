// Independent exact Bellman verifier for six R5 scalar hypotheses.
// Read SIX_SUPPORTS.txt produced by the pinned integer-source checker.
// Usage: g++ -O2 -std=c++17 VERIFY_R5_SEXTET_CPP.cpp -o check && ./check SIX_SUPPORTS.txt
#include <array>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
struct Action { int cost; vector<int> masks; };
vector<Action> actions;
int f, radix;
unordered_map<uint64_t,int> cache;
uint64_t key_of(const array<int,6>&s){
    uint64_t out=0, factor=1;
    for(int v:s){out+=factor*v;factor*=radix;}
    return out;
}
int V(const array<int,6>&s){
    unsigned live=0;
    for(int i=0;i<6;i++)if(s[i]<=f)live|=1u<<i;
    if(__builtin_popcount(live)<=1)return 0;
    uint64_t key=key_of(s);
    auto it=cache.find(key);
    if(it!=cache.end())return it->second;
    int best=100000000;
    for(const auto&a:actions){
        bool idle=false;
        for(int mask:a.masks)if((unsigned(mask)&live)==live)idle=true;
        if(idle)continue;
        int worst=0;
        for(int mask:a.masks){
            array<int,6> next=s;
            for(int i=0;i<6;i++)
                if(!(mask&(1<<i)))next[i]=min(f+1,next[i]+1);
            worst=max(worst,V(next));
        }
        best=min(best,a.cost+worst);
    }
    if(best==100000000)throw runtime_error("nonterminal without separating action");
    cache.emplace(key,best);
    return best;
}
int main(int argc,char**argv){
    if(argc!=2)return 2;
    ifstream in(argv[1]);if(!in)return 3;
    string line;
    while(getline(in,line)){
        if(line.empty()||line[0]=='#')continue;
        istringstream ss(line);Action a;int n;
        if(!(ss>>a.cost>>n))return 4;
        for(int i=0;i<n;i++){int m;if(!(ss>>m))return 5;a.masks.push_back(m);}
        actions.push_back(a);
    }
    if(actions.size()!=4)return 6;
    const int expected[12]={732,1678,2624,3570,4516,5462,
                            6408,7354,8300,9246,10192,11138};
    for(f=0;f<=11;f++){
        radix=f+2;cache.clear();array<int,6> start{};
        int actual=V(start);
        if(actual!=expected[f]){cerr<<"FAIL f="<<f<<" value="<<actual<<"\n";return 7;}
        cout<<"f="<<f<<" exact="<<actual<<" nonterminal_states="<<cache.size()<<"\n";
    }
    cout<<"PASS_R5_SEXTET_CPP_12_F_VALUES\n";
    return 0;
}
