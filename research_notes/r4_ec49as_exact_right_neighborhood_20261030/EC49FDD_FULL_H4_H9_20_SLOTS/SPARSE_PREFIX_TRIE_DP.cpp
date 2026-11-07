// Exact labelled signed-prefix trie DP, sparse reachable-mask variant.
// Each prefix-edge cost is zero if already supported by fixed original paths;
// otherwise it is one and charged once if at least one chosen word uses the edge.
// Each node's terminal bitmask offers every subset of its available labels.
// All states have nonnegative cost; cap at the original 158-edge witness.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using State=pair<uint32_t,uint16_t>; // (label mask, new-edge cost)
int main(int argc,char**argv){
  if(argc<2||argc>3){cerr<<"usage: sparse_solver trie.txt [upperbound]\n";return 2;}
  ifstream in(argv[1]);if(!in){cerr<<"cannot read input\n";return 2;}
  int n,k,fixed;in>>n>>k>>fixed;
  int upper=(argc==3)?stoi(argv[2]):158;
  if(!in||n<=0||k<1||k>24||fixed<0||fixed>upper){cerr<<"invalid header\n";return 3;}
  int N=1<<k,cap=upper-fixed,INF=1000000000;
  vector<vector<int>> children(n);
  vector<uint8_t> edge(n);
  vector<uint32_t> terminal(n);
  for(int i=0;i<n;i++){
    int p,e,t;in>>p>>e>>t;
    if(!in||e<0||e>1||t<0||t>=N||(i>0&&(p<0||p>=i))){cerr<<"invalid row "<<i<<"\n";return 4;}
    if(i)children[p].push_back(i);
    edge[i]=e;terminal[i]=t;
  }
  vector<vector<State>> dp(n);
  vector<int> best(N,INF);
  vector<uint32_t> touched; touched.reserve(N);
  uint64_t inspected=0,valid_pairs=0;
  size_t peak_states=0;
  for(int v=n-1;v>=0;--v){
    auto &q=dp[v];int t=terminal[v];
    for(int m=t;;m=(m-1)&t){q.emplace_back(m,0);if(!m)break;}
    for(int u:children[v]){
      auto &d=dp[u];
      for(const State &a:q){
        for(const State &b:d){
          ++inspected;
          if(a.first&b.first)continue;
          ++valid_pairs;
          int cost=a.second+b.second+(b.first?edge[u]:0);
          if(cost>cap)continue;
          int mask=a.first|b.first;
          if(best[mask]==INF){best[mask]=cost;touched.push_back(mask);}
          else if(cost<best[mask])best[mask]=cost;
        }
      }
      q.clear();q.reserve(touched.size());
      for(uint32_t mask:touched){q.emplace_back(mask,best[mask]);best[mask]=INF;}
      touched.clear();
      vector<State>().swap(d);
    }
    peak_states=max(peak_states,q.size());
  }
  int value=INF;
  for(auto [mask,cost]:dp[0])if(mask==N-1)value=min(value,(int)cost);
  cout<<"{\"trie_nodes\":"<<n<<",\"variable_slots\":"<<k<<",\"fixed_edges\":"<<fixed
  <<",\"new_edges_optimal\":"<<(value==INF?-1:value)
  <<",\"total_exact_optimum\":"<<(value==INF?-1:fixed+value)
  <<",\"inspected_state_pairs\":"<<inspected<<",\"disjoint_state_pairs\":"<<valid_pairs
  <<",\"peak_node_states\":"<<peak_states<<",\"search_upperbound\":"<<upper<<"}\n";
  return value==INF?5:0;
}
