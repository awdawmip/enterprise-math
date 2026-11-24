// Exact f-error minimax Bellman solver for <=12 distinct named slots.
// Input: n f ; number-of-actions ; repeated: physical-cost count masks...
// Each mask is inclusion-maximal correct-candidate response support.
// For n=9, masks are 9-bit and counters each occupy 4 bits.
#include <bits/stdc++.h>
using namespace std;
struct Action {int cost;vector<uint16_t> supports;};
int n,F;
vector<Action> acts;
unordered_map<uint64_t,int> memo;
int eval(uint64_t state){
 auto it=memo.find(state);
 if(it!=memo.end())return it->second;
 int live=0;
 for(int i=0;i<n;i++)live+=((state>>(4*i)&15)<=F);
 if(live<=1)return 0;
 int best=INT_MAX/4;
 for(const auto &a:acts){
  vector<uint64_t> nxts;nxts.reserve(a.supports.size());
  bool self_loop=false;
  for(uint16_t mask:a.supports){
   uint64_t nxt=state;
   for(int i=0;i<n;i++){
    int x=(state>>(4*i))&15;
    if(x<=F && !(mask&(1u<<i))) nxt+=(1ULL<<(4*i));
   }
   if(nxt==state){self_loop=true;break;}
   if(find(nxts.begin(),nxts.end(),nxt)==nxts.end())nxts.push_back(nxt);
  }
  if(self_loop)continue; // positive-cost self-loop actions cannot minimize V
  int worst=0;
  for(uint64_t s:nxts){
   int c=eval(s);
   if(c>worst)worst=c;
   if(a.cost+worst>=best)break;
  }
  best=min(best,a.cost+worst);
 }
 if(best>=INT_MAX/4){cerr<<"NO_FINITE_SOLUTION "<<state<<"\n";exit(2);}
 memo[state]=best;return best;
}
int main(){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 if(!(cin>>n>>F)||n<1||n>12||F<0||F>14)return 2;
 int na;if(!(cin>>na)||na<=0)return 2;
 for(int j=0;j<na;j++){
  Action a;int sz;cin>>a.cost>>sz;
  for(int i=0;i<sz;i++){int mask;cin>>mask;a.supports.push_back(uint16_t(mask));}
  acts.push_back(move(a));
 }
 auto t=chrono::steady_clock::now();
 memo.reserve(1000000);
 int cost=eval(0);
 cout<<"EXACT cost="<<cost<<" states="<<memo.size()
     <<" actions="<<na<<" time="
     <<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
}
