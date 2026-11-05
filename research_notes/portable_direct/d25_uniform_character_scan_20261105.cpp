#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using u64=uint64_t; using u128=unsigned __int128; using i128=__int128;
static u64 mul(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 inv(u64 a,u64 m){
 i128 r=m, nr=a, t=0, nt=1;
 while(nr){i128 q=r/nr; i128 tmp=r-q*nr;r=nr;nr=tmp;tmp=t-q*nt;t=nt;nt=tmp;}
 if(r!=1){std::cerr<<"noninvertible\n";std::exit(2);}
 t%=m;if(t<0)t+=m; return (u64)t;
}
int main(int argc,char**argv){
 int cap=argc>1?atoi(argv[1]):10000;
 std::vector<bool> prime(cap+1,true); prime[0]=false;prime[1]=false;
 for(int i=2;i*i<=cap;i++)if(prime[i])for(int j=i*i;j<=cap;j+=i)prime[j]=false;
 std::cout<<"p,mod6,sign,full_p3,full_p4,p4_correction,p3_residue,half_p3,first_high_p3,tail3_p3\n";
 for(int p=5;p<=cap;p++){
  if(!prime[p])continue;
  u64 mod=(u64)p*p*p*p, p3=(u64)p*p*p;
  u64 a=1,sum=1,half=1,tail3=0, firsthigh=0;
  int m=(p-1)/2;
  for(int k=0;k<p-1;k++){
   u64 numerator=mul(mul(2*k+1,3*k+1,mod),3*k+2,mod);
   u64 d=mul(36,mul((u64)(k+1),mul((u64)(k+1),k+1,mod),mod),mod);
   a=mul(a,mul(numerator,inv(d,mod),mod),mod);
   int j=k+1;
   u64 term=mul(6*j+1,a,mod);
   sum=(sum+term)%mod;
   if(j<=m)half=(half+term)%mod;
   if(j>m) firsthigh=(firsthigh+term)%mod;
   if(j>(2*p)/3)tail3=(tail3+term)%mod;
  }
  int sign=p%3==1?1:-1;
  u64 target=sign==1?(u64)p:(mod-p);
  u64 diff=(sum+mod-target)%mod;
  u64 p4correction=diff%p3==0?diff/p3:UINT64_MAX;
  std::cout<<p<<','<<p%6<<','<<sign<<','<<sum%p3<<','<<sum<<','<<p4correction<<','<<((sum%p3+p3-(target%p3))%p3)<<','<<half%p3<<','<<firsthigh%p3<<','<<tail3%p3<<'\n';
 }
}
