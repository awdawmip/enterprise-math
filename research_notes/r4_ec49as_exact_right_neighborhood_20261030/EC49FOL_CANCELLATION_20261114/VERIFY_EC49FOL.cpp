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


// EC49FOL: complete-assignment cancellation and first-separation census.
// Same frozen input and exact native signed-prefix root DP as EC49FOK.
// ./verify_fol edges.txt FOJ_reference.csv results.csv < frozen_master.txt
struct Config {
    array<const RootData*,4> rooted{};
    array<vector<int>,24> legal{};
    array<array<int,24>,4> bit{};
};
struct Census {
    long long assignments=0, equal_total=0, changed_total=0;
    long long nonzero_component=0, cancel=0, mixed_nonzero=0;
    int first=INF, first_a=INF, first_b=INF;
    int max_abs_cancel=0;
    string first_example, cancel_example;
};
string encoding(const array<int,24>&a){
    string s;for(int l=0;l<24;l++){if(l)s+=' ';s+=to_string(a[l]);}return s;
}
int main(int argc,char**argv) {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    if(argc!=4)throw runtime_error("Expected edge_file FOJ_reference output_file");
    int nk,nw,nc;cin>>nk>>nw>>nc;
    if(nk!=94||nw!=178850||nc!=38169)throw runtime_error("Unexpected frozen source shape");
    words.resize(nk);
    for(int k=0;k<nk;k++){
        int n;cin>>n;
        for(int j=0;j<n;j++){
            int l;string s;cin>>l>>s;
            words[k].push_back({l,stoi(s.substr(0,2),nullptr,16),s});
        }
    }
    vector<array<int,7>> cases(nc);
    for(auto&v:cases)for(auto &k:v)cin>>k;
    ifstream es(argv[1]);if(!es)throw runtime_error("Missing original edges");
    vector<pair<int,int>> edges;set<int> ids;int a,b;
    while(es>>a>>b){edges.push_back({a,b});ids.insert(a);ids.insert(b);}
    if(edges.size()!=84||ids.size()!=51)throw runtime_error("Frozen edge census mismatch");
    ifstream fs(argv[2]);if(!fs)throw runtime_error("Missing original FOJ table");
    string line;getline(fs,line);
    if(line!="src,dst,first_separation_threshold")throw runtime_error("Unexpected original FOJ table schema");
    map<pair<int,int>,int> original;
    while(getline(fs,line)){
        replace(line.begin(),line.end(),',',' ');
        istringstream ss(line);int x,y,z;
        if(!(ss>>x>>y>>z))throw runtime_error("Malformed FOJ row");
        original[{x,y}]=z;
    }
    if(original.size()!=84)throw runtime_error("Missing FOJ edges");
    const array<int,4> R{3,5,6,7};
    map<int,Config> cfg;
    for(int id:ids){
        Config c;
        for(int r=0;r<4;r++){
            c.rooted[r]=&table(R[r],vector<int>(cases[id].begin(),cases[id].end()));
            c.bit[r].fill(-1);
            for(int j=0;j<(int)c.rooted[r]->labels.size();j++){
                int l=c.rooted[r]->labels[j]; c.legal[l].push_back(r); c.bit[r][l]=1<<j;
            }
        }
        for(const auto& l:c.legal)if(l.empty())throw runtime_error("Illegal empty demand domain");
        cfg[id]=move(c);
    }
    ofstream csv(argv[3]);
    if(!csv)throw runtime_error("Cannot open output file");
    csv<<"src,dst,same_domain,assignments,changed_total,equal_total,nonzero_root_delta,canceled_nonzero,mixed_sign_nonzero,first_cost_separation,foj_first,max_abs_cancel,first_witness_root_deltas,cancel_witness_root_deltas\n";
    auto exactMap=[&](const Config &q){
        map<uint64_t,int> costs;
        array<int,4> masks{};
        function<void(int,uint64_t)> rec=[&](int l,uint64_t code){
            if(l==24){
                int cost=0;
                for(int r=0;r<4;r++)cost+=q.rooted[r]->dp[masks[r]];
                costs.emplace(code,cost);
                return;
            }
            for(int r:q.legal[l]){
                masks[r]|=q.bit[r][l];rec(l+1,code|((uint64_t)r<<(2*l)));
                masks[r]^=q.bit[r][l];
            }
        };
        rec(0,0);
        return costs;
    };
    long long total_assignments=0,all_canceled=0,all_changed=0;
    int identical=0,finite=0,scope_domain_change=0, edges_with_cancel=0, edges_with_mixed=0;
    for(const auto& [src,dst]:edges){
        const Config&A=cfg.at(src),&B=cfg.at(dst);
        if(A.legal!=B.legal){
            scope_domain_change++;
            auto ma=exactMap(A),mb=exactMap(B);
            int separate=INF;uint64_t witness=0;
            for(auto [key,cost]:ma){
                auto it=mb.find(key);
                if(it==mb.end()||it->second!=cost){
                    int first_cost=it==mb.end()?cost:min(cost,it->second);
                    if(first_cost<separate){separate=first_cost;witness=key;}
                }
            }
            for(auto [key,cost]:mb)if(ma.find(key)==ma.end()&&cost<separate){separate=cost;witness=key;}
            if(separate!=original.at({src,dst}))throw runtime_error("Domain-changing first separation mismatch");
            cerr<<"DOMAIN_CHANGE_EXACT_PASS "<<src<<"->"<<dst<<" domain_A="<<ma.size()
                <<" domain_B="<<mb.size()<<" first="<<separate<<" witness_encoding="<<witness<<"\n";
            csv<<src<<","<<dst<<",0,"<<ma.size()<<":"<<mb.size()<<",0,0,0,0,0,"
               <<separate<<","<<original.at({src,dst})<<",0,NA,NA\n";
            continue;
        }
        Census c;
        array<int,24> assigned{};
        array<int,4> mask{};
        function<void(int)> go = [&](int l) {
            if(l==24){
                array<int,4> d{};int sum=0,ca=0,cb=0;
                bool plus=false,minus=false,nonzero=false;
                for(int r=0;r<4;r++){
                    int x=A.rooted[r]->dp[mask[r]],y=B.rooted[r]->dp[mask[r]];
                    if(x>=INF||y>=INF)throw runtime_error("Unreachable projected cost");
                    d[r]=y-x;sum+=d[r];ca+=x;cb+=y;
                    if(d[r]>0)plus=true;
                    if(d[r]<0)minus=true;
                    nonzero|=d[r]!=0;
                }
                c.assignments++;
                if(plus&&minus)c.mixed_nonzero++;
                if(nonzero){
                    c.nonzero_component++;
                    if(sum==0){
                        c.cancel++;int strength=0;
                        for(int x:d)if(x>0)strength+=x;
                        c.max_abs_cancel=max(c.max_abs_cancel,strength);
                        if(c.cancel_example.empty()){
                            c.cancel_example=to_string(d[0])+":"+to_string(d[1])+":"+to_string(d[2])+":"+to_string(d[3]);
                            cerr<<"CANCEL_WITNESS "<<src<<"->"<<dst<<" roots="<<c.cancel_example<<" assignment="<<encoding(assigned)<<" exact_cost="<<ca<<"\n";
                        }
                    }
                }
                if(sum==0)c.equal_total++;
                else {
                    c.changed_total++;
                    if(min(ca,cb)<c.first){
                        c.first=min(ca,cb);c.first_a=ca;c.first_b=cb;
                        c.first_example=to_string(d[0])+":"+to_string(d[1])+":"+to_string(d[2])+":"+to_string(d[3]);
                    }
                }
                return;
            }
            for(int r:A.legal[l]){
                assigned[l]=R[r]; mask[r]|=A.bit[r][l];
                go(l+1);
                mask[r]^=A.bit[r][l];
            }
        };
        go(0);
        int foj=original.at({src,dst});
        if((c.first==INF?-1:c.first)!=foj)throw runtime_error("First separation differs from FOJ: "+to_string(src)+"->"+to_string(dst)+" computed="+to_string(c.first)+" FOJ="+to_string(foj));
        total_assignments+=c.assignments;all_canceled+=c.cancel;all_changed+=c.changed_total;
        if(c.first==INF)identical++;else finite++;
        edges_with_cancel+=(c.cancel>0);edges_with_mixed+=(c.mixed_nonzero>0);
        csv<<src<<","<<dst<<",1,"<<c.assignments<<","<<c.changed_total<<","<<c.equal_total
           <<","<<c.nonzero_component<<","<<c.cancel<<","<<c.mixed_nonzero<<","<<(c.first==INF?-1:c.first)
           <<","<<foj<<","<<c.max_abs_cancel<<","<<(c.first_example.empty()?"NA":c.first_example)
           <<","<<(c.cancel_example.empty()?"NA":c.cancel_example)<<"\n";
    }
    if(identical!=32||finite!=50||scope_domain_change!=2)throw runtime_error("Unexpected original frontier classification");
    cerr<<"EC49FOL_EXACT_PASS stable_domains=82 all_budget_equal="<<identical<<" differing="<<finite
        <<" domain_changes="<<scope_domain_change<<" assignments="<<total_assignments
        <<" changed_assignments="<<all_changed<<" canceled_components="<<all_canceled
        <<" edges_with_cancellation="<<edges_with_cancel<<" edges_with_mixed_delta="<<edges_with_mixed
        <<" cached_root_profiles="<<cache.size()<<"\n";
}
