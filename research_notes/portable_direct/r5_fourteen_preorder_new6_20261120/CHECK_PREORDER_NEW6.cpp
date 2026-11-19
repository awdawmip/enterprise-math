// Frozen R5 14-label priced-joint-support preorder census.
// Compile in this research directory; source precondition: frozen window_adj.bin.
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
int previous_solver_main(int argc,char**argv){
 if(argc<4){cerr<<"USAGE: solver window_adj.bin u v [state_cap]\n";return 2;}
 ifstream in(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 in.read((char*)adj.data(),adj.size());if(!in||in.gcount()!=(streamsize)adj.size())return 3;
 int u=stoi(argv[2]),v=stoi(argv[3]);if(u==v)return 4;
 for(int x:seed)if(u==x||v==x)return 5;
 auto sig=signature(adj,u,v);DP d(argc>4?stoull(argv[4]):12000000);
 try{int val=d.rec(0,sig);cout<<"PAIR="<<u<<","<<v<<" F8="<<val<<" STATES="<<d.memo.size()<<" ACTIONS="<<sig.size()<<"\n";}
 catch(exception&e){cerr<<e.what()<<"\n";return 6;}
}

bool action_leq(const Act&a,const Act&b){
 if(a.cost>b.cost)return false;
 for(int x:a.masks){bool found=false;for(int y:b.masks)if((x&y)==x){found=true;break;}if(!found)return false;}
 return true;
}
bool preorder(const Sig&a,const Sig&b){
 for(const auto&bb:b){bool found=false;for(const auto&aa:a)if(action_leq(aa,bb)){found=true;break;}if(!found)return false;}
 return true;
}
int swap_extra(int x){int a=(x>>12)&1,b=(x>>13)&1;return(x&~(3<<12))|(a<<13)|(b<<12);}
struct C{int u,v,members;Sig a,b;};
string fingerprint(const Sig&s){string t;for(const auto&a:s){t+=to_string(a.cost)+":";for(int m:a.masks)t+=to_string(m)+",";t+=";";}return t;}
int main(){
 ifstream f("window_adj.bin",ios::binary);vector<uint8_t>adj((size_t)Q*N*N);f.read((char*)adj.data(),adj.size());if(f.gcount()!=(streamsize)adj.size())return 2;
 bool used[N]={};for(int h:seed)used[h]=true;
 unordered_map<string,int>ids;vector<C>cl;
 for(int u=0;u<N;u++)if(!used[u])for(int v=u+1;v<N;v++)if(!used[v]){
  auto a=signature(adj,u,v);auto key=fingerprint(a);auto it=ids.find(key);int id;
  if(it==ids.end()){id=cl.size();ids[key]=id;auto b=a;for(auto&act:b)for(int&m:act.masks)m=swap_extra(m);cl.push_back({u,v,0,move(a),move(b)});}
  else id=it->second;
  cl[id].members++;
 }
 int n=cl.size();if(n!=1906)return 3;
 vector<vector<uint8_t>>e(n,vector<uint8_t>(n));int edges=0;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++){
  e[i][j]=preorder(cl[i].a,cl[j].a)||preorder(cl[i].a,cl[j].b);
  edges+=e[i][j];
 }
 vector<int>par(n);iota(par.begin(),par.end(),0);
 auto find=[&](int i){while(par[i]!=i){par[i]=par[par[i]];i=par[i];}return i;};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(e[i][j]&&e[j][i]){
  int a=find(i),b=find(j);if(a!=b)par[a]=b;
 }
 set<int>scc,sinks;int sinkMembers=0;
 for(int i=0;i<n;i++){
  scc.insert(find(i));bool out=false;
  for(int j=0;j<n;j++)if(e[i][j]&&!e[j][i]){out=true;break;}
  if(!out){sinks.insert(find(i));sinkMembers++;}
 }
 const int old[]={0,1,2,10,709,1281,1362,1905,206,1048,1199,1205,616,601,929,935,15,693,220,610,846,1278};
 const int additions[]={295,354,291,3,368,360,1090,842,232,668};
 int oc=0,op=0,nc=0,np=0;
 for(int i=0;i<n;i++){
  bool past=false,current=false;
  for(int j:old)if(e[i][j])past=true;
  current=past;
  for(int j:additions)if(e[i][j])current=true;
  if(past){oc++;op+=cl[i].members;}
  if(current){nc++;np+=cl[i].members;}
 }
 if(cl[295].u!=19||cl[295].v!=88||cl[354].u!=21||cl[354].v!=85||cl[291].u!=19||cl[291].v!=81)return 4;
 cout<<"classes="<<n<<" edges="<<edges<<" scc="<<scc.size()<<" sink_scc="<<sinks.size()<<" sink_classes="<<sinkMembers
 <<" old_classes="<<oc<<" old_pairs="<<op<<" new_classes="<<nc<<" new_pairs="<<np<<"\n";
 return (edges==38127&&scc.size()==1066&&sinks.size()==333&&sinkMembers==367&&oc==836&&op==20159&&nc==1008&&np==23828)?0:5;
}
