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
bool solve(M free,int left,vector<int>&cnt,const Pools&pool){
 ++nodes;if(left==1){for(int j=0;j<(int)cnt.size();j++)if(cnt[j])return find(pool[j].begin(),pool[j].end(),free)!=pool[j].end();return !free;}
 int smallest=1<<30,tchoice=-1,pivot=-1;
 Pools choices(cnt.size());array<int,125>freq{};M united=0;
 for(int j=0;j<cnt.size();j++)if(cnt[j]){
  auto &v=choices[j];for(M m:pool[j])if((m&free)==m){v.push_back(m);united|=m;}
  if(v.size()<cnt[j])return false;
  if(v.size()<smallest){smallest=v.size();tchoice=j;}
 }
 if(united!=free)return false;
 if(left>2){
  for(int j=0;j<cnt.size();j++)if(cnt[j])for(M m:choices[j])for(M q=m;q;q&=q-1)++freq[pos(q)];
  for(M q=free;q;q&=q-1){int i=pos(q);if(freq[i]<smallest){smallest=freq[i];pivot=i;tchoice=-1;}}
 }
 for(int j=0;j<cnt.size();j++)if(cnt[j]&&(tchoice<0||tchoice==j)){
  --cnt[j];auto &v=choices[j];
  if(tchoice>=0&&cnt[j]){
    auto all=move(v);for(int i=0;i<=int(all.size())-cnt[j]-1;++i){
       v.assign(all.begin()+i+1,all.end());if(solve(free^all[i],left-1,cnt,choices))return true;
    }v=move(all);
  }else{
    for(M m:v)if((pivot<0||((m>>pivot)&1))&&solve(free^m,left-1,cnt,choices))return true;
  }
  ++cnt[j];
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
 int val;while(cin>>val){
  vector<int> orig(n);for(int& x:orig)cin>>x;
  vector<int> ids,cnt;int k=0,h=0,left=0;
  for(int j=0;j<n;j++)if(orig[j]){
   if(types[j].sz==13||types[j].sz==12&&types[j].price==1104){k+=orig[j];if(types[j].sz==13)h+=orig[j];}
   else{ids.push_back(j);cnt.push_back(orig[j]);left+=orig[j];}
  }
  Pools pool;for(int i:ids)pool.push_back(types[i].all);
  bool found=false;nodes=0;
  if(!k){int anchor=0;for(int j=1;j<ids.size();j++)if(make_pair(types[ids[j]].reps.size(),types[ids[j]].all.size())<make_pair(types[ids[anchor]].reps.size(),types[ids[anchor]].all.size()))anchor=j;
   --cnt[anchor];for(M m:types[ids[anchor]].reps)if(solve(FULL^m,left-1,cnt,pool)){found=true;break;}
  }else{for(M m:spaces[{k,h}])if(solve(m,left,cnt,pool)){found=true;break;}}
  cout<<val<<" "<<nodes<<" "<<found<<endl;
 }
}
