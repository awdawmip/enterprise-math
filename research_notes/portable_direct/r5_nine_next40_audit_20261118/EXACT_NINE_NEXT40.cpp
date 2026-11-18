// Exact Bellman solver: nine named slots, at most eight arbitrary unmarked errors.
// stdin: n f newline, action_count newline, then cost support_count support_masks...
// Identical maximal-support families are premerged to their least-cost physical k.
#include <bits/stdc++.h>
using namespace std;
struct Action {int cost;vector<uint16_t> supports;};
int n,F;vector<Action> acts;unordered_map<uint64_t,int> memo;
size_t maxstates=12000000;
int eval(uint64_t state){
 auto it=memo.find(state);if(it!=memo.end())return it->second;
 int live=0;for(int i=0;i<n;i++)live+=((state>>(4*i)&15)<=F);
 if(live<=1)return 0;
 if(memo.size()>maxstates){cerr<<"LIMIT memo="<<memo.size()<<"\n";exit(3);}
 int best=INT_MAX/4;
 for(auto&a:acts){vector<uint64_t> nxts;bool loop=false;
  for(uint16_t m:a.supports){uint64_t next=state;
   for(int i=0;i<n;i++){int e=(state>>(4*i))&15;if(e<=F&&!(m&(1u<<i)))next+=(1ULL<<(4*i));}
   if(next==state){loop=true;break;}
   if(find(nxts.begin(),nxts.end(),next)==nxts.end())nxts.push_back(next);
  }
  if(loop)continue;
  sort(nxts.begin(),nxts.end(),[&](uint64_t a,uint64_t b){
   int sa=0,sb=0;for(int i=0;i<n;i++){int x=(a>>(4*i))&15,y=(b>>(4*i))&15;if(x<=F)sa+=16-x;if(y<=F)sb+=16-y;}return sa>sb;});
  int mx=0;for(auto s:nxts){int v=eval(s);mx=max(mx,v);if(a.cost+mx>=best)break;}
  best=min(best,a.cost+mx);
 }
 if(best>=INT_MAX/4){cerr<<"NO_FINITE_SOLUTION state="<<state<<"\n";exit(2);}
 memo[state]=best;return best;
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);if(!(cin>>n>>F))return 2;int na;cin>>na;
 for(int i=0;i<na;i++){Action a;int sz;cin>>a.cost>>sz;for(int j=0;j<sz;j++){int m;cin>>m;a.supports.push_back(m);}acts.push_back(move(a));}
 memo.reserve(1500000);auto t=chrono::steady_clock::now();int v=eval(0);
 cout<<"EXACT cost="<<v<<" states="<<memo.size()<<" actions="<<na<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
}
