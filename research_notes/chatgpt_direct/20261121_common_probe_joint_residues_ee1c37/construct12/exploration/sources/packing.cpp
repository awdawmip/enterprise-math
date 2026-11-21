// Whole-legal-class tabu search. It preserves class legality at every step;
// only disjointness is relaxed. This is a witness search, never an exclusion.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>
using namespace std;
using U=uint64_t;using M=__uint128_t;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
int pop(M x){return __builtin_popcountll(U(x))+__builtin_popcountll(U(x>>64));}
struct Rec{U lo,hi;unsigned c,s;};
struct C{M m;int c,s;long long tabu=0;};
int main(int argc,char**argv){
 if(argc<6)return 2;
 ifstream f(argv[1],ios::binary);Rec r;vector<C> bank;vector<int> anchors;
 int mode=atoi(argv[2]),orb=atoi(argv[3]);long long steps=atoll(argv[4]);mt19937_64 rng(strtoull(argv[5],0,10));
 while(f.read((char*)&r,sizeof(r))){int s=r.s%256;if((s==10&&(mode?r.c<=772:r.c==744))||(s==11&&(mode?r.c<=960:r.c==936))){
  if(s==11&&r.c==936&&r.s>=256)anchors.push_back(bank.size());bank.push_back({M(r.lo)|(M(r.hi)<<64),int(r.c),s,0});
 }}
 assert(anchors.size()==2);auto fixed=bank[anchors.at(orb)];M region=((M(1)<<125)-1)^fixed.m;
 vector<C> rows;vector<int> types[14];for(auto c:bank)if(!(c.m&fixed.m)){types[c.s].push_back(rows.size());rows.push_back(c);}
 cerr<<"candidates "<<rows.size()<<" anchor_cost "<<fixed.c<<"\n";
 int sizes[11]={10,10,10,10,10,10,10,11,11,11,11};
 vector<int> state(11),beststate;int cnt[125]{},cost=0,energy=0,best=1000;
 auto add=[&](int j,int dir){cost+=dir*rows[j].c;for(M m=rows[j].m;m;m&=m-1){int p=at(m);if(dir==1){energy+=cnt[p];cnt[p]++;}else{cnt[p]--;energy-=cnt[p];}}};
 auto output=[&](long long step,bool found){cout<<"{\"step\":"<<step<<",\"mode\":"<<mode<<",\"orbit\":"<<orb<<",\"energy\":"<<energy<<",\"cost\":"<<cost+fixed.c<<",\"found\":"<<(found?"true":"false")<<",\"groups\":[";
  vector<M> ms{fixed.m};for(int j:state)ms.push_back(rows[j].m);
  for(int j=0;j<(int)ms.size();j++){if(j)cout<<',';cout<<'[';bool b=false;for(M m=ms[j];m;m&=m-1){if(b)cout<<',';b=true;cout<<at(m);}cout<<']';}cout<<"]}"<<endl;
 };
 // Start from cheapest classes. Global cost remains at most 9,995 throughout.
 for(int i=0;i<11;i++){auto&opts=types[sizes[i]];int j;do{j=opts[rng()%opts.size()];}while(rows[j].c!=(sizes[i]==10?744:936));state[i]=j;add(j,1);}
 int last=-1;
 for(long long step=0;step<steps;step++){
  if(energy<best){best=energy;beststate=state;output(step,energy==0);if(!energy)return 0;}
  // Inspect a whole-class neighborhood; tabu tenure changes to avoid short cycles.
  int which=rng()%11; if(which==last)which=(which+1+rng()%10)%11;last=which;
  int old=state[which];add(old,-1);
  M plane[12]{};int maxcount=0;
  for(int p=0;p<125;p++)for(int q=0;q<cnt[p];q++){plane[q]|=M(1)<<p;maxcount=max(maxcount,q+1);}
  int localbest=10000,pick=-1,ties=0;int cap=9995-fixed.c-cost;
  for(int j:types[sizes[which]]){
   auto&c=rows[j];if(j==old||c.c>cap)continue;
   int e=0;for(int q=0;q<maxcount;q++)e+=pop(c.m&plane[q]);
   if(c.tabu>step&&energy+e>=best)continue;
   if(e<localbest){localbest=e;pick=j;ties=1;}else if(e==localbest&&rng()%++ties==0)pick=j;
  }
  if(pick<0){state[which]=old;add(old,1);continue;}
  rows[old].tabu=step+7+rng()%11;state[which]=pick;add(pick,1);
  // Periodic multi-class kicks preserve the size profile and exact budget.
  if(step%20000==19999){
   for(int a=0;a<4;a++){int i=rng()%11;int before=state[i];add(before,-1);auto&opts=types[sizes[i]];int j;do{j=opts[rng()%opts.size()];}while(rows[j].c!=(sizes[i]==10?744:936));state[i]=j;add(j,1);}
  }
 }
 cerr<<"finished steps "<<steps<<" best_energy "<<best<<"; no exclusion claim\n";
}
