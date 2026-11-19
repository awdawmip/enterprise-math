// Independent exact R5 13-label Bellman oracle; 4-bit counter packing.
// Actions are independently reconstructed from frozen integer centers
// at doubled LEFT endpoints; this is not the primary base-(f+2) solver.
#include <vector>
#include <string>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
using namespace std;
struct A{int k;vector<unsigned> m;};
int n,f;vector<A> acts;unordered_map<uint64_t,int> memo;
int V(uint64_t state){
 int alive=0;
 for(int h=0;h<n;h++)alive+=((state>>(h*4)&15)<=f);
 if(alive<=1)return 0;
 auto it=memo.find(state);if(it!=memo.end())return it->second;
 int best=INT32_MAX/2;
 for(auto &act:acts){
  if(act.k>=best)continue;
  bool loop=false;int worst=0;
  for(auto mask:act.m){
   uint64_t next=state;
   for(int h=0;h<n;h++){
    int e=(state>>(4*h))&15;
    if(e<=f && !(mask>>h&1))next+=uint64_t(1)<<(4*h);
   }
   if(next==state){loop=true;break;}
   int c=V(next);if(c>worst)worst=c;
   if(worst+act.k>=best)break;
  }
  if(!loop)best=min(best,act.k+worst);
 }
 memo.emplace(state,best);
 return best;
}
int main(int argc,char**argv){
 if(argc<3)return 2;
 ifstream a(argv[1]);int ac;a>>n>>ac;f=atoi(argv[2]);
 if(!a || n!=13 || f<0 || f>8)return 2;
 for(int i=0;i<ac;i++){
  A q;int c;a>>q.k>>c;
  for(int j=0;j<c;j++){unsigned m;a>>m;q.m.push_back(m);}
  acts.push_back(move(q));
 }
 int res=V(0);
 cout<<"EXACT_RESTRICTED n="<<n<<" f="<<f<<" V="<<res<<" states="<<memo.size()<<" actions="<<ac<<"\n";
}
