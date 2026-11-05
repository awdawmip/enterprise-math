#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using u64=uint64_t;using u128=unsigned __int128;using i128=__int128;
u64 mul(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
u64 inv(u64 a,u64 m){i128 r=m,n=a,t=0,nt=1;while(n){i128 q=r/n,rr=r-q*n;r=n;n=rr;rr=t-q*nt;t=nt;nt=rr;}if(r!=1)exit(2);t%=m;if(t<0)t+=m;return (u64)t;}
int main(int argc,char**argv){int cap=argc>1?atoi(argv[1]):10000;std::vector<bool> s(cap+1,true);s[0]=s[1]=false;for(int i=2;i*i<=cap;i++)if(s[i])for(int j=i*i;j<=cap;j+=i)s[j]=false;
std::cout<<"p,residue24,w4,v4,difference_p3,difference_p4,p4_transport_digit,v_tail_p3\n";
for(int p=5;p<=cap;p++){if(!s[p])continue;u64 mod=(u64)p*p*p*p,p3=(u64)p*p*p,w=1,v=1,aw=1,av=1,vlast=0;
for(int k=0;k<p-1;k++){
 u64 wn=mul(mul(2*k+1,3*k+1,mod),3*k+2,mod);
 u64 vn=mul(mul(4*k+1,4*k+2,mod),4*k+3,mod);
 u64 k3=mul(k+1,mul(k+1,k+1,mod),mod);
 aw=mul(aw,mul(wn,inv(mul(36,k3,mod),mod),mod),mod);
 av=mul(av,mul(vn,inv(mul(576,k3,mod),mod),mod),mod);
 u64 tw=mul(6*(k+1)+1,aw,mod),tv=mul(8*(k+1)+1,av,mod);
 w=(w+tw)%mod;v=(v+tv)%mod;
 if(k+1 > (3*p-1)/4)vlast=(vlast+tv)%mod;
}
u64 d=(w+mod-v)%mod;std::cout<<p<<','<<p%24<<','<<w<<','<<v<<','<<d%p3<<','<<d<<','<<(d%p3==0?d/p3:UINT64_MAX)<<','<<vlast%p3<<'\n';
}
}
