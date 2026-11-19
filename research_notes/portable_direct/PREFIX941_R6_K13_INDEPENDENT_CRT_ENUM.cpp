// Independent k=13 named XOR collision enumeration: solve the linear congruence
// k*a-t*b = 2^i-sign*2^j before testing the named source-bit sign.
// Scientific input pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
// g++ -std=c++17 -O3 PREFIX941_R6_K13_INDEPENDENT_CRT_ENUM.cpp -o crt
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr int L=262145,U=524287,NQ=131072,K=13,TMAX=26;
int mod(int x,int d){int r=x%d;return r<0?r+d:r;}
int floor_div(int x,int d){if(d<=0)throw runtime_error("bad denominator");int q=x/d,r=x%d;return q-((r<0)?1:0);}
int ceil_div(int x,int d){return -floor_div(-x,d);}
int main(int argc,char**argv){
 if(argc!=2)throw runtime_error("usage: ./crt W13_CRT.bin");
 vector<u64> ids;ids.reserve(22000000);u64 raw_by_t[TMAX+1]={};
 for(int t=1;t<=TMAX;++t)for(int j=0;j<=18;++j)for(int i=0;i<=18;++i)for(int sign:{-1,+1}){
  int c=(1<<i)-sign*(1<<j),g=gcd(K,t);if(c%g)continue;
  int t1=t/g,k1=K/g,c1=c/g,a0=0;
  if(t1>1){for(;a0<t1;++a0)if(mod(k1*a0-c1,t1)==0)break;if(a0==t1)throw runtime_error("modular inverse missing");}
  int b0=(K*a0-c)/t;
  int p=mod(1-b0,2);if(mod(a0+t1*p,2)!=1)continue;
  int A=a0+t1*p,B=b0+k1*p,sa=2*t1,sb=2*k1;
  int lo=max(ceil_div(L-A,sa),ceil_div(L-B,sb));
  int hi=min(floor_div(U-A,sa),floor_div(U-B,sb));
  for(int m=lo;m<=hi;++m){int a=A+sa*m,b=B+sb*m;
   if((int)((K*a>>j)&1)!=(sign==-1))continue;
   // Independent validity check of original XOR and both modular ports.
   int y=(K*a)^(1<<j),d=y-(1<<i);
   if(d!=t*b || a%2!=1 || b%2!=1 || a<L || a>U || b<L || b>U)throw runtime_error("CRT invalid pair");
   ids.push_back((u64)((a-L)/2)*NQ+((b-L)/2));++raw_by_t[t];
  }
 }
 sort(ids.begin(),ids.end());ids.erase(unique(ids.begin(),ids.end()),ids.end());
 ofstream f(argv[1],ios::binary);for(u64 x:ids)f.write((char*)&x,8);if(!f)throw runtime_error("write failed");
 u64 raw=0;for(int t=1;t<=TMAX;++t)raw+=raw_by_t[t];
 cout<<"k=13 raw="<<raw<<" unique="<<ids.size()<<"\n";
 for(int t=1;t<=TMAX;++t)cout<<"t"<<t<<"="<<raw_by_t[t]<<"\n";
}
