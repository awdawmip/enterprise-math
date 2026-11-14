// EC49FOP: original 94-key signed-prefix BRC rooted-cover DP, exact two-key inventory perturbations.
// Frozen master_and_radius3_cases.txt SHA256:
// cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
// Build: g++ -std=c++17 -O2 VERIFY_EC49FOP_NEIGHBOR_EXTRACT.cpp -o ec49fop
// Run: ./ec49fop < master_and_radius3_cases.txt > EC49FOP_2KEY_PROFILES_ALL.csv
// Author finite computational evidence / NOT_REVIEWED.
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
// EC49FOP exact two-key same-domain neighborhood of baseline case 32315.
int main(){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int nk,nw,nc;cin>>nk>>nw>>nc;
 if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("wrong frozen source");
 words.resize(nk);
 for(int k=0;k<nk;k++){int n;cin>>n;for(int j=0;j<n;j++){
  int l;string s;cin>>l>>s;words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
 }}
 vector<array<int,7>>cases(nc);for(auto&v:cases)for(int&k:v)cin>>k;
 vector<int> baseline(cases[32315].begin(),cases[32315].end());
 array<int,4> roots{3,5,6,7};
 auto domains=[&](const vector<int>&ks){array<int,24> a{};
  for(int k:ks)for(const auto&w:words[k]){
   auto it=find(roots.begin(),roots.end(),w.root);
   if(it==roots.end())throw runtime_error("unexpected root");
   a[w.label]|=1<<(it-roots.begin());
  }
  return a;
 };
 auto domain=domains(baseline);
 vector<tuple<int,int,int,int,vector<int>>>good;
 for(int i=0;i<(int)baseline.size();i++)for(int j=i+1;j<(int)baseline.size();j++){
  int out1=baseline[i],out2=baseline[j];
  for(int in1=0;in1<nk;in1++){
   if(find(baseline.begin(),baseline.end(),in1)!=baseline.end())continue;
   for(int in2=in1+1;in2<nk;in2++){
    if(find(baseline.begin(),baseline.end(),in2)!=baseline.end())continue;
    vector<int> ks=baseline;ks[i]=in1;ks[j]=in2;
    if(domains(ks)==domain)good.push_back({out1,out2,in1,in2,ks});
   }
  }
 }
 if(good.size()!=341)throw runtime_error("two-key neighbor count unexpected "+to_string(good.size()));
 cout<<"out1,out2,in1,in2,root,must,opt,subset,cost\n";
 auto emit=[&](int o1,int o2,int n1,int n2,const vector<int>&ks){
  for(int r:roots){const auto&d=table(r,ks);
   int must=0,opt=0;vector<int>opts;
   for(int j=0;j<(int)d.labels.size();j++){
    int l=d.labels[j];int m=1<<l;
    if(__builtin_popcount(domain[l])==1)must|=m;
    else{opt|=m;opts.push_back(j);}
   }
   for(int q=0;q<(1<<(int)opts.size());q++){
    int mask=0,namedmask=0;
    for(int j=0;j<(int)d.labels.size();j++)if(must>>d.labels[j]&1)mask|=1<<j;
    for(int j=0;j<(int)opts.size();j++)if(q>>j&1){mask|=1<<opts[j];namedmask|=1<<d.labels[opts[j]];}
    int cost=d.dp[mask];if(cost>=INF)throw runtime_error("INF");
    cout<<o1<<","<<o2<<","<<n1<<","<<n2<<","<<r<<","<<must<<","<<opt<<","<<namedmask<<","<<cost<<"\n";
   }
  }
 };
 emit(-1,-1,-1,-1,baseline);
 for(const auto&[o1,o2,n1,n2,ks]:good)emit(o1,o2,n1,n2,ks);
 cerr<<"EC49FOP_TWO_KEY_PASS swaps="<<good.size()<<" cached_root_profiles="<<cache.size()<<"\n";
}
