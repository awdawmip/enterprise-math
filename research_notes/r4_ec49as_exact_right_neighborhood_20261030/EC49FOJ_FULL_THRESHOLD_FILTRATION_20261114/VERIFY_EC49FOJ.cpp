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

// EC49FOJ: exact budget-filtration and 51-case full-assignment map census.
// Reuses the source-frozen EC49FOI native ordered signed-prefix trie DP above.
// The entire legal complete-assignment domain must be enumerated at B=210.
using Terminal = map<array<uint32_t,4>,int>;
struct Sweep {Terminal leaf; long long visits=0,cuts=0;};
Sweep sweep(const Config&c,int budget) {
 Sweep s; array<uint32_t,4> masks{};
 auto dfs=[&](auto&&self,int depth)->void {
  s.visits++;
  int lb=getcost(c,masks);
  if(lb>budget){s.cuts++;return;}
  if(depth==24){s.leaf[masks]=lb;return;}
  int l=c.order[depth];
  for(auto [r,j]:c.opts[l]) {
   masks[r]|=uint32_t(1)<<l;
   self(self,depth+1);
   masks[r]&=~(uint32_t(1)<<l);
  }
 };
 dfs(dfs,0);return s;
}
int main(int argc,char**argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 if(argc!=6){
  cerr<<"usage: VERIFY_EC49FOJ edges.txt 210 edge.csv partition.csv complete.csv < original_master.txt\n";
  return 2;
 }
 int B=stoi(argv[2]);if(B!=210)throw runtime_error("full cost-map check requires threshold 210");
 int nk,nw,nc;cin>>nk>>nw>>nc;
 if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("frozen input dimensions differ");
 words.resize(nk);
 for(int k=0;k<nk;k++) {
  int n;cin>>n;
  for(int j=0;j<n;j++) {
   int l;string s;cin>>l>>s;
   words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
  }
 }
 vector<vector<int>> cases(nc,vector<int>(7));
 for(auto&v:cases)for(auto&k:v)cin>>k;
 ifstream in(argv[1]);if(!in)throw runtime_error("frozen edge file missing");
 vector<pair<int,int>> edges;set<int> ids;int a,b;
 while(in>>a>>b){edges.push_back({a,b});ids.insert(a);ids.insert(b);}
 if(edges.size()!=84||ids.size()!=51)throw runtime_error("frozen edge census mismatch");
 map<int,Config> config;
 for(int id:ids){
  Config c{};c.id=id;
  for(int r=0;r<4;r++)c.data[r]=&table(array<int,4>{3,5,6,7}[r],cases[id]);
  prepare(c);config.emplace(id,move(c));
 }
 map<int,Sweep> all;
 long long total=0;int max_cost=0;
 for(auto &[id,c]:config){
  all[id]=sweep(c,B);
  long long product=1;
  for(int l=0;l<24;l++)product*=c.opts[l].size();
  if(product!=(long long)all[id].leaf.size())throw runtime_error("incomplete legal-assignment enumeration");
  total+=product;
  for(auto [mask,cost]:all[id].leaf)max_cost=max(max_cost,cost);
  cerr<<"CASE "<<id<<" full="<<product<<" visits="<<all[id].visits<<"\n";
 }
 if(total!=34344||max_cost!=195)throw runtime_error("full census mismatch");
 ofstream complete(argv[5]);
 complete<<"case_id,root03_mask,root05_mask,root06_mask,root07_mask,exact_cost\n";
 for(auto &[id,s]:all)for(auto [m,c]:s.leaf)
  complete<<id<<","<<m[0]<<","<<m[1]<<","<<m[2]<<","<<m[3]<<","<<c<<"\n";
 ofstream detail(argv[3]);
 detail<<"src,dst,first_separation_threshold,first_sep_root03_mask,first_sep_root05_mask,first_sep_root06_mask,first_sep_root07_mask,first_sep_cost_src,first_sep_cost_dst,terminals_src_at_Bmax,terminals_dst_at_Bmax,visits_src_at_Bmax,visits_dst_at_Bmax,different_at_Bmax,shared_assignments_cost_different_at_Bmax,symmetric_terminal_assignments_at_Bmax,identical_root_tables\n";
 map<int,int> histogram;int never=0;
 for(auto [a,b]:edges) {
  auto &A=all.at(a),&Z=all.at(b);
  int earliest=INT_MAX,ca=-1,cb=-1;
  array<uint32_t,4> witness{};
  int equal_roots=0,different_shared=0,symmetric=0;
  for(int r=0;r<4;r++)
   if(config.at(a).data[r]->labels==config.at(b).data[r]->labels
      &&config.at(a).data[r]->dp==config.at(b).data[r]->dp)equal_roots++;
  set<array<uint32_t,4>> keys;
  for(auto [k,v]:A.leaf)keys.insert(k);
  for(auto [k,v]:Z.leaf)keys.insert(k);
  for(auto &k:keys){
   auto ia=A.leaf.find(k),ib=Z.leaf.find(k);
   int va=ia==A.leaf.end()?INT_MAX:ia->second;
   int vb=ib==Z.leaf.end()?INT_MAX:ib->second;
   if(va!=vb){
    if(va!=INT_MAX&&vb!=INT_MAX)different_shared++;else symmetric++;
    int t=min(va,vb);
    if(t<earliest){
     earliest=t;witness=k;
     ca=va==INT_MAX?-1:va;
     cb=vb==INT_MAX?-1:vb;
    }
   }
  }
  if(earliest==INT_MAX)never++;else histogram[earliest]++;
  detail<<a<<","<<b<<","<<(earliest==INT_MAX?-1:earliest)<<","
        <<witness[0]<<","<<witness[1]<<","<<witness[2]<<","<<witness[3]<<","
        <<ca<<","<<cb<<","<<A.leaf.size()<<","<<Z.leaf.size()<<","
        <<A.visits<<","<<Z.visits<<","<<int(earliest!=INT_MAX)<<","
        <<different_shared<<","<<symmetric<<","<<equal_roots<<"\n";
 }
 if(never!=32||histogram[156]!=14||histogram[157]!=4||histogram[164]!=30||
    histogram[165]!=1||histogram[171]!=1||histogram[174]!=2)throw runtime_error("edge transition histogram mismatch");
 ofstream out(argv[4]);
 out<<"threshold,class_index,member_count,members,terminal_records\n";
 map<int,int> class_hist;
 for(int threshold:vector<int>{155,156,157,164,165,171,174,195}){
  map<Terminal,vector<int>> grouped;
  for(auto &[id,s]:all){
   Terminal filtered;
   for(auto [m,c]:s.leaf)if(c<=threshold)filtered[m]=c;
   grouped[move(filtered)].push_back(id);
  }
  vector<pair<vector<int>,int>> groups;
  for(auto &[map,members]:grouped)groups.push_back({members,int(map.size())});
  sort(groups.begin(),groups.end(),[](auto&a,auto&b){return a.first.front()<b.first.front();});
  class_hist[threshold]=groups.size();
  for(int i=0;i<(int)groups.size();i++){
   auto &[members,n]=groups[i];
   out<<threshold<<","<<i<<","<<members.size()<<",";
   for(int j=0;j<(int)members.size();j++){if(j)out<<";";out<<members[j];}
   out<<","<<n<<"\n";
  }
 }
 if(class_hist[155]!=5||class_hist[156]!=7||class_hist[157]!=10||
    class_hist[164]!=12||class_hist[165]!=13||class_hist[171]!=14||
    class_hist[174]!=15||class_hist[195]!=15)throw runtime_error("partition mismatch");
 cerr<<"EC49FOJ_EXACT_PASS configs=51 full_assignments=34344 max_cost=195 "
     <<"edges=84 permanent=32 finite_separating=52 full_classes=15\n";
}
