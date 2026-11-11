#include <bits/stdc++.h>
using namespace std;
using u64=unsigned long long;using u128=__uint128_t;
static inline u64 mm(u64 a,u64 b,u64 M){return (u128)a*b%M;}
static inline u64 qp(u64 a,u64 q,u64 M){u64 v=1;while(q){if(q&1)v=mm(v,a,M);a=mm(a,a,M);q>>=1;}return v;}
static inline int chiminus6(int p){return qp((p-(6%p))%p,(p-1)/2,p)==1?1:-1;}
int main(int argc,char**argv){
 int end=argc>=2?atoi(argv[1]):250000;
 int low=argc>=3?atoi(argv[2]):5;
 vector<bool> prime(end+1,true);prime[0]=prime[1]=false;
 for(int i=2;i*i<=end;++i)if(prime[i])for(int j=i*i;j<=end;j+=i)prime[j]=false;
 int cnt=0,a0=0,b0=0,fail=0;vector<int> anomalies;uint64_t acc=0;
 ofstream csv;
 if(argc>=4){csv.open(argv[3]);csv<<"p,e,m,A_mod_p2,B_mod_p2,zero_port,zero_port_order_at_least_2,chi_minus6\n";}
 for(int p=max(low,5);p<=end;++p)if(prime[p]){
   int e=(p%6==1?0:1),m=(p-1-4*e)/6;u64 M=1ULL*p*p;
   vector<u64> inv(m+1);if(m)inv[1]=1;
   // For k<p, gcd(k,p^2)=1. Euclid recurrence works even for composite modulus p^2.
   for(int k=2;k<=m;++k){inv[k]=(M-mm(M/k,inv[M%k],M))%M;}
   u64 term=1,A=1,B=(M+1-6*e)%M;u64 half=(M+1)/2;
   for(int k=1;k<=m;++k){
     term=mm(term,(u64)(m-k+1)*(2*m+e-k+1)%M,M);
     term=mm(term,mm(inv[k],inv[k],M),M);
     term=mm(term,half,M); A=(A+term)%M;
     u64 w=(1-6*e+12*k);B=(B+mm(term,w,M))%M;
   }
   bool az=A%p==0,bz=B%p==0;
   if(az==bz || (az!=(chiminus6(p)==-1))){cerr<<"FAIL p="<<p<<" A="<<A<<" B="<<B<<"\n";fail++;}
   a0+=az;b0+=bz;cnt++;
   if(csv.is_open())csv<<p<<","<<e<<","<<m<<","<<A<<","<<B<<","<<(az?"A":"B")<<","<<((az?A:B)==0)<<","<<chiminus6(p)<<"\n";
   if((az?A:B)==0){anomalies.push_back(p);cout<<"ORDER>=2 "<<p<<" e="<<e<<" m="<<m<<" A="<<A<<" B="<<B<<"\n";}
   acc=(acc*1315423911ULL+p*17ULL+A*31ULL+B*43ULL+e)%1000000007ULL;
 }
 cout<<"SUMMARY low="<<low<<" hi="<<end<<" count="<<cnt<<" a0="<<a0<<" b0="<<b0<<" failure="<<fail<<" anomalies="<<anomalies.size()<<" checksum="<<acc<<"\n";
 for(auto p:anomalies)cout<<"EXCEPTION "<<p<<"\n";
 return !!fail;
}