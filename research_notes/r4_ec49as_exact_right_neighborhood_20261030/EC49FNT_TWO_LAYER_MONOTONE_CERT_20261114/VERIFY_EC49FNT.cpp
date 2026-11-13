// EC49FNT: native rooted-prefix DP and two-layer monotone cutoff certificate.
// stdin: EC49FNN master_and_radius3_cases.txt; argv[1]: generated first-neutral edges.
// Does not enumerate/optimize complete 24-demand root assignments.
#include <bits/stdc++.h>
using namespace std;
constexpr int INF=1000000000;
struct Word{int label,root;string code;};
struct Node{map<unsigned char,int> next;int labels=0;};
struct RootData{vector<int> labels,dp;};
struct Signature{int root;uint64_t lo,hi;bool operator<(const Signature&b)const{
 return tie(root,lo,hi)<tie(b.root,b.lo,b.hi);}};
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
 for(int key:keys){
  for(const auto&w:words[key])if(w.root==root){containing.push_back(key);break;}
 }
 uint64_t lo=0,hi=0;
 for(int key:containing){
  if(key<64)lo|=1ULL<<key;else hi|=1ULL<<(key-64);
 }
 Signature signature{root,lo,hi};
 auto it=cache.find(signature);
 if(it==cache.end())it=cache.emplace(signature,compute(root,containing)).first;
 return it->second;
}

struct Result {int best,ways,second,visit_nodes=0,pruned=0,leaves=0,all_count=1; map<uint64_t,int> low;};
Result check(int id,const vector<int>&keys,int best,int ways,int second){
  const vector<int> roots={3,5,6,7};
  vector<const RootData*> data;
  for(int r:roots)data.push_back(&table(r,keys));
  vector<vector<pair<int,int>>> opts(24);
  for(int i=0;i<4;i++)for(int j=0;j<(int)data[i]->labels.size();j++)opts[data[i]->labels[j]].push_back({i,j});
  vector<int> order(24);iota(order.begin(),order.end(),0);
  for(int l=0;l<24;l++)if(opts[l].empty())throw runtime_error("missing label");
  sort(order.begin(),order.end(),[&](int x,int y){
    if(opts[x].size()!=opts[y].size())return opts[x].size()<opts[y].size();
    auto mincost=[&](int l){int a=INF;for(auto [r,j]:opts[l])a=min(a,data[r]->dp[1<<j]);return a;};
    if(mincost(x)!=mincost(y))return mincost(x)>mincost(y);
    return x<y;
  });
  Result ans;ans.best=best;ans.ways=ways;ans.second=second;
  for(int l=0;l<24;l++)ans.all_count*=int(opts[l].size());
  vector<int> acc(4,0);
  function<void(int,uint64_t)> dfs=[&](int pos,uint64_t enc){
    ans.visit_nodes++;
    int score=0;for(int k=0;k<4;k++)score+=data[k]->dp[acc[k]];
    if(score>second){ans.pruned++;return;}
    if(pos==24){ans.leaves++;if(!ans.low.emplace(enc,score).second)throw runtime_error("duplicate assignment");return;}
    int lab=order[pos];
    for(auto [r,j]:opts[lab]){acc[r]|=1<<j;dfs(pos+1,enc|uint64_t(r)<<(2*lab));acc[r]&=~(1<<j);}
  };
  dfs(0,0);
  int mini=INF,secondmini=INF,mins=0;
  for(auto [enc,c]:ans.low){if(c<mini){secondmini=mini;mini=c;mins=1;}
    else if(c==mini)mins++;else if(c<secondmini)secondmini=c;}
  if(mini!=best||secondmini!=second||mins!=ways)
    throw runtime_error("low-layer verification fails for "+to_string(id));
  return ans;
}
int main(int argc,char**argv){
  if(argc!=3)throw runtime_error("usage: EC49FNT <edges> <exact-file> < master");
  ios::sync_with_stdio(false);cin.tie(nullptr);
  int nk,nw,ncases;cin>>nk>>nw>>ncases;
  if(nk!=94||nw!=178850||ncases!=38169)throw runtime_error("frozen dimensions changed");
  words.resize(nk);int count=0;
  for(int k=0;k<nk;k++){int n;cin>>n;count+=n;
    for(int j=0;j<n;j++){int l;string s;cin>>l>>s;words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});}}
  if(count!=nw)throw runtime_error("word count changed");
  vector<vector<int>> cases(ncases,vector<int>(7));for(auto &v:cases)for(auto&k:v)cin>>k;
  ifstream f(argv[1]);vector<pair<int,int>> edges;int a,b;
  while(f>>a>>b)edges.push_back({a,b});
  if(edges.size()!=84)throw runtime_error("expected 84 edges");
  ifstream g(argv[2]);map<int,tuple<int,int,int>> costs;string line;
  while(getline(g,line)){stringstream ss(line);int id,c,m,next; if(ss>>id>>c>>m>>next)costs[id]={c,m,next};}
  set<int> ids;for(auto [i,j]:edges){ids.insert(i);ids.insert(j);}
  map<int,Result> results;
  for(int id:ids){auto [c,m,n]=costs.at(id);results[id]=check(id,cases[id],c,m,n);}
  int strong=0,equal=0,weak=0;
  for(auto [i,j]:edges){
    bool identical=true;for(int r:{3,5,6,7})if(table(r,cases[i]).labels!=table(r,cases[j]).labels||table(r,cases[i]).dp!=table(r,cases[j]).dp)identical=false;
    if(identical)strong++;
    bool same=results[i].low==results[j].low;
    if(same)equal++;else weak++;
    cout<<"EDGE "<<i<<' '<<j<<' '<<int(identical)<<' '<<int(same)<<' '
      <<results[i].leaves<<' '<<results[j].leaves<<"\n";
  }
  for(int id:ids){auto const&x=results[id];cout<<"VERTEX "<<id<<' '<<x.best<<' '<<x.ways<<' '<<x.second<<' '
   <<x.all_count<<' '<<x.visit_nodes<<' '<<x.pruned<<' '<<x.leaves<<"\n";}
  cerr<<"EC49FNT_DONE edges="<<edges.size()<<" vertices="<<ids.size()<<" strong="<<strong
     <<" low_equal="<<equal<<" low_unequal="<<weak<<" root_cache="<<cache.size()<<"\n";
}
