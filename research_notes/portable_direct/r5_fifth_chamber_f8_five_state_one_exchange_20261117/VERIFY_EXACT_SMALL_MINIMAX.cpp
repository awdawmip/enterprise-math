// Exact finite minimax for <=12 named hypotheses and f<=14 unmarked corruptions.
#include <vector>
#include <string>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
using namespace std;
struct A { int k; vector<unsigned> m; };
int n,f;
vector<A> acts;
unordered_map<uint64_t,int> memo;
int V(uint64_t state) {
  int alive=0;
  for(int h=0;h<n;h++) alive+=((state>>(h*4)&15)<=f);
  if(alive<=1) return 0;
  auto it=memo.find(state);
  if(it!=memo.end()) return it->second;
  int best=INT32_MAX/2;
  for(auto const &act:acts){
    if(act.k>=best) continue;
    bool loop=false; int worst=0;
    for(auto mask:act.m){
      uint64_t next=state;
      for(int h=0;h<n;h++){
        int e=(state>>(4*h))&15;
        if(e<=f && !(mask>>h&1)) next+=uint64_t(1)<<(4*h);
      }
      if(next==state){loop=true;break;}
      int c=V(next);
      if(c>worst) worst=c;
      if(worst+act.k>=best) break;
    }
    if(!loop) best=min(best,act.k+worst);
  }
  memo.emplace(state,best);
  return best;
}
int main(int argc,char **argv){
  if(argc<3) return 2;
  ifstream a(argv[1]);int ac;
  if(!(a>>n>>ac)) return 2;
  f=atoi(argv[2]);
  if(n>12||f>14||n<2||f<0) return 2;
  for(int i=0;i<ac;i++){
    A q;int c;a>>q.k>>c;
    for(int j=0;j<c;j++){unsigned m;a>>m;q.m.push_back(m);}
    acts.push_back(move(q));
  }
  int ans=V(0);
  cout<<"EXACT_RESTRICTED n="<<n<<" f="<<f<<" V="<<ans
      <<" states="<<memo.size()<<" actions="<<ac<<"\n";
}
