// Exhaustive finite m=10 parity/sign-completion certificate for the R762HD/HE candidate.
// Conditional candidate, NOT native TRIADIC_CLOSURE_E admission or official review.
// Compile: c++ -O3 -std=c++17 driver_r762he_m10_sign_completion_20261120.cpp -o check && ./check
#include <array>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;

constexpr int M=10;
struct Edge {int to;int triple;};
array<vector<Edge>,15> edges;
bool reach[M+1][15][64]={};
int supports[M];
uint64_t checked=0, failures=0;
unordered_map<uint64_t,bool> memo;

uint32_t code(int s){
    uint32_t x=0;
    for(int a=0;a<6;a++) x+= ((s>>a)&1)<<(4*a);
    return x;
}
bool possible(){
    int s[M];copy(supports,supports+M,s);sort(s,s+M);
    uint64_t key=0;
    for(int i=0;i<M;i++) key=(key<<6)|s[i];
    auto it=memo.find(key);
    if(it!=memo.end())return it->second;
    uint32_t codes[M], total=0;
    for(int i=0;i<M;i++){codes[i]=code(s[i]);total+=codes[i];}
    uint32_t target=0;
    for(int a=0;a<6;a++) target|=(((total>>(4*a))&15)/2)<<(4*a);
    bool yes=false;
    // Full displacement zero entails exactly five positive and five negative
    // three-axis steps: summing all six coordinates gives 3*sum(sigma)=0.
    for(int mask=0;mask<(1<<M);mask++)
      if(__builtin_popcount((unsigned)mask)==M/2){
        uint32_t sum=0;
        for(int i=0;i<M;i++)if(mask&(1<<i))sum+=codes[i];
        if(sum==target){yes=true;break;}
      }
    memo.emplace(key,yes);
    return yes;
}
void walk(int depth,int p,int parity){
    if(depth==M){
        ++checked;
        if(!possible()){
            ++failures;
            if(failures==1){
              cerr<<"first missing sign completion: ";
              for(int i=0;i<M;i++)cerr<<supports[i]<<",";
              cerr<<"\n";
            }
        }
        return;
    }
    int remaining=M-depth;
    for(auto e:edges[p]){
      int q=parity^e.triple;
      if(reach[remaining-1][e.to][q]){
        supports[depth]=e.triple;
        walk(depth+1,e.to,q);
      }
    }
}
int main(){
    vector<pair<int,int>> ports;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)ports.emplace_back(a,b);
    for(int p=0;p<15;p++)for(int q=0;q<15;q++){
      int common=0;
      for(int a=0;a<6;a++)
        if((ports[p].first==a||ports[p].second==a) &&
           (ports[q].first==a||ports[q].second==a))++common;
      if(common==1){
        int s=(1<<ports[p].first)|(1<<ports[p].second)|
              (1<<ports[q].first)|(1<<ports[q].second);
        edges[p].push_back({q,s});
      }
    }
    // Complete finite-reachability DP for remaining suffix support XOR.
    reach[0][0][0]=true;
    for(int n=1;n<=M;n++)for(int p=0;p<15;p++)
      for(auto e:edges[p])for(int parity=0;parity<64;parity++)
        if(reach[n-1][e.to][parity])
          reach[n][p][parity^e.triple]=true;
    walk(0,0,0);
    cout<<"parity-pass length-10 Port-return histories: "<<checked<<"\n";
    cout<<"distinct triple-support multisets: "<<memo.size()<<"\n";
    cout<<"histories lacking zero-displacement sign completion: "<<failures<<"\n";
    assert(checked==7289184); // Independently established R762HE character count.
    assert(failures==0);
    cout<<"PASS: exact exhaustive candidate finite m=10 parity sufficiency\n";
}