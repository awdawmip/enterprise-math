// R436: signed BRC row r=21, full PF4 sign certificate.
// Build: g++ -O3 -std=c++17 -fno-fast-math R436_PF4_R21_FAST.cpp -o r436fast
// Run: ./r436fast 1 19
#include <algorithm>
#include <array>
#include <cfenv>
#include <cfloat>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <limits>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::int256_t;
using u64=unsigned long long;
static constexpr int N=19;
static const long long A[N+1]={265937685LL,5052816015LL,44755366500LL,245123196435LL,928703791575LL,2580473188755LL,5440446007920LL,8883931485000LL,11370958222140LL,11473827951300LL,9134206720080LL,5715598465395LL,2787996290625LL,1046134052145LL,296152950600LL,61538108580LL,9027870995LL,883364625LL,53024972LL,1616615LL};
static inline long long entry(int h){return (h>=0&&h<=N)?A[h]:0;}
static std::array<std::array<int,4>,24> PERM;
static int SIGN[24];
static void init(){std::array<int,4> p={0,1,2,3};int z=0;do{
 PERM[z]=p;int inversions=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)inversions+=(p[i]>p[j]);
 SIGN[z]=(inversions&1)?-1:1;++z;
}while(std::next_permutation(p.begin(),p.end()));}
static inline int256_t d3(const long long*x,const long long*y,const long long*z){
 return int256_t(x[0])*(int256_t(y[1])*z[2]-int256_t(y[2])*z[1])
       -int256_t(x[1])*(int256_t(y[0])*z[2]-int256_t(y[2])*z[0])
       +int256_t(x[2])*(int256_t(y[0])*z[1]-int256_t(y[1])*z[0]);
}
static inline int256_t exact_det4(const long long m[4][4]){
 int256_t d=0;
 for(int q=0;q<4;q++){
  int ix[3],j=0;for(int k=0;k<4;k++)if(k!=q)ix[j++]=k;
  long long x[3]={m[1][ix[0]],m[1][ix[1]],m[1][ix[2]]};
  long long y[3]={m[2][ix[0]],m[2][ix[1]],m[2][ix[2]]};
  long long z[3]={m[3][ix[0]],m[3][ix[1]],m[3][ix[2]]};
  int256_t t=int256_t(m[0][q])*d3(x,y,z);
  d+=(q&1)?-t:t;
 }
 return d;
}
static inline int certified_sign(const long long m[4][4],u64& ambiguous){
 long double d=0, S=0;
 for(int j=0;j<24;j++){
  const auto &p=PERM[j];
  long double t=((long double)m[0][p[0]]*(long double)m[1][p[1]])*
                 (long double)m[2][p[2]];
  t*=(long double)m[3][p[3]];
  d+=(SIGN[j]>0)?t:-t;
  S+=std::fabs(t);
 }
 constexpr long double CUTOFF=1.0e-15L;
 if(d>CUTOFF*S)return 1;
 if(d<-CUTOFF*S)return -1;
 ambiguous++;
 int256_t x=exact_det4(m);
 return (x>0)-(x<0);
}
int main(int argc,char** argv){
 if(LDBL_MANT_DIG<64 || !std::numeric_limits<long double>::is_iec559 ||
    std::fegetround()!=FE_TONEAREST){std::cerr<<"Unsupported floating environment\n";return 9;}
 init();
 int begin=1,end=N;
 if(argc>1)begin=std::stoi(argv[1]);if(argc>2)end=std::stoi(argv[2]);
 u64 pos=0,zero=0,neg=0,ambiguous=0;int u[]={0,0,0,0},v[4];
 for(u[1]=begin;u[1]<=end;u[1]++)
 for(u[2]=u[1]+1;u[2]<=u[1]+N;u[2]++)
 for(u[3]=u[2]+1;u[3]<=u[2]+N;u[3]++)
 for(v[0]=0;v[0]<=N;v[0]++)
 for(v[1]=std::max(v[0]+1,u[1]);v[1]<=u[1]+N;v[1]++)
 for(v[2]=std::max(v[1]+1,u[2]);v[2]<=u[2]+N;v[2]++)
 for(v[3]=std::max(v[2]+1,u[3]);v[3]<=u[3]+N;v[3]++){
   long long m[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++)m[i][j]=entry(v[j]-u[i]);
   const int sign=certified_sign(m,ambiguous);
   pos+=(sign>0);zero+=(sign==0);neg+=(sign<0);
   if(sign<0 && neg<=10){std::cerr<<"NEG rows=0,"<<u[1]<<","<<u[2]<<","<<u[3]
    <<" cols="<<v[0]<<","<<v[1]<<","<<v[2]<<","<<v[3]
    <<" exact_det="<<exact_det4(m)<<"\n";}
 }
 std::cout<<"R436_PF4_R21_CERTIFIED u1="<<begin<<".."<<end<<" pos="<<pos<<" zero="<<zero<<" neg="<<neg
 << " total="<<(pos+zero+neg)<<" exact_fallback="<<ambiguous
 <<" cutoff=1e-15 mant="<<LDBL_MANT_DIG<<"\n";
 return neg?1:0;
}
