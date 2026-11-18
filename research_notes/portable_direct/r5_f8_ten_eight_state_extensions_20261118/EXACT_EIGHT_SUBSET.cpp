#include <bits/stdc++.h>
using namespace std;
struct Action {int cost; vector<unsigned char> supports;};
int n,F,dead;
vector<Action> acts;
unordered_map<uint64_t,int> memo;
int eval(uint64_t state) {
    auto it=memo.find(state);
    if(it!=memo.end()) return it->second;
    int live=0;
    for(int i=0;i<n;i++) live+=((state>>(4*i)&15)<=F);
    if(live<=1) return 0;
    int best=INT_MAX/4;
    for(auto &a:acts) {
        vector<uint64_t> nxts;
        nxts.reserve(a.supports.size());
        bool loop=false;
        for(unsigned mask:a.supports) {
            uint64_t nxt=state;
            for(int i=0;i<n;i++) {
                int x=(state>>(4*i))&15;
                if(x<=F && !(mask&(1u<<i))) nxt+=(1ULL<<(4*i));
            }
            if(nxt==state){loop=true;break;}
            if(find(nxts.begin(),nxts.end(),nxt)==nxts.end())
                nxts.push_back(nxt);
        }
        if(loop) continue;
        int maxcost=0;
        for(uint64_t successor:nxts) {
            int c=eval(successor);
            maxcost=max(maxcost,c);
            if(a.cost+maxcost>=best) break;
        }
        best=min(best,a.cost+maxcost);
    }
    if(best>=INT_MAX/4){
        cerr<<"NO_FINITE_SOLUTION "<<state<<"\n"; exit(2);
    }
    memo[state]=best;
    return best;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    if(!(cin>>n>>F)) return 2;
    dead=F+1;
    if(n>8||F>14) return 2;
    int action_count;cin>>action_count;
    acts.reserve(action_count);
    for(int j=0;j<action_count;j++){
        Action a;int size;cin>>a.cost>>size;
        for(int i=0;i<size;i++){int mask;cin>>mask;a.supports.push_back((unsigned char)mask);}
        acts.push_back(move(a));
    }
    auto t=chrono::steady_clock::now();
    memo.reserve(1000000);
    int value=eval(0);
    cout<<"EXACT cost="<<value<<" states="<<memo.size()
        <<" actions="<<action_count
        <<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()
        <<"\n";
    return 0;
}
