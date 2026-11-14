// EC49FOP exact 411-case frozen neighborhood native prefix-profile exporter (NOT_REVIEWED).
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


// EC49FOM exact root-reachable profile exporter, inheriting the immutable FOL native trie-DP.
// ./fom_extract original_84_edges.txt < frozen_master_and_radius3_cases.txt > exact_profiles.csv
int main(int argc,char **argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);if(argc!=2)throw runtime_error("need case-ID file");
 int nk,nw,nc;cin>>nk>>nw>>nc;
 if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("original source mismatch");
 words.resize(nk);
 for(int k=0;k<nk;k++){int n;cin>>n;for(int j=0;j<n;j++){
  int l;string s;cin>>l>>s;words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
 }}
 vector<array<int,7>> cases(nc);
 for(auto &v:cases)for(int &k:v)cin>>k;
 ifstream in(argv[1]);if(!in)throw runtime_error("case-ID file unavailable");
 set<int> ids;int a;
 while(in>>a){if(a<0||a>=nc)throw runtime_error("case ID out of range");ids.insert(a);}
 if(ids.size()!=411)throw runtime_error("radius-two selected case count mismatch");
 const array<int,4> roots{3,5,6,7};
 cout<<"config,root,must,opt,subset,cost\n";
 long long nprofile=0;
 for(int id:ids){
  array<const RootData*,4> p{};
  array<vector<int>,24> dom{};
  for(int i=0;i<4;i++){
   p[i]=&table(roots[i],vector<int>(cases[id].begin(),cases[id].end()));
   for(int l:p[i]->labels)dom[l].push_back(i);
  }
  for(const auto &v:dom)if(v.empty())throw runtime_error("no legal root");
  for(int i=0;i<4;i++){
   const auto &d=*p[i];int must=0,opt=0,local_must=0;vector<int> local_opt;
   for(int j=0;j<(int)d.labels.size();j++){
    int l=d.labels[j];
    if(dom[l].size()==1){must|=1<<l;local_must|=1<<j;}
    else{opt|=1<<l;local_opt.push_back(j);}
   }
   for(int m=0;m<(1<<local_opt.size());m++){
    int mask=local_must,named=0;
    for(int j=0;j<(int)local_opt.size();j++)if(m>>j&1){
     mask|=1<<local_opt[j];named|=1<<d.labels[local_opt[j]];
    }
    int cost=d.dp[mask];if(cost>=INF)throw runtime_error("unreachable rooted cover");
    cout<<id<<","<<roots[i]<<","<<must<<","<<opt<<","<<named<<","<<cost<<"\n";
    nprofile++;
   }
  }
 }
 cerr<<"EC49FOP_EXTRACT_COMPLETE configs="<<ids.size()
     <<" cached_native_root_profiles="<<cache.size()<<" projected_entries="<<nprofile<<"\n";
}
