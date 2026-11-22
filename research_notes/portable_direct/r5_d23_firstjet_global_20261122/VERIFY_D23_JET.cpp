#include <bits/stdc++.h>
using namespace std;
using I=long long; constexpr int D=23;
using Poly=array<I,D>;
struct Jet {Poly v{}, d{};};
const vector<vector<int>> E={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221}};
Poly shift(const Poly&a,int p){Poly b{};p%=D;for(int j=0;j<D;j++)b[(j+p)%D]=a[j];return b;}
void add_to(Poly&a,const Poly&b,int sign=1){for(int j=0;j<D;j++)a[j]+=sign*b[j];}
void add_to(Jet&a,const Jet&b,int sign=1){add_to(a.v,b.v,sign);add_to(a.d,b.d,sign);}
Jet shifted(const Jet&a,int p){Jet b;b.v=shift(a.v,p);b.d=shift(a.d,p);for(int j=0;j<D;j++)b.d[j]+=(I)p*b.v[j];return b;}
void mul_factor(Jet&a,int p){Jet b=shifted(a,p);add_to(a,b,-1);}
Jet cjet(int m){Jet t;t.v[0]=1;for(int p=296;p<=312;p++)mul_factor(t,p*m);return t;}
vector<I> canon(const Poly&a){vector<I>b(D-1);for(int j=0;j<D-1;j++)b[j]=a[j]-a[D-1];return b;}
string coeff(const Poly&a){auto b=canon(a);ostringstream out;for(int j=0;j<D-1;j++)out<<(j?";":"")<<b[j];return out.str();}
bool iszero(const Poly&a){auto b=canon(a);for(auto x:b)if(x)return false;return true;}
int main(){const int M=92;vector<Jet>A(M+1);
for(int mask=1;mask<8;mask++){
 vector<int>ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
 for(int id:ids)for(int p:E[id])U.push_back(p);
 sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
 int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
 vector<int>move(U.size()),belongs(U.size());
 for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M){if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){move[t]+=place;belongs[t]|=1<<j;}}
 vector<Jet> dp(total);dp[0].v[0]=1;
 for(size_t t=0;t<U.size();t++)for(int code=0;code<total;code++){
 int tmp=code;bool valid=true;for(int j=0;j<n;j++,tmp/=M)if((belongs[t]>>j&1)&&tmp%M==0){valid=false;break;}
 if(valid){Jet z=shifted(dp[code-move[t]],U[t]);add_to(dp[code],z);}
 }
 vector<Jet>layer(M);for(int code=0;code<total;code++){int x=code,k=0;for(int j=0;j<n;j++,x/=M)k=max(k,x%M);add_to(layer[k],dp[code]);}
 Jet prefix{};int sign=__builtin_popcount((unsigned)mask)%2?1:-1;
 for(int m=1;m<=M;m++){add_to(prefix,layer[m-1]);Jet z=prefix;for(int p:U)mul_factor(z,p);add_to(A[m],z,sign);}
 cerr<<"mask "<<mask<<" done\n";
 }
 cerr<<"primitive23 zero-order check: ";
 int failures=0;
 int n_nonzero=0, n_periodic=0;for(int r=1;r<=46;r++){if(!iszero(A[r].v))n_nonzero++;if(iszero(A[r].v)!=(r>=42))failures++;Poly diff=A[r+46].v;add_to(diff,A[r].v,-1);if(iszero(diff))n_periodic++;else failures++;}
 cerr<<"nonzero="<<n_nonzero<<" zero="<<(46-n_nonzero)<<" periodic="<<n_periodic<<"/46\n";
 cout<<"r,value_r_zero,value_r46_zero,base_dotR_coeff,delta_dotR_coeff,dotA_r_coeff,dotC_r_coeff\n";
 for(int r=42;r<=46;r++){
   auto C0=cjet(r),C1=cjet(r+46);Jet r0=A[r], r1=A[r+46];
   // at these phases A_r = A_(r+46) = 0 and B = C = 0, dotB = 0.
   add_to(r0.d,C0.d); add_to(r1.d,C1.d);
   Poly delta=r1.d;add_to(delta,r0.d,-1);
   I c0=canon(r0.d)[0], c1=canon(delta)[0];if(!iszero(A[r].v)||!iszero(A[r+46].v)||c0*c1<=0)failures++;
   cout<<r<<","<<iszero(A[r].v)<<","<<iszero(A[r+46].v)<<","<<coeff(r0.d)<<","<<coeff(delta)<<","<<coeff(A[r].d)<<","<<coeff(C0.d)<<"\n";
 }
 int total_s=0, d23_candidates=0;for(int s=1;s<=79808;s++){if((s%58==0||s%58>=54)&&(s%64==0||s%64>=60)&&(s%43==0||s%43>=37)){total_s++;int r=s%46;if(r==0||r>=42)d23_candidates++;}}
 if(total_s!=91||d23_candidates!=9)failures++;
 cerr<<"R5 d23 check: phases="<<n_periodic<<" nonzero_value="<<n_nonzero<<" zero_value="<<(46-n_nonzero)<<" S="<<total_s<<" affected="<<d23_candidates<<" failures="<<failures<<"\n";
 return failures?1:0;
}
