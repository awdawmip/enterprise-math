// R252 independent C++17 author-side positive BRC DP; restricted SIX-axis affine family.
#include <map>
#include <tuple>
#include <cassert>
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
using U=uint64_t;
using Key=tuple<int,int,int>; // hidden control, orientation on axes 1&2, first-axis translation
using Dist=map<Key,U>;
struct Edge {int next,sign,shift;};
const vector<vector<Edge>> edges={
  {{2,-1,-1},{2,1,-1}},
  {{0,-1,-1},{0,1,-1}},
  {{1,1,1},{2,1,-1}}
};
Dist step(const Dist& old) {
  Dist out;
  for(const auto& [key,n]:old) {
    auto [q,s,v]=key;
    for(const auto& edge:edges.at(q))
      out[{edge.next,edge.sign*s,edge.sign*v+edge.shift}]+=n;
  }
  return out;
}
map<int,U> inverse_anchor(const Dist& cur) {
  map<int,U> h;
  for(const auto& [key,n]:cur) {
    auto [q,s,v]=key;
    h[-s*v]+=n;
  }
  return h;
}
map<pair<int,int>,U> full_effect(const Dist& cur) {
  map<pair<int,int>,U> h;
  for(const auto& [key,n]:cur) {
    auto [q,s,v]=key;
    h[{s,v}]+=n;
  }
  return h;
}
int main() {
  Dist cur[2] = {{{Key{0,1,0},1}},{{Key{1,1,0},1}}};
  for(int m=0;m<=30;++m) {
    const auto a=inverse_anchor(cur[0]), b=inverse_anchor(cur[1]);
    assert(a==b);
    U choose=1,total=0;
    for(int j=0;j<=m;++j) {
      assert(a.at(m-2*j)==choose);
      total+=choose;
      if(j<m) choose=choose*(m-j)/(j+1);
    }
    assert(total==(U(1)<<m));
    if(m<=2) assert(full_effect(cur[0])==full_effect(cur[1]));
    if(m==3) assert(full_effect(cur[0])!=full_effect(cur[1]));
    if(m<30) {cur[0]=step(cur[0]);cur[1]=step(cur[1]);}
  }
  cout<<"R252_CPP17_PASS depths_0_to_30 unit_positive_BRC binomial full_difference_at_3\n";
}
