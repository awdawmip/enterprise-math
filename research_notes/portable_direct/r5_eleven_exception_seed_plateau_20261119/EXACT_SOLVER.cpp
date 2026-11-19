// Exact 11-label R5 scalar Bellman and price-aware quotient. C++17.
// Requires 101*256*256 byte window_adj.bin, A[k,i,j] = [0<=N_j(k)-N_i(k)<=tau].
// Source JSON pin SHA256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
// Usage: ./a.out MAX_F CAP_PER_CLASS [ONLY_CLASS]. For all 50 classes run
// ./a.out 8 5000000 CLASS for CLASS=0,...,49.
// Original labels are NEVER dropped from class members.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int H=256, N=11, Q=101, FULL=(1<<N)-1;
constexpr array<int,10> seed={0,16,32,48,1,64,17,80,18,24};
struct A{int price;vector<int> masks;};
using Sig=vector<A>;
vector<int> maximal(vector<int> v){
 sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
 vector<int> r;
 for(int s:v){bool dominated=false;
  for(int t:v)if(s!=t&&(s&t)==s){dominated=true;break;}
  if(!dominated)r.push_back(s);
 }
 return r;
}
Sig actions(const vector<uint8_t>&adj,int extra){
 array<int,N> h;copy(seed.begin(),seed.end(),h.begin());h[10]=extra;
 map<vector<int>,int> cheapest;
 for(int k=0;k<Q;k++){
  const auto*p=&adj[size_t(k)*H*H];vector<int> masks;
  for(int i=0;i<N;i++){int m=0;
   for(int j=0;j<N;j++)if(p[size_t(h[i])*H+h[j]])m|=1<<j;
   masks.push_back(m);
  }
  auto f=maximal(masks);
  if(f.size()==1&&f[0]==FULL)continue;
  cheapest.emplace(move(f),214+k);
 }
 Sig r;
 for(auto&[m,c]:cheapest)r.push_back({c,m});
 sort(r.begin(),r.end(),[](const A&a,const A&b){return a.price<b.price;});
 return r;
}
string key(const Sig&a){
 string s;
 for(const auto&v:a){s+=to_string(v.price)+":";
  for(int m:v.masks)s+=to_string(m)+",";
  s+=";";
 }
 return s;
}
int f0(const Sig&a){
 int dp[1<<N]={};
 for(int live=1;live<=FULL;live++){
  if(__builtin_popcount(unsigned(live))<=1)continue;
  int best=1000000000;
  for(auto&v:a){bool stall=false;
   for(int m:v.masks)if((m&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;for(int m:v.masks)worst=max(worst,dp[live&m]);
   best=min(best,v.price+worst);
  }
  if(best==1000000000)throw runtime_error("no progress f0");
  dp[live]=best;
 }
 return dp[FULL];
}
struct DP{
 int f,base;uint64_t weights[N];unordered_map<uint64_t,int> memo;
 size_t calls=0,cap;
 DP(int ff,size_t maxs):f(ff),base(ff+2),cap(maxs){
  weights[0]=1;for(int i=1;i<N;i++)weights[i]=weights[i-1]*base;
  memo.reserve(50000);
 }
 int solve(uint64_t state,const Sig&a){
  if(auto it=memo.find(state);it!=memo.end())return it->second;
  uint64_t x=state;int err[N],live=0;
  for(int i=0;i<N;i++){err[i]=x%base;x/=base;if(err[i]<=f)live|=1<<i;}
  if(__builtin_popcount(unsigned(live))<=1)return 0;
  if(++calls>cap)throw runtime_error("STATE_CAP_REACHED");
  int best=1000000000;
  for(auto&v:a){
   bool stall=false;for(int m:v.masks)if((m&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int m:v.masks){
    uint64_t next=state;
    for(int i=0;i<N;i++)if(!(m&(1<<i))&&err[i]<f+1)next+=weights[i];
    worst=max(worst,solve(next,a));
    if(v.price+worst>=best)break;
   }
   best=min(best,v.price+worst);
  }
  if(best==1000000000)throw runtime_error("no progress");
  memo.emplace(state,best);return best;
 }
};
int main(int argc,char**argv){
 int maxf=argc>1?stoi(argv[1]):6;
 size_t cap=argc>2?stoull(argv[2]):5000000;
 int only=argc>3?stoi(argv[3]):-1;
 if(maxf<0||maxf>8)throw runtime_error("f must be 0..8");
 ifstream f("window_adj.bin",ios::binary);
 vector<uint8_t> adj(size_t(Q)*H*H);
 f.read((char*)adj.data(),adj.size());
 if(!f||f.gcount()!=streamsize(adj.size()))throw runtime_error("missing adjacency");
 map<string,int> id;
 vector<Sig> classes;vector<vector<int>> members;vector<vector<int>> values;
 for(int t=0;t<H;t++){
  if(find(seed.begin(),seed.end(),t)!=seed.end())continue;
  auto a=actions(adj,t);auto k=key(a);auto it=id.find(k);int j;
  if(it==id.end()){
   j=classes.size();id.emplace(move(k),j);
   classes.push_back(move(a));members.push_back({});values.push_back({f0(classes.back())});
  }else j=it->second;
  members[j].push_back(t);
 }
 if(classes.size()!=50)throw runtime_error("expected exactly 50 signatures");
 for(int ff=1;ff<=maxf;ff++)for(size_t j=0;j<classes.size();j++){
  if(only>=0&&int(j)!=only){values[j].push_back(-2);continue;}
  DP solver(ff,cap);
  try{int v=solver.solve(0,classes[j]);values[j].push_back(v);}
  catch(const exception&e){cerr<<"UNFINISHED class "<<j<<" f "<<ff<<" "<<e.what()<<"\n";values[j].push_back(-1);}
 }
 cout<<"label,class";for(int ff=0;ff<=maxf;ff++)cout<<",f"<<ff;cout<<"\n";
 for(size_t j=0;j<classes.size();j++)for(int t:members[j]){
  cout<<t<<","<<j;for(int val:values[j])cout<<","<<val;cout<<"\n";
 }
}
