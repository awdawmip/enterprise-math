// R435: signed BRC row r=19 complete fourth-order Toeplitz positivity.
// Fast filter uses an IEEE-754 80-bit long double forward-error bound;
// ambiguous cases and negative witnesses are recomputed using signed int256_t.
// Build: g++ -O3 -std=c++17 -fno-fast-math R435_FAST_CERTIFIED_PF4.cpp -o R435_FAST_CERTIFIED_PF4
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
static constexpr int N=17;
static const long long A[18]={
883631595LL,15021737115LL,118215578250LL,570420017475LL,1885199008440LL,4516469666280LL,
8099050221360LL,11069635101525LL,11635491988575LL,9424350050115LL,5858143180890LL,
2766367523205LL,975765719500LL,250607657300LL,45153996888LL,5398847454LL,394777383LL,14549535LL};
static inline long long entry(int h){return h>=0&&h<=N?A[h]:0;}
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
 // Exact input cast: every coefficient is below 2^44; 80-bit significand has 64 bits.
 for(int j=0;j<24;j++){
  const auto &p=PERM[j];
  long double t=((long double)m[0][p[0]]*(long double)m[1][p[1]])*
                 (long double)m[2][p[2]];
  t*=(long double)m[3][p[3]];
  d+=(SIGN[j]>0)?t:-t;
  S+=std::fabs(t);
 }
 // Products: three rounded multiplications; sums: at most 23 additions.
 // Unit roundoff 2^-64 implies <=gamma_26*S_true total absolute error.
 // Shat differs from S_true by <=gamma_26*S_true.
 // Thus |Dhat-D| <=gamma_26/(1-gamma_26)*Shat < 1e-15*Shat.
 constexpr long double CUTOFF=1.0e-15L;
 if(d>CUTOFF*S)return 1;
 if(d<-CUTOFF*S)return -1;
 ambiguous++;
 int256_t x=exact_det4(m);
 return (x>0)-(x<0);
}
int main(){
 if(LDBL_MANT_DIG<64 || !std::numeric_limits<long double>::is_iec559 ||
    std::fegetround()!=FE_TONEAREST){std::cerr<<"Unsupported floating environment\n";return 9;}
 init();
 // Independent published r=6 negative witness recomputed with exact integer matrix.
 const long long B[5]={132,528,900,672,280};const int ru[4]={0,1,2,3},cv[4]={1,4,5,6};
 long long cm[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++){
  int h=cv[j]-ru[i];cm[i][j]=(h>=0&&h<5)?B[h]:0;
 }
 if(exact_det4(cm)!=-4117994496LL){std::cerr<<"NEG_CONTROL_ERROR\n";return 4;}
 u64 pos=0,zero=0,neg=0,ambiguous=0;int u[]={0,0,0,0},v[4];
 for(u[1]=1;u[1]<=N;u[1]++)
 for(u[2]=u[1]+1;u[2]<=u[1]+N;u[2]++)
 for(u[3]=u[2]+1;u[3]<=u[2]+N;u[3]++)
 for(v[0]=0;v[0]<=N;v[0]++)
 for(v[1]=std::max(v[0]+1,u[1]);v[1]<=u[1]+N;v[1]++)
 for(v[2]=std::max(v[1]+1,u[2]);v[2]<=u[2]+N;v[2]++)
 for(v[3]=std::max(v[2]+1,u[3]);v[3]<=u[3]+N;v[3]++){
   long long m[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++)m[i][j]=entry(v[j]-u[i]);
   const int sign=certified_sign(m,ambiguous);
   pos+=(sign>0);zero+=(sign==0);neg+=(sign<0);
   if(sign<0 && neg<=5){std::cerr<<"NEG rows=0,"<<u[1]<<","<<u[2]<<","<<u[3]
    <<" cols="<<v[0]<<","<<v[1]<<","<<v[2]<<","<<v[3]
    <<" exact_det="<<exact_det4(m)<<"\n";}
 }
 std::cout<<"R435_PF4_R19_CERTIFIED pos="<<pos<<" zero="<<zero<<" neg="<<neg
 <<" total="<<(pos+zero+neg)<<" exact_fallback="<<ambiguous
 <<" cutoff=1e-15 long_double_mant_dig="<<LDBL_MANT_DIG<<" neg_control=PASS\n";
 return neg?1:0;
}
