// Independent exact Bellman calculation for W from W_ENDPOINT_FAMILIES.txt.
// The family list must be independently checked against the frozen integer centers.
#include <bits/stdc++.h>
using namespace std;
constexpr int K=12,F=8;
struct Act {int price;vector<int> masks;};
struct DP {
 array<uint64_t,K> p;unordered_map<uint64_t,int> cache;
 DP(){p[0]=1;for(int i=1;i<K;i++)p[i]=p[i-1]*(F+2);}
 int solve(uint64_t code,const vector<Act>&actions){
  auto it=cache.find(code);if(it!=cache.end())return it->second;
  uint64_t t=code;array<int,K>e{};int live=0;
  for(int i=0;i<K;i++){e[i]=t%(F+2);t/=F+2;if(e[i]<=F)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  int best=INT_MAX/8;
  for(const auto&a:actions){
   if(any_of(a.masks.begin(),a.masks.end(),
     [&](int mask){return (mask&live)==live;}))continue;
   int worst=0;
   for(int mask:a.masks){
    uint64_t next=code;
    for(int j=0;j<K;j++)if(e[j]<=F && !(mask&(1<<j)))next+=p[j];
    worst=max(worst,solve(next,actions));
    if(a.price+worst>=best)break;
   }
   best=min(best,a.price+worst);
  }
  if(best>=INT_MAX/8)throw runtime_error("NO_PROGRESS");
  cache.emplace(code,best);
  return best;
 }
};
int main(){
 ifstream in("W_ENDPOINT_FAMILIES.txt");string line;vector<Act>a;
 while(getline(in,line)){
  if(line.empty()||line[0]=='#')continue;
  istringstream ss(line);Act x;int count,mask;
  if(!(ss>>x.price>>count))throw runtime_error("bad family");
  while(count--){if(!(ss>>mask))throw runtime_error("truncated");x.masks.push_back(mask);}
  a.push_back(move(x));
 }
 if(a.size()!=7)throw runtime_error("wrong family count");
 DP dp;int v=dp.solve(0,a);
 cout<<"V8="<<v<<" cached_states="<<dp.cache.size()<<"\n";
 if(v!=8335 || dp.cache.size()!=2840397)return 2;
}
