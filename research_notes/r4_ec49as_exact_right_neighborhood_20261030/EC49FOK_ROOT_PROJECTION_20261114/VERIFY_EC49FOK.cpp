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


int main(int argc,char**argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 if(argc!=4){cerr<<"usage: verify_fok edges.txt FOJ_edge_first_separation.csv result.csv < frozen_master.txt\n";return 2;}
 int nk,nw,nc;cin>>nk>>nw>>nc;
 if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("frozen input dimensions changed");
 words.resize(nk);
 for(int k=0;k<nk;k++){int n;cin>>n;for(int j=0;j<n;j++){int l;string s;cin>>l>>s;words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});}}
 vector<vector<int>> cases(nc,vector<int>(7));for(auto&v:cases)for(auto&k:v)cin>>k;
 ifstream f(argv[1]);if(!f)throw runtime_error("missing edge file");
 vector<pair<int,int>> edges;set<int> ids;int a,b;
 while(f>>a>>b){edges.push_back({a,b});ids.insert(a);ids.insert(b);}
 if(edges.size()!=84||ids.size()!=51)throw runtime_error("unexpected edge/domain count");
 map<pair<int,int>,int> parent;ifstream fs(argv[2]);if(!fs)throw runtime_error("missing independent FOJ baseline");
 string line;getline(fs,line);if(line!="src,dst,first_separation_threshold")throw runtime_error("FOJ schema mismatch");
 while(getline(fs,line)){replace(line.begin(),line.end(),',',' ');istringstream ss(line);int x,y,t;if(!(ss>>x>>y>>t))throw runtime_error("bad FOJ row");parent[{x,y}]=t;}
 if(parent.size()!=84)throw runtime_error("bad FOJ baseline size");
 struct Case{array<const RootData*,4> roots;array<vector<int>,24> opts;};
 map<int,Case> cfg;
 for(int id:ids){
  Case c{};
  for(int r=0;r<4;r++){c.roots[r]=&table(array<int,4>{3,5,6,7}[r],cases[id]);for(int l:c.roots[r]->labels)c.opts[l].push_back(r);}
  for(auto&v:c.opts)if(v.empty())throw runtime_error("missing legal root");
  cfg.emplace(id,move(c));
 }
 ofstream out(argv[3]);if(!out)throw runtime_error("cannot create output CSV");
 out<<"src,dst,same_legal_domain,projected_equal,first_sep_FOJ,rooted_table_diff_total,projected_cost_diff_total,root03_masks,root05_masks,root06_masks,root07_masks,root03_proj_diff,root05_proj_diff,root06_proj_diff,root07_proj_diff\n";
 int stable=0,passes=0,failures=0,hidden=0;long long compared=0;
 for(auto [a,b]:edges){
  auto&A=cfg.at(a),&B=cfg.at(b);
  bool same=A.opts==B.opts;int whole=0,visible=0;
  array<int,4> counts{},changed{};
  if(same){
   stable++;
   for(int r=0;r<4;r++){
    const auto&x=*A.roots[r],&y=*B.roots[r];if(x.labels!=y.labels||x.dp.size()!=y.dp.size())throw runtime_error("root profile domain mismatch");
    for(int mask=0;mask<(int)x.dp.size();mask++)whole+=(x.dp[mask]!=y.dp[mask]);
    int mandatory=0;vector<int>optional;
    for(int j=0;j<(int)x.labels.size();j++){
      int l=x.labels[j];if(A.opts[l].size()==1)mandatory|=1<<j;else optional.push_back(j);
    }
    counts[r]=1<<optional.size();
    for(int sub=0;sub<counts[r];sub++){
      int m=mandatory;for(int i=0;i<(int)optional.size();i++)if(sub>>i&1)m|=1<<optional[i];
      if(x.dp[m]!=y.dp[m])changed[r]++;
    }
    visible+=changed[r];compared+=counts[r];
   }
   bool eq=visible==0;
   passes+=eq;failures+=!eq;hidden+=eq&&whole>0;
   if(eq!=(parent.at({a,b})==-1))throw runtime_error("contradicts FOJ full assignment census");
  }
  out<<a<<","<<b<<","<<same<<","<<(same?int(visible==0):-1)<<","<<parent.at({a,b})<<","<<whole<<","<<visible;
  for(int v:counts)out<<","<<v;for(int v:changed)out<<","<<v;out<<"\n";
  if((a==32315 && b==32308)||(a==32315 && b==32324))
   cerr<<"HIDDEN_PROFILE "<<a<<"->"<<b<<" full_root_mask_diffs="<<whole<<" projected_diffs="<<visible
       <<" projected_masks="<<accumulate(counts.begin(),counts.end(),0)<<"\n";
 }
 if(stable!=82||passes!=32||failures!=50||hidden!=2||compared!=13776)throw runtime_error("frozen test census changed");
 cerr<<"EC49FOK_EXACT_PASS stable_edges="<<stable<<" projection_equal="<<passes
     <<" projection_different="<<failures<<" domain_change=2 hidden_profile_edges="<<hidden
     <<" projected_root_comparisons="<<compared<<" cached_root_profiles="<<cache.size()<<"\n";
}
