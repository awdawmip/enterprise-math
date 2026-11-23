#include <bits/stdc++.h>
using namespace std;
using u64=unsigned long long;
constexpr int P=17,CAP=2331,K=5;
constexpr int MOD[K]={17,289,4913,83521,1419857};
struct Sig { array<int,K> v{}; };
Sig add(Sig a,const Sig& b){for(int k=0;k<K;k++)a.v[k]=(a.v[k]+b.v[k])%MOD[k];return a;}
u64 key4(const Sig& s){return (u64)s.v[0]+17ULL*s.v[1]+4913ULL*s.v[2]+24137569ULL*s.v[3];}
u64 key5(const Sig& s){return key4(s)+2015993900449ULL*(u64)s.v[4];}
int inverse(int x,int m){
 int a=x,b=m,u=1,v=0;
 while(b){int q=a/b,t=a-q*b;a=b;b=t;t=u-q*v;u=v;v=t;}
 if(a!=1)throw runtime_error("non-unit");u%=m;if(u<0)u+=m;return u;
}
Sig unit_sig(int a){
 Sig s;
 for(int k=1;k<=K;k++){
  int m=MOD[k-1],inv=inverse(a%m,m);long long v=1;
  for(int j=0;j<k;j++)v=v*inv%m;
  s.v[k-1]=(int)v;
 }
 return s;
}
bool smooth(int n){for(int p:{2,3,5,7,11,13,17})while(n%p==0)n/=p;return n==1;}
struct Atom{int q,r,cost;Sig sig;};
vector<Atom> atoms;
vector<pair<int,Sig>> vertical[8];
void build_vertical(int target,int first,int left,int cost,Sig s){
 if(left==0){vertical[target].push_back({cost,s});return;}
 for(int i=first;i<(int)atoms.size();i++){
  const auto &a=atoms[i];
  if(a.q<=left && cost+a.cost<=CAP)
   build_vertical(target,i,left-a.q,cost+a.cost,add(s,a.sig));
 }
}
struct Z{int cost;Sig sig;};
vector<Z> q0;
Sig q0_sig[17];
void build_q0(int j,int cost,Sig s){
 if(j==17){q0.push_back({cost,s});return;}
 int c=17*j-1;const Sig &t=q0_sig[j];
 for(int n=0;cost+n*c<=854;n++){
  build_q0(j+1,cost+n*c,s);
  s=add(s,t);
 }
}
int main(){
 for(int q=1;q<=7;q++)for(int r=1;r<=16;r++)
  if(smooth(17*q+r))atoms.push_back({q,r,289*q+17*r-1,unit_sig(17*q+r)});
 if(atoms.size()!=60)throw runtime_error("atom roster");
 for(int q:{5,6,7})build_vertical(q,0,q,0,Sig{});
 for(int j=1;j<=16;j++)q0_sig[j]=unit_sig(j);
 build_q0(1,0,Sig{});
 unordered_set<u64> q7_four,q7_five;
 q7_four.reserve(100000);q7_five.reserve(100000);
 u64 n7=0;
 for(auto &[mass,v]:vertical[7])for(const auto &z:q0)if(mass+z.cost<=CAP){
  Sig s=add(v,z.sig);q7_four.insert(key4(s));q7_five.insert(key5(s));n7++;
 }
 vector<u64> q6_five;
 q6_five.reserve(7000000);
 u64 n6=0,hit_q6_q7_four=0,hit_q6_q7_five=0;
 for(auto &[mass,v]:vertical[6])for(const auto &z:q0)if(mass+z.cost<=CAP){
  Sig s=add(v,z.sig);n6++;q6_five.push_back(key5(s));
  hit_q6_q7_four+=q7_four.count(key4(s));
  hit_q6_q7_five+=q7_five.count(key5(s));
 }
 sort(q6_five.begin(),q6_five.end());
 u64 q6_self_five_collisions=0;
 for(size_t i=1;i<q6_five.size();i++)
  if(q6_five[i-1]==q6_five[i])q6_self_five_collisions++;
 u64 n5=0,hit_q5_q7_five=0;
 for(auto &[mass,v]:vertical[5])for(const auto &z:q0)if(mass+z.cost<=CAP){
  Sig s=add(v,z.sig);n5++;hit_q5_q7_five+=q7_five.count(key5(s));
 }
 cout<<"atoms="<<atoms.size()<<" v5="<<vertical[5].size()<<" v6="<<vertical[6].size()
     <<" v7="<<vertical[7].size()<<" q0_le854="<<q0.size()<<"\n";
 cout<<"q5_states="<<n5<<" q6_states="<<n6<<" q7_states="<<n7<<"\n";
 cout<<"q7_four_distinct="<<q7_four.size()<<" q7_five_distinct="<<q7_five.size()<<"\n";
 cout<<"q6_q7_four_collisions="<<hit_q6_q7_four
     <<" q6_q7_five_collisions="<<hit_q6_q7_five
     <<" q6_self_five_collisions="<<q6_self_five_collisions
     <<" q5_q7_five_collisions="<<hit_q5_q7_five<<"\n";
 if(atoms.size()!=60 || vertical[5].size()!=8573 || vertical[6].size()!=11105
    ||vertical[7].size()!=1907 || q0.size()!=1144444
    ||n5!=172059801 || n6!=6992576 || n7!=55347
    ||q7_four.size()!=n7 || q7_five.size()!=n7
    ||hit_q6_q7_four || hit_q6_q7_five || q6_self_five_collisions || hit_q5_q7_five)
   return 1;
}
