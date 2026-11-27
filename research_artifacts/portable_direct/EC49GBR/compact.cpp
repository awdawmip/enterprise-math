#include <bits/stdc++.h>
using namespace std; using ll=long long;
struct Out{int rejected=0; long long cost=0; vector<int> keep,blocks;};
Out solve(const vector<ll>& c, const vector<int>& a,const vector<ll>& w,int W,int cap=INT_MAX){
 int n=c.size(),m=a.size(),R=((1<<n)-1)^W; Out o;
 vector<int> E(m+1),pos(m+1,-1),order(m); vector<vector<int>> occ(n);
 for(int i=0;i<m;i++) E[i]=a[i]&R,iota(order.begin()+i,order.begin()+i+1,i);
 stable_sort(order.begin(),order.end(),[&](int i,int j){return w[i]>w[j];});
 auto erase=[&](int x){int p=pos[x];if(p>=0){auto& v=occ[p];v.erase(find(v.begin(),v.end(),x));pos[x]=-1;}};
 auto aug=[&](int x){int reached=0;vector<int> pred(n,-1),q;
  auto push=[&](int y){for(int b=E[y]&~reached;b;b&=b-1){int p=__builtin_ctz((unsigned)b);reached|=1<<p;pred[p]=y;q.push_back(p);}};
  push(x); for(size_t k=0;k<q.size();k++){int p=q[k];if((ll)occ[p].size()<c[p]){while(p>=0){int y=pred[p],old=pos[y];erase(y);pos[y]=p;occ[p].push_back(y);p=old;}return 0;}for(int y:occ[p])push(y);}return reached;
 };
 for(int x:order){if(!E[x])continue; if(aug(x)!=0)throw runtime_error("first augment");E[m]=E[x];int V=aug(m);if(!V){erase(m);o.keep.push_back(x);}else{erase(x);o.rejected++;o.cost+=w[x];for(size_t j=0;j<o.blocks.size();)if(V&o.blocks[j]){V|=o.blocks[j];o.blocks.erase(o.blocks.begin()+j);}else j++;o.blocks.push_back(V);if(o.rejected>cap)break;}}
 return o;
}
bool feasible(const vector<ll>& c,const vector<int>& a,int R,const vector<int>& keep){for(int v=R;v;v=(v-1)&R){ll z=0;for(int i=0;i<(int)c.size();i++)if(v>>i&1)z+=c[i];for(int x:keep)if((a[x]&R)&&!((a[x]&R)&~v))z--;if(z<1)return false;}return true;}
int main(){mt19937 rng(20261127);long long random_rows=0,subsets=0,caprows=0,rows=0,checks=0;map<int,ll> hist;for(int t=0;t<1000;t++){int n=1+rng()%6,m=rng()%9,all=(1<<n)-1;vector<ll> c(n),w(m);vector<int>a(m);for(auto& x:c)x=1+rng()%3;for(int i=0;i<m;i++)a[i]=rng()%(all+1),w[i]=rng()%11;for(int W=0;W<=all;W++){int R=all^W;auto o=solve(c,a,w,W);ll total=0,best=0;for(int i=0;i<m;i++)if(a[i]&R)total+=w[i];for(int s=0;s<(1<<m);s++){vector<int> k;ll val=0;for(int i=0;i<m;i++)if((s>>i&1)&&(a[i]&R))k.push_back(i),val+=w[i];if(feasible(c,a,R,k))best=max(best,val);subsets++;}if(!feasible(c,a,R,o.keep)||o.cost!=total-best)throw runtime_error("weighted");random_rows++;}}
 int n,m;while(cin>>n>>m){vector<ll>c(n),w(m,1);vector<int>a(m);for(auto& x:c)cin>>x;for(auto&x:a)cin>>x;int all=(1<<n)-1;for(int W=0;W<=all;W++){int R=all^W;auto o=solve(c,a,w,W);if(!feasible(c,a,R,o.keep))throw runtime_error("primal");ll dual=0;int unionV=0;for(int V:o.blocks){if(V&unionV)throw runtime_error("overlap");unionV|=V;ll k=1;for(int i=0;i<n;i++)if(V>>i&1)k-=c[i];for(int x:a)if((x&R)&&!((x&R)&~V))k++;dual+=k;}if(dual!=o.rejected)throw runtime_error("dual");hist[o.rejected]++;rows++;checks+=(1LL<<__builtin_popcount((unsigned)R))-1;if(rows%16==0)for(int d=0;d<3;d++){auto z=solve(c,a,w,W,d);if((z.rejected<=d)!=(o.rejected<=d)||z.rejected!=min(o.rejected,d+1))throw runtime_error("cap");caprows++;}}}
 cout<<"weighted_random_rows="<<random_rows<<" brute_subsets="<<subsets<<"\nfrozen_rows="<<rows<<" primal_constraints="<<checks<<" capped_checks="<<caprows<<" mismatches=0\n";for(auto [d,k]:hist)cout<<d<<" "<<k<<"\n";
}
