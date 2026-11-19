// Exact C++17 R5 13-label scalar Bellman census, f=0..6.
// Input window_adj.bin: 101*256*256 bytes, [0<=N_j(k)-N_i(k)<=tau].
// Scientific SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,Q=101,K=13,FULL=(1<<K)-1;
constexpr int seed[12]={0,16,32,48,1,64,17,80,18,24,34,82};
struct Act {int cost; vector<int> masks;};
using Sig=vector<Act>;
vector<int> maxfam(vector<int>a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());vector<int>r;
 for(int m:a){bool dominated=false;for(int n:a)if(m!=n&&(m&n)==m){dominated=true;break;}if(!dominated)r.push_back(m);}
 return r;
}
Sig signature(const vector<uint8_t>&adj,int t){
 int h[K];copy(begin(seed),end(seed),h);h[12]=t;map<vector<int>,int> p;
 for(int qi=0;qi<Q;qi++){
  const uint8_t* data=adj.data()+(size_t)qi*N*N;vector<int>masks;
  for(int i=0;i<K;i++){int m=0;for(int j=0;j<K;j++)if(data[h[i]*N+h[j]])m|=1<<j;masks.push_back(m);}
  auto fam=maxfam(move(masks));if(fam.size()==1&&fam[0]==FULL)continue;
  if(!p.count(fam))p[fam]=214+qi;
 }
 Sig a;for(const auto&[m,c]:p)a.push_back({c,m});
 sort(a.begin(),a.end(),[](const Act&a,const Act&b){return a.cost<b.cost;});return a;
}
string key(const Sig&s){
 string z;for(const auto&a:s){z+=to_string(a.cost);z+=':';for(int m:a.masks){z+=to_string(m);z+=',';}z+=';';}return z;
}
int fzero(const Sig&s){
 int d[1<<K]={};
 for(int live=1;live<=FULL;live++){
  if(__builtin_popcount((unsigned)live)<=1)continue;int best=INT_MAX/4;
  for(const auto&a:s){
   int worst=0;bool skip=false;
   for(int m:a.masks){int q=live&m;if(q==live){skip=true;break;}worst=max(worst,d[q]);}
   if(!skip)best=min(best,a.cost+worst);
  }
  if(best==INT_MAX/4)throw runtime_error("NO_PROGRESS");
  d[live]=best;
 }
 return d[FULL];
}
struct DP {
 int f,b;uint64_t W[K];unordered_map<uint64_t,int>M;size_t calls=0,cap;
 DP(int ff,size_t limit):f(ff),b(ff+2),cap(limit){
  W[0]=1;for(int i=1;i<K;i++)W[i]=W[i-1]*b;M.reserve(50000);
 }
 int rec(uint64_t idx,const Sig&a){
  auto it=M.find(idx);if(it!=M.end())return it->second;
  uint64_t y=idx;int e[K],live=0;
  for(int i=0;i<K;i++){e[i]=y%b;y/=b;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++calls>cap)throw runtime_error("STATE_CAP_REACHED");
  int best=INT_MAX/4;
  for(const auto&act:a){
   bool stall=false;for(int s:act.masks)if((s&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int s:act.masks){
    uint64_t next=idx;
    for(int i=0;i<K;i++)if(!(s&(1<<i))&&e[i]<f+1)next+=W[i];
    worst=max(worst,rec(next,a));if(act.cost+worst>=best)break;
   }
   best=min(best,act.cost+worst);
  }
  if(best==INT_MAX/4)throw runtime_error("NO_PROGRESS");
  M.emplace(idx,best);return best;
 }
};
int main(int argc,char**argv){
 if(argc<2){cerr<<"Usage: program window_adj.bin [cap]\n";return 2;}
 ifstream fi(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 fi.read((char*)adj.data(),adj.size());
 if(!fi||fi.gcount()!=(streamsize)adj.size())return 3;
 size_t cap=argc>2?stoull(argv[2]):5000000;
 map<string,pair<vector<int>,int>>cache;map<string,int>hist;
 cout<<"t,class,f0,f1,f2,f3,f4,f5,f6\n";
 bool used[N]={};for(int x:seed)used[x]=true;
 for(int t=0;t<N;t++)if(!used[t]){
  auto s=signature(adj,t);auto k=key(s);auto it=cache.find(k);
  vector<int>val;int cls;
  if(it==cache.end()){
   val.push_back(fzero(s));
   for(int f=1;f<=6;f++){DP solver(f,cap);val.push_back(solver.rec(0,s));}
   cls=cache.size();cache.emplace(move(k),make_pair(val,cls));
  }else{val=it->second.first;cls=it->second.second;}
  cout<<t<<","<<cls;for(int v:val)cout<<","<<v;cout<<"\n";
  string pr;for(int v:val){pr+=to_string(v)+",";}hist[pr]++;
 }
 cerr<<"CLASSES "<<cache.size()<<"\n";
 for(auto&[v,n]:hist)cerr<<"PROFILE "<<v<<" "<<n<<"\n";
 return 0;
}
