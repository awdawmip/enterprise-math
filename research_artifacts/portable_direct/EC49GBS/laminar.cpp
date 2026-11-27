#include <bits/stdc++.h>
using namespace std; using ll=long long;
struct Node{int mask;ll hi,lo=0;};
struct Cert{vector<int> pos;vector<Node> nodes;};
Cert solve(const vector<ll>&c,const vector<int>&a,const vector<ll>&w,int R){
 int n=c.size(),m=a.size(); vector<int>E(m+1),ord(m),pos(m+1,-1),active; vector<vector<int>>occ(n); vector<Node>nodes;
 iota(ord.begin(),ord.end(),0);for(int i=0;i<m;i++)E[i]=a[i]&R;
 stable_sort(ord.begin(),ord.end(),[&](int x,int y){return w[x]>w[y];});
 auto erase=[&](int x){int p=pos[x];if(p>=0){auto&v=occ[p];v.erase(find(v.begin(),v.end(),x));pos[x]=-1;}};
 auto aug=[&](int x){int seen=0;vector<int>q,pred(n,-1);auto push=[&](int y){for(int b=E[y]&~seen;b;b&=b-1){int p=__builtin_ctz((unsigned)b);seen|=1<<p;pred[p]=y;q.push_back(p);}};push(x);for(size_t k=0;k<q.size();k++){int p=q[k];if((ll)occ[p].size()<c[p]){while(p>=0){int y=pred[p],old=pos[y];erase(y);pos[y]=p;occ[p].push_back(y);p=old;}return 0;}for(int y:occ[p])push(y);}return seen;};
 for(int x:ord){if(!E[x])continue;if(aug(x))throw runtime_error("first augmentation");E[m]=E[x];int V=aug(m);if(!V){erase(m);continue;}erase(x);vector<int>hit;for(int j:active)if(nodes[j].mask&V)hit.push_back(j);for(int j:hit)V|=nodes[j].mask;if(hit.size()==1&&V==nodes[hit[0]].mask)continue;for(int j:hit)nodes[j].lo=w[x];active.erase(remove_if(active.begin(),active.end(),[&](int j){return (nodes[j].mask&V)!=0;}),active.end());active.push_back(nodes.size());nodes.push_back({V,w[x],0});}
 pos.pop_back();return {pos,nodes};
}
// Independent verifier: matching plus reverse reachability; interval dual uses only original inputs.
ll verify(const vector<ll>&c,const vector<int>&a,const vector<ll>&w,int R,const Cert&z){
 int n=c.size(),m=a.size();vector<ll>load(n);vector<int>rev(n);ll cost=0,dual=0;int reach=0;
 for(int x=0;x<m;x++){int E=a[x]&R,p=z.pos[x];if(!E){if(p!=-1)throw runtime_error("empty label");continue;}if(p<0){cost+=w[x];continue;}if(p>=n||!(E>>p&1))throw runtime_error("bad assignment");load[p]++;for(int b=E;b;b&=b-1)rev[__builtin_ctz((unsigned)b)]|=1<<p;}
 for(int i=0;i<n;i++)if(R>>i&1){if(load[i]>c[i])throw runtime_error("capacity");if(load[i]<c[i])reach|=1<<i;}
 for(int old=-1;old!=reach;){old=reach;for(int b=old;b;b&=b-1)reach|=rev[__builtin_ctz((unsigned)b)];}if(reach!=R)throw runtime_error("strict Hall");
 if(z.nodes.size()>(size_t)max(0,2*__builtin_popcount((unsigned)R)-1))throw runtime_error("node bound");
 for(size_t j=0;j<z.nodes.size();j++){auto [V,h,l]=z.nodes[j];if(!V||(V&~R)||l<0||h<l)throw runtime_error("interval");for(size_t k=0;k<j;k++){auto t=z.nodes[k];if((V&t.mask)&&max(l,t.lo)<min(h,t.hi))throw runtime_error("overlap");}ll cap=0;for(int i=0;i<n;i++)if(V>>i&1)cap+=c[i];dual-=(cap-1)*(h-l);for(int x=0;x<m;x++){int E=a[x]&R;if(E&&!(E&~V))dual+=max(0LL,min(w[x],h)-l);}}
 if(dual!=cost)throw runtime_error("duality gap");return cost;
}
bool feasible(const vector<ll>&c,const vector<int>&a,int R,int s){for(int V=R;V;V=(V-1)&R){ll t=0;for(int i=0;i<(int)c.size();i++)if(V>>i&1)t+=c[i];for(int x=0;x<(int)a.size();x++)if((s>>x&1)&&(a[x]&R)&&!((a[x]&R)&~V))t--;if(t<1)return false;}return true;}
int main(){mt19937 rng(20261127);ll randomrows=0,subsets=0,rows=0,nodes=0,layernodes=0,nonzero=0,maxnodes=0,weighted=0;for(int t=0;t<1000;t++){int n=1+rng()%6,m=rng()%9,all=(1<<n)-1;vector<ll>c(n),w(m);vector<int>a(m);for(auto&x:c)x=1+rng()%3;for(int i=0;i<m;i++)a[i]=rng()%(all+1),w[i]=rng()%17;for(int R=0;R<=all;R++){auto z=solve(c,a,w,R);ll v=verify(c,a,w,R,z),best=LLONG_MAX;for(int s=0;s<(1<<m);s++){if(feasible(c,a,R,s)){ll cost=0;for(int i=0;i<m;i++)if(!(s>>i&1)&&(a[i]&R))cost+=w[i];best=min(best,cost);}subsets++;}if(v!=best)throw runtime_error("brute");randomrows++;}}
 int n,m;ll record=0;while(cin>>n>>m){vector<ll>c(n),w(m);vector<int>a(m);for(auto&x:c)cin>>x;for(auto&x:a)cin>>x;for(int i=0;i<m;i++)w[i]=(record*13+i*7)%17;record++;int all=(1<<n)-1;for(int R=0;R<=all;R++){auto z=solve(c,a,w,R);ll v=verify(c,a,w,R,z);weighted+=v;nonzero+=v>0;rows++;nodes+=z.nodes.size();maxnodes=max(maxnodes,(ll)z.nodes.size());set<ll>levels;for(int i=0;i<m;i++)if((a[i]&R)&&w[i]>0)levels.insert(w[i]);for(auto q:z.nodes)for(ll h:levels)if(q.lo<h&&h<=q.hi)layernodes++;}}
 cout<<"random_rows="<<randomrows<<" brute_subsets="<<subsets<<"\nfrozen_records="<<record<<" frozen_rows="<<rows<<" nonzero="<<nonzero<<" weighted_sum="<<weighted<<"\nforest_nodes="<<nodes<<" layer_block_entries="<<layernodes<<" max_nodes="<<maxnodes<<" mismatches=0\n";
}
