// PREFIX-943 independent signed-bit CRT progression enumeration (k=17).
// Source pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
// Compile: g++ -O3 -std=c++17 PREFIX943_R6_K17_INDEPENDENT_CRT_ENUM.cpp -o k17_crt
// Run: ./k17_crt W17_CRT.bin
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using i64=long long;
using u64=uint64_t;
static constexpr i64 L=262145,U=524287,K=17,Q=131072,TMAX=34;
static i64 ceil_div(i64 a,i64 b){return a>=0?(a+b-1)/b:a/b;}
static i64 floor_div(i64 a,i64 b){return a>=0?a/b:-((-a+b-1)/b);}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 vector<u64> ids;ids.reserve(24000000);
 u64 raw=0,by_t[TMAX+1]={};
 for(i64 j=0;j<19;++j)for(i64 i=0;i<19;++i)
 for(i64 t=1;t<=TMAX;++t)for(i64 s:{-1LL,1LL}){
  i64 c=s*(1LL<<j)-(1LL<<i),g=gcd(K,2*t);
  if((t-c)%g)continue;
  i64 M=2*t/g,rhs=(t-c)/g,r=-1;
  for(i64 a0=0;a0<M;++a0)if(((K/g)*a0-rhs)%M==0){r=a0;break;}
  if(r<0||r%2==0)continue;
  i64 lower=max(L,ceil_div(t*L-c,K));
  i64 upper=min(U,floor_div(t*U-c,K));
  if(lower>upper)continue;
  i64 h0=ceil_div(lower-r,M),h1=floor_div(upper-r,M);
  for(i64 h=h0;h<=h1;++h){
    i64 a=r+M*h,x=K*a;
    if(((x>>j)&1)!=(s==-1))continue;
    i64 d=x+s*(1LL<<j)-(1LL<<i);
    if(d%t!=0||d<t*L||d>t*U)throw runtime_error("bad congruence range");
    i64 b=d/t;
    if(a%2!=1||b%2!=1)throw runtime_error("bad parity");
    ids.push_back(((a-L)/2)*Q+(b-L)/2);++raw;++by_t[t];
  }
 }
 sort(ids.begin(),ids.end());ids.erase(unique(ids.begin(),ids.end()),ids.end());
 ofstream f(argv[1],ios::binary);if(!f)throw runtime_error("output open failed");
 for(u64 x:ids)f.write((char*)&x,8);
 if(!f)throw runtime_error("output write failed");
 cout<<"k=17 raw="<<raw<<" unique="<<ids.size()<<" by_t=";
 for(i64 t=1;t<=TMAX;++t)cout<<(t==1?"":",")<<by_t[t];cout<<"\n";
}
