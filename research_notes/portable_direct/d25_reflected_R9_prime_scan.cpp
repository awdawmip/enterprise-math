// Exact bounded census of R_p(9) for p == 3 (mod 8), p>=11.
// Author-side auxiliary check; no native experiment or acceptance claim.
#include <cstdint>
#include <iostream>
#include <cstdlib>
#include <vector>
using i64=long long;
int main(int argc,char** argv){
  const int bound= argc>1 ? std::atoi(argv[1]):100000;
  if(bound<11 || bound>1000000){std::cerr<<"bound must be 11..1000000\n"; return 2;}
  std::vector<bool> isprime(bound+1,true);isprime[0]=isprime[1]=false;
  for(int d=2;d*d<=bound;++d)if(isprime[d])for(int k=d*d;k<=bound;k+=d)isprime[k]=false;
  int count=0,stationary=0,zero=0;
  for(int p=11;p<=bound;p+=8){
    if(!isprime[p]) continue;
    ++count;
    std::vector<int> inv(p);
    inv[1]=1;
    for(int k=2;k<p;k++)inv[k]=(i64)(p-p/k)*inv[p%k]%p;
    int m=(p-3)/8; int n=2*m;
    auto pw=[&](int a,int exponent){i64 y=1,b=a;while(exponent){if(exponent&1)y=y*b%p;b=b*b%p;exponent/=2;}return int(y);};
    i64 h=1,powprime=pw(9,n),R=0,Rprime=0;
    for(int j=0;j<=n;++j){
      i64 v=(8LL*j+5)*h%p*powprime%p;
      Rprime=(Rprime+v)%p;
      R=(R+v*9%p*inv[n+1+j])%p;
      if(j<n){
        i64 x=4LL*j+3;
        h=h*x%p*x%p*x%p;
        h=h*inv[4*j+4]%p*inv[4*j+5]%p*inv[4*j+6]%p;
      }
      powprime=powprime*9%p;
    }
    if(Rprime==0) ++stationary;
    else {std::cout<<"FAIL-STATIONARY "<<p<<" "<<Rprime<<"\n";return 1;}
    if(R==0){++zero;std::cout<<"ROOT "<<p<<"\n";}
    if(p==11||p==19||p==3347) std::cout<<"ANCHOR "<<p<<" "<<R<<" "<<Rprime<<"\n";
  }
  std::cout<<"SUMMARY p<="<<bound<<" count="<<count<<" stationary="<<stationary<<" zero="<<zero<<"\n";
}
