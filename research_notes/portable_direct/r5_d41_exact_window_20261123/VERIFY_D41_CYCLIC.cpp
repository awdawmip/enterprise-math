// Exact cyclic integer proof for frozen R5 five-event scalar observer.
// Science: awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
// Computes A_m modulo x^41-1 in Z[x]; all 41 coefficients are printed/tested.
// For m <= 83, |intermediate coefficient| <= 7*2^8*m^8 < INT64_MAX.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
constexpr int D=41;
using Ring = array<int64_t,D>;
const vector<int> E[3]={
 {214,215,216,217,218},
 {214,216,217,218,219,220,221},
 {215,216,217,218,219,220,221}
};
inline void add_shift(Ring &target,const Ring &source,int shift){
 for(int k=0;k<D;k++) target[(k+shift)%D]+=source[k];
}
inline void mul_one_minus(Ring &target,int price){
 Ring old=target;int r=price%D;
 for(int k=0;k<D;k++) target[(k+r)%D]-=old[k];
}
Ring calc_mask(int m,int mask){
 vector<int> selected,prices;
 for(int k=0;k<3;k++) if(mask&(1<<k))selected.push_back(k);
 for(int price=214;price<=221;price++){
  bool active=false;
  for(int k:selected) if(find(E[k].begin(),E[k].end(),price)!=E[k].end())active=true;
  if(active)prices.push_back(price);
 }
 const int r=(int)selected.size();
 vector<int> stride(r,1);for(int j=r-2;j>=0;j--)stride[j]=stride[j+1]*m;
 int n=1;for(int k=0;k<r;k++)n*=m;
 vector<Ring> dp(n);
 dp[0][0]=1;
 for(int price:prices){
  int offset=0;vector<int> delta(r);
  for(int j=0;j<r;j++){
   delta[j]=find(E[selected[j]].begin(),E[selected[j]].end(),price)!=E[selected[j]].end();
   offset+=delta[j]*stride[j];
  }
  for(int idx=offset;idx<n;idx++){
   bool ok=true;
   for(int j=0;j<r;j++)if(delta[j]&&(idx/stride[j])%m==0){ok=false;break;}
   if(ok)add_shift(dp[idx],dp[idx-offset],price%D);
  }
 }
 Ring sum{};for(const Ring&v:dp)for(int k=0;k<D;k++)sum[k]+=v[k];
 for(int price:prices)mul_one_minus(sum,price);
 return sum;
}
Ring calc_A(int m){
 Ring out{};
 for(int mask=1;mask<8;mask++){
  Ring term=calc_mask(m,mask);
  int parity=__builtin_popcount((unsigned)mask);
  for(int k=0;k<D;k++)out[k]+=(parity%2?term[k]:-term[k]);
 }
 return out;
}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: verify_d41_exact FIRST LAST\n";return 2;}
 int lo=atoi(argv[1]),hi=atoi(argv[2]);
 if(lo<1||hi>83||lo>hi){cerr<<"Require 1<=FIRST<=LAST<=83 for int64 bound\n";return 3;}
 for(int m=lo;m<=hi;m++){
  Ring a=calc_A(m);
  bool same=true;int64_t minv=a[0],maxv=a[0];
  for(int j=1;j<D;j++){same&=(a[j]==a[0]);minv=min(minv,a[j]);maxv=max(maxv,a[j]);}
  cout<<"m="<<m<<" phi41_divides_A="<<same<<" coeff0="<<a[0]<<" min="<<minv<<" max="<<maxv<<"\n";
  if(!same){for(int k=0;k<D;k++)if(a[k]!=a[0]){cout<<"first_diff="<<k<<" delta="<<a[k]-a[0]<<"\n";break;}}
 }
}
