#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>
using Eff=std::pair<int,int>; // orientation epsilon, integer shift k
using Key=std::tuple<int,int,int>; // target control, epsilon, shift
using Dist=std::map<Key,std::int64_t>;
using Hist=std::map<Eff,std::int64_t>;
const std::array<std::array<std::pair<int,Eff>,2>,3> edges = {{{{
    {2,{-1,-1}}, {2,{1,-1}}
}},{{
    {0,{-1,-1}}, {0,{1,-1}}
}},{{
    {1,{1,1}}, {2,{1,-1}}
}}}};
Eff then(Eff f,Eff g){return {g.first*f.first,g.first*f.second+g.second};}
Dist advance(const Dist& h){
 Dist nxt;
 for(const auto& [key,num]:h){
  auto [s,eps,k]=key;
  for(const auto& [to,g]:edges[s]){
   auto v=then({eps,k},g);
   nxt[{to,v.first,v.second}]+=num;
  }
 }
 return nxt;
}
Hist obs(const Dist& h){
 Hist r;
 for(const auto& [key,num]:h){auto [s,eps,k]=key; r[{eps,k}]+=num;}
 return r;
}
int main(){
 std::array<Dist,2> states{{{{{0,1,0},1}},{{{1,1,0},1}}}};
 for(int depth=0;depth<=12;depth++){
  const Hist a=obs(states[0]),b=obs(states[1]);
  std::int64_t mass_a=0,mass_b=0;
  for(auto [x,n]:a)mass_a+=n;
  for(auto [x,n]:b)mass_b+=n;
  if(mass_a!=(1LL<<depth)||mass_b!=(1LL<<depth))return 1;
  if((depth<=2)&&(a!=b))return 2;
  if((depth==3)&&(a==b))return 3;
  if(depth==3){
   Hist diff=a;
   for(auto [key,num]:b)diff[key]-=num;
   if(diff[{-1,-1}]!=1 || diff[{1,-1}]!=1 || diff[{-1,1}]!=-1 || diff[{1,1}]!=-1)return 4;
   std::cout<<"depth3 four signed external histogram-difference atoms verified\n";
  }
  states[0]=advance(states[0]);states[1]=advance(states[1]);
 }
 std::cout<<"PASS positive six-axis affine subfamily, 2^k paths for both states, depths 0..12\n";
}
