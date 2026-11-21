#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
using M=__uint128_t;using U=uint64_t;using S=uint64_t;
int idx(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}
int pop(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
using W=array<U,4>;
M bad[125][125];W obs[125][125];int g[125],period,norbits,labelcount;
struct Rec{int cost;M seed;};
struct Part{S support;int length;Rec d;};
map<S,Rec> best[13];vector<int> cycles[64];vector<M> choices[64];vector<int> loc;
int kmax=13,ar=0;long long seednodes[13]={};
M banned(M orig,M add,M prev){
 for(M a=add;a;a&=a-1){int p=idx(a);if(prev&(M(1)<<p))return ~M(0);for(M b=orig;b;b&=b-1)prev|=bad[p][idx(b)];orig|=M(1)<<p;}
 return prev;
}
int price(M m){
 int cost=0;for(M a=m;a;a&=a-1){W w{};int p=idx(a);for(M b=m;b;b&=b-1){auto &o=obs[p][idx(b)];for(int j=0;j<4;j++)w[j]|=o[j];}for(U v:w)cost+=__builtin_popcountll(v);}
 return cost;
}
void gen(int i,int r,M row,M illegal,S support){
 ++seednodes[r];
 if(row){
  int p=price(row)*r;auto z=best[r].find(support);
  if(z==best[r].end()||p<z->second.cost)best[r][support]={p,row};
 }
 for(int j=i;j<loc.size();j++){
  int t=loc[j];const int nm=cycles[t].size()/r;if(pop(row)+nm>kmax)continue;
  for(M m:choices[t]){if(m&illegal)continue;M f=banned(row,m,illegal);if(f!=~M(0))gen(j+1,r,row|m,f,support|(S(1)<<t));if(!row)break;}
 }
}
void init(int r){
 loc.clear();for(int t=0;t<norbits;t++){
  choices[t].clear();auto& cyc=cycles[t];if(cyc.size()%r)continue;
  for(int j=0;j<r;j++){M m=0;for(int z=j;z<cyc.size();z+=r)m|=M(1)<<cyc[z];choices[t].push_back(m);}
  loc.push_back(t);
 }
}
int main(int argc,char**argv){
 ifstream f(argv[1],ios::binary);f.read((char*)obs,sizeof(obs));array<unsigned char,3> e;while(f.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream perm(argv[2]);perm>>period;for(int&i:g)perm>>i;labelcount=stoi(argv[3]); array<bool,125>seen{};for(int p=0;p<125;p++)if(!seen[p]){int q=p;do{cycles[norbits].push_back(q);seen[q]=true;q=g[q];}while(q!=p);++norbits;}
 if(norbits>63)return 2;
 for(int r=1;r<4;r++)if(period%r==0){init(r);gen(0,r,0,0,0);cerr<<"bank "<<r<<" "<<best[r].size()<<" "<<seednodes[r]<<endl;}
 for(int r=1;r<4;r++)for(auto& v:best[r])cout<<r<<" "<<v.first<<" "<<v.second.cost<<" "<<U(v.second.seed)<<" "<<U(v.second.seed>>64)<<"\n";
}
