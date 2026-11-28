#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using I=int64_t;
struct Pair{int v; I u;};
struct Eval {
 int d,p,s,g; I mod,period; std::vector<I> pw; std::vector<Pair> U,N,tail,weights; 
 Eval(int d_,int p_,int s_):d(d_),p(p_),s(s_),g(0),mod(1),period(1),pw(s+1),U(d+1),N(d+1),tail(d+1),weights(d+2){
  pw[0]=1;for(int i=1;i<=s;i++)pw[i]=pw[i-1]*p;mod=pw[s];
  I m=d+2;while(m){m/=p;g+=m;}for(I a=p;a<=d+2;a*=p)g--;
  period=mod;for(I a=p;a<=d;a*=p){if(period>INT64_MAX/p){period=0;break;}period*=p;}
  for(int k=1;k<=d+1;k++)weights[k]=split(k);
 }
 I mul(I a,I b)const{if(p==2)return (I)((uint64_t(a)*uint64_t(b))&uint64_t(mod-1));return (I)((__int128(a)*b)%mod);}
 Pair split(I x)const{assert(x>0);int v=0;while(x%p==0){x/=p;v++;}return {v,x%mod};}
 Pair prod(Pair a,Pair b)const{return {a.v+b.v,mul(a.u,b.u)};}
 void branch(I v,std::vector<Pair>& out){tail[d]={0,1};for(int k=d-1;k>=0;k--)tail[k]=prod(tail[k+1],split(v+k+3));Pair pre={0,1};for(int k=0;k<=d;k++){out[k]=prod(pre,tail[k]);if(k<d)pre=prod(pre,split(v-k));}}
 I norm(Pair a)const{int e=a.v-2*g;assert(e>=0);return e>=s?0:mul(a.u,pw[e]);}
 I operator()(I q){I u=q+d,n=2*q+d;branch(u,U);branch(n,N);I v=0,b=0,a=0;
  for(int k=0;k<=d;k++){int l=d-k;I A=norm(prod(prod(U[k],N[l]),prod(weights[k+1],weights[l+1]))),B=l?norm(prod(prod(U[k],N[l-1]),prod(weights[k+1],weights[l]))):0;
   v=(v+A)%mod;b=(b+B)%mod;a=(a+mul(mul((u-k)%mod,(u+k+2)%mod),(A+B)%mod))%mod;}
  I J=mul(2*u%mod,(2*u+1)%mod),L=(4*n+2)%mod;
  I ep=norm(prod(U[d],N[0]));for(I x:{u,q, I(2*d+3),n+2})ep=mul(ep,x%mod);
  I W=(mul(L,a)+ep)%mod,Q=mul(mul(J,L),b),Z=mul(L,(mul(q%mod,a)+mul(J,(b+v)%mod))%mod),F=(4*q+3*d+1)%mod;
  I r=(mul(mul(mul(3*q%mod,mul(F,F)),W),Q)-mul(mul(32%mod,(3*q+d+1)%mod),mul(Z,Z)))%mod;return (r+mod)%mod;
 }
};
int main(int argc,char**argv){int lo=argc>1?atoi(argv[1]):3001,hi=argc>2?atoi(argv[2]):3003;for(int d=lo;d<=hi;d++){I low=(4LL*d*d+4)/5,high=4LL*d*d/3;std::vector<I> cand;for(I q=low;q<=high;q++)cand.push_back(q);std::cout<<"d="<<d<<" initial="<<cand.size()<<std::endl;for(int p:{2,3,5,7}){int s=p==2?54:p==3?33:p==5?23:19;Eval e(d,p,s);int min=s;for(int q=0;q<=4*d+9;q++){I x=e(q);int v=0;while(v<s&&x%p==0){v++;x/=p;}min=std::min(min,v);}if(min==s){std::cout<<"saturated p="<<p<<std::endl;continue;}Eval z(d,p,min+1);I period=p;for(I a=p;a<=4*d+9;a*=p)period*=p;std::vector<char> pass(period);I count=0;for(I q=0;q<period;q++){pass[q]=(z(q)==0);count+=pass[q];}auto end=std::remove_if(cand.begin(),cand.end(),[&](I q){return !pass[q%period];});cand.erase(end,cand.end());std::cout<<"p="<<p<<" g="<<e.g<<" extra="<<min<<" period="<<period<<" zero_classes="<<count<<" remaining="<<cand.size()<<std::endl;if(cand.empty())break;}}}
