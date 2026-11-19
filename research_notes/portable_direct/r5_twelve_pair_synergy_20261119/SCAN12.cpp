// R5 frozen scalar twelve-label two-addition census. Exact Bellman DP.
// Frozen JSON sha256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
// Run make_adj.py first, then ./scan12 [f=0|1|2] [state_cap].
#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,Q=101,K=12,FULL=(1<<K)-1;
const array<int,10> seed={0,16,32,48,1,64,17,80,18,24};
struct Act {int k;vector<int> masks;};
vector<uint8_t> adj;
vector<int> maximal(vector<int>a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int>out;
 for(int x:a){bool dominated=false;for(int y:a)
   if(x!=y && (x&y)==x){dominated=true;break;}
  if(!dominated)out.push_back(x);}
 return out;
}
vector<Act> acts_for(int u,int v){
 array<int,K> labels;copy(seed.begin(),seed.end(),labels.begin());
 labels[10]=u;labels[11]=v;
 map<vector<int>,int>best;
 for(int qi=0;qi<Q;qi++){
  const uint8_t*p=&adj[(size_t)qi*N*N];vector<int>masks;
  for(int i=0;i<K;i++){int m=0;for(int j=0;j<K;j++)
    if(p[(size_t)labels[i]*N+labels[j]])m|=1<<j;
   masks.push_back(m);
  }
  auto fam=maximal(masks);if(fam.size()==1 && fam[0]==FULL)continue;
  auto it=best.find(fam);
  if(it==best.end() || 214+qi<it->second)best[fam]=214+qi;
 }
 vector<Act>a;for(auto&[fam,k]:best)a.push_back({k,fam});
 sort(a.begin(),a.end(),[](const Act&x,const Act&y){return x.k<y.k;});
 return a;
}
struct Solver{
 int f,base;array<uint64_t,K>powers;
 unordered_map<uint64_t,int>memo;
 size_t calls=0,cap;
 Solver(int ff,size_t limit):f(ff),base(ff+2),cap(limit){
  powers[0]=1;for(int i=1;i<K;i++)powers[i]=powers[i-1]*base;
 }
 int rec(uint64_t code,const vector<Act>&a){
  auto it=memo.find(code);if(it!=memo.end())return it->second;
  uint64_t z=code;int e[K],live=0;
  for(int i=0;i<K;i++){e[i]=z%base;z/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++calls>cap)throw runtime_error("STATE_CAP");
  int best=INT_MAX/8;
  for(auto&act:a){
   bool stall=false;for(int m:act.masks)
    if((m&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int m:act.masks){
    uint64_t nxt=code;for(int i=0;i<K;i++)
      if(!(m&(1<<i))&&e[i]<f+1)nxt+=powers[i];
    worst=max(worst,rec(nxt,a));
    if(act.k+worst>=best)break;
   }
   best=min(best,act.k+worst);
  }
  if(best>=INT_MAX/8)throw runtime_error("NO_PROGRESS_ACTION");
  memo.emplace(code,best);return best;
 }
};
int main(int argc,char**argv){
 int f=argc>1?stoi(argv[1]):0;
 if(f<0||f>8)throw runtime_error("negative or unsupported f");
 size_t cap=argc>2?stoull(argv[2]):300000;
 ifstream in("window_adj.bin",ios::binary);
 adj.resize((size_t)Q*N*N);in.read((char*)adj.data(),adj.size());
 if(!in||in.gcount()!=(streamsize)adj.size())throw runtime_error("missing window adjacency");
 set<int>s(seed.begin(),seed.end());vector<int>labels;
 for(int h=0;h<N;h++)if(!s.count(h))labels.push_back(h);
 int n=0,unknown=0;map<int,int>hist;
 cout<<"u,v,value,states,action_families\n";
 for(int i=0;i<(int)labels.size();i++)for(int j=i+1;j<(int)labels.size();j++){
  auto actions=acts_for(labels[i],labels[j]);
  int v=-1;size_t states=0;
  try{Solver sol(f,cap);v=sol.rec(0,actions);states=sol.calls;}
  catch(const exception&e){unknown++;}
  cout<<labels[i]<<","<<labels[j]<<","<<v<<","<<states<<","<<actions.size()<<"\n";
  hist[v]++;n++;
 }
 cerr<<"n="<<n<<" f="<<f<<" unknown="<<unknown<<"\n";
 for(auto[v,count]:hist)cerr<<v<<" "<<count<<"\n";
 return (n==30135 && unknown==0)?0:3;
}