// Exact author-side native rooted signed-prefix BRC / cutoff DFS checker.
// Input: frozen EC49FNS master_and_radius3_cases.txt via stdin.
// Root tables are recomputed; original 1,000 complete optimizations not rerun.
#include <bits/stdc++.h>
using namespace std;
constexpr int INF=1000000000;
struct Word{int label,root;string code;};
struct Node{map<unsigned char,int> next;int labels=0;};
struct RootData{vector<int> labels,dp;};
struct Signature{int root;uint64_t lo,hi;bool operator<(const Signature&b)const{return tie(root,lo,hi)<tie(b.root,b.lo,b.hi);}};
vector<vector<Word>> words;
map<Signature,RootData> cache;
vector<Node> trie;
vector<int> local;
void addpath(const string&s,int label){
 int u=0;
 for(int j=2;j+1<(int)s.size();j+=2){
  int ch=stoi(s.substr(j,2),nullptr,16);
  if(!trie[u].next.count(ch)){
   int v=trie.size();trie[u].next[ch]=v;trie.push_back({});u=v;
  }else u=trie[u].next[ch];
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
struct Obs {long long visits=0, cuts=0, leaves_le=0, leaves_gt=0; int maxdepth=0;};
int main(){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int nk,nw,nc;cin>>nk>>nw>>nc;
 words.resize(nk);
 for(int k=0;k<nk;k++){
  int n;cin>>n;
  for(int j=0;j<n;j++){
   int l;string s;cin>>l>>s;
   words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
  }
 }
 vector<vector<int>>cases(nc,vector<int>(7));for(auto&v:cases)for(auto&k:v)cin>>k;
 const array<int,2> ids={32279,32315};
 array<array<const RootData*,4>,2> data;
 for(int c=0;c<2;c++) for(int r=0;r<4;r++)data[c][r]=&table(array<int,4>{3,5,6,7}[r],cases[ids[c]]);
 auto make_opts=[&](const array<const RootData*,4>&d){
   vector<vector<pair<int,int>>> opts(24);
   for(int r=0;r<4;r++)for(int j=0;j<(int)d[r]->labels.size();j++)opts[d[r]->labels[j]].push_back({r,j});
   return opts;
 };
 array<vector<int>,2> orders;
 for(int c=0;c<2;c++){
  auto opts=make_opts(data[c]);
  auto mincost=[&](int l){int z=INF;for(auto[r,j]:opts[l])z=min(z,data[c][r]->dp[1<<j]);return z;};
  vector<int>order(24);iota(order.begin(),order.end(),0);
  sort(order.begin(),order.end(),[&](int x,int y){
    if(opts[x].size()!=opts[y].size())return opts[x].size()<opts[y].size();
    if(mincost(x)!=mincost(y))return mincost(x)>mincost(y);
    return x<y;
  });
  orders[c]=order;
 }
 cout<<"root_mix order_source visits cuts finished_le155 finished_gt155 maxdepth\n";
 for(int mix=0;mix<16;mix++){
  array<const RootData*,4> d;
  for(int r=0;r<4;r++)d[r]=data[(mix>>r)&1][r];
  auto opts=make_opts(d);
  int uncovered=0;for(int l=0;l<24;l++)if(opts[l].empty())uncovered|=(1<<l);
  if(uncovered){cerr<<"INVALID_HYBRID "<<mix<<" missing_mask="<<uncovered<<"\n";continue;}
  for(int ord=0;ord<2;ord++){
    Obs ob; array<int,4> acc{};
    auto dfs=[&](auto&&self,int depth)->void{
      ob.visits++;ob.maxdepth=max(ob.maxdepth,depth);
      int lb=0;for(int r=0;r<4;r++)lb+=d[r]->dp[acc[r]];
      if(lb>155){ob.cuts++;if(depth==24)ob.leaves_gt++;return;}
      if(depth==24){ob.leaves_le++;return;}
      int l=orders[ord][depth];
      for(auto [r,j]:opts[l]){acc[r]|=1<<j;self(self,depth+1);acc[r]&=~(1<<j);}
    };
    dfs(dfs,0);
    cout<<mix<<" "<<ids[ord]<<" "<<ob.visits<<" "<<ob.cuts<<" "<<ob.leaves_le<<" "<<ob.leaves_gt<<" "<<ob.maxdepth<<"\n";
  }
 }
}
