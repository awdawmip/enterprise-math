#include <bits/stdc++.h>
using namespace std;using W=uint64_t;using P=pair<W,W>;int pc(W x){return __builtin_popcountll(x);}constexpr int M=25,H=14;
const vector<int> F={23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005};
struct S{W act;array<P,M> c;bool operator==(const S&o)const{return act==o.act&&c==o.c;}};
struct Key{S s;int k;bool operator==(const Key&o)const{return k==o.k&&s==o.s;}};
struct Hash{size_t operator()(const Key&x)const{W z=x.s.act^W(x.k)*0x9e3779b97f4a7c15ULL;for(auto[a,b]:x.s.c){z=(z^(a+0x9e3779b97f4a7c15ULL+(z<<6)+(z>>2)));z=(z^(b+0x9e3779b97f4a7c15ULL+(z<<6)+(z>>2)));}return z;}};
struct Solver{array<W,10> R{};int cap,calls=0;int bin[M+1][M+1]{};unordered_map<Key,int,Hash> mem;Solver(int cc):cap(cc){for(int r=0;r<10;r++)for(int i=0;i<(int)F.size();i++)if(F[i]>>r&1)R[r]|=W(1)<<i;for(int n=0;n<=M;n++){bin[n][0]=1;for(int k=1;k<=n;k++)bin[n][k]=bin[n-1][k-1]+bin[n-1][k];}}
 void norm(S&s){W dead=0,sat=0;for(W v=s.act;v;v&=v-1){W b=v&-v;int n=0;for(auto[x,y]:s.c)n+=!!(x&b);if(n>H)dead|=b;else if(n==H)sat|=b;}s.act&=~dead;for(auto&[a,b]:s.c){a&=s.act;b&=s.act&~sat;}sort(s.c.begin(),s.c.end());}
 S child(const S&s,int r,int j,bool yes){S t=s;auto[a,b]=s.c[j];W rr=R[r];if(yes){t.act&=rr&~a;t.c[j]={0,0};}else{t.act&=~rr|(a|b);t.c[j]={a|(rr&b),b&~rr};}norm(t);return t;}
 long long count(const S&s){long long z=0;for(W v=s.act;v;v&=v-1){W b=v&-v;int h=0,p=0;for(auto[x,y]:s.c){h+=!!(x&b);p+=!!(y&b);}for(int j=0;j<=min(p,H-h);j++)z+=bin[p][j];}return z;}
 int solve(const S&s,int k){long long n=count(s);if(n<=1)return -2;if(!k||n>(1LL<<k))return -1;Key key{s,k};auto it=mem.find(key);if(it!=mem.end())return it->second;if(++calls>cap)throw 1;vector<int> ids,B,A,free;W tight=0;for(W v=s.act;v;v&=v-1){W b=v&-v;int i=__builtin_ctzll(b),a=0,h=0;for(int j=0;j<M;j++){if(s.c[j].first&b)h|=1<<j;if(s.c[j].second&b)a|=1<<j;}int p=pc(a);if(p>k)return mem.emplace(key,-1).first->second;if(p==k)tight|=b;ids.push_back(i);B.push_back(h);A.push_back(h|a);free.push_back(p);}
 if(ids.size()==1)return mem.emplace(key,-3).first->second; // direct variable-column recovery
 // Minimum negative row cover of same-hole strict supersets at each minimal fiber state.
 vector<pair<int,int>> tightNeg;
 for(int i=0;i<(int)ids.size();i++){int p=free[i],u=F[ids[i]],budget=k-p; if(budget>3)continue;
 vector<int> dif;for(int j=0;j<(int)ids.size();j++)if(i!=j&&(B[j]&~B[i])==0&&(B[i]&~A[j])==0&&(F[ids[j]]&u)==u)dif.push_back(F[ids[j]]^u);
 if(dif.empty())continue; int rows=0;for(int z:dif)rows|=z;int best=budget+1,uni=0;
 for(int z=rows;z;z=(z-1)&rows){int c=pc(z);if(c>best||c>budget)continue;bool ok=true;for(int q:dif)if(!(q&z)){ok=false;break;}if(ok){if(c<best){best=c;uni=0;}uni|=z;}}
 if(best>budget)return mem.emplace(key,-1).first->second;
 if(best==budget)tightNeg.push_back({i,uni});}
 struct O{long long score,bal;int q;S a,b;};vector<O> opts;for(int j=0;j<M;j++){if(j&&s.c[j]==s.c[j-1])continue;auto[x,y]=s.c[j];if(tight&~y)continue;for(int r=0;r<10;r++){if(tight&~R[r])continue;bool ok=true;for(auto[i,rows]:tightNeg){int u=F[ids[i]];if(!(((u>>r&1)&&((A[i]^B[i])>>j&1))||((rows>>r&1)&&!(B[i]>>j&1)))){ok=false;break;}}if(!ok)continue;W Y=s.act&R[r]&~x,N=s.act&(~R[r]|x|y);if(!Y||!N)continue;S a=child(s,r,j,true),b=child(s,r,j,false);long long ca=count(a),cb=count(b);if(!ca||!cb||ca+cb!=n||max(ca,cb)>(1LL<<(k-1)))continue;long long score=max(ca,cb);opts.push_back({score, max(pc(a.act),pc(b.act)),r*M+j,a,b});}}
 sort(opts.begin(),opts.end(),[](auto&a,auto&b){return tie(a.score,a.bal,a.q)<tie(b.score,b.bal,b.q);});for(auto&o:opts){if(count(o.a)<count(o.b))swap(o.a,o.b);if(solve(o.a,k-1)!=-1&&solve(o.b,k-1)!=-1)return mem.emplace(key,o.q).first->second;}return mem.emplace(key,-1).first->second;}
 // Normalize actual-label fibers to canonical columns, retaining the label mapping.
 pair<S,array<int,M>> normalize_labels(S s){array<int,M> a; iota(a.begin(),a.end(),0);sort(a.begin(),a.end(),[&](int i,int j){return tie(s.c[i],i)<tie(s.c[j],j);});auto old=s.c;for(int i=0;i<M;i++)s.c[i]=old[a[i]];return {s,a};}
 // verify against actual labeled state list, independently by filtering observed outcomes
 void replay(const vector<pair<int,int>>&states,const S&raw,int k){for(auto[u,h]:states){vector<pair<int,int>> x=states;S s=raw;int rem=k;array<int,M> labs; iota(labs.begin(),labs.end(),0);while(x.size()>1){auto [t,perm]=normalize_labels(s);array<int,M> next;for(int j=0;j<M;j++)next[j]=labs[perm[j]];labs=next;s=t;assert(rem>0);int q=mem.at(Key{s,rem});if(q==-3){int r=__builtin_ctz((unsigned)u);for(int j=0;j<M&&x.size()>1;j++){bool zero=false,one=false;for(auto[v,g]:x){assert(v==u);if(g>>labs[j]&1)zero=true;else one=true;}if(zero&&one){bool ans=!(h>>labs[j]&1);x.erase(remove_if(x.begin(),x.end(),[&](auto z){return bool(!(z.second>>labs[j]&1))!=ans;}),x.end());--rem;}}break;}
 assert(q>=0);int r=q/M,j=q%M;bool yes=(u>>r&1)&&!(h>>labs[j]&1);x.erase(remove_if(x.begin(),x.end(),[&](auto z){return bool((z.first>>r&1)&&!(z.second>>labs[j]&1))!=yes;}),x.end());--rem;
 // update without sorting to preserve actual-label map
 auto[a,b]=s.c[j];W rr=R[r];if(yes){s.act&=rr&~a;s.c[j]={0,0};}else{s.act&=~rr|(a|b);s.c[j]={a|(rr&b),b&~rr};}W dead=0,sat=0;for(W v=s.act;v;v&=v-1){W z=v&-v;int n=0;for(auto[p,q]:s.c)n+=!!(p&z);if(n>H)dead|=z;else if(n==H)sat|=z;}s.act&=~dead;for(auto&[a,b]:s.c){a&=s.act;b&=s.act&~sat;}assert(count(s)==(long long)x.size());}
 assert(rem>=0&&x.size()==1&&x[0]==make_pair(u,h));}}
};
int main(){int cases;cin>>cases;while(cases--){int id,n,m,k,cap;cin>>id>>n>>m>>k>>cap;assert(m==M);vector<pair<int,int>>st(n);map<int,pair<int,int>> masks;for(auto&[u,h]:st){cin>>u>>h;if(!masks.count(u))masks[u]={h,h};else{masks[u].first&=h;masks[u].second|=h;}}S raw{};for(auto[u,p]:masks){int i=lower_bound(F.begin(),F.end(),u)-F.begin();assert(i<(int)F.size()&&F[i]==u);W b=W(1)<<i;raw.act|=b;for(int j=0;j<M;j++){if(p.first>>j&1)raw.c[j].first|=b;else if(p.second>>j&1)raw.c[j].second|=b;}}Solver v(cap);assert(v.count(raw)==n);S s=raw;v.norm(s);int res;try{res=v.solve(s,k);}catch(int){res=-4;}if(res!=-1&&res!=-4){v.replay(st,raw,k);res=1;}else if(res==-4)res=0;cout<<id<<","<<n<<","<<res<<","<<v.calls<<endl;}}
