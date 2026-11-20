#include <cstdint>
#include <algorithm>
#include <array>
#include <bit>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
using Mask=unsigned __int128;using U=uint64_t;using Obs=array<U,4>;
int bit(Mask a){return U(a)?countr_zero(U(a)):64+countr_zero(U(a>>64));}
int cardinal(Mask a){return popcount(U(a))+popcount(U(a>>64));}
Mask bad[125][125];Obs obs[125][125];int best;
int price(Mask a){
 int v=0;for(Mask m=a;m;m&=m-1){Obs o{};for(Mask n=a;n;n&=n-1)for(int j=0;j<4;j++)o[j]|=obs[bit(m)][bit(n)][j];for(auto w:o)v+=popcount(w);}return v;
}
struct Hash{size_t operator()(Mask m)const{return U(m)^(U(m>>64)*0x9e3779b97f4a7c15ULL);}};
struct Row{Mask m;int c,extra;};
array<vector<Row>,12> allowed;vector<int> trial,witness;
int offset[12];vector<Row> allRows;Mask original[12];int take,give;
long long nodes;
int lower_table[13][126];
void grow(Mask m,Mask candidates,Mask *forbid,int slots,unordered_set<Mask,Hash>& made){
 if(m)made.insert(m);
 if(!slots || cardinal(m)==13)return;
 for(Mask x=candidates;x;x&=x-1){int p=bit(x);
  Mask rest=x&(x-1)&~forbid[p],next[125];
  for(Mask t=rest;t;t&=t-1)next[bit(t)]=forbid[bit(t)]|bad[p][bit(t)];
  grow(m|(Mask(1)<<p),rest,next,slots-1,made);
 }
}
void shapes(int cls,Mask removed,Mask pool,int slots,unordered_set<Mask,Hash>& made){
 Mask keep=original[cls]^removed,forbid[125]{},block=0;
 for(Mask x=keep;x;x&=x-1)for(Mask y=x&(x-1);y;y&=y-1)block|=bad[bit(x)][bit(y)];
 Mask candidates=((Mask(1)<<125)-1)&~(block|original[cls]);
 for(Mask t=candidates;t;t&=t-1)for(Mask z=keep;z;z&=z-1)forbid[bit(t)]|=bad[bit(t)][bit(z)];
 grow(keep,candidates,forbid,give,made);
 if(!slots)return;
 for(Mask t=pool;t;t&=t-1)shapes(cls,removed|(Mask(1)<<bit(t)),t&(t-1),slots-1,made);
}
void solve(Mask free,int labels,int cost,int spare,array<vector<int>,12> const& poss){
 ++nodes;
 if(cost+lower_table[popcount((unsigned)labels)][cardinal(free)]>=best)return;
 if(!labels){if(!free && cost<best){best=cost;witness=trial;cerr<<"hit "<<best<<endl;}return;}
 array<vector<int>,12> next;
 int floor=cost,counts[125]{},low[12]{};
 vector<int>pool;int first=0,least=2000000;int countRows=0;
 for(int i=0;i<12;i++)if(labels&(1<<i)){
  int v=2000000;
  for(int j:poss[i]){auto&r=allRows[j];if(r.extra>spare || r.m&~free)continue;v=min(v,r.c);next[i].push_back(j);}
  if(v==2000000)return;floor+=v;low[i]=v;
 }
 if(floor>=best)return;
 for(int i=0;i<12;i++)if(labels&(1<<i)){
  auto &v=next[i];v.erase(remove_if(v.begin(),v.end(),[&](int j){return floor-low[i]+allRows[j].c>=best;}),v.end());
  if(v.empty())return;
  if(v.size()<least){least=v.size();first=~i;}
  for(int j:v)for(Mask x=allRows[j].m;x;x&=x-1)++counts[bit(x)];
 }
 for(Mask x=free;x;x&=x-1){int j=bit(x);if(!counts[j])return;if(counts[j]<least){least=counts[j];first=j;}}
 for(int i=0;i<12;i++)if((labels&(1<<i)) && (first>=0||i==~first)){
  for(int j:next[i]){auto&r=allRows[j];if(first>=0 && !(r.m&(Mask(1)<<first)))continue;trial.push_back(j);solve(free^r.m,labels^(1<<i),cost+r.c,spare-r.extra,next);trial.pop_back();}
 }
}
int main(int argc,char **argv){ifstream f(argv[1],ios::binary),classes(argv[2]);f.read((char*)obs,sizeof(obs));array<unsigned char,3> e;while(f.read((char*)e.data(),3)){do{bad[e[0]][e[1]]|=Mask(1)<<e[2];}while(next_permutation(e.begin(),e.end()));}
 take=stoi(argv[3]);give=stoi(argv[4]);best=stoi(argv[5])+1;array<vector<int>,12> poss;
 for(int i=0;i<12;i++){U lo,hi;classes>>lo>>hi;original[i]=Mask(hi)<<64|lo;unordered_set<Mask,Hash> made;shapes(i,0,original[i],take,made);
  for(auto m:made){poss[i].push_back(allRows.size());allRows.push_back({m,price(m),max(0,cardinal(original[i]&~m)-1)});}
  sort(poss[i].begin(),poss[i].end(),[&](int x,int y){return allRows[x].c<allRows[y].c;});
  cerr<<i<<" "<<made.size()<<endl;
 }
 const int m[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};for(int i=0;i<=12;i++)for(int n=0;n<=125;n++)lower_table[i][n]=999999;lower_table[0][0]=0;for(int i=1;i<=12;i++)for(int n=0;n<=125;n++)for(int j=1;j<=min(13,n);j++)lower_table[i][n]=min(lower_table[i][n],m[j]+lower_table[i-1][n-j]);
 solve((Mask(1)<<125)-1,(1<<12)-1,0,take-1,poss);cout<<best<<" "<<nodes<<endl;
 for(auto j:witness){auto m=allRows[j].m;for(;m;m&=m-1)cout<<bit(m)<<" ";cout<<endl;}
}
