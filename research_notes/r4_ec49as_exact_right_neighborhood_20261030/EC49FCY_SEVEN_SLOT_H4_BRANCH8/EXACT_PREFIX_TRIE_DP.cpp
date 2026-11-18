// Exact labelled signed-primitive prefix trie dynamic program (EC49FCY).
// Input: first line n,k,|F|; then n lines parent-index, edge-new-cost, terminal-label-mask.
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char **argv) {
  ios::sync_with_stdio(false);cin.tie(nullptr);
  if(argc!=2) {cerr<<"usage: solver trie.txt\n";return 2;}
  ifstream in(argv[1]); if(!in) {cerr<<"input missing\n";return 2;}
  int n,k,fixed; in>>n>>k>>fixed;
  if(!in||k<1||k>12||n<1) return 3;
  int N=1<<k,INF=100000000;
  vector<int> parent(n),edge(n),terminal(n);
  vector<vector<int>> children(n);
  for(int i=0;i<n;i++){
    in>>parent[i]>>edge[i]>>terminal[i];
    if(!in||terminal[i]<0||terminal[i]>=N||(i && (parent[i]<0||parent[i]>=i)))return 4;
    if(i)children[parent[i]].push_back(i);
  }
  vector<vector<int>> dp(n,vector<int>(N,INF));
  long long transitions=0;
  for(int v=n-1;v>=0;v--){
    auto &q=dp[v];int t=terminal[v];
    for(int m=t;;m=(m-1)&t){q[m]=0;if(!m)break;}
    for(int u:children[v]){
      auto &d=dp[u];vector<int> next(N,INF);
      for(int mask=0;mask<N;mask++){
        for(int sub=mask;;sub=(sub-1)&mask){
          int a=q[mask^sub],b=d[sub];
          if(a<INF&&b<INF)next[mask]=min(next[mask],a+b+(sub?edge[u]:0));
          ++transitions;
          if(sub==0)break;
        }
      }
      q.swap(next);
    }
  }
  cout<<"{\"trie_nodes\":"<<n<<",\"variable_slots\":"<<k
      <<",\"fixed_edges\":"<<fixed<<",\"new_edges_optimal\":"<<dp[0][N-1]
      <<",\"total_exact_optimum\":"<<fixed+dp[0][N-1]
      <<",\"dp_transitions\":"<<transitions<<"}\n";
  return 0;
}
