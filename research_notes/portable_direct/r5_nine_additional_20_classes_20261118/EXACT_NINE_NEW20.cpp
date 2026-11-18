// Exact nine-slot f-error minimax Bellman solver used for NEW20 results.
// Input: n F, number of actions, then for each action physical cost,
// number of maximal supports and support masks. All arithmetic exact integers.
// Original previous solver: R5 nine_pair_endpoint_quotient @0470362186.
// This variant only reorders child search states to reduce search work.
#include <bits/stdc++.h>
using namespace std;
struct Action {int cost; vector<uint16_t> supports;};
int n,F;vector<Action> acts;
unordered_map<uint64_t,int> memo;
uint64_t calls=0;size_t maxstates=12000000;
int eval(uint64_t state){
 auto it=memo.find(state); if(it!=memo.end()) return it->second;
 int live=0;for(int i=0;i<n;i++)live+=((state>>(4*i)&15)<=F);
 if(live<=1)return 0;
 if(memo.size()>maxstates){cerr<<"LIMIT memo="<<memo.size()<<" calls="<<calls<<"\n";exit(3);}
 int best=INT_MAX/4;
 for(auto &a:acts){
  vector<uint64_t> nxts; nxts.reserve(a.supports.size());bool loop=false;
  for(uint16_t m:a.supports){uint64_t nxt=state;
   for(int i=0;i<n;i++){int x=(state>>(4*i))&15;if(x<=F && !(m&(1u<<i)))nxt+=(1ULL<<(4*i));}
   if(nxt==state){loop=true;break;}
   if(find(nxts.begin(),nxts.end(),nxt)==nxts.end())nxts.push_back(nxt);
  }
  if(loop)continue;
  // Order only, not pruning: highest live residual budget first.
  sort(nxts.begin(),nxts.end(),[&](uint64_t a,uint64_t b){
   int sa=0,sb=0;
   for(int i=0;i<n;i++){
    int x=(a>>(4*i))&15,y=(b>>(4*i))&15;
    if(x<=F)sa+=16-x;
    if(y<=F)sb+=16-y;
   }
   return sa>sb;
  });
  int mx=0;
  for(uint64_t s:nxts){int c=eval(s);mx=max(mx,c);if(a.cost+mx>=best)break;}
  best=min(best,a.cost+mx);
 }
 if(best>=INT_MAX/4){cerr<<"NO_FINITE_SOLUTION "<<state<<"\n";exit(2);}
 memo[state]=best;calls++;return best;
}
int main(int argc,char**argv){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 if(!(cin>>n>>F))return 2;
 int na;cin>>na;
 for(int j=0;j<na;j++){
  Action a;int sz;cin>>a.cost>>sz;
  for(int i=0;i<sz;i++){int m;cin>>m;a.supports.push_back((uint16_t)m);}
  acts.push_back(move(a));
 }
 auto t=chrono::steady_clock::now();memo.reserve(1000000);
 int val=eval(0);
 cout<<"EXACT cost="<<val<<" states="<<memo.size()
     <<" actions="<<na<<" time="
     <<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
}
