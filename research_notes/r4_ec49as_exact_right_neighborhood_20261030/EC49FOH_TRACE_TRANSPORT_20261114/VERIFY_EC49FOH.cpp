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
 if(argc!=2){cerr<<"need exact 84-edge file\n";return 2;}
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
 cout<<"src,dst,src_visits,dst_visits,src_cuts,dst_cuts,full_trace_same,certificate,order_equal,visited_domain_equal,all_cut_sign_equal,changed_lb_on_src,changed_sign_on_src,changed_branch_on_src,first_order_mismatch,max_abs_delta\n";
 int passed=0,actual=0,order=0,sameelig=0;int boundfail=0;
 for(auto[a,b]:edges){
  auto&A=configs.at(a);auto&B=configs.at(b);
  auto cert=certify(A,B);
  bool exact_same=A.trace.size()==B.trace.size();
  if(exact_same)for(size_t i=0;i<A.trace.size();i++){
   auto&x=A.trace[i];auto&y=B.trace[i];
   if(x.depth!=y.depth||x.assigned!=y.assigned||x.cut!=y.cut){exact_same=false;break;}
  }
  if(cert.passed&&!exact_same)throw runtime_error("CERTIFICATE UNSOUND");
  passed+=cert.passed; actual+=exact_same;order+=cert.order_eq;sameelig+=cert.domains_visited_eq;
  if(!cert.all_sign_eq)boundfail++;
  cout<<a<<","<<b<<","<<A.trace.size()<<","<<B.trace.size()<<","<<A.cuts<<","<<B.cuts<<","<<int(exact_same)<<","<<int(cert.passed)<<","<<int(cert.order_eq)<<","<<int(cert.domains_visited_eq)<<","<<int(cert.all_sign_eq)<<","<<cert.changed_lb<<","<<cert.changed_cut<<","<<cert.changed_branch<<","<<cert.order_mismatch_at_first<<","<<cert.max_abs_delta<<"\n";
 }
 cerr<<"PASS "<<passed<<" ACTUAL_SAME "<<actual<<" ORDER_EQUAL "<<order<<" VISITED_ELIGIBILITY_EQUAL "<<sameelig<<" SIGN_FAIL "<<boundfail<<"\n";
}
