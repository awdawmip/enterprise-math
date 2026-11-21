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
#include "marginals.hpp"
#include "exact_margins.hpp"
bool solve(M free,int left,vector<int>&cnt,const Pools&pool){
 ++nodes;if(!exact_margins(free,cnt))return false;
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
   --cnt[j];for(int q=0;q<125;q++)bound_at[left-1][q]=bound_at[left][q]-level_bound[0][j][q];
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
long long geometric_nodes,leaf_nodes;
bool add_big(M free,int left,int punct,int start,vector<int>&cnt,const Pools&pool,const vector<M>&large){
 ++geometric_nodes;
 if(!exact_margins(free,cnt))return false;
 if(punct<0||cnt[punct]==0){++leaf_nodes;return solve(free,left,cnt,pool);}
 int num=cnt[punct]--;for(int j=start;j+num<=large.size();j++){M m=large[j];if(m&~free)continue;
 if(add_big(free^m,left-1,punct,j+1,cnt,pool,large))return true;}
 ++cnt[punct];return false;
}
int main(int argc,char**argv){
 ifstream db(argv[1],ios::binary);struct BR{uint64_t lo,hi;unsigned c,s;};BR rr;map<pair<int,int>,Type> all_types;
 while(db.read((char*)&rr,sizeof(rr))){int size=rr.s&255;auto& t=all_types[{size,rr.c}];t.sz=size;t.price=rr.c;M m=M(rr.lo)|(M(rr.hi)<<64);t.all.push_back(m);if(rr.s>=256)t.reps.push_back(m);}
 for(auto& [k,t]:all_types)types.push_back(move(t));int n=types.size();
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
 prepare_bounds();init_shapes();multi_id[{}]=0;multis.push_back({});reachable.push_back({0});
 struct Frame{M f; vector<M>rows;};
 map<tuple<int,int,int>,vector<Frame>> prec;
 auto frames=[&](int k,int h,int a)->const vector<Frame>&{
  auto key=make_tuple(k,h,a);if(prec.count(key))return prec[key];
  string nm=string(argv[3])+"/"+(a==2?"pair":"anchored")+to_string(k)+"_"+to_string(h);
  ifstream ds(nm);uint64_t lo,hi;int n;if(!ds)throw runtime_error(nm);
  auto &frames=prec[key];while(ds>>lo>>hi>>n){Frame r{M(lo)|(M(hi)<<64),{}};for(int j=0;j<n;j++){ds>>lo>>hi;r.rows.push_back(M(lo)|(M(hi)<<64));}
  frames.push_back(move(r));}return frames;};
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
  actual_ids=ids;table.clear();bound_at[left].fill(0);level_bound[0].clear();
  for(int j=0;j<ids.size();j++){level_bound[0].push_back(shape_max[ids[j]]);for(int t=0;t<125;t++)bound_at[left][t]+=cnt[j]*shape_max[ids[j]][t];}
  bool found=false;nodes=0;
  int punct=-1;for(int j=0;j<ids.size();j++)if(types[ids[j]].sz==12&&types[ids[j]].price==1116)punct=j;
  geometric_nodes=leaf_nodes=0;
  int count_p=punct<0?0:cnt[punct],pre=min(count_p,k<=1?2:1);
  if(pre){
   auto &sub=frames(k,h,pre);cnt[punct]-=pre;
   for(const auto&r:sub)if(add_big(r.f,left-pre,punct,0,cnt,pool,r.rows)){found=true;break;}
  }else if(k){for(M f:spaces[{k,h}])if(add_big(f,left,punct,0,cnt,pool,{})){found=true;break;}}
  else{int a=0;for(int j=1;j<ids.size();j++)if(types[ids[j]].all.size()<types[ids[a]].all.size())a=j;
   --cnt[a];for(M m:types[ids[a]].reps)if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){found=true;break;}
  }
  cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<endl;
 }
}
