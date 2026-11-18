// R5 frozen scalar observer; nine-slot exact f=8 Bellman solver.
// Input: n F; number of actions; cost, maximal support count and support masks per action.
// Every named hypothesis retains its own 4-bit error counter; all arithmetic exact.
#include <bits/stdc++.h>
using namespace std;
struct Action {int cost; vector<uint16_t> supports;};
int n,F;vector<Action> acts;unordered_map<uint64_t,int> memo;
constexpr size_t LIMIT=12000000;
int eval(uint64_t state) {
 auto it=memo.find(state); if(it!=memo.end())return it->second;
 int live=0;for(int i=0;i<n;i++)live+=((state>>(4*i)&15)<=F);
 if(live<=1)return 0;
 if(memo.size()>LIMIT){cerr<<"LIMIT memo="<<memo.size()<<"\n";exit(3);}
 int best=INT_MAX/4;
 for(auto &a:acts) {
  vector<uint64_t> nxts;nxts.reserve(a.supports.size());bool loop=false;
  for(uint16_t mask:a.supports) {
   uint64_t nx=state;
   for(int i=0;i<n;i++){
    int x=(state>>(4*i))&15;
    if(x<=F && !(mask&(1u<<i)))nx+=(1ULL<<(4*i));
   }
   if(nx==state){loop=true;break;}
   if(find(nxts.begin(),nxts.end(),nx)==nxts.end())nxts.push_back(nx);
  }
  if(loop)continue;
  sort(nxts.begin(),nxts.end(),[&](uint64_t aa,uint64_t bb){
   int sa=0,sb=0;
   for(int i=0;i<n;i++){
    int x=(aa>>(4*i))&15,y=(bb>>(4*i))&15;
    if(x<=F)sa+=16-x;
    if(y<=F)sb+=16-y;
   }
   return sa>sb;
  });
  int mx=0;for(uint64_t s:nxts){int c=eval(s);mx=max(mx,c);if(a.cost+mx>=best)break;}
  best=min(best,a.cost+mx);
 }
 if(best>=INT_MAX/4){cerr<<"NO_FINITE_SOLUTION state="<<state<<"\n";exit(2);}
 memo[state]=best;return best;
}
int main() {
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
 cout<<"EXACT cost="<<val<<" states="<<memo.size()<<" actions="<<na
     <<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
}
