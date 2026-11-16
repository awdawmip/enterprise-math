#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <bit>
#include <map>
#include <set>
#include <string>
#include <tuple>
using namespace std;
using M=__uint128_t;
const M FULL=(M(1)<<125)-1;
int pos(M b){return (uint64_t)b?__builtin_ctzll((uint64_t)b):64+__builtin_ctzll((uint64_t)(b>>64));}
struct Type{int sz,price;vector<M> all,reps;};
vector<Type> types;
using Pools=vector<vector<M>>;
uint64_t nodes;
M slices[15];
vector<array<int,15>> abs_lo,abs_hi;
bool solve(M free,int left,vector<int>&cnt,const Pools&pool){
 ++nodes;
 for(int e=0;e<15;++e){
   int lo=0,hi=0;
   for(int j=0;j<cnt.size();j++)if(cnt[j]) {lo+=cnt[j]*abs_lo[j][e];hi+=cnt[j]*abs_hi[j][e];}
   M m=free&slices[e];
   int v=popcount(uint64_t(m))+popcount(uint64_t(m>>64));
   if(v<lo||v>hi)return false;
 }
 int choice=-1,best=2147483647;vector<int> count(cnt.size());
 for(int j=0;j<cnt.size();j++)if(cnt[j]){
   int n=0;for(M m:pool[j])if((m&free)==m)++n;
   if(n<cnt[j])return false;
   if(n<best){best=n;choice=j;}count[j]=n;
 }
 if(left==1)return choice>=0&&count[choice];
 if(choice<0)return !free;
 Pools options(cnt.size());M united=0;
 for(int j=0;j<cnt.size();j++)if(cnt[j]){
  auto& dest=options[j];dest.reserve(count[j]);
  for(M m:pool[j])if((m&free)==m){dest.push_back(m);united|=m;}
 }
 if(united!=free)return false;
 int pivot=-1;
 if(best>10){
   array<int,125>freq{};for(int j=0;j<cnt.size();j++)if(cnt[j])for(M m:options[j])for(M q=m;q;q&=q-1)++freq[pos(q)];
   for(M q=free;q;q&=q-1)if(freq[pos(q)]<best){best=freq[pos(q)];pivot=pos(q);choice=-1;}
 }
 for(int j=0;j<cnt.size();j++)if(cnt[j]&&(choice<0||choice==j)){
   --cnt[j];
   auto all=std::move(options[j]);
   if(choice>=0&&cnt[j]){
     for(int i=0;i+cnt[j]<all.size();i++){
       options[j].assign(all.begin()+i+1,all.end());
       if(solve(free^all[i],left-1,cnt,options))return true;
     }
   }else{
     if(cnt[j])options[j]=all;
     for(M m:all)if((pivot<0||((m>>pivot)&1))&&solve(free^m,left-1,cnt,options))return true;
   }
   options[j]=std::move(all);++cnt[j];
 }
 return false;
}
int main(int argc,char**argv){
 ifstream db(argv[1]);int n;db>>n;types.resize(n);
 for(auto&t:types){int l;db>>t.sz>>t.price>>l;for(int k=0;k<l;++k){uint64_t a,b;int r;db>>a>>b>>r;M m=M(a)|(M(b)<<64);t.all.push_back(m);if(r)t.reps.push_back(m);}}

 map<pair<int,int>,vector<M>> spaces;
 for(int k=1;k<=6;k++){
  ifstream f(string(argv[2])+"/cores"+to_string(k)+".txt");
  uint64_t a,b;set<pair<int,M>> unique;
  while(f>>a>>b){vector<int> centers(k);for(int&i:centers)f>>i;
   for(int h=0;h<(1<<k);h++){
    M m=M(a)|(M(b)<<64);bool ok=true;
    for(int i=0;i<k;i++)if(h>>i&1){M bit=M(1)<<centers[i];if(!(bit&m)){ok=false;break;}m^=bit;}
    if(ok)unique.emplace(popcount((unsigned)h),m);
   }
  }
  for(auto [h,m]:unique)spaces[{k,h}].push_back(m);
 }
 for(int i=0;i<125;i++){M bit=M(1)<<i;slices[i/25]|=bit;slices[5+i/5%5]|=bit;slices[10+i%5]|=bit;}
 int val;while(cin>>val){
  vector<int> orig(n);for(int& x:orig)cin>>x;
  vector<int> ids,cnt;int k=0,h=0,left=0;
  for(int j=0;j<n;j++)if(orig[j]){
   if(types[j].sz==13||types[j].sz==12&&types[j].price==1104){k+=orig[j];if(types[j].sz==13)h+=orig[j];}
   else{ids.push_back(j);cnt.push_back(orig[j]);left+=orig[j];}
  }
  Pools pool;for(int i:ids)pool.push_back(types[i].all);
  abs_lo.resize(pool.size());abs_hi.resize(pool.size());
  for(int j=0;j<pool.size();j++){
   abs_lo[j].fill(13);abs_hi[j].fill(0);
   for(int e=0;e<15;e++)for(M s:pool[j]){
    M m=s&slices[e];int v=popcount(uint64_t(m))+popcount(uint64_t(m>>64));
    abs_lo[j][e]=min(abs_lo[j][e],v);abs_hi[j][e]=max(abs_hi[j][e],v);
   }
  }
  bool found=false;nodes=0;
  if(!k){int anchor=0;for(int j=1;j<ids.size();j++)if(make_pair(types[ids[j]].reps.size(),types[ids[j]].all.size())<make_pair(types[ids[anchor]].reps.size(),types[ids[anchor]].all.size()))anchor=j;
   --cnt[anchor];for(M m:types[ids[anchor]].reps)if(solve(FULL^m,left-1,cnt,pool)){found=true;break;}
  }else{for(M m:spaces[{k,h}])if(solve(m,left,cnt,pool)){found=true;break;}}
  cout<<val<<" "<<nodes<<" "<<found<<endl;
 }
}
