#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using ll=long long;
int md(ll x,int p){int r=x%p;return r<0?r+p:r;}
int pw(int a,int n,int p){int r=1;while(n){if(n&1)r=md((ll)r*a,p);a=md((ll)a*a,p);n>>=1;}return r;}
struct F {int a,b;};
F mul(F u,F v,int p){return {md((ll)u.a*v.a+2LL*u.b*v.b,p),md((ll)u.a*v.b+(ll)u.b*v.a,p)};}
F add(F u,F v,int p){return {md(u.a+v.a,p),md(u.b+v.b,p)};}
int norm(F u,int p){return md((ll)u.a*u.a-2LL*u.b*u.b,p);}
bool prime(int p){for(int i=2;i*i<=p;i++)if(p%i==0)return false;return p>1;}
int main(){
 int count=0;
 for(int p=19;p<800;p++){
  if(!prime(p)||p%24!=19)continue;
  vector<int> chi(p,-1);chi[0]=0;
  for(int i=1;i<p;i++)chi[(ll)i*i%p]=1;
  assert(chi[2]==-1&&chi[3]==-1&&chi[6]==1);
  int eta=0;for(int i=1;i<p;i++)if((ll)i*i%p==6){eta=i;break;}
  assert(eta!=0);
  F T{0,md(2LL*pw(3,p-2,p),p)};
  F B{pw(8,p-2,p),pw(12,p-2,p)};
  F s{md(-pw(eta,p-2,p),p),pw(eta,p-2,p)}; // (sqrt(2)-1)/eta
  F delta{md((ll)(1)*pw(2,p-2,p),p),md(-1LL*T.b*pw(2,p-2,p),p)}; // (1-T)/2
  F s2=mul(s,s,p);assert(s2.a==delta.a&&s2.b==delta.b);
  int half=pw(2,p-2,p);
  F rho_plus{md((ll)(s.a-1)*half,p),md((ll)s.b*half,p)};
  F rho_minus{md((ll)(-1-s.a)*half,p),md(-(ll)s.b*half,p)};
  for(F v : {rho_plus,rho_minus}){
    F f=add(add(mul(v,v,p),v,p),B,p);assert(f.a==0&&f.b==0);
    assert(chi[norm(v,p)]==-1); // non-square in F_(p^2)
  }
  ll sum=0;
  for(int a=0;a<p;a++)for(int b=0;b<p;b++){
   F x{a,b},x2=mul(x,x,p),x3=mul(x2,x,p);
   F z=add(add(x3,x2,p),mul(B,x,p),p);
   sum+=chi[norm(z,p)];
  }
  int aq=(int)-sum;
  assert(aq==2*p);
  count++;
  cout<<"p="<<p<<" eta="<<eta<<" norm_root_1="<<norm(rho_plus,p)<<" norm_root_2="<<norm(rho_minus,p)<<" trace="<<aq<<" points="<<(ll)(p-1)*(p-1)<<"\n";
 }
 cout<<"PASS_GH117_INERT_CM_TRACE count="<<count<<"\n";
}
