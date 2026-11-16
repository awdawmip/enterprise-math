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
 ++nodes;
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

 struct Frame {M free;vector<M> punct;};
 vector<Frame> frames;ifstream ff(argv[3]);uint64_t lo,hi;int nr;
 while(ff>>lo>>hi>>nr){Frame fr{M(lo)|(M(hi)<<64),{}};for(int i=0;i<nr;i++){ff>>lo>>hi;fr.punct.push_back(M(lo)|(M(hi)<<64));}frames.push_back(move(fr));}
 int ix,val;while(cin>>ix>>val){
  vector<int> orig(n);for(int& x:orig)cin>>x;vector<int> ids,cnt;int per=-1,left=0;
  for(int j=0;j<n;j++)if(orig[j]){
   if(types[j].sz==13||types[j].sz==12&&types[j].price==1104)continue;
   if(types[j].sz==12&&types[j].price==1116){per=ids.size();if(--orig[j]==0)continue;}
   ids.push_back(j);cnt.push_back(orig[j]);left+=orig[j];
  }
  Pools pool;for(int i:ids)pool.push_back(types[i].all);
  bool found=false;nodes=0;
  for(auto& fr:frames){if(per>=0&&per<ids.size()&&types[ids[per]].price==1116)pool[per]=fr.punct;
   if(solve(fr.free,left,cnt,pool)){found=true;break;}}
  cout<<ix<<" "<<val<<" "<<nodes<<" "<<found<<endl;

 }
}
