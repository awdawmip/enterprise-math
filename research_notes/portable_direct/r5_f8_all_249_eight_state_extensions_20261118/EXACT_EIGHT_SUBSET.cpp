#include <bits/stdc++.h>
using namespace std;
struct Action {int cost;vector<unsigned char> supports;};
int n,F,dead; vector<Action> acts;
unordered_map<uint64_t,int> memo;
int eval(uint64_t state) {
 auto it=memo.find(state); if(it!=memo.end()) return it->second;
 int live=0;for(int i=0;i<n;i++) live+=((state>>(4*i)&15)<=F);
 if(live<=1) return 0;
 int best=INT_MAX/4;
 for(auto &a:acts){
  vector<uint64_t> nxts; nxts.reserve(a.supports.size());
  bool loop=false;
  for(unsigned m:a.supports){
   uint64_t nxt=state;
   for(int i=0;i<n;i++){
    int x=(state>>(4*i))&15;
    if(x<=F && !(m&(1u<<i))) nxt+=(1ULL<<(4*i));
   }
   if(nxt==state){loop=true;break;}
   if(find(nxts.begin(),nxts.end(),nxt)==nxts.end()) nxts.push_back(nxt);
  }
  if(loop) continue;
  int mxcost=0;
  for(uint64_t s:nxts){
   int c=eval(s);
   if(c>mxcost)mxcost=c;
   if(a.cost+mxcost>=best)break;
  }
  best=min(best,a.cost+mxcost);
 }
 if(best>=INT_MAX/4){cerr<<"NO_FINITE_SOLUTION state "<<state<<"\n";exit(2);}
 memo[state]=best;return best;
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 if(!(cin>>n>>F)){cerr<<"BAD_HEADER";return 2;}
 dead=F+1;
 if(n!=8 || F!=8) return 2;
 int na;cin>>na;acts.reserve(na);
 for(int j=0;j<na;j++){
  Action a;int sz;cin>>a.cost>>sz;
  for(int i=0;i<sz;i++){int m;cin>>m;a.supports.push_back((unsigned char)m);}
  acts.push_back(move(a));
 }
 auto t=chrono::steady_clock::now();memo.reserve(1000000);
 int val=eval(0);
 cout<<"EXACT cost="<<val<<" states="<<memo.size()<<" actions="<<na<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
 return 0;
}
