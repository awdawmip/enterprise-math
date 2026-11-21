#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;
struct Hash{size_t operator()(M m)const{return W(m)^(W(m>>64)*0x9e3779b97f4a7c15ULL);}};
int main(int argc,char**av){
  ifstream pf(av[1]),gf(av[2],ios::binary),sf(av[3]);array<M,250> parents;
  for(auto&m:parents){W l,h;pf>>l>>h;m=(M(h)<<64)|l;}
  array<vector<array<unsigned char,125>>,125> rotations;
  array<unsigned char,125> g;while(gf.read((char*)g.data(),125)){int j=find(g.begin(),g.end(),0)-g.begin();rotations[j].push_back(g);}
  array<int,14> cap{};istringstream in(av[5]);for(auto&v:cap)in>>v;
  array<unordered_set<M,Hash>,14> seen;array<int,14> orbits{};
  array<ofstream,14> out;for(int i=8;i<=12;i++)out[i].open(string(av[4])+to_string(i),ios::binary);
  int s,c,x[14];while(sf>>s>>c){
    M m=0;for(int i=0;i<s;i++){sf>>x[i];m|=M(1)<<x[i];}
    if(c>cap[s]||seen[s].contains(m)||any_of(parents.begin(),parents.end(),[&](M p){return !(m&~p);} ))continue;
    ++orbits[s];for(int j=0;j<s;j++)for(auto&g:rotations[x[j]]){
      M a=0;for(int i=0;i<s;i++)a|=M(1)<<g[x[i]];
      if(seen[s].insert(a).second){W w[]={W(a),W(a>>64),W(c)};out[s].write((char*)w,sizeof(w));}
    }
  }
  for(int i=8;i<=12;i++)cerr<<i<<" "<<orbits[i]<<" "<<seen[i].size()<<"\n";
}
