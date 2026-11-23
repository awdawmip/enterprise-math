#include <bits/stdc++.h>
using namespace std;
using u64=unsigned long long;
constexpr int P=17,CAP=2331,K=5;
constexpr int MOD[K]={17,289,4913,83521,1419857};
struct Sig{array<int,K> v{};};
Sig add(Sig a,const Sig& b){for(int k=0;k<K;k++)a.v[k]=(a.v[k]+b.v[k])%MOD[k];return a;}
u64 key5(const Sig& s){return (u64)s.v[0]+17ULL*s.v[1]+4913ULL*s.v[2]+24137569ULL*s.v[3]+2015993900449ULL*(u64)s.v[4];}
int inverse(int x,int m){int a=x,b=m,u=1,v=0;while(b){int q=a/b,t=a-q*b;a=b;b=t;t=u-q*v;u=v;v=t;}if(a!=1)throw runtime_error("non-unit");u%=m;if(u<0)u+=m;return u;}
Sig unit_sig(int a){Sig s;for(int k=1;k<=K;k++){int m=MOD[k-1],inv=inverse(a%m,m);long long v=1;for(int j=0;j<k;j++)v=v*inv%m;s.v[k-1]=(int)v;}return s;}
bool smooth(int n){for(int p:{2,3,5,7,11,13,17})while(n%p==0)n/=p;return n==1;}
struct Atom{int q,r,cost;Sig sig;};vector<Atom> atoms;vector<pair<int,Sig>> vertical[8];
void build_vertical(int target,int first,int left,int cost,Sig s){if(left==0){vertical[target].push_back({cost,s});return;}for(int i=first;i<(int)atoms.size();i++){const auto &a=atoms[i];if(a.q<=left&&cost+a.cost<=CAP)build_vertical(target,i,left-a.q,cost+a.cost,add(s,a.sig));}}
struct Z{int cost;Sig sig;};vector<Z> q0;Sig q0_sig[17];
void build_q0(int j,int cost,Sig s){if(j==17){q0.push_back({cost,s});return;}int c=17*j-1;const Sig&t=q0_sig[j];for(int n=0;cost+n*c<=854;n++){build_q0(j+1,cost+n*c,s);s=add(s,t);}}
int main(){for(int q=1;q<=7;q++)for(int r=1;r<=16;r++)if(smooth(17*q+r))atoms.push_back({q,r,289*q+17*r-1,unit_sig(17*q+r)});
 if(atoms.size()!=60)throw runtime_error("atoms");
 for(int q:{5,6})build_vertical(q,0,q,0,Sig{});for(int j=1;j<=16;j++)q0_sig[j]=unit_sig(j);build_q0(1,0,Sig{});

 sort(q0.begin(),q0.end(),[](const Z&a,const Z&b){return a.cost<b.cost;});
 const size_t TS=1<<24; const u64 EMPTY=~0ULL;
 vector<u64> table(TS, EMPTY);
 auto slot=[](u64 x)->size_t{ x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return (size_t)x & ((1<<24)-1);};
 auto insert=[&](u64 x){size_t h=slot(x);while(table[h]!=EMPTY){if(table[h]==x)return false;h=(h+1)&(TS-1);}table[h]=x;return true;};
 auto contains=[&](u64 x){size_t h=slot(x);while(table[h]!=EMPTY){if(table[h]==x)return true;h=(h+1)&(TS-1);}return false;};

 u64 n6=0,n5=0,intersections=0,internal6_dups=0;vector<u64> witness;
 for(auto &[mass,v]:vertical[6]) for(const auto& z:q0){if(mass+z.cost>CAP)break;u64 k=key5(add(v,z.sig));n6++;if(!insert(k))internal6_dups++;}
 for(auto &[mass,v]:vertical[5]) for(const auto& z:q0){if(mass+z.cost>CAP)break;u64 k=key5(add(v,z.sig));n5++;if(contains(k)){intersections++;if(witness.size()<10)witness.push_back(k);}}
 cout<<"atoms="<<atoms.size()<<" v5="<<vertical[5].size()<<" v6="<<vertical[6].size()<<" q0="<<q0.size()<<" n5="<<n5<<" n6="<<n6<<" distinct6="<<(n6-internal6_dups)<<" duplicates6="<<internal6_dups<<" cross5="<<intersections<<"\n";
 for(auto x:witness)cout<<"witness key="<<x<<"\n";
 if(n5!=172059801 || n6!=6992576 || internal6_dups!=0) return 2;
}
