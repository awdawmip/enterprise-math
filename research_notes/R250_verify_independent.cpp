// R250 independent C++17 exact positive-BRC direct path propagation; no Python dependency.
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
using G=std::pair<int,int>;
using Edge=std::pair<int,G>;
using Front=std::map<std::tuple<int,int,int>,std::int64_t>;
using Hist=std::map<G,std::int64_t>;
G then(G a,G b){return {a.first*b.first,b.first*a.second+b.second};}
const std::array<std::array<Edge,2>,3> edges{{
  {{{2,{-1,-1}}, {2,{1,-1}}}},
  {{{0,{-1,-1}}, {0,{1,-1}}}},
  {{{1,{1,1}},   {2,{1,-1}}}}
}};
Hist evolve(int s,int depth){
 Front f; f[{s,1,0}]=1;
 for(int k=0;k<depth;k++){
    Front next;
    for(const auto &it:f){
        auto [q,sign,shift]=it.first;
        for(auto [t,e]:edges.at(q)){
            G g=then({sign,shift},e);
            next[{t,g.first,g.second}]+=it.second;
        }
    }
    f=std::move(next);
 }
 Hist out;
 for(const auto &it:f){auto [q,sign,shift]=it.first;out[{sign,shift}]+=it.second;}
 return out;
}
int main(){
  const bool same[4]={true,true,true,false};
  for(int d=0;d<=8;d++){
    auto a=evolve(0,d),b=evolve(1,d);
    if(d<4 && (a==b)!=same[d]) return 1;
    std::int64_t sumA=0,sumB=0;
    for(auto const &x:a)sumA+=x.second;
    for(auto const &x:b)sumB+=x.second;
    if(sumA!=(1LL<<d)||sumB!=(1LL<<d)) return 2;
  }
  if(evolve(0,3).count({1,1}) || evolve(1,3).at({1,1})!=1) return 3;
  std::cout<<"PASS: independent exact C++17 path DP, first distinguish at depth=3\n";
}
