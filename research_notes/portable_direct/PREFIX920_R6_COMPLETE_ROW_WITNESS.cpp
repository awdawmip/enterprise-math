// Exact, source-labeled row witness search reusing the PREFIX-918 interval kernel.
// Compile: g++ -O3 -std=c++17 PREFIX920_R6_COMPLETE_ROW_WITNESS.cpp -o prefix920w
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <numeric>
using i64=std::int64_t;
static i64 floor_div(i64 z,i64 d){i64 q=z/d;if(z%d<0)--q;return q;}
static i64 bit_one_prefix(i64 z,int j){i64 h=i64(1)<<j,per=2*h,q=floor_div(z,per),r=z-q*per;return q*h+std::max<i64>(0,r-h);}
static i64 clamp(i64 z,i64 low,i64 high){return std::min(high,std::max(low,z));}
static i64 high_low_prefix(i64 z,int h,int l,int hb,int lb,i64 shift){
 i64 H=i64(1)<<h,per=2*H,q=z/per,r=z%per;
 i64 len=clamp(r-i64(hb)*H,0,H);
 i64 ones=bit_one_prefix(shift+len,l)-bit_one_prefix(shift,l);
 return q*(H/2)+(lb?ones:len-ones);
}
static i64 same_index_prefix(i64 z,int i,int hb,int lb,i64 A){
 i64 H=i64(1)<<i,per=2*H,rA=A%per;
 auto tail=[&](i64 limit)->i64{ i64 L=i64(hb)*H,R=L+H,total=0;
 for(int m=0;m<=1;m++){i64 X=i64(lb)*H-rA+i64(m)*per,Y=X+H;
 total+=std::max<i64>(0,std::min({R,Y,limit})-std::max(L,X));}
 return total;};
 return (z/per)*tail(per)+tail(z%per);
}
static i64 kernel_prefix(i64 z,i64 A,int i,int j,int eps,int eta){
 int bi=(eps<0),bj=(eta<0);
 if(i>j)return high_low_prefix(z,i,j,bi,bj,A);
 if(i<j)return high_low_prefix(A+z,j,i,bj,bi,-A)-high_low_prefix(A,j,i,bj,bi,-A);
 return same_index_prefix(z,i,bi,bj,A);
}
static i64 mod(i64 x,i64 m){i64 r=x%m;return r<0?r+m:r;}
static i64 egcd_inv(i64 a,i64 m){if(m==1)return 0;
 i64 t=0,nt=1,r=m,nr=mod(a,m);while(nr){i64 q=r/nr; i64 T=t-q*nt; t=nt;nt=T; i64 R=r-q*nr;r=nr;nr=R;}
 if(r!=1){std::cerr<<"bad inverse\n";std::exit(3);}return mod(t,m);}
struct Witness{int type=0; i64 x=0,y=0,k=0; int i=-1,j=-1,eps=0,eta=0;};
static void verify(int a,int b,Witness w){
 constexpr i64 N=i64(1)<<32;
 if(w.type<1 || w.type>3 || w.x<0 || w.y<=w.x || w.y>=N) {std::cerr<<"invalid witness range\n";std::exit(4);}
 auto terminal=[](i64 x,int i)->i64{return i<0 ? x : (x^(i64(1)<<i));};
 i64 U=terminal(w.x,w.i),V=terminal(w.y,w.j);
 if((w.y-w.x)%a!=0 || (V-U)%b!=0){std::cerr<<"invalid witness residue "<<a<<","<<b<<"\n";std::exit(4);}
}
static Witness scan(int a,int b){
 constexpr i64 N=i64(1)<<32;
 i64 g=std::gcd(a,b), d=(i64(a)/g)*b;
 if(d<N){Witness w;w.type=1;w.x=0;w.y=d;verify(a,b,w);return w;}
 int cap=(N-1)/a;
 if(g==1){
  i64 q=egcd_inv(a,b);
  for(int i=0;i<32;i++){
   i64 H=i64(1)<<i;
   if(q<=cap){Witness w;w.type=2;w.i=i;w.j=-1;w.k=q;w.x=0;w.y=q*a;verify(a,b,w);return w;}
   if(b-q<= (N-1-H)/a){Witness w;w.type=2;w.i=i;w.j=-1;w.k=b-q;w.x=H;w.y=H+(b-q)*a;verify(a,b,w);return w;}
   q=(q*2)%b;
  }
 }
 i64 bb=b/g,inv=egcd_inv(a/g,bb);
 for(int i=0;i<32;i++)for(int j=0;j<32;j++)for(int eps=-1;eps<=1;eps+=2)for(int eta=-1;eta<=1;eta+=2){
  i64 delta=i64(eps)*(i64(1)<<i)-i64(eta)*(i64(1)<<j);
  if(delta%g!=0)continue;
  i64 k0=mod(mod(delta/g,bb)*inv,bb),k=k0?k0:bb;
  for(;k<=cap;k+=bb){
   i64 A=k*a,L=N-A;
   if(kernel_prefix(L,A,i,j,eps,eta)==0)continue;
   i64 lo=0,hi=L;
   while(lo+1<hi){i64 mid=(lo+hi)/2;
    if(kernel_prefix(mid,A,i,j,eps,eta)>0)hi=mid;else lo=mid;
   }
   i64 x=kernel_prefix(1,A,i,j,eps,eta)>0?0:hi-1;
   // Binary search minimal z with count>0: z=hi, hence x=hi-1.
   if(kernel_prefix(1,A,i,j,eps,eta)==0)x=hi-1;
   i64 y=x+A;
   if(x<0 || y>=N || (((x>>i)&1)!=(eps<0)) || (((y>>j)&1)!=(eta<0))){
    std::cerr<<"failed kernel x construction: "<<a<<","<<b<<","<<x<<","<<i<<","<<j<<"\n";std::exit(2);}
   i64 u=x^(i64(1)<<i),v=y^(i64(1)<<j);
   if((y-x)%a || (v-u)%b){std::cerr<<"failed congruence\n";std::exit(2);}
   Witness w;w.type=3;w.x=x;w.y=y;w.k=k;w.i=i;w.j=j;w.eps=eps;w.eta=eta;verify(a,b,w);return w;
  }
 }
 return {};
}
int main(){
 int b=440665;
 i64 count[5]={0,0,0,0,0};
 for(int a=262145;a<=524287;a+=2){
  Witness w=scan(a,b);count[w.type]++;
  if(w.type==0)std::cout<<"NO_COLLISION "<<a<<","<<b<<"\n";
  std::cout<<"W "<<a<<","<<b<<","<<w.type<<","<<w.x<<","<<w.y<<","<<w.i<<","<<w.j<<"\n";
  if(a==262151)std::cout<<"TARGET "<<a<<" type="<<w.type<<" x="<<w.x<<" y="<<w.y<<" k="<<w.k<<" i="<<w.i<<" j="<<w.j<<" eps="<<w.eps<<" eta="<<w.eta<<"\n";
 }
 std::cout<<"TOTAL no="<<count[0]<<" zerozero="<<count[1]<<" mixed="<<count[2]<<" twoflip_only="<<count[3]<<" entries="<<count[0]+count[1]+count[2]+count[3]<<"\n";
}
