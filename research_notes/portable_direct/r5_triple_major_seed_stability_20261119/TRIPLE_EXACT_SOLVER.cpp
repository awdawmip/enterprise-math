#include <bits/stdc++.h>
using namespace std;
// Exact R5 scalar 9-label Bellman: requires window_adj.bin from the frozen-source
// MAKE_WINDOW_ADJ.py; no native Port/X6 quotient is made.
constexpr int N=256, K=9, Q=101;
constexpr int B[6]={0,16,32,48,1,64};
struct Act {int price; vector<int> masks;};
vector<int> maximal(vector<int> a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int> z;
 for(int x:a){bool sub=false;for(int y:a)if(x!=y&&(x&y)==x){sub=true;break;}if(!sub)z.push_back(x);}
 return z;
}
vector<Act> build(const vector<unsigned char>& adj,int t){
 int labels[K]={0,16,32,48,1,64,17,80,t};
 map<vector<int>,int> cheapest;
 for(int k=0;k<Q;k++){
  vector<int> m;const unsigned char* arr=adj.data()+(size_t)k*N*N;
  for(int i=0;i<K;i++){
   int s=0;for(int j=0;j<K;j++)if(arr[(size_t)labels[i]*N+labels[j]])s|=1<<j;
   m.push_back(s);
  }
  auto masks=maximal(m);
  if(masks.size()==1&&masks[0]==(1<<K)-1)continue;
  if(!cheapest.count(masks))cheapest[masks]=k+214;
 }
 vector<Act> v;for(const auto&[m,k]:cheapest)v.push_back({k,m});
 sort(v.begin(),v.end(),[](auto&a,auto&b){return a.price<b.price;});
 return v;
}
struct Solver{
 int f,base,p[K+1],stamp=0,states=0;
 vector<int> memo,mark;unordered_map<int,int> sparse;bool use_sparse;
 Solver(int ff):f(ff),base(ff+2){
  p[0]=1;for(int i=1;i<=K;i++)p[i]=p[i-1]*base;
  use_sparse=(f>=5);if(use_sparse)sparse.reserve(200000);
  else{memo.resize(p[K]);mark.resize(p[K]);}
 }
 int value(int idx,const vector<Act>& as){
  if(use_sparse){auto it=sparse.find(idx);if(it!=sparse.end())return it->second;}
  else if(mark[idx]==stamp)return memo[idx];
  int e[K],q=idx,live=0;
  for(int i=0;i<K;i++){e[i]=q%base;q/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1){
   if(use_sparse)sparse[idx]=0;else{memo[idx]=0;mark[idx]=stamp;}return 0;
  }
  states++;int best=INT_MAX/8;
  for(const Act& a:as){
   bool nonprogress=false;
   for(int s:a.masks)if((s&live)==live){nonprogress=true;break;}
   if(nonprogress)continue;
   int worst=0;
   for(int s:a.masks){
    int nxt=idx;
    for(int i=0;i<K;i++)if(!(s&(1<<i))&&e[i]<f+1)nxt+=p[i];
    worst=max(worst,value(nxt,as));
    if(a.price+worst>=best)break;
   }
   best=min(best,a.price+worst);
  }
  if(best==INT_MAX/8){cerr<<"NO PROGRESS "<<idx<<"\n";exit(3);}
  if(use_sparse)sparse[idx]=best;else{mark[idx]=stamp;memo[idx]=best;}return best;
 }
 int root(const vector<Act>& as){
  stamp++;states=0;if(use_sparse)sparse.clear();
  return value(0,as);
 }
};
int main(int argc,char**argv){
 ifstream f("window_adj.bin",ios::binary);
 vector<unsigned char> adj((size_t)Q*N*N);f.read((char*)adj.data(),adj.size());
 if(!f||size_t(f.gcount())!=adj.size()){cerr<<"MISSING_OR_BAD_WINDOW_ADJ";return 2;}
 int max_f=argc>1?stoi(argv[1]):8,first=argc>2?stoi(argv[2]):2,last=argc>3?stoi(argv[3]):2;
 if(max_f<0||max_f>8||first<0||last>255)return 2;
 cout<<"t,actions";for(int j=0;j<=max_f;j++)cout<<",f"<<j;cout<<"\n";
 vector<unique_ptr<Solver>> solvers;
 for(int j=0;j<=max_f;j++)solvers.push_back(make_unique<Solver>(j));
 for(int t=first;t<=last;t++){
  bool excluded=(t==17||t==80);for(int b:B)if(t==b)excluded=true;
  if(excluded)continue;
  auto as=build(adj,t);cout<<t<<","<<as.size();
  for(int j=0;j<=max_f;j++)cout<<","<<solvers[j]->root(as);
  cout<<"\n";
 }
}
