#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
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
 int c;while(cin>>c){vector<int> orig(n);int labels=0;for(int&x:orig){cin>>x;labels+=x;}
  vector<int> ids,counts;int anchor=-1;for(int j=0;j<n;j++)if(orig[j]){ids.push_back(j);counts.push_back(orig[j]);if(anchor<0||make_pair(types[j].reps.size(),types[j].all.size())<make_pair(types[ids[anchor]].reps.size(),types[ids[anchor]].all.size()))anchor=ids.size()-1;}
  Pools pool;for(int id:ids)pool.push_back(types[id].all);--counts[anchor];nodes=0;bool found=false;
  for(M m:types[ids[anchor]].reps)if(solve(FULL^m,labels-1,counts,pool)){found=true;break;}
  cout<<c<<" "<<nodes<<" "<<found<<endl;
 }
}
