// Frozen R5 scalar D14 exact Bellman, integer-only. C++17.
// ./solver window_adj.bin classes_1906.tsv f [all | selected_ids.txt]
#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,Q=101,K=14,FULL=(1<<K)-1;
const int seed[12]={0,16,32,48,1,64,17,80,18,24,34,82};
struct Action {int cost;vector<int> masks;};
using Signature=vector<Action>;
vector<int> maximal(vector<int> a){
 sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
 vector<int> out;for(int x:a){bool dominated=false;
  for(int y:a)if(x!=y&&(x&y)==x){dominated=true;break;}
  if(!dominated)out.push_back(x);
 }return out;
}
Signature signature(const vector<uint8_t>&adj,int u,int v){
 int h[K];copy(begin(seed),end(seed),h);h[12]=u;h[13]=v;
 map<vector<int>,int> cheapest;
 for(int qi=0;qi<Q;qi++){
  const auto* row=adj.data()+(size_t)qi*N*N;
  vector<int> supports;
  for(int i=0;i<K;i++){
   int mask=0;
   for(int j=0;j<K;j++)if(row[h[i]*N+h[j]])mask|=1<<j;
   supports.push_back(mask);
  }
  auto fam=maximal(move(supports));
  if(fam.size()==1&&fam[0]==FULL)continue;
  auto it=cheapest.find(fam);
  if(it==cheapest.end()||214+qi<it->second)cheapest[fam]=214+qi;
 }
 Signature ans;
 for(auto &kv:cheapest)ans.push_back({kv.second,kv.first});
 sort(ans.begin(),ans.end(),[](const auto &a,const auto &b){return a.cost<b.cost;});
 return ans;
}
struct Solver {
 int F,base;uint64_t powers[K];
 unordered_map<uint64_t,int> memo;
 size_t limit,states=0;
 Solver(int f,size_t cap):F(f),base(f+2),limit(cap){
  powers[0]=1;for(int i=1;i<K;i++)powers[i]=powers[i-1]*base;
  memo.reserve(150000);
 }
 int value(uint64_t s,const Signature&a){
  auto it=memo.find(s);if(it!=memo.end())return it->second;
  int e[K],live=0;uint64_t z=s;
  for(int i=0;i<K;i++){e[i]=z%base;z/=base;if(e[i]<=F)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++states>limit)throw runtime_error("STATE_CAP");
  int best=INT_MAX/4;
  for(const auto &act:a){
   bool stall=false;
   for(int mask:act.masks)if((mask&live)==live){stall=true;break;}
   if(stall)continue;
   int worst=0;
   for(int mask:act.masks){
    uint64_t next=s;
    for(int i=0;i<K;i++)if(e[i]<=F&&!(mask&(1<<i)))next+=powers[i];
    worst=max(worst,value(next,a));
    if(act.cost+worst>=best)break;
   }
   best=min(best,act.cost+worst);
  }
  if(best==INT_MAX/4)throw runtime_error("NO_PROGRESS");
  memo.emplace(s,best);return best;
 }
};
int main(int argc,char**argv){
 if(argc<4){cerr<<"Usage: solver window_adj.bin classes_1906.tsv f [all | idfile] [cap]\n";return 1;}
 int f=stoi(argv[3]);if(f<0||f>8)return 2;
 size_t cap=argc>5?stoull(argv[5]):2000000;
 ifstream bin(argv[1],ios::binary);
 vector<uint8_t> adj((size_t)Q*N*N);
 bin.read((char*)adj.data(),adj.size());
 if(bin.gcount()!=(streamsize)adj.size())return 3;
 set<int>selected;
 bool all=argc<=4||string(argv[4])=="all";
 if(!all){ifstream fi(argv[4]);int id;while(fi>>id)selected.insert(id);}
 ifstream cls(argv[2]);string s;getline(cls,s);
 cout<<"class,u,v,members,actions,f,value,nonterminal_states\n";
 int count=0;
 while(getline(cls,s)){
  if(s.empty())continue;
  istringstream in(s);int id,u,v,m,a;
  in>>id>>u>>v>>m>>a;
  if(!all&&!selected.count(id))continue;
  Signature sig=signature(adj,u,v);
  if((int)sig.size()!=a)throw runtime_error("PRICED_ACTION_MISMATCH");
  Solver solver(f,cap);int result=solver.value(0,sig);
  cout<<id<<','<<u<<','<<v<<','<<m<<','<<a<<','<<f<<','<<result<<','<<solver.states<<'\n';
  count++;
 }
 cerr<<"PASS_ROOTS="<<count<<" F="<<f<<"\n";
 if(!all&&count!=(int)selected.size())return 4;
 return 0;
}