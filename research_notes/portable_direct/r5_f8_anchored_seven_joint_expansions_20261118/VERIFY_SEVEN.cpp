// Exact finite R5 restricted unmarked-error minimax, 7 hypotheses x 4-bit counters.
// stdin: n number_of_distinct_actions, then cost support_count support_masks...
// argv[1]: f, at most 14; tested f=8. The sum of live error counts is a DAG rank.
#include <vector>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
#include <climits>
using namespace std;
struct Action { int k; vector<unsigned> masks; };
int n,f;
vector<Action> actions;
unordered_map<uint64_t,int> memo;
int V(uint64_t state) {
  int alive=0;
  for(int h=0;h<n;++h) alive+=((state>>(4*h)&15)<=f);
  if(alive<=1) return 0;
  auto it=memo.find(state);
  if(it!=memo.end()) return it->second;
  int best=INT32_MAX/2;
  for(auto &a:actions){
    if(a.k>=best) continue;
    int worst=0; bool loop=false;
    for(auto support:a.masks){
      uint64_t next=state;
      for(int h=0;h<n;++h){
        int e=(state>>(4*h))&15;
        if(e<=f && !(support>>h&1)) next+=(uint64_t(1)<<(4*h));
      }
      if(next==state){loop=true;break;}
      int v=V(next);
      worst=max(worst,v);
      if(worst+a.k>=best) break;
    }
    if(!loop) best=min(best,a.k+worst);
  }
  memo.emplace(state,best);
  return best;
}
int main(int argc,char**argv){
  if(argc<2) return 2;
  int count;
  if(!(cin>>n>>count)) return 2;
  f=atoi(argv[1]); if(n<=1||n>12||f<0||f>14)return 2;
  for(int i=0;i<count;++i){
    Action a;int length;
    if(!(cin>>a.k>>length))return 2;
    for(int j=0;j<length;++j){unsigned mask;cin>>mask;a.masks.push_back(mask);}
    actions.push_back(move(a));
  }
  int result=V(0);
  cout<<"EXACT_RESTRICTED n="<<n<<" f="<<f<<" V="<<result
      <<" states="<<memo.size()<<" actions="<<count<<"\n";
}
