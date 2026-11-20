#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <array>
#include <map>
#include <vector>
using namespace std;using Q=uint64_t;using M=__uint128_t;
int bit(M a){return Q(a)?__builtin_ctzll(Q(a)):64+__builtin_ctzll(Q(a>>64));}
const M FULL=(M(1)<<125)-1;
struct Row{M m; int s,c;};vector<Row>db,bank;using V=vector<Q>;
vector<V>touch,excludeT,ct;vector<M>selected;vector<int>quota,type_ids;uint64_t nodes;
bool dfs(M free,const V &pool,int remain){
 ++nodes;if(!remain)return !free;
 int best=1<<25,choice=-1,n=pool.size();
 for(M xs=free;xs;xs&=xs-1){
  int j=bit(xs),v=0;auto&r=touch[j];for(int h=0;h<n&&v<best;h++)v+=__builtin_popcountll(pool[h]&r[h]);
  if(!v)return false;if(v<best){best=v;choice=j;}
 }
 auto &opts=touch[choice];for(int h=0;h<n;h++)for(Q x=pool[h]&opts[h];x;x&=x-1){
  int i=64*h+__builtin_ctzll(x),k=type_ids[i];V next(n);--quota[k];auto&ban=excludeT[i];auto &color=ct[k];
  if(!quota[k])for(int j=0;j<n;j++)next[j]=pool[j]&~(ban[j]|color[j]);
  else for(int j=0;j<n;j++)next[j]=pool[j]&~ban[j];
  selected.push_back(bank[i].m);if(dfs(free^bank[i].m,next,remain-1))return true;selected.pop_back();++quota[k];
 }
 return false;
}
bool run(M used,map<int,int>counts){
 bank.clear();quota.clear();type_ids.clear();int left=0;
 for(auto [c,num]:counts)if(num>0){int id=quota.size();quota.push_back(num);left+=num;
  for(auto r:db)if(r.c==c&&!(r.m&used)){bank.push_back(r);type_ids.push_back(id);}}
 int n=bank.size(),w=(n+63)/64;
 touch.assign(125,V(w));excludeT.assign(n,V(w));ct.assign(quota.size(),V(w));V pool(w);
 for(int i=0;i<n;i++){Q v=Q(1)<<(i%64);pool[i/64]|=v;ct[type_ids[i]][i/64]|=v;for(M x=bank[i].m;x;x&=x-1)touch[bit(x)][i/64]|=v;}
 for(int i=0;i<n;i++)for(M x=bank[i].m;x;x&=x-1){auto&t=touch[bit(x)];for(int j=0;j<w;j++)excludeT[i][j]|=t[j];}
 return dfs(FULL^used,pool,left);
}
int main(int argc,char**argv){
 ifstream data(argv[1]),jobs(argv[2]);int s,c,n,f;Q lo,hi;
 while(data>>s>>c>>n)while(n--){data>>lo>>hi>>f;db.push_back({(M(hi)<<64)|lo,s,c});}
 int profile,nfixed,nt,ix=0;
 while(jobs>>profile>>nfixed>>nt){
  selected.clear();M used=0;for(int k=0;k<nfixed;k++){jobs>>lo>>hi;M m=(M(hi)<<64)|lo;selected.push_back(m);used|=m;}
  map<int,int>count;for(int k=0;k<nt;k++){int n;jobs>>c>>n;count[c]=n;}
  nodes=0;bool ok=run(used,count);
  cout<<ix++<<" "<<profile<<" "<<nfixed<<" "<<bank.size()<<" "<<nodes<<" "<<ok<<endl;
  if(ok){ofstream w("win_anchored.txt");for(M a:selected){for(;a;a&=a-1)w<<bit(a)<<" ";w<<"\n";}return 0;}
 }
}
