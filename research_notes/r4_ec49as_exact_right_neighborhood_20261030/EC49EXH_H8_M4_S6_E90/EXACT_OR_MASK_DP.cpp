// Exact integer subset-OR group-Steiner DP on signed native-prefix tree.
// Input: N K then N lines: parent, prepaid-edge-flag, terminal-color-bitmask.
// From previously verified EC49EU kernel; no floating-point arithmetic.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
struct Node {int parent,base,mask;vector<int> kids;};
int main(){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int N,K;if(!(cin>>N>>K))return 2;
 if(K>20||N>1000000){cerr<<"bad bounds";return 2;}
 vector<Node> ns(N);
 for(int i=0;i<N;i++){
  cin>>ns[i].parent>>ns[i].base>>ns[i].mask;
  if(i&&ns[i].parent>=0&&ns[i].parent<i)ns[ns[i].parent].kids.push_back(i);
  else if(i){cerr<<"invalid parent";return 2;}
 }
 vector<unordered_map<int,int>> dp(N);
 size_t largest=0;long long conv=0;
 for(int i=N-1;i>=0;--i){
  unordered_map<int,int> state;state.reserve(16);state[0]=0;
  if(ns[i].mask)state[ns[i].mask]=0;
  for(int c:ns[i].kids){
   auto &child=dp[c];unordered_map<int,int> next;
   next.reserve(min(size_t(200000),state.size()*child.size()+1));
   for(auto [m,a]:state)for(auto [n,b]:child){
    ++conv;
    int mm=m|n,v=a+b+(n&&!ns[c].base);
    auto it=next.find(mm);
    if(it==next.end()||v<it->second)next[mm]=v;
   }
   state.swap(next);child.clear();child.rehash(0);
  }
  largest=max(largest,state.size());dp[i]=move(state);
 }
 int full=(1<<K)-1;auto it=dp[0].find(full);
 if(it==dp[0].end()){cout<<"INFEASIBLE\n";return 4;}
 cout<<"PASS min_extra="<<it->second<<" total="<<(it->second+28)
     <<" nodes="<<N<<" colors="<<K<<" largest_states="<<largest
     <<" convolutions="<<conv<<"\n";
}
