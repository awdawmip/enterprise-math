#include <bits/stdc++.h>
using namespace std;
using I=long long;
const vector<vector<int>> E={{214,215,216,217,218}, {214,216,217,218,219,220,221}, {215,216,217,218,219,220,221}};
template<int D> struct Ring {
 using Poly=array<I,D>;
 struct Jet {Poly v{}, d{};};
 static Poly shift(const Poly&a,int p){Poly b{};p%=D;for(int j=0;j<D;j++)b[(j+p)%D]=a[j];return b;}
 static void add(Poly&a,const Poly&b,int sign=1){for(int j=0;j<D;j++)a[j]+=sign*b[j];}
 static void add(Jet&a,const Jet&b,int sign=1){add(a.v,b.v,sign);add(a.d,b.d,sign);}
 static Jet shifted(const Jet&a,int p){Jet b;b.v=shift(a.v,p);b.d=shift(a.d,p);for(int j=0;j<D;j++)b.d[j]+=(I)p*b.v[j];return b;}
 static void factor(Jet&a,int p){Jet b=shifted(a,p);add(a,b,-1);}
 static Jet cjet(int m){Jet x;x.v[0]=1;for(int p=296;p<=312;p++)factor(x,m*p);return x;}
 static vector<I> canon(const Poly&a){vector<I>x(D-1);for(int j=0;j<D-1;j++)x[j]=a[j]-a[D-1];return x;}
 static bool zero(const Poly&a){auto x=canon(a);return all_of(x.begin(),x.end(),[](I v){return v==0;});}
 static vector<Jet> compute(int M){vector<Jet>A(M+1);
  for(int mask=1;mask<8;mask++){
   vector<int>ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
   for(int id:ids)for(int p:E[id])U.push_back(p);
   sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
   int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
   vector<int>move(U.size()),belongs(U.size());
   for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M){
    if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){move[t]+=place;belongs[t]|=1<<j;}
   }
   vector<Jet>dp(total);dp[0].v[0]=1;
   for(size_t t=0;t<U.size();t++)for(int code=0;code<total;code++){
    int tmp=code;bool valid=true;
    for(int j=0;j<n;j++,tmp/=M)if((belongs[t]>>j&1)&&tmp%M==0){valid=false;break;}
    if(valid)add(dp[code],shifted(dp[code-move[t]],U[t]));
   }
   vector<Jet>layer(M);
   for(int code=0;code<total;code++){
    int tmp=code,k=0;for(int j=0;j<n;j++,tmp/=M)k=max(k,tmp%M);add(layer[k],dp[code]);
   }
   Jet pref{};int sign=__builtin_popcount((unsigned)mask)%2?1:-1;
   for(int m=1;m<=M;m++){add(pref,layer[m-1]);Jet z=pref;for(int p:U)factor(z,p);add(A[m],z,sign);}
  }
  return A;
 }
 static int cert(const Poly&base,const Poly&delta){auto b=canon(base),v=canon(delta);
  for(int j=0;j<D-1;j++)if((b[j]>0&&v[j]>=0)||(b[j]<0&&v[j]<=0))return j;
  return -1;
 }
 static void row(int r,string mode,int j,const Poly&b,const Poly&delta){auto x=canon(b),v=canon(delta);
  cout<<D<<","<<r<<","<<mode<<","<<j<<","<<x[j]<<","<<v[j]<<"\n";
 }
};
int main(){cout<<"order,residue,component,coefficient_index,base,step\n";int fails=0,n17value=0,n17deriv=0;
 {
  using R=Ring<19>; auto A=R::compute(76);
  for(int r=1;r<=38;r++){
   auto base=A[r].v,delta=A[r+38].v;R::add(delta,base,-1);
   int j=R::cert(base,delta);if(j<0 || R::zero(base))fails++;else R::row(r,"R0",j,base,delta);
  }
 }
 {
  using R=Ring<17>;auto A=R::compute(102);
  for(int r=1;r<=34;r++){
   auto base=A[r].v,step=A[r+34].v;R::add(step,base,-1);
   auto second=A[r+68].v;R::add(second,A[r+34].v,-2);R::add(second,base,1);
   if(!R::zero(second))fails++;
   if(!R::zero(base)){
    n17value++;int j=R::cert(base,step);if(j<0)fails++;else R::row(r,"R0",j,base,step);
   }else{
    n17deriv++;if(!R::zero(step))fails++;
    auto b=A[r].d,v=A[r+34].d,z=A[r+68].d;
    R::add(b,R::cjet(r).d);R::add(v,R::cjet(r+34).d);R::add(z,R::cjet(r+68).d);
    auto d1=v;R::add(d1,b,-1);R::add(z,v,-2);R::add(z,b,1);
    if(!R::zero(z))fails++;
    int j=R::cert(b,d1);if(j<0)fails++;else R::row(r,"dotR",j,b,d1);
   }
  }
 }
 int S=0,need17deriv=0;for(int s=1;s<=79808;s++)if((s%58==0||s%58>=54)&&(s%64==0||s%64>=60)&&(s%43==0||s%43>=37)){
  S++;int r=(s-1)%34+1;if((13<=r&&r<=17)||(30<=r&&r<=34))need17deriv++;
 }
 if(S!=91||need17deriv!=25||n17value!=24||n17deriv!=10)fails++;
 cerr<<"D17_D19: order19=38/38 order17_R0="<<n17value<<"/34 order17_dot="<<n17deriv<<"/34 S="<<S<<" S17dot="<<need17deriv<<" eliminated="<<(S+S+need17deriv)<<" remaining="<<(1375-S-S-need17deriv)<<" failures="<<fails<<"\n";
 return fails?1:0;
}
