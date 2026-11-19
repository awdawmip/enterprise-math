// PREFIX-943B: independent full-domain signed-bit CRT quotient census.
// Source pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
// Compile: g++ -O3 -std=c++17 PREFIX943B_R6_QUOTIENT_LOCALITY_CRT.cpp -o qlocal_crt
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using i64=long long;using u64=uint64_t;
static constexpr i64 L=262145,U=524287,K=17,Q=131072,TMAX=34;
static i64 ceil_div(i64 a,i64 b){return a>=0?(a+b-1)/b:a/b;}
static i64 floor_div(i64 a,i64 b){return a>=0?a/b:-((-a+b-1)/b);}
int main(){
 vector<u64> keys;keys.reserve(24000000);
 u64 raw=0,by_t[TMAX+1]={};
 for(i64 j=0;j<19;++j)for(i64 i=0;i<19;++i)
 for(i64 t=1;t<=TMAX;++t)for(i64 s:{-1LL,1LL}){
  i64 c=s*(1LL<<j)-(1LL<<i),g=gcd(K,2*t);
  if((t-c)%g)continue;
  i64 M=2*t/g,rhs=(t-c)/g,r=-1;
  for(i64 a0=0;a0<M;++a0)if(((K/g)*a0-rhs)%M==0){r=a0;break;}
  if(r<0||r%2==0)continue;
  i64 lower=max(L,ceil_div(t*L-c,K)),upper=min(U,floor_div(t*U-c,K));
  if(lower>upper)continue;
  i64 h0=ceil_div(lower-r,M),h1=floor_div(upper-r,M);
  for(i64 h=h0;h<=h1;++h){
   i64 a=r+M*h,x=K*a;
   if(((x>>j)&1)!=(s==-1))continue;
   i64 d=x+s*(1LL<<j)-(1LL<<i);
   if(d%t!=0||d<t*L||d>t*U)throw runtime_error("bad congruence range");
   i64 b=d/t;if((a&1)!=1||(b&1)!=1)throw runtime_error("bad parity");
   keys.push_back(((((a-L)/2)*Q+(b-L)/2)<<6)|t);++raw;++by_t[t];
  }
 }
 sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());
 u64 one=0,two_adj=0,two_gap2=0,three=0,bad=0,unique=0;
 for(size_t p=0;p<keys.size();){
  u64 pair=keys[p]>>6;int t[36],n=0;
  do{t[n++]=keys[p++]&63;}while(p<keys.size()&&(keys[p]>>6)==pair);
  ++unique;
  if(n==1)++one;
  else if(n==2){if(t[1]-t[0]==1)++two_adj;else if(t[1]-t[0]==2)++two_gap2;else ++bad;}
  else if(n==3&&t[2]-t[0]==2&&t[1]-t[0]==1)++three;
  else ++bad;
 }
 cout<<"CRT raw="<<raw<<"\npair_t="<<keys.size()<<"\nunique="<<unique
     <<"\none="<<one<<"\ntwo_adj="<<two_adj<<"\ntwo_gap2="<<two_gap2
     <<"\nthree="<<three<<"\nbad="<<bad<<"\n";
 if(raw!=19318164||unique!=15136736||bad!=0)return 4;
}
