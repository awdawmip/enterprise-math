// Exact 14-name unflagged-error Bellman oracle, scalar R5 frozen input SHA256
// 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
#include <bits/stdc++.h>
using namespace std;
static constexpr int N=256,Q=101,K=14,FULL=(1<<K)-1;
static constexpr int W[12]={0,16,32,48,1,64,17,80,18,24,34,82};
struct Act {int cost;vector<int> masks;};
using Sig=vector<Act>;
static vector<int> maximal(vector<int> ms){
 sort(ms.begin(),ms.end());ms.erase(unique(ms.begin(),ms.end()),ms.end());
 vector<int> out;
 for(int m:ms){bool sub=false;for(int n:ms)if(n!=m&&(m&n)==m){sub=true;break;}if(!sub)out.push_back(m);}
 return out;
}
static Sig signature(const vector<uint8_t>&adj,int u,int v){
 int h[K];copy(begin(W),end(W),h);h[12]=u;h[13]=v;
 map<vector<int>,int> costs;
 for(int q=0;q<Q;q++){
  const uint8_t* data=adj.data()+(size_t)q*N*N;
  vector<int> masks;
  for(int i=0;i<K;i++){int m=0;for(int j=0;j<K;j++)if(data[h[i]*N+h[j]])m|=1<<j;masks.push_back(m);}
  auto fam=maximal(move(masks));
  if(fam.size()==1&&fam[0]==FULL)continue;
  auto it=costs.find(fam);
  if(it==costs.end()||it->second>214+q)costs[fam]=214+q;
 }
 Sig a;for(auto &[m,k]:costs)a.push_back({k,m});
 sort(a.begin(),a.end(),[](auto& x,auto& y){return x.cost<y.cost;});
 return a;
}
struct Bellman{
 int f,b;uint64_t weights[K];size_t visits=0,cap;const Sig& acts;
 unordered_map<uint64_t,int> memo;
 Bellman(const Sig&a,int ff,size_t limit):f(ff),b(ff+2),cap(limit),acts(a){
  weights[0]=1;for(int i=1;i<K;i++)weights[i]=weights[i-1]*b;memo.reserve(100000);
 }
 int V(uint64_t state){
  auto it=memo.find(state);if(it!=memo.end())return it->second;
  auto old=state;int e[K],live=0;
  for(int i=0;i<K;i++){e[i]=old%b;old/=b;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++visits>cap)throw runtime_error("CAP_REACHED");
  int best=100000000;
  for(const auto& a:acts){
   bool stall=false;
   for(int mask:a.masks)if((mask&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int mask:a.masks){
    uint64_t next=state;
    for(int i=0;i<K;i++)if(e[i]<f+1&&!(mask&(1<<i)))next+=weights[i];
    int sub=V(next);
    if(sub>worst)worst=sub;
    if(a.cost+worst>=best)break;
   }
   best=min(best,a.cost+worst);
  }
  if(best==100000000)throw runtime_error("NO_PROGRESS");
  memo.emplace(state,best);return best;
 }
};
int main(int argc,char**argv){
 if(argc<5){cerr<<"usage: window_adj.bin u v f [statecap]\n";return 2;}
 ifstream fd(argv[1],ios::binary);vector<uint8_t>a((size_t)Q*N*N);
 fd.read((char*)a.data(),a.size());if(fd.gcount()!=(streamsize)a.size())return 3;
 int u=stoi(argv[2]),v=stoi(argv[3]),f=stoi(argv[4]);
 size_t cap=argc>5?stoull(argv[5]):5000000;
 auto acts=signature(a,u,v);
 cerr<<"u="<<u<<" v="<<v<<" f="<<f<<" actions="<<acts.size()<<endl;
 auto t=chrono::steady_clock::now();
 try{
  Bellman dp(acts,f,cap);int value=dp.V(0);
  cout<<"PASS u="<<u<<" v="<<v<<" f="<<f<<" VALUE="<<value
      <<" states="<<dp.memo.size()
      <<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<endl;
  if(!getenv("NO_ROOT")){
   cout<<"ROOT ";
   for(auto&act:acts){
    int worst=0;bool stall=false;for(int s:act.masks)if(s==FULL)stall=true;
    if(stall)continue;
    for(int s:act.masks){
     uint64_t next=0;for(int i=0;i<K;i++)if(!(s&(1<<i)))next+=dp.weights[i];
     worst=max(worst,dp.V(next));if(worst+act.cost>value)break;
    }
    if(worst+act.cost==value)cout<<act.cost<<",";
   }
   cout<<endl;
  }
 }catch(exception&e){
  cerr<<"FAIL "<<e.what()<<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<endl;return 4;
 }
 return 0;
}
