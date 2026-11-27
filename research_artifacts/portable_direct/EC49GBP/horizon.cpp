#include <algorithm>
#include <cassert>
#include <chrono>
#include <iostream>
#include <map>
#include <random>
#include <vector>
using namespace std;
using V=vector<int>;
const int INF=1000000;
V raw(const V& c,const V& a){int N=1<<c.size(); V s(N);for(int w=0;w<N;++w){for(int i=0;i<(int)c.size();++i)if(w>>i&1)s[w]+=c[i];for(int e:a)if((w&e)==e)--s[w];}return s;}
V horizons(const V& c,const V& s){int N=s.size(),F=N-1,zero=0;for(int i=0;i<(int)c.size();++i)if(!c[i])zero|=1<<i;V h(N),dp(N);for(int w=0;w<N;++w){int R=F^w;if(R&zero){h[w]=INF;continue;}dp[0]=0;for(int v=R;v;v=(v-1)&R)dp[v]=0; // fill in increasing numeric order via complement
for(int q=R;;q=(q-1)&R){int v=R^q;if(v){int bit=v&-v;int best=dp[v^bit];for(int t=v;t;t=(t-1)&v)if(t&bit)best=max(best,dp[v^t]+1+s[w]-s[w|t]);dp[v]=best;}if(!q)break;}h[w]=dp[R];}return h;}
void observe(const V& s,int d,V& ref){int N=s.size();V g=s;for(int bit=1;bit<N;bit*=2)for(int w=0;w<N;++w)if(!(w&bit))g[w]=min(g[w],g[w|bit]);for(int w=0;w<N;++w){bool keep=true;for(int bit=1;bit<N;bit*=2)if(!(w&bit)&&s[w]>=g[w|bit]){keep=false;break;}if(keep)ref[w]=min(ref[w],d);}}
void change(V& s,int e,int d){int R=(int(s.size())-1)^e;for(int t=R;;t=(t-1)&R){s[t|e]+=d;if(!t)break;}}
V exhaustive(V s,const V& a,long long& states){V ref(s.size(),INF);for(int mask=0;mask<(1<<a.size());++mask){V z=s;for(int i=0;i<(int)a.size();++i)if(mask>>i&1)change(z,a[i],1);observe(z,__builtin_popcount((unsigned)mask),ref);++states;}return ref;}
V two(V s,const V& a,long long& states){map<int,int> m;for(int e:a)++m[e];V ref(s.size(),INF);observe(s,0,ref);++states;for(auto [e,count]:m){change(s,e,1);observe(s,1,ref);++states;for(auto [f,n]:m)if(f>e||(f==e&&count>=2)){change(s,f,1);observe(s,2,ref);++states;change(s,f,-1);}change(s,e,-1);}return ref;}
int main(){auto start=chrono::steady_clock::now();mt19937 rng(49261127);long long states=0,rows=0;for(int k=0;k<1000;++k){int n=1+rng()%6;V c(n),a(rng()%9);for(int& x:c)x=rng()%4;for(int& x:a)x=rng()%(1<<n);V s=raw(c,a),h=horizons(c,s);assert(h==exhaustive(s,a,states));rows+=s.size();}cout<<"random_records=1000 exhaustive_states="<<states<<" threshold_rows="<<rows<<" mismatches=0\n";int n,k;long long records=0,checks=0;states=0;map<int,long long> hist;long long inc=0;while(cin>>n>>k){V c(n),a(k);for(int& x:c)cin>>x;for(int& x:a)cin>>x;V s=raw(c,a),h=horizons(c,s),ref=two(s,a,states);bool more=false;for(int w=0;w<(int)s.size();++w){assert((h[w]<=2?h[w]:INF)==ref[w]);++hist[h[w]];if(h[w]==2)more=true;}inc+=more;checks+=s.size();++records;}cout<<"frozen_records="<<records<<" deletion_states="<<states<<" threshold_rows="<<checks<<" records_with_new_d2="<<inc<<" mismatches=0\n";for(auto [d,count]:hist)cout<<"min_deletion="<<d<<" rows="<<count<<"\n";cout<<"seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";}
