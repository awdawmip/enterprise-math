#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
using ll=long long;
static int mod(ll x,int p){int r=(int)(x%p);return r<0?r+p:r;}
static int inv(int a,int p){int t=1,x=mod(a,p),e=p-2;while(e){if(e&1)t=mod((ll)t*x,p);x=mod((ll)x*x,p);e>>=1;}return t;}
struct F {int a,b;};
static F mul(F u,F v,int p){return {mod((ll)u.a*v.a+2LL*u.b*v.b,p),mod((ll)u.a*v.b+(ll)u.b*v.a,p)};}
static int legendre_coeff(int p){
 int m=(p-3)/8,deg=2*m, Y=mod(8LL*inv(9,p),p);
 F prev{1,0},cur{0,1};
 for(int n=1;n<deg;n++){
  F z{mod((ll)cur.b*Y,p),cur.a};int r=inv(n+1,p);
  F next{mod(((ll)(2*n+1)*z.a-(ll)n*prev.a)*r,p),mod(((ll)(2*n+1)*z.b-(ll)n*prev.b)*r,p)};
  prev=cur;cur=next;
 }
 assert(cur.b==0); return cur.a;
}
static bool is_prime(int x){if(x<2)return false;for(int d=2;d*d<=x;d++)if(x%d==0)return false;return true;}
static pair<int,int> representation(int p){
 pair<int,int> ans{-1,-1};
 for(int x=1;2*x*x<p;x++){
   int r=p-2*x*x;
   if(r%3)continue;
   int y=(int)sqrt(r/3);
   while(3*(y+1)*(y+1)<=r)y++;
   while(3*y*y>r)y--;
   if(y>0 && 3*y*y==r){assert(ans.first==-1);ans={x,y};}
 }
 return ans;
}
static int point_trace(int p){
 vector<int> chi(p,-1);chi[0]=0;for(int k=1;k<p;k++)chi[(ll)k*k%p]=1;
 F B{inv(8,p),inv(12,p)};ll S=0;
 for(int a=0;a<p;a++)for(int b=0;b<p;b++){
  F z{a,b},z2=mul(z,z,p),z3=mul(z2,z,p),bz=mul(B,z,p);
  F f{mod((ll)z3.a+z2.a+bz.a,p),mod((ll)z3.b+z2.b+bz.b,p)};
  int norm=mod((ll)f.a*f.a-2LL*f.b*f.b,p);
  S+=chi[norm];
 }
 return (int)-S;
}
int main(){
 int split=0,inert=0;
 for(int p=11;p<800;p++){
  if(!is_prime(p)||p%8!=3)continue;
  int trace=point_trace(p),E=legendre_coeff(p),modtrace=mod(trace,p);
  assert(modtrace==mod((ll)E*E,p));
  if(p%24==11){
   auto [x,y]=representation(p);assert(x>0&&y>0);
   int expected=6*y*y-4*x*x;
   assert(trace==expected);
   assert(mod(4LL*x*x-6LL*y*y,p)==mod(8LL*x*x,p));
   assert(E!=0);
   split++;
   cout<<"SPLIT p="<<p<<" x="<<x<<" y="<<y<<" a_q="<<trace<<" E="<<E<<" points="<<((ll)p*p+1-trace)<<"\n";
  }else{
   assert(p%24==19);assert(E==0);inert++;
   cout<<"INERT p="<<p<<" a_q="<<trace<<" E=0\n";
  }
 }
 {
  int p=3347,x=40,y=7,E=legendre_coeff(p);
  assert(representation(p)==make_pair(x,y));
  int expected=6*y*y-4*x*x;
  assert(expected==-6106);
  assert(E==783);assert(mod((ll)E*E,p)==mod(expected,p));
  cout<<"LARGE p=3347 x=40 y=7 predicted_a_q="<<expected<<" E="<<E<<" predicted_points="<<(ll)p*p+1-expected<<" [independent direct point count is GH-115]\n";
 }
 cout<<"PASS_GH116_SPLIT_CM_TRACE split="<<split<<" inert_diagnostics="<<inert<<"\n";
}
