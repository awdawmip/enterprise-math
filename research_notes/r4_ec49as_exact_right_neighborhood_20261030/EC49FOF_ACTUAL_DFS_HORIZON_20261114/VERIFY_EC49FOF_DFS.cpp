// EC49FOF: 51 native BRC endpoint caches on 84 neutral swaps.
// Reuses the exact EC49FNU ordered signed-prefix trie kernel.
// stdin: frozen master_and_radius3_cases.txt ; argv[1]: original 84-edge list.
// Output includes all actual DFS visits (cut nodes and leaves) and full-future forcing cores.
#include <bits/stdc++.h>
using namespace std;
constexpr int INF=1000000000, B=155;
struct Word{int label,root;string code;};
struct Node{map<unsigned char,int> next;int labels=0;};
struct RootData{vector<int> labels,dp;};
struct Signature{int root;uint64_t lo,hi;bool operator<(const Signature&b)const{return tie(root,lo,hi)<tie(b.root,b.lo,b.hi);}};
vector<vector<Word>> words;
map<Signature,RootData> cache;
vector<Node> trie;vector<int> local;
void addpath(const string&s,int label){
 int u=0;
 for(int j=2;j+1<(int)s.size();j+=2){
  int ch=stoi(s.substr(j,2),nullptr,16);
  if(!trie[u].next.count(ch)){int v=trie.size();trie[u].next[ch]=v;trie.push_back({});u=v;}
  else u=trie[u].next[ch];
 }
 auto it=lower_bound(local.begin(),local.end(),label);
 if(it==local.end()||*it!=label)throw runtime_error("missing root label");
 trie[u].labels|=1<<int(it-local.begin());
}
unordered_map<int,int> dp_node(int u){
 unordered_map<int,int> dp;dp[0]=0;if(trie[u].labels)dp[trie[u].labels]=0;
 for(const auto&[ch,v]:trie[u].next){
  auto next=dp_node(v);unordered_map<int,int> updated;
  for(auto[a,ca]:dp)for(auto[b,cb]:next){
   int mask=a|b,c=ca+cb;
   auto it=updated.find(mask);
   if(it==updated.end()||c<it->second)updated[mask]=c;
  }
  dp.swap(updated);
 }
 for(auto &[mask,c]:dp)if(mask)c++;
 return dp;
}
RootData compute(int root,const vector<int>&keys){
 set<int> labels;
 for(int key:keys)for(const auto&w:words[key])if(w.root==root)labels.insert(w.label);
 local.assign(labels.begin(),labels.end());
 if(local.size()>20)throw runtime_error("root dimension exceeds 20");
 trie.clear();trie.push_back({});
 for(int key:keys)for(const auto&w:words[key])if(w.root==root)addpath(w.code,w.label);
 auto exact=dp_node(0);
 vector<int> f(1<<local.size(),INF);
 for(auto[mask,c]:exact)f[mask]=c;
 for(int j=0;j<(int)local.size();j++)for(int mask=0;mask<(int)f.size();mask++)
  if(!(mask>>j&1))f[mask]=min(f[mask],f[mask|(1<<j)]);
 return {local,f};
}
const RootData& table(int root,const vector<int>&keys){
 vector<int> containing;
 for(int key:keys){for(const auto&w:words[key])if(w.root==root){containing.push_back(key);break;}}
 uint64_t lo=0,hi=0;
 for(int key:containing){if(key<64)lo|=1ULL<<key;else hi|=1ULL<<(key-64);}
 Signature signature{root,lo,hi};
 auto it=cache.find(signature);
 if(it==cache.end())it=cache.emplace(signature,compute(root,containing)).first;
 return it->second;
}
int eval(const vector<const RootData*>&ds,const vector<vector<pair<int,int>>>&opts,
         const array<int,4>& base,const vector<int>&set){
 array<int,4> state=base;vector<int> flex;
 for(int l:set){if(opts[l].size()==1){auto[r,j]=opts[l][0];state[r]|=1<<j;}else flex.push_back(l);}
 int best=INF;
 auto rec=[&](auto&&self,int q)->void{
  if(q==(int)flex.size()){int val=0;for(int r=0;r<4;r++)val+=ds[r]->dp[state[r]];best=min(best,val);return;}
  int l=flex[q];
  for(auto[r,j]:opts[l]){state[r]|=1<<j;self(self,q+1);state[r]&=~(1<<j);}
 };
 rec(rec,0);return best;
}
int main(int argc,char**argv){
 if(argc!=2)throw runtime_error("usage: verify_ec49fof FIRST_NEUTRAL_EDGES_EC49FNS.txt < master");
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int nk,nw,nc;cin>>nk>>nw>>nc;
 if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("unexpected frozen dimensions");
 words.resize(nk);
 for(int k=0;k<nk;k++){int n;cin>>n;for(int j=0;j<n;j++){int l;string s;cin>>l>>s;words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});}}
 vector<vector<int>>cases(nc,vector<int>(7));for(auto&v:cases)for(auto&k:v)cin>>k;
 ifstream input(argv[1]);set<int>ids;int a,b;int edges=0;
 while(input>>a>>b){ids.insert(a);ids.insert(b);edges++;}
 if(edges!=84||ids.size()!=51)throw runtime_error("expected 84 edges/51 endpoint caches");
 cout<<"K total_visited depth6_visited depth6_doomed depth6_unique_full_core max_exact_horizon_depth depth\n";
 for(int id:ids){
  vector<const RootData*>d;vector<vector<pair<int,int>>>opts(24);
  for(int r:{3,5,6,7}){auto&t=table(r,cases[id]);d.push_back(&t);for(int j=0;j<(int)t.labels.size();j++)opts[t.labels[j]].push_back({(int)d.size()-1,j});}
  for(int l=0;l<24;l++)if(opts[l].empty())throw runtime_error("unassignable demand");
  auto mincost=[&](int l){int z=INF;for(auto[r,j]:opts[l])z=min(z,d[r]->dp[1<<j]);return z;};
  vector<int>order(24);iota(order.begin(),order.end(),0);
  sort(order.begin(),order.end(),[&](int x,int y){
   if(opts[x].size()!=opts[y].size())return opts[x].size()<opts[y].size();
   if(mincost(x)!=mincost(y))return mincost(x)>mincost(y);
   return x<y;
  });
  array<int,4>acc{};map<int,int>visited,doomed,full_hor;int vmax=0,vdepth=-1;
  auto dfs=[&](auto&&self,int depth)->void{
   int lb=0;for(int r=0;r<4;r++)lb+=d[r]->dp[acc[r]];
   visited[depth]++;
   if(lb>B || depth==24)return;
   vector<int>remaining(order.begin()+depth,order.end());
   if(depth>=1 && depth<=23){
    int exact=eval(d,opts,acc,remaining);
    if(exact>B){
     doomed[depth]++;bool alldel=true;
     for(int omitted:remaining){
      vector<int>small;for(int l:remaining)if(l!=omitted)small.push_back(l);
      if(eval(d,opts,acc,small)>B){alldel=false;break;}
     }
     if(alldel){
      full_hor[depth]++;if((int)remaining.size()>vmax){vmax=remaining.size();vdepth=depth;}
      if((id==32279&&remaining.size()==7)||(id==32315&&remaining.size()==5)){
       cerr<<"WITNESS K="<<id<<" depth="<<depth<<" lb="<<lb<<" full="<<exact<<" masks=";
       for(int r=0;r<4;r++){uint32_t m=0;for(int j=0;j<(int)d[r]->labels.size();j++)if(acc[r]>>j&1)m|=1U<<d[r]->labels[j];cerr<<m<<(r<3?",":"");}
       cerr<<" future=";for(int l:remaining)cerr<<l<<",";cerr<<"\n";
      }
     }
    }
   }
   int l=order[depth];
   for(auto[r,j]:opts[l]){acc[r]|=1<<j;self(self,depth+1);acc[r]&=~(1<<j);}
  };
  dfs(dfs,0);
  int total=0;for(auto [h,n]:visited)total+=n;
  cout<<id<<" "<<total<<" "<<visited[6]<<" "<<doomed[6]<<" "<<full_hor[6]<<" "<<vmax<<" "<<vdepth;
  for(auto [dep,n]:doomed)cout<<" d"<<dep<<":"<<n<<"/"<<full_hor[dep];
  cout<<"\n";
 }
}
