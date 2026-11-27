#include <algorithm>
#include <cassert>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>
using namespace std;
struct Result { vector<int> del,blocks; int rho; };
Result witness(const vector<int>& c,const vector<int>& a,int W){
 int n=c.size(),R=((1<<n)-1)^W;
 for(int i=0;i<n;i++) if((R>>i&1)&&!c[i]) return {{},{},-1};
 vector<int> p,owner,e=a,del,blocks;
 for(int i=0;i<n;i++) if(R>>i&1) for(int k=0;k<c[i];k++) p.push_back(1<<i);
 owner.assign(p.size(),-1); for(int &x:e)x&=R;
 e.push_back(0); int probe=a.size();
 vector<char> seen(p.size()); int reached=0;
 auto dfs=[&](auto&& self,int x)->bool{
  for(int j=0;j<(int)p.size();j++) if((e[x]&p[j])&&!seen[j]){
   seen[j]=1; reached|=p[j];
   if(owner[j]<0||self(self,owner[j])){owner[j]=x;return true;}
  }return false;
 };
 auto augment=[&](int x){fill(seen.begin(),seen.end(),0);reached=0;return dfs(dfs,x);};
 auto remove=[&](int x){auto it=find(owner.begin(),owner.end(),x);assert(it!=owner.end());*it=-1;};
 for(int x=0;x<probe;x++)if(e[x]){
  assert(augment(x)); e[probe]=e[x];
  if(augment(probe)){remove(probe);continue;}
  int V=reached; assert(V&&(e[x]&V)==e[x]);remove(x);del.push_back(x);
  for(int j=0;j<(int)blocks.size();)if(blocks[j]&V){V|=blocks[j];blocks.erase(blocks.begin()+j);j=0;}else j++;
  blocks.push_back(V);
 }
 return {del,blocks,(int)del.size()};
}
long long rows=0,states=0,rejected=0,dualblocks=0; vector<long long> hist(100);
void check(const vector<int>& c,const vector<int>& a){
 int n=c.size(),N=1<<n;vector<int> cap(N),s(N),f(N),dp(N);
 for(int x:a)f[x]++;for(int i=0;i<n;i++)for(int V=0;V<N;V++)if(V>>i&1)f[V]+=f[V^(1<<i)];
 for(int V=1;V<N;V++){int i=__builtin_ctz((unsigned)V);cap[V]=cap[V^(1<<i)]+c[i];}
 for(int V=0;V<N;V++)s[V]=cap[V]-f[V];
 for(int W=0;W<N;W++){
  int R=N-1-W;auto z=witness(c,a,W);rows++;
  bool zero=false;for(int i=0;i<n;i++)if((R>>i&1)&&!c[i])zero=true;
  if(zero){assert(z.rho==-1);continue;}
  assert(z.rho>=0);dp[0]=0;
  for(int V=R; ;V=(V-1)&R){if(!V)break;dp[V]=0;}
  // Ascending numeric order visits every proper submask first.
  for(int V=1;V<N;V++)if((V&R)==V){int i=V&-V;dp[V]=dp[V^i];for(int T=V;T;T=(T-1)&V)if(T&i)dp[V]=max(dp[V],dp[V^T]+1+s[W]-s[W|T]);}
  assert(z.rho==dp[R]);
  vector<char> gone(a.size());for(int x:z.del){assert(!gone[x]&&(a[x]&R));gone[x]=1;}
  // Direct primal and dual certificate validation, independent of augmenting paths.
  for(int V=R;V;V=(V-1)&R){int kept=0;for(int x=0;x<(int)a.size();x++){int E=a[x]&R;if(!gone[x]&&E&&(E&V)==E)kept++;}assert(kept<cap[V]);states++;}
  int unionV=0,pay=0;for(int V:z.blocks){assert(V&&!(V&unionV)&&((V&R)==V));unionV|=V;pay+=1+s[W]-s[W|V];}assert(pay==z.rho);
  hist[z.rho]++;rejected+=z.rho;dualblocks+=z.blocks.size();
 }
}
int main(){
 auto start=chrono::steady_clock::now();mt19937 rng(20261127);
 for(int t=0;t<1000;t++){int n=1+rng()%6,m=rng()%10;vector<int> c(n),a(m);for(int &x:c)x=rng()%4;for(int &x:a)x=rng()%(1<<n);check(c,a);}
 cout<<"random_records=1000 rows="<<rows<<" primal_constraints="<<states<<" rejected="<<rejected<<" dual_blocks="<<dualblocks<<" mismatches=0\n";
 rows=states=rejected=dualblocks=0;fill(hist.begin(),hist.end(),0);
 int n,m,k=0;while(cin>>n>>m){vector<int>c(n),a(m);for(int &x:c)cin>>x;for(int &x:a)cin>>x;check(c,a);k++;}
 cout<<"frozen_records="<<k<<" rows="<<rows<<" primal_constraints="<<states<<" rejected="<<rejected<<" dual_blocks="<<dualblocks<<" mismatches=0\n";
 for(int i=0;i<(int)hist.size();i++)if(hist[i])cout<<i<<" "<<hist[i]<<"\n";
 cout<<"seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
