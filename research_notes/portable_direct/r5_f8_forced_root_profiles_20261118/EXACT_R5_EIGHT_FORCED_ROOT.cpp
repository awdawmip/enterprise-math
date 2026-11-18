// Exact f=8 Bellman solver and forced-first-action cost profile.
// stdin: n f, action_count, then (cost support_count support_mask...).
// Masks are exact subsets of n <= 8 named hypotheses; an action is the
// complete family of inclusion-maximal correct-response supports.
#include <bits/stdc++.h>
using namespace std;
struct Action { int cost; vector<unsigned char> supports; };
int n, F; vector<Action> actions; unordered_map<uint64_t, int> memo;

int evaluate(uint64_t s) {
    auto it=memo.find(s); if(it!=memo.end()) return it->second;
    int live=0;
    for(int i=0;i<n;++i) live+=((s>>(4*i)&15)<=F);
    if(live<=1) return 0;
    int best=INT_MAX/4;
    for(const auto &a:actions) {
        vector<uint64_t> nxts; bool self_loop=false;
        for(unsigned mask:a.supports) {
            uint64_t t=s;
            for(int i=0;i<n;i++) {
                unsigned e=(s>>(4*i))&15;
                if(e<=F && !(mask&(1u<<i))) t+=(1ull<<(4*i));
            }
            if(t==s) { self_loop=true; break; }
            if(find(nxts.begin(),nxts.end(),t)==nxts.end()) nxts.push_back(t);
        }
        if(self_loop) continue; // Only for unrestricted V, not the forced root.
        int worst=0;
        for(uint64_t t:nxts) {
            worst=max(worst,evaluate(t));
            if(a.cost+worst>=best) break;
        }
        best=min(best,a.cost+worst);
    }
    if(best>=INT_MAX/4) { cerr<<"NO_FINITE_STATE "<<s<<"\n"; exit(2); }
    memo.emplace(s,best); return best;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    if(!(cin>>n>>F) || n<2 || n>8 || F<0 || F>14) return 2;
    int action_count; cin>>action_count;
    for(int j=0;j<action_count;j++) {
        Action a; int length; cin>>a.cost>>length;
        for(int i=0;i<length;i++) {
            int mask; cin>>mask;
            if(mask<0 || mask>=(1<<n)) return 2;
            a.supports.push_back(static_cast<unsigned char>(mask));
        }
        actions.push_back(move(a));
    }
    memo.reserve(2000000);
    const int optimum=evaluate(0);
    cout<<"OPT "<<optimum<<" "<<memo.size()<<"\n";
    for(const auto &a:actions) {
        int worst=0;
        for(unsigned mask:a.supports) {
            uint64_t t=0;
            for(int i=0;i<n;i++) if(!(mask&(1u<<i))) t+=(1ull<<(4*i));
            // A compelled first query may leave the initial state unchanged;
            // the continuation is V(0), not an illegal action.
            worst=max(worst,t==0 ? optimum : evaluate(t));
        }
        cout<<a.cost<<" "<<a.cost+worst<<"\n";
    }
    cout<<"STATES "<<memo.size()<<"\n";
}
