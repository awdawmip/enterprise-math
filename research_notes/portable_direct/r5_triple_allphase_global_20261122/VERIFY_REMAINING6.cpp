// Frozen R5 five-event scalar numerator, exact first-jet certificates in Z[q]/Phi_D(q).
// Build separately for D = 7, 11, 13, 25, 27, 31: g++ -O2 -std=c++17 -DD=25 VERIFY_REMAINING6.cpp -o check && ./check
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdint>
#include <stdexcept>
using namespace std;
static_assert(D==7||D==11||D==13||D==25||D==27||D==31,"supported orders");
using I=int64_t;using P=array<I,D>;struct J{P v{},d{};};
const vector<vector<int>> E={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221}};
P shift(const P &a,int p){P b{};p%=D;for(int j=0;j<D;j++)b[(j+p)%D]+=a[j];return b;}
void add(P &a,const P &b,int s=1){for(int j=0;j<D;j++)a[j]+=s*b[j];}
void add(J &a,const J &b,int s=1){add(a.v,b.v,s);add(a.d,b.d,s);}
J shifted(const J &a,int p){J b;b.v=shift(a.v,p);b.d=shift(a.d,p);for(int j=0;j<D;j++)b.d[j]+=(I)p*b.v[j];return b;}
void factor(J &a,int p){J b=shifted(a,p);add(a,b,-1);}
J C(int m){J z;z.v[0]=1;for(int p=296;p<=312;p++)factor(z,m*p);return z;}
constexpr int PHI = (D==25 ? 20 : D==27 ? 18 : D-1);
array<I,PHI> canon(const P &a){array<I,PHI>b{};
 for(int j=0;j<PHI;j++){
  if constexpr(D==25)b[j]=a[j]-a[20+j%5];
  else if constexpr(D==27)b[j]=a[j]-a[18+j%9];
  else b[j]=a[j]-a[D-1];
 }return b;
}
bool zero(const P &a){auto b=canon(a);return all_of(b.begin(),b.end(),[](I x){return x==0;});}
int main(){constexpr int M=(D==7||D==11||D==13)?8*D:6*D;
 vector<J>A(M+1);
 for(int mask=1;mask<8;mask++){
  vector<int>ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
  for(int id:ids)for(int p:E[id])U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
  vector<int>mv(U.size()),belongs(U.size());
  for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M)
    if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){mv[t]+=place;belongs[t]|=1<<j;}
  vector<J>dp(total);dp[0].v[0]=1;
  for(size_t t=0;t<U.size();t++)for(int code=0;code<total;code++){
    int tmp=code;bool valid=true;for(int j=0;j<n;j++,tmp/=M)
      if((belongs[t]>>j&1)&&tmp%M==0){valid=false;break;}
    if(valid)add(dp[code],shifted(dp[code-mv[t]],U[t]));
  }
  vector<J>layer(M);for(int code=0;code<total;code++){
    int tmp=code,k=0;for(int j=0;j<n;j++,tmp/=M)k=max(k,tmp%M);add(layer[k],dp[code]);
  }
  J prefix{};int sign=__builtin_popcount((unsigned)mask)%2?1:-1;
  for(int m=1;m<=M;m++){add(prefix,layer[m-1]);J z=prefix;for(int p:U)factor(z,p);add(A[m],z,sign);}
 }
 cout<<"d,r,component,coordinate,U,V,W,X\n";
 int count0=0,countdot=0;
 for(int r=1;r<=2*D;r++){
   auto a=canon(A[r].v),b=canon(A[r+2*D].v),c=canon(A[r+4*D].v);
   int idx=-1;I u=0,v=0,w=0,x=0;string comp="R0";
   for(int j=0;j<PHI;j++){
     I U=a[j],V=b[j]-a[j],W=c[j]-2*b[j]+a[j];
     if(U && U*V>=0 && U*W>=0){idx=j;u=U;v=V;w=W;break;}
   }
   if(idx>=0)count0++;
   else {
     if(!zero(A[r].v)||!zero(A[r+2*D].v)||!zero(A[r+4*D].v))
       throw runtime_error("Nonzero R0 not covered by witness; need mixed-root analysis");
     auto da=canon(A[r].d),db=canon(A[r+2*D].d),dc=canon(A[r+4*D].d);
     auto ca=canon(C(r).d),cb=canon(C(r+2*D).d),cc=canon(C(r+4*D).d);
     array<I,PHI> dd{};
     if constexpr(D==7||D==11||D==13){
       auto z=canon(A[r+6*D].d);dd=z;
     }
     comp="Rdot";
     for(int j=0;j<PHI;j++){
       I U=da[j]+ca[j],B=db[j]+cb[j],CC=dc[j]+cc[j];
       I V=B-U,W=CC-2*B+U;
       I X=0;
       if constexpr(D==7||D==11||D==13){
         auto d4=canon(C(r+6*D).d);
         X=dd[j]+d4[j]-3*CC+3*B-U;
       }
       if(U && U*V>=0 && U*W>=0 && U*X>=0){idx=j;u=U;v=V;w=W;x=X;break;}
     }
     if(idx<0)throw runtime_error("No scalar sign certificate");
     countdot++;
   }
   cout<<D<<","<<r<<","<<comp<<","<<idx<<","<<u<<","<<v<<","<<w<<","<<x<<"\n";
 }
 cerr<<"D="<<D<<" checked="<<2*D<<" R0="<<count0<<" Rdot="<<countdot<<"\n";
}
