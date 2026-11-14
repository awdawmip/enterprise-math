// EC49FOI exact author-side terminal observer and first-divergence checker (NOT_REVIEWED).
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

#include <cassert>
struct TraceNode { array<uint32_t,4> assigned{}; int depth=0; bool cut=false; int lb=0; };
struct Config {
 int id;
 array<const RootData*,4> data;
 array<vector<pair<int,int>>,24> opts;
 vector<int> order;
 vector<TraceNode> trace;
 int cuts=0;
};
int getcost(const Config &c,const array<uint32_t,4>&by_label){
 int val=0;
 for(int r=0;r<4;r++){
   int mask=0;
   for(int j=0;j<(int)c.data[r]->labels.size();j++)
     if(by_label[r] & (uint32_t(1)<<c.data[r]->labels[j]))mask|=1<<j;
   if(c.data[r]->dp[mask]>=INF) return INF;
   val+=c.data[r]->dp[mask];
 }
 return val;
}
void prepare(Config &c){
 for(int r=0;r<4;r++)for(int j=0;j<(int)c.data[r]->labels.size();j++)
   c.opts[c.data[r]->labels[j]].push_back({r,j});
 for(int l=0;l<24;l++)if(c.opts[l].empty())throw runtime_error("missing label");
 c.order.resize(24);iota(c.order.begin(),c.order.end(),0);
 auto score=[&](int l){int z=INF;for(auto[r,j]:c.opts[l])z=min(z,c.data[r]->dp[1<<j]);return z;};
 sort(c.order.begin(),c.order.end(),[&](int x,int y){
  if(c.opts[x].size()!=c.opts[y].size())return c.opts[x].size()<c.opts[y].size();
  if(score(x)!=score(y))return score(x)>score(y);
  return x<y;
 });
}
void trace_config(Config &c) {
 array<uint32_t,4> masks{};
 auto dfs=[&](auto&&self,int depth)->void{
   int lb=getcost(c,masks);
   if(lb>=INF)throw runtime_error("source impossible");
   bool cut=lb>155;
   c.trace.push_back({masks,depth,cut,lb});
   c.cuts+=cut;
   if(cut||depth==24)return;
   int l=c.order[depth];
   for(auto[r,j]:c.opts[l]){
     masks[r]|=uint32_t(1)<<l;
     self(self,depth+1);
     masks[r]&=~(uint32_t(1)<<l);
   }
 };
 dfs(dfs,0);
}
struct Certificate {
 bool passed=true, order_eq=true, domains_visited_eq=true, all_sign_eq=true;
 int visited=0, changed_lb=0, changed_cut=0, changed_branch=0, order_mismatch_at_first=-1;
 int max_abs_delta=0;
};
Certificate certify(const Config&A,const Config&B){
 Certificate cert;cert.visited=(int)A.trace.size();
 cert.order_eq=(A.order==B.order);
 for(const auto&n:A.trace){
  int tgt=getcost(B,n.assigned);
  bool cut=tgt>155;
  if(tgt!=n.lb)cert.changed_lb++;
  if(cut!=n.cut){cert.all_sign_eq=false;cert.changed_cut++;}
  if(tgt<INF)cert.max_abs_delta=max(cert.max_abs_delta,abs(tgt-n.lb));
  if(!n.cut && n.depth<24){
   int la=A.order[n.depth], lb=B.order[n.depth];
   if(la!=lb && cert.order_mismatch_at_first<0)cert.order_mismatch_at_first=n.depth;
   vector<int> ra,rb;
   for(auto[r,j]:A.opts[la])ra.push_back(r);
   for(auto[r,j]:B.opts[lb])rb.push_back(r);
   if(la!=lb||ra!=rb){cert.changed_branch++;cert.domains_visited_eq=false;}
  }
 }
 cert.passed=cert.all_sign_eq&&cert.domains_visited_eq;
 return cert;
}
int main(int argc,char**argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 if(argc<2||argc>3){cerr<<"need exact 84-edge file, optional terminal certificate CSV path\n";return 2;}
 int nk,nw,nc;cin>>nk>>nw>>nc; words.resize(nk);
 for(int k=0;k<nk;k++){
  int n;cin>>n;
  for(int j=0;j<n;j++){
   int l;string s;cin>>l>>s;
   words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
  }
 }
 vector<vector<int>>cases(nc,vector<int>(7));
 for(auto&v:cases)for(auto&k:v)cin>>k;
 ifstream edgein(argv[1]);if(!edgein){cerr<<"cannot open edges\n";return 2;}
 vector<pair<int,int>>edges;set<int> ids;
 int a,b;
 while(edgein>>a>>b){edges.push_back({a,b});ids.insert(a);ids.insert(b);}
 if(edges.size()!=84)throw runtime_error("expected 84 edges");
 map<int,Config> configs;
 for(int id:ids){
  Config c{};c.id=id;
  for(int r=0;r<4;r++)c.data[r]=&table(array<int,4>{3,5,6,7}[r],cases[id]);
  prepare(c);trace_config(c);
  configs.emplace(id,move(c));
 }
 cerr<<"CONFIGS "<<configs.size()<<" ROOT_SIGNED_PREFIX_PROFILES "<<cache.size()<<" EDGES "<<edges.size()<<"\n";

 if(argc==3){
  ofstream out(argv[2]);
  if(!out)throw runtime_error("cannot write terminal certificate file");
  out<<"case_id,root03_mask,root05_mask,root06_mask,root07_mask,exact_cost\n";
  for(auto &[id,c]:configs)
   for(const auto&n:c.trace)if(n.depth==24&&!n.cut)
    out<<id<<","<<n.assigned[0]<<","<<n.assigned[1]<<","<<n.assigned[2]<<","<<n.assigned[3]<<","<<n.lb<<"\n";
 }
 cout<<"src,dst,nA,nB,cutA,cutB,exact_trace,order_same,eligibility_same,changed_elig_labels,first_order_depth,order_mismatch_positions,first_trace_diff_index,common_trace_prefix,first_failure_type,first_failure_depth,first_failure_src_trace_idx,src_first_failure_lb,target_first_failure_lb,src_next_label,target_next_label,cut_mismatch_in_A,branch_mismatch_in_A,full_mask_set_same,cut_mask_set_same,full_leaves_same,feasible_leaves_A,feasible_leaves_B,leaf_cost_maps_same,leaf_cost_abs_max,max_rooted_lb_delta\n";
 for(auto[a,b]:edges){
  auto&A=configs.at(a);auto&B=configs.at(b);
  int echange=0;bool elig_same=true;
  for(int l=0;l<24;l++){
    vector<int> ar,br;
    for(auto [r,j]:A.opts[l])ar.push_back(r);
    for(auto [r,j]:B.opts[l])br.push_back(r);
    if(ar!=br){echange++;elig_same=false;}
  }
  int firstorder=-1, odiff=0;
  for(int d=0;d<24;d++)if(A.order[d]!=B.order[d]){odiff++;if(firstorder<0)firstorder=d;}
  int lcp=0;
  while(lcp<(int)A.trace.size()&&lcp<(int)B.trace.size()){
    const auto &x=A.trace[lcp],&y=B.trace[lcp];
    if(x.assigned!=y.assigned||x.depth!=y.depth||x.cut!=y.cut)break;
    lcp++;
  }
  bool same=lcp==(int)A.trace.size()&&lcp==(int)B.trace.size();
  set<array<uint32_t,4>> ma,mb,ca,cb,la,lb;
  for(const auto&n:A.trace){ma.insert(n.assigned);if(n.cut)ca.insert(n.assigned);if(n.depth==24&&!n.cut)la.insert(n.assigned);}
  for(const auto&n:B.trace){mb.insert(n.assigned);if(n.cut)cb.insert(n.assigned);if(n.depth==24&&!n.cut)lb.insert(n.assigned);}
  map<array<uint32_t,4>,int> lac,lbc;
  for(const auto&n:A.trace)if(n.depth==24&&!n.cut)lac[n.assigned]=n.lb;
  for(const auto&n:B.trace)if(n.depth==24&&!n.cut)lbc[n.assigned]=n.lb;
  if(lac!=lbc)throw runtime_error("TERMINAL_COST_MAP_INVARIANCE_FAILED");
  int lcmax=0;
  for(auto[k,v]:lac)if(lbc.count(k))lcmax=max(lcmax,abs(v-lbc[k]));
  int first_bad_idx=-1,depth=-1,costA=-1,costB=-1,labelA=-1,labelB=-1;
  string kind="NONE";
  int cutdiff=0,branchdiff=0,maxdelta=0;
  for(int i=0;i<(int)A.trace.size();i++){
   const auto &n=A.trace[i];
   int vl=getcost(B,n.assigned);
   maxdelta=max(maxdelta,vl>=INF?0:abs(vl-n.lb));
   bool c=n.cut, cb=vl>155;
   bool badcut=(c!=cb);
   bool badbranch=false;
   if(!c&&n.depth<24){
    int nextA=A.order[n.depth],nextB=B.order[n.depth];
    vector<int> ra,rb;
    for(auto[r,j]:A.opts[nextA])ra.push_back(r);
    for(auto[r,j]:B.opts[nextB])rb.push_back(r);
    badbranch=nextA!=nextB||ra!=rb;
   }
   cutdiff+=badcut;branchdiff+=badbranch;
   if(first_bad_idx<0&&(badcut||badbranch)){
    first_bad_idx=i;depth=n.depth;costA=n.lb;costB=vl;
    labelA=depth<24?A.order[depth]:-1;
    labelB=depth<24?B.order[depth]:-1;
    kind=badcut&&badbranch?"BOTH":badcut?"CUT":"BRANCH";
   }
  }
  cout<<a<<","<<b<<","<<A.trace.size()<<","<<B.trace.size()<<","<<A.cuts<<","<<B.cuts<<","<<int(same)<<","<<int(A.order==B.order)<<","<<int(elig_same)<<","<<echange<<","<<firstorder<<","<<odiff<<","<<lcp<<","<<lcp<<","<<kind<<","<<depth<<","<<first_bad_idx<<","<<costA<<","<<costB<<","<<labelA<<","<<labelB<<","<<cutdiff<<","<<branchdiff<<","<<int(ma==mb)<<","<<int(ca==cb)<<","<<int(la==lb)<<","<<la.size()<<","<<lb.size()<<","<<int(lac==lbc)<<","<<lcmax<<","<<maxdelta<<"\n";
 }
}
