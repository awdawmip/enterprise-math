#include <algorithm>
#include <array>
#include <bit>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <random>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;
constexpr M full=(M(1)<<126)-1, dummy=M(1)<<125;
int first(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
int card(M x){return popcount(W(x))+popcount(W(x>>64));}
struct Row{M m;int df;array<uint8_t,9> pts;};
vector<Row> bank;vector<Row> levels[15];long long nodes,limit;vector<M> sol;int dualLevel=0;
bool search(M f,M used,int k,int lo,int hi,int prevDanger,Row *avail,int count){
 ++nodes;if(nodes>limit)return false;
 if(k<=1){if(!k)return true;for(int i=0;i<count;i++)if(avail[i].m==f){sol.push_back(f);return true;}return false;}
 int danger=~(lo|hi)&32767,strict=k>=4?0:k==3?(lo&hi):hi;
 if(k==2&&(lo&hi))return false;
 int bans=danger&~prevDanger;
 M reach=0,twice=0;int seen=0,second=0;
 Row* next=levels[k].data();int n=0;
 for(int i=0;i<count;i++){
  const auto&r=avail[i];
  if((r.m&used)||(r.df&bans)||(strict&~r.df))continue;
  next[n++]=r;
  twice|=reach&r.m;reach|=r.m;
  second|=seen&r.df;seen|=r.df;
 }
 if(reach!=f||((lo|hi)&~seen)||(hi&~second))return false;
 if(k==2){for(int i=0;i<n;i++)for(int j=0;j<i;j++)if((next[i].m|next[j].m)==f){
      sol.push_back(next[i].m);sol.push_back(next[j].m);return true;}return false;}
 M p=f&~twice;int defect=(lo&~hi)&~second;
 int pivot=-1,dv=0;
 if(p)pivot=first(p);
 else if(defect)dv=defect&-defect;
 else{
  array<uint16_t,141> deg{};
  for(int i=0;i<n;i++){auto&r=next[i];for(auto x:r.pts)++deg[x];for(int z=r.df;z;z&=z-1)++deg[126+countr_zero((unsigned)z)];}
  int few=10000;
  for(M z=f;z;z&=z-1){int x=first(z);if(deg[x]<few){few=deg[x];pivot=x;}}
  for(int z=lo&~hi;z;z&=z-1){int x=countr_zero((unsigned)z);if(deg[126+x]<few){few=deg[126+x];dv=1<<x;pivot=-1;}}
  if(dualLevel&& k<=dualLevel){
   M rem=f, pick=0;
   // Any two points in pick cannot be covered by one remaining row.
   int times=0;
   while(rem){
    int c=first(rem);
    for(M z=rem;z;z&=z-1){int x=first(z);if(deg[x]<deg[c])c=x;}
    M b=M(1)<<c,ng=0;pick|=b;
    for(int i=0;i<n;i++){if(next[i].m&b)ng|=next[i].m;}
    rem&=~ng;
    if(++times>k)return false;
   }
   if(times==k){int h=0;for(int i=0;i<n;i++)if(next[i].m&pick)next[h++]=next[i];n=h;}
  }
 }
 M need=pivot>=0?M(1)<<pivot:0;
 for(int i=0;i<n;i++){
  const auto&r=next[i];
  if(!(r.m&need)&&!(r.df&dv))continue;
  sol.push_back(r.m);
  if(search(f^r.m,r.m,k-1,lo^r.df,hi^(r.df&~lo),danger,next,n))return true;
  sol.pop_back();if(nodes>=limit)return false;
 }
 return false;
}
int main(int argc,char**argv){
 string dir=argv[1];int shard=stoi(argv[2]),step=stoi(argv[3]),nk=stoi(argv[4]);limit=stoll(argv[5]);int seed=stoi(argv[6]);int only=argc>7?stoi(argv[7]):-1;dualLevel=argc>8?stoi(argv[8]):0;
 auto load=[&](string n){vector<M> v;ifstream f(dir+"/"+n);W a,b;while(f>>a>>b)v.push_back(M(b)<<64|a);return v;};
 array<M,15> p{};for(int i=0;i<125;i++){p[i/25]|=M(1)<<i;p[i/5%5+5]|=M(1)<<i;p[i%5+10]|=M(1)<<i;}
 auto keep=load("keep9");
 for(int s:{8,9})for(M m:load("full"+to_string(s))){
   Row r{m|(s==8?dummy:0)};int pos=0;for(M z=r.m;z;z&=z-1)r.pts[pos++]=first(z);
   for(int i=0;i<15;i++){int d=card(m&p[i]);if(d==1)r.df|=1<<i;else if(d!=2)abort();}
   bank.push_back(r);
 }
 if(seed){mt19937 g(seed);shuffle(bank.begin(),bank.end(),g);}
 for(auto&v:levels)v.resize(bank.size());
 int seq=0;
 for(int set=0;set<512;set++)if(popcount((unsigned)set)==nk){
  if(seq++%step!=shard||(only>=0&&set!=only))continue;
  M used=0;for(int i=0;i<9;i++)if(set>>i&1)used|=keep[i];int lo=0,hi=0;
  for(int i=0;i<15;i++){int d=2*(14-nk)-card((full^used)&p[i]);if(d<0||d>3)abort();lo|=(d&1)<<i;hi|=(d/2)<<i;}
  nodes=0;sol.clear();bool ok=search(full^used,used,14-nk,lo,hi,0,bank.data(),bank.size());
  cout<<set<<" "<<nodes<<" "<<(ok?1:nodes>=limit?-1:0);
  if(ok)for(auto m:sol){m&=~dummy;cout<<" "<<W(m)<<" "<<W(m>>64);}cout<<endl;
 }
}
