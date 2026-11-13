// EC49FNS: original frozen native-prefix rooted-subset DP, local profile census.
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
int main(int argc,char**argv){
 if(argc!=2)throw runtime_error("usage: ROOT_PROFILE_EC49FNS <first-neutral-edges.txt> < master.txt");
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int nk,nw,ncases;cin>>nk>>nw>>ncases;
 if(nk!=94||nw!=178850||ncases!=38169)throw runtime_error("frozen corpus dimensions mismatch");
 words.resize(nk);int count=0;
 for(int k=0;k<nk;k++){
  int n;cin>>n;count+=n;
  for(int j=0;j<n;j++){
   int label;string code;cin>>label>>code;
   words[k].push_back({label,stoi(code.substr(0,2),nullptr,16),code});
  }
 }
 if(count!=nw)throw runtime_error("word count mismatch");
 vector<vector<int>> cases(ncases,vector<int>(7));
 for(auto&v:cases)for(auto&k:v)cin>>k;
 ifstream f(argv[1]);int a,b,total=0,strong=0;
 map<int,pair<int,int>> per_source;
 while(f>>a>>b){
  if(a<32000||a>=33000||b<32000||b>=33000)throw runtime_error("case out of range");
  int matched=0;bool equal=true;int differing_masks=0;
  for(int root:{3,5,6,7}){
   const auto& A=table(root,cases[a]);const auto&B=table(root,cases[b]);
   if(A.labels==B.labels&&A.dp==B.dp)matched++;
   else{
    equal=false;
    if(A.labels!=B.labels)differing_masks=-1;
    else if(differing_masks!=-1){
     for(size_t j=0;j<A.dp.size();j++)differing_masks+=(A.dp[j]!=B.dp[j]);
    }
   }
  }
  total++;strong+=equal;per_source[a].first++;per_source[a].second+=equal;
  cout<<a<<' '<<b<<' '<<int(equal)<<' '<<matched<<' '<<differing_masks<<'\n';
 }
 if(total!=84||strong!=30)throw runtime_error("unexpected exact local-profile census");
 const map<int,pair<int,int>> expected={{32275,{1,1}},{32276,{2,2}},
  {32315,{39,24}},{32318,{39,0}},{32703,{1,1}},{32719,{2,2}}};
 if(per_source!=expected)throw runtime_error("unexpected source-specific local-profile census");
 cerr<<"ROOT_PROFILE_CERT_PASS first_edges="<<total
     <<" identical_root_profiles="<<strong
     <<" nonidentical="<<(total-strong)
     <<" cached_root_subsets="<<cache.size()<<"\n";
}
