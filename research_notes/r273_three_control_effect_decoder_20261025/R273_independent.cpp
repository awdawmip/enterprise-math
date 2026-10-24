// R273 independent exact verifier (C++17, Boost multiprecision).
// Formal positive two-selector BRC; not a native heartbeat X6 experiment.
#include <boost/multiprecision/cpp_int.hpp>
#include <cassert>
#include <iostream>
#include <map>
#include <array>
#include <tuple>
using boost::multiprecision::cpp_int;
using State=std::tuple<int,int,int,int>; // q,r,epsilon,k
using Fiber=std::tuple<int,int,int>;     // q,epsilon,k

struct Edge {int target,eta,bias;};
constexpr Edge E[3][2]={
  {{2,-1,-1},{2,+1,-1}},
  {{0,-1,-1},{0,+1,-1}},
  {{1,+1,+1},{2,+1,-1}}
};
constexpr int DELTA[3][2]={{1,0},{2,0},{2,2}};

static State step(State s,int a){
    auto [q,r,eps,k]=s;
    auto ed=E[q][a];
    return {ed.target,DELTA[r][a],ed.eta*eps,ed.eta*k+ed.bias};
}
static cpp_int fib(int n){
    cpp_int a=0,b=1;
    for(int i=0;i<n;i++){cpp_int t=a+b;a=b;b=t;}
    return a;
}
static cpp_int minint(const cpp_int &a,const cpp_int &b){return a<b?a:b;}

int main(){
    std::map<State,cpp_int> layer;
    layer[{0,0,1,0}]=1;
    for(int n=0;n<=96;n++){
        std::map<Fiber,std::array<cpp_int,2>> fibers;
        cpp_int total=0,avoiding=0,minority=0;
        for(auto& [state,w]:layer){
            auto [q,r,eps,k]=state;
            total+=w;
            if(r!=2)avoiding+=w;
            fibers[{q,eps,k}][r==2?1:0]+=w;
        }
        for(auto& [key,v]:fibers)
            minority+=minint(v[0],v[1]);
        assert(total==(cpp_int(1)<<n));
        assert(avoiding==fib(n+2));
        assert(minority<=avoiding);
        if(n<=2)assert(minority==0);
        if(n>=3)assert(minority>0);
        if(n==3)assert(minority==1);
        if(n==7)assert(minority==20);
        if(n==8)assert(minority==36);
        if(n==20)assert(minority==17416);
        if(n==30){
            assert(minority==2176446);
            assert(layer[State{0,0,1,-4}]==16482);
        }
        if(n==60)assert(minority==cpp_int("4052739183615"));
        if(n==80)assert(minority==cpp_int("61305790715800460"));
        if(n==96)
          std::cout<<"R273_CXX17_PASS depth_0_to_96\n"
                   <<"M_96="<<minority<<"\n"
                   <<"F_98="<<avoiding<<"\n";
        if(n<96){
            std::map<State,cpp_int> next;
            for(auto& [state,w]:layer)
                for(int a=0;a<2;a++)next[step(state,a)]+=w;
            layer.swap(next);
        }
    }
    std::cout<<"R273_RESET_30=16482\n";
    return 0;
}
