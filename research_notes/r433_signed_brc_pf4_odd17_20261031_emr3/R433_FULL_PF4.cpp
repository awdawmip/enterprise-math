// R433: Exact complete fourth-order sign enumeration for signed BRC row r=17.
// Build: g++ -O3 -std=c++17 R433_FULL_PF4.cpp -o R433_FULL_PF4
// Requires Boost multiprecision headers, no third-party numeric runtime.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::int256_t;
using i128 = __int128_t;
using u64 = unsigned long long;
constexpr int n = 15;
// A[h] = H_{17,17-h}/38, h=0..15; H from original signed coefficient.
static const long long A[16] = {
  3411705LL, 51175575LL, 352336080LL, 1471685475LL,
  4156927425LL, 8382559185LL, 12423001500LL, 13726279710LL,
  11353874675LL, 6999985025LL, 3176099256LL, 1037186150LL,
  235481246LL, 35225190LL, 3208920LL, 145860LL
};
static inline long long entry(const long long *a, int size, int h) {
  return (h>=0 && h<size) ? a[h] : 0;
}
static inline i128 d3(const long long *x, const long long *y, const long long *z) {
  return i128(x[0]) * (i128(y[1])*z[2]-i128(y[2])*z[1])
       - i128(x[1]) * (i128(y[0])*z[2]-i128(y[2])*z[0])
       + i128(x[2]) * (i128(y[0])*z[1]-i128(y[1])*z[0]);
}
static int sign4(const long long *a, int size, const int *u, const int *v) {
  long long x[4][4];
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)x[i][j]=entry(a,size,v[j]-u[i]);
  int256_t val=0;
  for(int q=0;q<4;q++){
    int ix[3],k=0;
    for(int j=0;j<4;j++)if(j!=q)ix[k++]=j;
    long long y[]={x[1][ix[0]],x[1][ix[1]],x[1][ix[2]]};
    long long z[]={x[2][ix[0]],x[2][ix[1]],x[2][ix[2]]};
    long long w[]={x[3][ix[0]],x[3][ix[1]],x[3][ix[2]]};
    i128 b=d3(y,z,w);
    if(q%2) val -= int256_t(x[0][q])*int256_t(b);
    else    val += int256_t(x[0][q])*int256_t(b);
  }
  return (val>0)-(val<0);
}
int main(){
  // Known pre-R433 negative control, from original r=6 coefficients.
  const long long a6[]={132,528,900,672,280};
  const int negrows[]={0,1,2,3},negcols[]={1,4,5,6};
  if(sign4(a6,5,negrows,negcols)!=-1){std::cerr<<"negative control failed\n";return 2;}
  u64 positive=0, zero=0, negative=0;
  int u[]={0,0,0,0},v[4];
  for(u[1]=1;u[1]<=n;u[1]++)
  for(u[2]=u[1]+1;u[2]<=u[1]+n;u[2]++)
  for(u[3]=u[2]+1;u[3]<=u[2]+n;u[3]++)
  for(v[0]=0;v[0]<=n;v[0]++)
  for(v[1]=std::max(v[0]+1,u[1]);v[1]<=u[1]+n;v[1]++)
  for(v[2]=std::max(v[1]+1,u[2]);v[2]<=u[2]+n;v[2]++)
  for(v[3]=std::max(v[2]+1,u[3]);v[3]<=u[3]+n;v[3]++){
    const int s=sign4(A,16,u,v);
    positive+=(s>0);zero+=(s==0);negative+=(s<0);
    if(s<0 && negative<=3)
      std::cerr<<"negative witness rows="<<u[1]<<","<<u[2]<<","<<u[3]
               <<" cols="<<v[0]<<","<<v[1]<<","<<v[2]<<","<<v[3]<<"\n";
  }
  std::cout<<"R433_R17_PF4_EXACT positive="<<positive<<" zero="<<zero
           <<" negative="<<negative<<" total="<<(positive+zero+negative)
           <<" negative_control=PASS\n";
  return negative?1:0;
}
