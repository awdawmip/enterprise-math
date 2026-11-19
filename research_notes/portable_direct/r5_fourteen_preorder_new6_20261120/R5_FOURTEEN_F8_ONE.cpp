// Exact R5 14-label scalar Bellman minimax, f=8, frozen integer window adjacency.
// Input SHA256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,Q=101,K=14,FULL=(1<<K)-1,f=8;
constexpr int seed[12]={0,16,32,48,1,64,17,80,18,24,34,82};
struct Act{int cost;vector<int> masks;};
using Sig=vector<Act>;
vector<int> maxfam(vector<int> a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int> r;
 for(int m:a){bool sub=false;for(int n:a)if(n!=m&&(m&n)==m){sub=true;break;}if(!sub)r.push_back(m);}
 return r;
}
Sig signature(const vector<uint8_t>&adj,int u,int v){
 int h[K];copy(begin(seed),end(seed),h);h[12]=u;h[13]=v;
 map<vector<int>,int> chosen;
 for(int qi=0;qi<Q;qi++){
  const uint8_t* a=adj.data()+(size_t)qi*N*N;vector<int> masks;
  for(int i=0;i<K;i++){int m=0;for(int j=0;j<K;j++)if(a[h[i]*N+h[j]])m|=1<<j;masks.push_back(m);}
  auto fam=maxfam(move(masks));if(fam.size()==1&&fam[0]==FULL)continue;
  auto it=chosen.find(fam);if(it==chosen.end()||it->second>214+qi)chosen[fam]=214+qi;
 }
 Sig r;for(auto&[m,k]:chosen)r.push_back({k,m});
 sort(r.begin(),r.end(),[](auto&a,auto&b){return a.cost<b.cost;});
 return r;
}
struct DP{
 uint64_t weights[K];unordered_map<uint64_t,int> memo;size_t visited=0,cap;
 DP(size_t limit):cap(limit){weights[0]=1;for(int i=1;i<K;i++)weights[i]=weights[i-1]*(f+2);memo.reserve(50000);}
 int rec(uint64_t state,const Sig&acts){
  auto it=memo.find(state);if(it!=memo.end())return it->second;
  int e[K],live=0;auto t=state;
  for(int i=0;i<K;i++){e[i]=t%(f+2);t/=f+2;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++visited>cap)throw runtime_error("STATE_CAP");
  int best=INT_MAX/4;
  for(auto&act:acts){
   bool stall=false;for(int m:act.masks)if((m&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int m:act.masks){
    uint64_t next=state;
    for(int i=0;i<K;i++)if(e[i]<f+1&&!(m&(1<<i)))next+=weights[i];
    worst=max(worst,rec(next,acts));
    if(act.cost+worst>=best)break;
   }
   best=min(best,act.cost+worst);
  }
  if(best==INT_MAX/4)throw runtime_error("NO_PROGRESS");
  memo.emplace(state,best);return best;
 }
};
int main(int argc,char**argv){
 if(argc<4){cerr<<"USAGE: solver window_adj.bin u v [state_cap]\n";return 2;}
 ifstream in(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 in.read((char*)adj.data(),adj.size());if(!in||in.gcount()!=(streamsize)adj.size())return 3;
 int u=stoi(argv[2]),v=stoi(argv[3]);if(u==v)return 4;
 for(int x:seed)if(u==x||v==x)return 5;
 auto sig=signature(adj,u,v);DP d(argc>4?stoull(argv[4]):12000000);
 try{int val=d.rec(0,sig);cout<<"PAIR="<<u<<","<<v<<" F8="<<val<<" STATES="<<d.memo.size()<<" ACTIONS="<<sig.size()<<"\n";}
 catch(exception&e){cerr<<e.what()<<"\n";return 6;}
}
