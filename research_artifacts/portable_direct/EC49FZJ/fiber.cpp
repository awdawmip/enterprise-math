#include <bits/stdc++.h>
using namespace std;using W=uint64_t;int pc(W x){return __builtin_popcountll(x);}
struct Fiber{int u,h;};
struct Cert{
 int u,h,m,k;W mask;const vector<Fiber>& f;unordered_set<W> fail;long long nodes=0,checks=0;
 int cost(W x){int rows=x&1023,cols=x>>10;return max(pc(rows&u),pc(cols&(~h&mask)))+pc(rows&(~u&1023))+pc(cols&h);}
 bool go(W x){++nodes;if(cost(x)>k)return false;if(fail.count(x))return false;int row=x&1023,col=x>>10;int neg=col&h,pos=col&(~h&mask);W e=0;int best=100;
 for(auto[v,b]:f){++checks;if(v==u||((v^u)&row)||(b&pos)||pc(b|neg)>14)continue;int K=b|neg;W diff=W(v^u)|(W(h^K)<<10);assert(diff&&!(diff&x));int d=pc(diff);if(d<best){e=diff;best=d;if(d==1)break;}}
 if(!e)return true;vector<pair<int,W>> opts;while(e){W b=e&-e;e-=b;opts.push_back({cost(x|b),b});}sort(opts.begin(),opts.end());for(auto[c,b]:opts)if(c<=k&&go(x|b))return true;fail.insert(x);return false;}
};
int main(){int cases;cin>>cases;while(cases--){int id,n,m,k,cap;cin>>id>>n>>m>>k>>cap;vector<pair<int,int>>s(n);map<int,int> mins;int live=(1<<m)-1;for(auto&[u,h]:s){cin>>u>>h;live&=~h;if(!mins.count(u))mins[u]=h;else mins[u]&=h;}vector<Fiber> f;for(auto[u,h]:mins)f.push_back({u,h});W mask=(W(1)<<m)-1;long long nodes=0,checks=0;int strict=0,maxexact=0,found=-1,checked=0,unsat=0,unsat_strict=0,example=-1,exold=-1,exnew=-1;
 for(int i=0;i<n;i++){auto[u,h]=s[i];int base=mins[u];int J=(h&~base);if(pc(h)<14){J|=(mask&~(h|live));++unsat;} // at |H|<14 all free columns are singleton rivals
 vector<int>same;for(auto[v,b]:f)if(v!=u&&(b&~h)==0)same.push_back(u^v); // H itself is compatible under V
 int a=pc(J&~h),b=pc(J&h),old=100;for(int r=0;r<1024;r++){int val=b+max(a,pc(r&u))+pc(r&(~u&1023));if(val>=old)continue;bool ok=true;for(int d:same)if(!(r&d)){ok=false;break;}if(ok)old=val;}
 W forced=W(J)<<10;for(int d:same)if(pc(d)==1)forced|=d;
 Cert c{u,h,m,0,mask,f};int exact=old;for(;exact<=k;exact++){c.k=exact;c.fail.clear();if(c.go(forced))break;}nodes+=c.nodes;checks+=c.checks;checked++;maxexact=max(maxexact,exact);if(exact>old){strict++;if(pc(h)<14)unsat_strict++;if(example<0){example=i;exold=old;exnew=exact;}}if(exact>k){found=i;break;}
 }
 cout<<id<<","<<n<<","<<found<<","<<checked<<","<<maxexact<<","<<strict<<","<<example<<","<<exold<<","<<exnew<<","<<nodes<<","<<checks<<","<<unsat<<","<<unsat_strict<<endl;
}}
