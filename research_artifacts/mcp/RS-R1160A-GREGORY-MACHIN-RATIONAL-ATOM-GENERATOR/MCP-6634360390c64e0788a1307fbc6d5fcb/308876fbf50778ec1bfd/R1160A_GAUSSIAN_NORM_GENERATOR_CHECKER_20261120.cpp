#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Z {ll x,y;};
Z mul(Z a,Z b){return {a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x};}
Z pw(Z a,int e){Z z{1,0};for(;e;e>>=1,a=mul(a,a))if(e&1)z=mul(z,a);return z;}
int main(int argc,char**argv){int H=argc>1?atoi(argv[1]):100;int maxn=2*H*H;vector<int> spf(maxn+1);for(int i=2;i<=maxn;i++){if(spf[i]==0){spf[i]=i;if((ll)i*i<=maxn)for(int j=i*i;j<=maxn;j+=i)if(spf[j]==0)spf[j]=i;}}
map<int,Z> reps;int rep_search=0;auto repr=[&](int p)->Z{auto it=reps.find(p);if(it!=reps.end())return it->second;for(int a=1;2*a*a<=p;a++){int bb=p-a*a;int b=sqrt((double)bb);while((ll)(b+1)*(b+1)<=bb)b++;while((ll)b*b>bb)b--;rep_search++;if((ll)b*b==bb){Z r{b,a};reps[p]=r;return r;}}cerr<<"NO REP "<<p<<"\n";exit(3);};
long long emit=0,norms=0,descs=0;unordered_set<ll> atoms;unordered_set<string> freegroups;atoms.reserve(H*H/2);freegroups.reserve(H*H/2);vector<pair<int,int>> fs;
function<void(int,Z,vector<int>&)> visit=[&](int j,Z z,vector<int>&sgns){if(j==(int)fs.size()){descs++;int g=0;for(auto &e:fs)g=std::gcd(g,e.second);string key;int flip=sgns.empty()?1:sgns[0];for(size_t h=0;h<fs.size();h++)key+=to_string(fs[h].first)+":"+to_string(flip*sgns[h]*fs[h].second/g)+",";
Z rot=z;for(int k=0;k<4;k++){if(rot.x>rot.y&&rot.y>0&&rot.x<=H){ll code=rot.x*(H+1LL)+rot.y;emit++;atoms.insert(code);freegroups.insert(key);}rot={-rot.y,rot.x};}return;}
auto [p,e]=fs[j];Z base=repr(p),pos=pw(base,e),neg={pos.x,-pos.y};sgns.push_back(1);visit(j+1,mul(z,pos),sgns);sgns.back()=-1;visit(j+1,mul(z,neg),sgns);sgns.pop_back();};
for(int n=2;n<=maxn;n++){fs.clear();int q=n,two=0;bool ok=true;while(q>1){int p=spf[q],e=0;do{q/=p;e++;}while(q%p==0);if(p==2){if(e>1)ok=false;else two=1;}else if(p%4==3)ok=false;else fs.emplace_back(p,e);if(!ok)break;}if(!ok || fs.empty())continue;norms++; vector<int> signs; visit(0,two?Z{1,1}:Z{1,0},signs);}
long long oracle=0;for(int b=2;b<=H;b++)for(int a=1;a<b;a++)if(std::gcd(a,b)==1){oracle++;if(!atoms.count(b*(H+1LL)+a)){cerr<<"missing "<<b<<","<<a<<"\n";exit(2);}}
cerr<<"H="<<H<<" norms="<<norms<<" candidates="<<descs<<" emitted="<<emit<<" unique="<<atoms.size()<<" oracle="<<oracle<<" freegroups="<<freegroups.size()<<" rep_search="<<rep_search<<" split_primes="<<reps.size()<<"\n";
}