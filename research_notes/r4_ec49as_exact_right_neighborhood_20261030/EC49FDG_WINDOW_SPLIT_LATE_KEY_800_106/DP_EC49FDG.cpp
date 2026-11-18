// Exact integer subset-mask dynamic programming on a native signed-prefix Trie.
// Scientific frozen model is constructed by VERIFY_EC49FDG.py; no approximation.
#include <bits/stdc++.h>
using namespace std;
using State=pair<uint32_t,uint16_t>;
int main(int argc,char**argv){
 if(argc<2||argc>3){cerr<<"usage: dp trie [upper]\n";return 2;}
 ifstream in(argv[1]); if(!in) return 2;
 int n,k,fixed; in>>n>>k>>fixed;
 int upper=(argc==3)?stoi(argv[2]):158;
 if(!in || n<1||k<1||k>24 || fixed>upper) return 3;
 const int N=1<<k, cap=upper-fixed, INF=1e9;
 vector<vector<int>> children(n);vector<uint8_t> edge(n);vector<uint32_t> terminal(n);
 for(int i=0;i<n;++i){
   int p,e,t;in>>p>>e>>t;
   if(!in||e<0||e>1||t<0||t>=N||(i>0&&(p<0||p>=i)))return 4;
   if(i) children[p].push_back(i);
   edge[i]=e;terminal[i]=t;
 }
 vector<vector<State>> dp(n);vector<int> best(N,INF);vector<uint32_t> touched;
 uint64_t inspected=0,compatible=0;size_t peak=0;
 for(int v=n-1;v>=0;--v){
   auto &q=dp[v];int t=terminal[v];
   for(int m=t;;m=(m-1)&t){q.emplace_back(m,0);if(!m)break;}
   for(int u:children[v]){
     auto &d=dp[u];
     for(const auto&a:q)for(const auto&b:d){
       ++inspected;
       if(a.first&b.first) continue;
       ++compatible;
       int cost=a.second+b.second+(b.first?edge[u]:0);
       if(cost>cap)continue;
       uint32_t mask=a.first|b.first;
       if(best[mask]==INF){best[mask]=cost;touched.push_back(mask);}
       else if(cost<best[mask])best[mask]=cost;
     }
     q.clear();q.reserve(touched.size());
     for(uint32_t mask:touched){q.emplace_back(mask,best[mask]);best[mask]=INF;}
     touched.clear();vector<State>().swap(d);
   }
   peak=max(peak,q.size());
 }
 int value=INF;
 for(auto [m,c]:dp[0])if(m==N-1)value=min(value,(int)c);
 cout<<"{\"trie_nodes\":"<<n<<",\"labels\":"<<k<<",\"fixed_edges\":"<<fixed
 <<",\"new_edges_optimal\":"<<(value==INF?-1:value)
 <<",\"total_exact_optimum\":"<<(value==INF?-1:fixed+value)
 <<",\"inspected_pairs\":"<<inspected<<",\"compatible_pairs\":"<<compatible
 <<",\"peak_states\":"<<peak<<",\"cap\":"<<upper<<"}\n";
 return value==INF?5:0;
}
