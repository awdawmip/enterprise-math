// R5 fixed-tau full 244 one-label extension Bellman witness, f=7,8.
// Reproduces exact memoized values for one class representative t.
// Input: window_adj.bin from MAKE_ADJ.py and frozen exact integer centers.
#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,Q=101,K=13,FULL=(1<<K)-1;
constexpr int seed[12]={0,16,32,48,1,64,17,80,18,24,34,82};
struct Act { int k; vector<int> masks; };
using Sig=vector<Act>;
vector<int> maximal(vector<int> a) {
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int> r;
 for(int m:a){bool dominated=false;
  for(int n:a)if(m!=n&&(m&n)==m){dominated=true;break;}
  if(!dominated)r.push_back(m);
 }
 return r;
}
Sig signature(const vector<uint8_t>&adj,int t) {
 int h[K];copy(begin(seed),end(seed),h);h[12]=t;
 map<vector<int>,int> cheapest;
 for(int q=0;q<Q;q++){
  const auto *data=adj.data()+(size_t)q*N*N;
  vector<int> masks;
  for(int i=0;i<K;i++){
   int m=0;
   for(int j=0;j<K;j++)if(data[h[i]*N+h[j]])m|=1<<j;
   masks.push_back(m);
  }
  auto fam=maximal(move(masks));
  if(fam.size()==1&&fam[0]==FULL)continue;
  if(!cheapest.count(fam))cheapest[fam]=214+q;
 }
 Sig ans;for(auto &[fam,k]:cheapest)ans.push_back({k,fam});
 sort(ans.begin(),ans.end(),[](auto&a,auto&b){return a.k<b.k;});return ans;
}
struct Solver {
 int f,base; uint64_t weight[K]; unordered_map<uint64_t,int> memo;
 size_t visits=0,cap;
 Solver(int f_,size_t limit):f(f_),base(f_+2),cap(limit){
  weight[0]=1;
  for(int i=1;i<K;i++)weight[i]=weight[i-1]*base;
  memo.reserve(50000);
 }
 int solve(uint64_t idx,const Sig&a) {
  auto it=memo.find(idx);if(it!=memo.end())return it->second;
  uint64_t y=idx;int e[K],live=0;
  for(int i=0;i<K;i++){e[i]=y%base;y/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++visits>cap)throw runtime_error("STATE_CAP_REACHED");
  int best=INT_MAX/4;
  for(auto&act:a){
   bool stall=false;
   for(int s:act.masks)if((s&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int s:act.masks){
    uint64_t next=idx;
    for(int i=0;i<K;i++)if(!(s&(1<<i))&&e[i]<f+1)next+=weight[i];
    worst=max(worst,solve(next,a));
    if(act.k+worst>=best)break;
   }
   best=min(best,act.k+worst);
  }
  if(best==INT_MAX/4)throw runtime_error("NO_PROGRESS");
  memo.emplace(idx,best);return best;
 }
};
int main(int argc,char**argv){
 if(argc<4){cerr<<"USAGE: solver window_adj.bin t maxf [state_cap]\n";return 2;}
 ifstream in(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 in.read((char*)adj.data(),adj.size());
 if(!in||in.gcount()!=(streamsize)adj.size())return 3;
 int t=stoi(argv[2]),maxf=stoi(argv[3]);size_t cap=argc>4?stoull(argv[4]):25000000;
 if(t<0||t>=N||find(begin(seed),end(seed),t)!=end(seed)||maxf<7||maxf>8)return 4;
 auto actions=signature(adj,t);
 cerr<<"THIRD "<<t<<" ACTIONS "<<actions.size()<<"\n";
 for(int f=7;f<=maxf;f++){
  Solver dp(f,cap);
  int v=dp.solve(0,actions);
  cout<<t<<","<<f<<","<<v<<","<<dp.memo.size()<<"\n";
 }
}
