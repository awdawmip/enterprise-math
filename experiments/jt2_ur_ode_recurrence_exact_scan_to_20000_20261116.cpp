// JT2 norm-jet finite replication via Legendre differential equation coefficient recurrence.
// Independent from factorial-coefficient construction; deterministic exact modular arithmetic.
#include <bits/stdc++.h>
using namespace std;
using i64=long long;
i64 pw(i64 a,i64 e,i64 M){i64 v=1;for(;e;e>>=1,a=a*a%M)if(e&1)v=v*a%M;return v;}
bool prime(int p){if(p<2)return false;for(int q=2;q*q<=p;q++)if(p%q==0)return false;return true;}
struct Answer{int p,m,cm0,J,u,d,epsilon;};
Answer evaluate(int p){int m=(p-1)/6;int n=4*m+1;i64 M=(i64)p*p;
 // Invert all i<=4m+1 modulo p^2 with one inverse and a prefix/suffix product.
 vector<i64>prefix(n+1,1), inv(n+1,0);
 for(int i=1;i<=n;i++)prefix[i]=prefix[i-1]*i%M;
 i64 invprod=pw(prefix[n],(i64)p*(p-1)-1,M);
 for(int i=n;i>=1;i--){inv[i]=invprod*prefix[i-1]%M;invprod=invprod*i%M;}
 i64 c0=(m&1)?M-1:1;
 for(int i=1;i<=m;i++)c0=c0*(m+i)%M*inv[i]%M;
 c0=c0*pw(4,(i64)p*(p-1)-m,M)%M; // P_{2m}(0)=(-1)^m binom(2m,m)/4^m
 vector<int>q(m+1);i64 c=c0;
 for(int j=0;j<=m;j++){
  q[j]=c;
  if(j==m)break;
  i64 numerator=((i64)(j-m)*(2*j+2*m+1))%M;
  if(numerator<0)numerator+=M;
  c=c*numerator%M*inv[j+1]%M*inv[2*j+1]%M;
 }
 i64 half=inv[2], yp=1,value=0,deriv=0,derivPower=1;
 for(int j=0;j<=m;j++){
  value=(value+(i64)q[j]*yp)%M;
  if(j){deriv=(deriv+(i64)j*(q[j]%p)%p*derivPower)%p;derivPower=derivPower*(half%p)%p;}
  yp=yp*half%M;
 }
 vector<int> conv(2*m+1,0);
 for(int i=0;i<=m;i++){
  i64 ai=q[i]%p;
  for(int j=0;j<=i;j++) {
   i64 v=ai*(q[j]%p)%p;
   if(i!=j)v=2*v%p;
   conv[i+j]=(conv[i+j]+v)%p;
  }
 }
 vector<int> invp(n+1,0);invp[1]=1;
 for(int i=2;i<=n;i++) invp[i]=p-(i64)(p/i)*invp[p%i]%p;
 i64 J=0,yp2=1,half_p=half%p;
 for(int r=0;r<=2*m;r++){J=(J+yp2*conv[r]%p*invp[2*r+1])%p;yp2=yp2*half_p%p;}
 i64 u=(value%p)?-1:value/p; i64 eps=(u<0)?-1:(18*u*deriv-2*J-3)%p; if(eps<0 && u>=0)eps+=p;
 return {p,m,int(value%p),int(J),int(u),int(deriv),int(eps)};
}
int main(int argc,char**argv){int hi=argc>1?atoi(argv[1]):20000;int total=0,nonzero=0,cmfails=0;cout<<"p,m,CM0,J,u,d,epsilon\n";
for(int p=5;p<=hi;p++)if((p%24==13||p%24==19)&&prime(p)){auto a=evaluate(p);cout<<a.p<<','<<a.m<<','<<a.cm0<<','<<a.J<<','<<a.u<<','<<a.d<<','<<a.epsilon<<'\n';total++;cmfails+=(a.cm0!=0);nonzero+=(a.epsilon!=0);}
cerr<<"SUMMARY hi="<<hi<<" total="<<total<<" cmfails="<<cmfails<<" e_nonzero="<<nonzero<<"\n";}
