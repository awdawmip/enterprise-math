// EC49FOO exact C++17 native trie DP. Deterministic integer arithmetic.
// Independently checks the two-key construct via labels OR, min-plus,
// cost 1 per used nonroot prefix node (same recurrence as EC49FOM).
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Node {map<string,int> next; int labels=0;};
struct Trie {
  vector<Node> nodes{1};
  void add(const string &word,int labelbit) {
    int u=0;
    for(size_t j=2;j<word.size();j+=2) {
      string b=word.substr(j,2);
      auto it=nodes[u].next.find(b);
      if(it==nodes[u].next.end()){
        int v=nodes.size();nodes[u].next[b]=v;nodes.push_back({});u=v;
      } else u=it->second;
    }
    nodes[u].labels|=1<<labelbit;
  }
  map<int,int> dp(int u,bool root) const {
    map<int,int> cur{{0,0}};
    if(nodes[u].labels)cur[nodes[u].labels]=0;
    for(const auto &[b,v]:nodes[u].next) {
      auto child=dp(v,false);map<int,int> nxt;
      for(auto [a,ca]:cur)for(auto [c,cc]:child){
        int mask=a|c, sum=ca+cc;
        if(!nxt.count(mask)||sum<nxt[mask])nxt[mask]=sum;
      }
      cur.swap(nxt);
    }
    if(!root)for(auto &[mask,val]:cur)if(mask)val++;
    return cur;
  }
  array<int,4> costs() const {
    auto exact=dp(0,true);array<int,4> result;
    for(int req=0;req<4;req++){
      result[req]=1000000000;
      for(auto [set,cost]:exact)if((set&req)==req)
        result[req]=min(result[req],cost);
    }
    return result;
  }
};
using Codes=array<array<string,2>,2>; // root 06,07; labels 7,13
array<array<int,4>,2> evaluate(const Codes &c){
  array<array<int,4>,2> out;
  for(int root=0;root<2;root++){
    Trie trie;
    for(int lab=0;lab<2;lab++)trie.add(c[root][lab],lab);
    out[root]=trie.costs();
  }
  return out;
}
int main(){
  Codes A={{{"060102","060103"},{"0701","070203"}}};
  Codes B={{{"060203","0601"},{"070102","070103"}}};
  auto a=evaluate(A),b=evaluate(B);
  assert((a[0]==array<int,4>{0,2,2,3}));
  assert((b[0]==array<int,4>{0,2,1,3}));
  assert((a[1]==array<int,4>{0,1,2,3}));
  assert((b[1]==array<int,4>{0,2,2,3}));
  for(int assigned06=0;assigned06<4;assigned06++){
    int ca=a[0][assigned06]+a[1][3^assigned06];
    int cb=b[0][assigned06]+b[1][3^assigned06];
    assert(ca==cb);
    cout<<"assigned_to_06_mask="<<assigned06<<" A="<<ca<<" B="<<cb<<"\n";
  }
  cout<<"PASS native prefix DP: terminal-equal, root-profile-different\n";
}
