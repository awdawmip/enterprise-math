// Guided whole-class packing in a selected complete affine candidate family.
// All chosen classes remain legal. Temporary point overlaps are allowed.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
int pop(M x){return __builtin_popcountll(U(x))+__builtin_popcountll(U(x>>64));}
struct Rec{U lo,hi;unsigned c,s;};struct C{M m;int c,s;long long tabu=0;};
int main(int argc,char**argv){
 if(argc!=5)return 2;
 ifstream f(argv[1],ios::binary),init(argv[2]);long long steps=atoll(argv[3]);mt19937_64 rng(strtoull(argv[4],0,10));
 vector<C> rows,known;Rec r;while(f.read((char*)&r,sizeof(r)))rows.push_back({M(r.lo)|(M(r.hi)<<64),int(r.c),int(r.s%256),0});
 int s,c;while(init>>s>>c){M m=0;for(int i=0,p;i<s;i++){init>>p;m|=M(1)<<p;}known.push_back({m,c,s,0});}assert(known.size()==12);
 M forbidden=known[0].m|known[1].m;assert(!(known[0].m&known[1].m));int fixedcost=known[0].c+known[1].c;
 vector<int> state;for(int a=2;a<12;a++){int j=0;for(;j<(int)rows.size();j++)if(rows[j].m==known[a].m)break;if(j==(int)rows.size())rows.push_back(known[a]);else assert(rows[j].c==known[a].c);state.push_back(j);}
 vector<int> types[14];for(int j=0;j<(int)rows.size();j++){assert(!(rows[j].m&forbidden));types[rows[j].s].push_back(j);}
 cerr<<"classes "<<rows.size()<<" nine "<<types[9].size()<<" ten "<<types[10].size()<<"\n";
 int cnt[125]{},penalty[125];fill(penalty,penalty+125,1);int cost=0,energy=0,best=1000;
 auto add=[&](int j,int dir){cost+=dir*rows[j].c;for(M m=rows[j].m;m;m&=m-1){int p=at(m);if(dir>0){energy+=cnt[p];cnt[p]++;}else{cnt[p]--;energy-=cnt[p];}}};
 for(int j:state)add(j,1);
 auto output=[&](long long step,bool found){cout<<"{\"step\":"<<step<<",\"energy\":"<<energy<<",\"cost\":"<<cost+fixedcost<<",\"found\":"<<(found?"true":"false")<<",\"groups\":[";
  vector<M> ms{known[0].m,known[1].m};for(int j:state)ms.push_back(rows[j].m);for(int i=0;i<(int)ms.size();i++){if(i)cout<<',';cout<<'[';bool first=true;for(M m=ms[i];m;m&=m-1){if(!first)cout<<',';first=false;cout<<at(m);}cout<<']';}cout<<"]}"<<endl;
 };
 int last=-1;long long lastbest=0;
 for(long long step=0;step<steps;step++){
  if(cost+fixedcost<=9995&&energy<best){best=energy;lastbest=step;output(step,!energy);if(!energy)return 0;}
  int which=rng()%10;
  if(energy&&rng()%5){int total=0,pick=0;for(int i=0;i<10;i++){int a=0;for(M m=rows[state[i]].m;m;m&=m-1)a+=cnt[at(m)]-1;total+=a;if(total&&rng()%total<unsigned(a))pick=i;}which=pick;}
  if(which==last)which=(which+1+rng()%9)%10;last=which;int old=state[which],sz=rows[old].s;add(old,-1);
  M planes[16]{};int width=0;for(int p=0;p<125;p++){int value=cnt[p]*penalty[p];for(int q=0;value;q++,value>>=1){if(value&1)planes[q]|=M(1)<<p;width=max(width,q+1);}}
  int localbest=100000,pick=-1,ties=0,cap=9995-fixedcost-cost;
  for(int j:types[sz]){auto&a=rows[j];if(j==old||a.c>cap||a.tabu>step)continue;int value=0;for(int q=0;q<width;q++)value+=(1<<q)*pop(a.m&planes[q]);if(value<localbest){localbest=value;pick=j;ties=1;}else if(value==localbest&&rng()%++ties==0)pick=j;}
  if(pick<0){state[which]=old;add(old,1);continue;}rows[old].tabu=step+5+rng()%10;state[which]=pick;add(pick,1);
  if(step%100==99&&step-lastbest>=100){int peak=0;for(int p=0;p<125;p++){if(cnt[p]>=2)penalty[p]++;peak=max(peak,penalty[p]);}if(peak>=32)for(int&p:penalty)p=(p+1)/2;}
  if(step%10000==9999){for(int z=0;z<3;z++){int i=rng()%10,old=state[i],sz=rows[old].s;add(old,-1);int j;auto&opts=types[sz];do{j=opts[rng()%opts.size()];}while(rows[j].c>(sz==9?557:744));state[i]=j;add(j,1);}fill(penalty,penalty+125,1);}
 }
 cerr<<"finished "<<steps<<" best_energy "<<best<<"; no exclusion claim\n";
}
