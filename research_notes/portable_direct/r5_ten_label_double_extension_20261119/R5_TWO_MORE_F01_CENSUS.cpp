#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int NN=256, KK=10, QQ=101, full=(1<<KK)-1;
constexpr array<int,8> seed={0,16,32,48,1,64,17,80};
struct Action { int cost; vector<int> masks; };
using Signature=vector<Action>;
vector<int> max_support(vector<int> a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int> out;
 for(int x:a){bool sub=false; for(int y:a)if(x!=y&&(x&y)==x){sub=true;break;} if(!sub)out.push_back(x);}
 return out;
}
Signature build(const vector<unsigned char>&adj, int t,int u){
 array<int,KK> labels;copy(seed.begin(),seed.end(),labels.begin());labels[8]=t;labels[9]=u;
 map<vector<int>,int> best;
 for(int k=0;k<QQ;k++){
  const unsigned char *p=adj.data()+(size_t)k*NN*NN;
  vector<int> masks;
  for(int i=0;i<KK;i++){
   int mask=0;
   for(int j=0;j<KK;j++)if(p[(size_t)labels[i]*NN+labels[j]])mask|=1<<j;
   masks.push_back(mask);
  }
  auto fam=max_support(masks);
  if(fam.size()==1&&fam[0]==full)continue;
  auto it=best.find(fam);if(it==best.end())best.emplace(move(fam),214+k);
 }
 Signature actions;for(auto&[fam,k]:best)actions.push_back({k,fam});
 sort(actions.begin(),actions.end(),[](auto&a,auto&b){if(a.cost!=b.cost)return a.cost<b.cost;return a.masks<b.masks;});
 return actions;
}
string key(const Signature&s){
 string k;
 for(auto&a:s){k+=to_string(a.cost)+":";for(int m:a.masks)k+=to_string(m)+",";k+=';';}
 return k;
}
int solve_f0(const Signature &a){
 int val[1<<KK]{};
 for(int cnt=2;cnt<=KK;cnt++)for(int live=1;live<=full;live++){
  if(__builtin_popcount((unsigned)live)!=cnt)continue;
  int best=1000000000;
  for(auto&act:a){
   bool stalled=false;for(int m:act.masks)if((live&m)==live){stalled=true;break;}
   if(stalled)continue;
   int worst=0;for(int m:act.masks)worst=max(worst,val[live&m]);
   best=min(best,act.cost+worst);
  }
  if(best==1000000000)throw runtime_error("no-progress on live mask");
  val[live]=best;
 }
 return val[full];
}
struct Solver1 {
 static constexpr int base=3, f=1, total=59049;
 array<int,KK> weight{};
 vector<int> memo,stamp;
 int epoch=0,states=0;
 Solver1():memo(total,0),stamp(total,0){weight[0]=1;for(int i=1;i<KK;i++)weight[i]=weight[i-1]*base;}
 int rec(int idx,const Signature &a){
  if(stamp[idx]==epoch)return memo[idx];
  int tmp=idx,e[KK],live=0;
  for(int i=0;i<KK;i++){e[i]=tmp%base;tmp/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1){memo[idx]=0;stamp[idx]=epoch;return 0;}
  states++;int best=INT32_MAX/8;
  for(const auto&act:a){
   bool stalled=false;for(int m:act.masks)if((live&m)==live){stalled=true;break;}
   if(stalled)continue;
   int worst=0;
   for(int m:act.masks){int nxt=idx;for(int i=0;i<KK;i++)if(!(m&(1<<i))&&e[i]<f+1)nxt+=weight[i];
    worst=max(worst,rec(nxt,a));if(act.cost+worst>=best)break;}
   best=min(best,act.cost+worst);
  }
  if(best==INT32_MAX/8)throw runtime_error("no progress f1");
  memo[idx]=best;stamp[idx]=epoch;return best;
 }
 pair<int,int> root(const Signature&a){epoch++;states=0;int r=rec(0,a);return {r,states};}
};
int main(int argc,char**argv){
 ifstream f("window_adj.bin",ios::binary);vector<unsigned char> adj((size_t)QQ*NN*NN);
 f.read((char*)adj.data(),adj.size());if(!f||f.gcount()!=(streamsize)adj.size())throw runtime_error("bad adjacency");
 vector<int> pool;for(int x=0;x<NN;x++)if(find(seed.begin(),seed.end(),x)==seed.end())pool.push_back(x);
 map<string,int> ids;vector<Signature> fams;vector<int> counts;vector<int> results,results_f1,visited_f1;Solver1 solver;int minval=100000000,maxval=-1;
 cout<<"#R5_F01_TWO_MORE t,u,class_id,V0,V1\n";
 for(size_t i=0;i<pool.size();i++)for(size_t j=i+1;j<pool.size();j++){
  int t=pool[i],u=pool[j];auto sig=build(adj,t,u);string s=key(sig);
  auto it=ids.find(s);int id;
  if(it==ids.end()){id=(int)fams.size();ids.emplace(move(s),id);fams.push_back(move(sig));counts.push_back(0);results.push_back(solve_f0(fams.back()));auto [v1,nodes]=solver.root(fams.back());results_f1.push_back(v1);visited_f1.push_back(nodes);}
  else id=it->second;
  counts[id]++;int v=results[id];minval=min(minval,v);maxval=max(maxval,v);
  cout<<t<<","<<u<<","<<id<<","<<v<<","<<results_f1[id]<<"\n";
 }
 cerr<<"PAIRS="<<(pool.size()*(pool.size()-1)/2)<<" CLASSES="<<fams.size()<<" MIN="<<minval<<" MAX="<<maxval<<"\n";
 map<int,int> by_value;for(size_t id=0;id<results.size();id++)by_value[results[id]]+=counts[id];
 for(auto [v,n]:by_value)cerr<<"V0="<<v<<" COUNT="<<n<<"\n";
 map<int,int> f1counts;for(size_t j=0;j<results_f1.size();j++)f1counts[results_f1[j]]+=counts[j];
 for(auto[v,n]:f1counts)cerr<<"V1="<<v<<" COUNT="<<n<<"\n";
 int maxnode=*max_element(visited_f1.begin(),visited_f1.end());cerr<<"MAX_F1_STATES="<<maxnode<<"\n";
}
