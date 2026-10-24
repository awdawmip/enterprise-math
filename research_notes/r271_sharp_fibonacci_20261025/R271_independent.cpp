// R271 independent exact no-00 reset count checker, C++17 + Boost.Multiprecision.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using Key = std::tuple<int,int,int,int>; // control, last-zero flag, sign, translation

int main() {
    std::map<Key,cpp_int> state;
    state[{0,0,1,0}]=1;
    for(int n=1;n<=160;++n){
        std::map<Key,cpp_int> next;
        for(const auto &kv:state){
            auto [q,r,e,k]=kv.first;
            for(int a=0;a<=1;++a){
                if(r==1 && a==0)continue;
                int qp,sgn,b;
                if(q==2){qp=(a==0?1:2);sgn=1;b=(a==0?1:-1);}
                else{qp=(q==0?2:0);sgn=(a==0?-1:1);b=-1;}
                int rp=(a==0?1:0);
                next[{qp,rp,sgn*e,sgn*k+b}]+=kv.second;
            }
        }
        state.swap(next);
        cpp_int total=0;
        for(const auto &kv:state){
            auto [q,r,e,k]=kv.first;
            assert(abs(k)<=n && (k-n)%2==0);
            total+=kv.second;
        }
        // F_{n+2} iterative independent recurrence
        cpp_int fn2=0,prev=0,curr=1;
        for(int t=0;t<n+2;++t){cpp_int tmp=prev+curr;prev=curr;curr=tmp;}
        fn2=prev;
        assert(total==fn2);
        if(n==30 || n==60 || n==80 || n==160){
            cpp_int mx=0, rsum=0;
            int me=0,mk=0;
            for(const auto &kv:state){
                auto [q,r,e,k]=kv.first;
                if(q==0 && r==0){
                    rsum+=kv.second;
                    if(kv.second >mx){mx=kv.second;me=e;mk=k;}
                }
            }
            if(n==30){assert(state.at({0,0,1,-4})==16482);assert(rsum==372099);}
            if(n==60)assert(mx==cpp_int("21010024205"));
            if(n==80)assert(mx==cpp_int("273055000503388"));
            if(n==160)assert(mx==cpp_int("9992479752177812645565616065526"));
            std::cout<<n<<" max_reset="<<mx<<" effect=("<<me<<","<<mk<<") reset_total="<<rsum<<"\n";
        }
    }
    std::cout<<"PASS independent_cpp17 no00 DP 0..160\n";
}
