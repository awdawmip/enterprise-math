#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <tuple>
using boost::multiprecision::cpp_int;
using State=std::tuple<int,int,int,int>;
using Hist=std::map<State,cpp_int>;
int main(){
  Hist p; p[{0,0,1,0}]=1;
  const std::array<std::array<long long,6>,3> base={{{2,2,3,1,1,9},{1,6,1,9,2,16},{1,19,2,20,4,28}}};
  int E[3]={1,1,-1}, B[3]={-3,0,-1};
  for(int n=0;n<=80;n++){
    cpp_int total=0;for(const auto &[s,v]:p)total+=v;
    assert(total==(cpp_int(1)<<n));
    if(n>=7){
      int K=(n-7)/30,t=n-30*K,j=7+(t-7)%3,h=(t-j)/3;
      int e=E[j-7], k=B[j-7]-e*(4*K+h);
      std::array<cpp_int,6> c{};
      for(const auto &[s,v]:p){auto [q,r,ee,kk]=s;
        if(ee==e&&kk==k)c[2*q+(r==2)]+=v;
      }
      cpp_int z=1;for(int i=0;i<K;i++)z*=16482;
      for(int a=0;a<6;a++)assert(c[a]>=z*base[j-7][a]);
      if(n==j&&n<=9)for(int a=0;a<6;a++)assert(c[a]==base[n-7][a]);
    }
    if(n==30)assert((p[State{0,0,1,-4}]==16482));
    if(n==80)break;
    Hist next;
    for(const auto &[s,v]:p){
      auto [q,r,e,k]=s;
      int q1=(q==1?0:2),r1=(r==2?2:0);
      next[{q1,r1,e,k-1}]+=v;
      int q0=(q==2?1:(q==0?2:0)),eta=(q==2?1:-1),b=(q==2?1:-1);
      int r0=(r==0?1:2);
      next[{q0,r0,eta*e,eta*k+b}]+=v;
    }
    p.swap(next);
  }
  std::cout<<"PASS independent cpp_int n0..80, length30 reset 16482, all fiber bounds\n";
}
