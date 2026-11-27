#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <limits>
#include <vector>
// Each endpoint operation is enclosed by a relative 2^-50 plus absolute
// 2^-1000 padding. Assumes IEEE binary64 round-to-nearest, no fast-math.
struct I {
 double l,u;
 I(double x=0):l(x),u(x){} I(double x,double y):l(x),u(y){}
};
double dn(double x){ assert(std::isfinite(x)); return x-(std::abs(x)*0x1p-50+0x1p-1000); }
double up(double x){ assert(std::isfinite(x)); return x+(std::abs(x)*0x1p-50+0x1p-1000); }
I operator+(I x,I y){return {dn(x.l+y.l),up(x.u+y.u)};}
I operator-(I x,I y){return {dn(x.l-y.u),up(x.u-y.l)};}
I operator-(I x){return {-x.u,-x.l};}
I operator*(I x,I y){
 if(x.l>=0 && y.l>=0)return {dn(x.l*y.l),up(x.u*y.u)};
 if(x.u<=0 && y.l>=0)return {dn(x.l*y.u),up(x.u*y.l)};
 if(x.l>=0 && y.u<=0)return {dn(x.u*y.l),up(x.l*y.u)};
 double a=x.l*y.l,b=x.l*y.u,c=x.u*y.l,d=x.u*y.u;
 return {dn(std::min({a,b,c,d})),up(std::max({a,b,c,d}))};
}
I operator/(I x,I y){assert(y.l>0);return x*I(dn(1/y.u),up(1/y.l));}
struct J { I v,t; J(double x=0):v(x),t(0){} J(I x):v(x),t(0){} J(I x,I y):v(x),t(y){} };
J operator+(J x,J y){return {x.v+y.v,x.t+y.t};}
J operator-(J x,J y){return {x.v-y.v,x.t-y.t};}
J operator*(J x,J y){return {x.v*y.v,x.t*y.v+x.v*y.t};}
J operator/(J x,J y){I v=x.v/y.v;return {v,(x.t-v*y.t)/y.v};}
// Compute complete KA normalized carrier, with automatic derivative when T=J.
template<typename T> T residual(int d,T s){
 const I h=I(1)/I(d),h2=h*h;
 std::vector<T> U(d+1),M(d+1); U[0]=M[0]=T(1);
 for(int i=0;i<d;i++){
  // R_(lambda q+d)(k): ratio (1+(d-i)s/d^2)/(1+(d+i+3)s/d^2)
  T z=T(h2*I(d-i))*s,w=T(h2*I(d+i+3))*s;
  U[i+1]=U[i]*(T(1)+z)/(T(1)+w);
  M[i+1]=M[i]*(T(1)+z*T(.5))/(T(1)+w*T(.5));
 }
 T v(0),j(0),g(0),t=s*T(h2)/(T(1)+s*T(h));
 T den=T(1)+s*T(h),r=s/den, r2=r*r, ggden=T(2)*(T(2)+t);
 for(int k=0;k<=d;k++){
  I x=I(k)/I(d),y=I(d-k)/I(d),xh=x+h,yh=y+h;
  T fk=U[k]*M[d-k];
  T tk=s*T(y*y+h*y*I(.5))/(T(1)+s*T((h*x+h2)*I(.5)));
  T vv=T(xh*yh)*fk,jj=T(xh)*(T(1)-tk)*fk;
  T G=(T(1.5)*r-T(x*x+I(2)*x*h)*r2)/ggden;
  v=v+vv; j=j+jj; g=g+G*(T(2)*vv-T(h)*jj);
 }
 v=v*T(h);j=j*T(h);g=g*T(h);
 T b=v-T(h)*j,a=(v+b)*T(.25)+T(h2)*g;
 T e=U[d]*T(I(2)+I(3)*h)/(T(2)*(T(2)+T(2)*s*T(h)+s*T(h2)))
     *(T(2)+s*T(h)+T(2)*s*T(h2))/(T(8)+T(4)*s*T(h)+T(2)*s*T(h2));
 T P1=T(24)*s*T(I(3)+h)+T(3)*s*s*T(h*(I(3)+h)*(I(3)+h));
 T P=T(48)+T(h)*P1,T1=T(32)*s*T(I(1)+h),TT=T(96)+T(h)*T1;
 return T(-24)*a*j-T(96)*T(h)*a*g+P1*a*b-T1*a*a+T(h)*P*e*b
  -TT*(T(2)*a*s*T(h)*(v+b)+s*s*T(h2*h)*(v+b)*(v+b));
}
// Adaptive exact dyadic covering, endpoints are representable at depth <= 30.
uint64_t boxes=0,derboxes=0,signboxes=0; int maxdepth=0;
bool cover(int d,double a,double b,int mode,int depth=0){
 ++boxes;maxdepth=std::max(maxdepth,depth);
 if(mode==0){J f=residual(d,J(I(a,b),I(1)));if(f.t.l>0){++derboxes;return true;}}
 else {I f=residual(d,I(a,b));if((mode<0&&f.u<0)||(mode>0&&f.l>0)){++signboxes;return true;}}
 if(depth==30){std::printf("FAIL d=%d [%g,%g] mode=%d\n",d,a,b,mode);return false;}
 double mid=(a+b)/2;return cover(d,a,mid,mode,depth+1)&&cover(d,mid,b,mode,depth+1);
}
// Exact rational evaluation of original C mod prime p. Nonzero denominator
// and nonzero residue certify nonzero rational C, regardless of interval sign.
struct Z {
 static constexpr int64_t p=1000000007;
 int64_t a; Z(int64_t x=0):a((x%p+p)%p){}
};
Z operator+(Z x,Z y){return Z(x.a+y.a);}
Z operator-(Z x,Z y){return Z(x.a-y.a);}
Z operator*(Z x,Z y){return Z(x.a*y.a);}
Z operator/(Z x,Z y){assert(y.a!=0);Z r(1);int64_t n=Z::p-2;while(n){if(n&1)r=r*y;y=y*y;n>>=1;}return x*r;}
Z modC(int d,int q){
 Z u=q+d,m=2*q+d;std::vector<Z> U(d+1),M(d+1);U[0]=M[0]=1;
 for(int i=0;i<d;i++){U[i+1]=U[i]*(u-i)/(u+i+3);M[i+1]=M[i]*(m-i)/(m+i+3);}
 Z V=0,Q=0,A=0;
 for(int k=0;k<=d;k++){
  int l=d-k;Z a=Z(k+1)*Z(l+1)*U[k]*M[l],b=l?Z(k+1)*Z(l)*U[k]*M[l-1]:Z(0);
  V=V+a;Q=Q+b;A=A+(u-k)*(u+k+2)*(a+b)/(Z(2)*u*(Z(2)*u+1));
 }
 Z E=U[d]*(u-d)*Z(2*d+3)*(m+2)/(Z(2)*(Z(2)*u+1)*(Z(4)*m+2));
 Z W=A+E,B=Z(q)*A+Q+V,t=Z(4*q+3*d+1);
 return Z(3*q)*t*t*W*Q-Z(32)*Z(3*q+d+1)*B*B;
}
int main(int argc,char**argv){
 static_assert(std::numeric_limits<double>::is_iec559 && std::numeric_limits<double>::digits==53);
 int lo=argc>1?std::atoi(argv[1]):81,hi=argc>2?std::atoi(argv[2]):599;
 uint64_t candidates=0,modular=0; double mingap=1;int mind=0;
 for(int d=lo;d<=hi;d++){
  if(d<600 && (!cover(d,0,.75,-1)||!cover(d,.75,1.25,0)||!cover(d,1.25,4,1)))return 1;
  // Find adjacent integer budgets using signs at rational scale d^2/q.
  int a=d*d*4/5,b=(d*d*4+2)/3;
  auto sign=[&](int q){I f=residual(d,I(d*d)/I(q));return f.l>0?1:f.u<0?-1:0;};
  if(sign(a)!=1||sign(b)!=-1){std::printf("BRACKET FAIL %d\n",d);return 2;}
  bool usedmod=false;
  while(b-a>1){int m=(a+b)/2;int s=sign(m);if(!s){
    Z r=modC(d,m);
    if(sign(m-1)==1&&sign(m+1)==-1&&r.a!=0){std::printf("MOD PASS d=%d q=%d residue=%lld\n",d,m,(long long)r.a);a=m-1;b=m+1;usedmod=true;++modular;break;}
    std::printf("AMBIG %d %d residue=%lld\n",d,m,(long long)r.a);return 3;
   }if(s>0)a=m;else b=m;}
  assert(b-a==(usedmod?2:1));
  ++candidates;
  // gap is lower bound of |normalized residual| at the two bracket integers, not root distance.
  double gap=std::min(residual(d,I(d*d)/I(a)).l,-residual(d,I(d*d)/I(b)).u);
  if(gap<mingap){mingap=gap;mind=d;}
  if(d%50==0)std::printf("through %d boxes=%llu\n",d,(unsigned long long)boxes);
 }
 std::printf("PASS d=%d..%d count=%llu modular=%llu boxes=%llu sign_leaves=%llu derivative_leaves=%llu maxdepth=%d min_endpoint_residual_lower=%.17g at d=%d\n",lo,hi,(unsigned long long)candidates,(unsigned long long)modular,(unsigned long long)boxes,(unsigned long long)signboxes,(unsigned long long)derboxes,maxdepth,mingap,mind);
}
