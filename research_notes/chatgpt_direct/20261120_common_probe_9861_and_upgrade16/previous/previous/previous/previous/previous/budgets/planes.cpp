// Complete residual cover search for the two 8714 budgets and their nearby variants.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using M=__uint128_t;
using U=std::uint64_t;
using std::vector;
int bit(M a){return U(a)?__builtin_ctzll(U(a)):64+__builtin_ctzll(U(a>>64));}
int pop(M a){return __builtin_popcountll(U(a))+__builtin_popcountll(U(a>>64));}
struct Row{M m;int t;std::array<int,15>d;};
std::array<M,15>slices{};
vector<int> cost,quota,chosen;
vector<Row> rows;
U nodes=0;
bool search(M free,int k,const vector<int>&pool){
 ++nodes;if(!free)return k==0;
 int balanced9=0,extra=0;
 for(int t=0;t<int(cost.size());t++){
   if(cost[t]==557||cost[t]==564)balanced9+=quota[t];
   else if(cost[t]!=744)extra+=quota[t];
 }
 int demand[15],donors[15]={},freq[125]={};
 for(int j=0;j<15;j++){
   demand[j]=2*k-pop(slices[j]&free);
   if(!extra&&(demand[j]<0||demand[j]>balanced9))return false;
 }
 vector<int>live;live.reserve(pool.size());
 vector<int>freqT(cost.size());M covered=0;
 for(int i:pool){
   auto&r=rows[i];if(!quota[r.t]||(r.m&free)!=r.m)continue;
   if(!extra&&cost[r.t]!=744){
      bool ok=true;for(int j=0;j<15;j++)if(demand[j]<r.d[j]||demand[j]-r.d[j]>balanced9-1){ok=false;break;}
      if(!ok)continue;
   }
   live.push_back(i);covered|=r.m;freqT[r.t]++;
 }
 if(covered!=free)return false;
 for(int i:live){
    auto&r=rows[i];for(M b=r.m;b;b&=b-1)freq[bit(b)]++;
    if(!extra&&cost[r.t]!=744)for(int j=0;j<15;j++)donors[j]+=r.d[j];
 }
 int best=1000000,goal=-1;
 for(M b=free;b;b&=b-1){int j=bit(b);if(freq[j]<best){best=freq[j];goal=j;}}
 for(int j=0;j<15&&!extra;j++){
   if(donors[j]<demand[j])return false;
   if(demand[j]==1&&donors[j]<best){best=donors[j];goal=125+j;}
 }
 for(int t=0;t<int(cost.size());t++){
   if(freqT[t]<quota[t])return false;
   if(quota[t]==1 && freqT[t]<best){best=freqT[t];goal=140+t;}
 }
 for(int i:live){
    auto&r=rows[i];if(goal<125&&!(r.m&(M(1)<<goal)))continue;
    if(goal>=125&&goal<140&&!r.d[goal-125])continue;
    if(goal>=140&&r.t!=goal-140)continue;
    quota[r.t]--;chosen.push_back(i);
    if(search(free^r.m,k-1,live))return true;
    chosen.pop_back();quota[r.t]++;
 }
 return false;
}
int main(int argc,char**argv){
 std::string base=argv[1];int job=std::stoi(argv[3]);
 for(int i=0;i<125;i++){int v[3]={i/25,i/5%5,i%5};for(int j=0;j<3;j++)slices[j*5+v[j]]|=M(1)<<i;}
 std::ifstream f(base+"/bank"),jobs(base+"/"+argv[2]);int nt;f>>nt;cost.resize(nt);quota.resize(nt);
 int id,price;U a,b,c,d;
 for(int i=0;i<=job;i++){if(!(jobs>>id>>price>>a>>b>>c>>d))return 2;for(auto&v:quota)jobs>>v;}
 M first=(M(b)<<64)|a,second=(M(d)<<64)|c,free=((M(1)<<125)-1)^first^second;
 vector<int>pool;
 for(int t=0;t<nt;t++){int size,n;f>>size>>cost[t]>>n;while(n--){U lo,hi;f>>lo>>hi;M m=(M(hi)<<64)|lo;
  if(quota[t]&&(m&free)==m){Row r{m,t,{}};for(int j=0;j<15;j++)r.d[j]=2-pop(m&slices[j]);pool.push_back(rows.size());rows.push_back(r);}}}
 bool ok=search(free,11,pool);std::cout<<job<<" "<<id<<" "<<price<<" "<<nodes<<" "<<ok<<std::endl;
 if(ok){auto print=[](M m){for(;m;m&=m-1)std::cerr<<bit(m)<<" ";std::cerr<<"\n";};print(first);print(second);for(int i:chosen)print(rows[i].m);}
}
