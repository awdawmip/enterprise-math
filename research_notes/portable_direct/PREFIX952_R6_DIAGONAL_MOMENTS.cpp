// PREFIX-952: exhaustive strict-Q19 named diagonal witness multiplicities
// g++ -O3 -std=c++17 PREFIX952_R6_DIAGONAL_MOMENTS.cpp -o prefix952
// Run in a writable directory; reproduces entire per-core CSV and summary.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
int main() {
  constexpr int p=19,H=1<<(p-1),M=1<<p,A=H+1,N=H/2;
  vector<uint64_t> hist(p+2,0);
  uint64_t total=0,base=0,bonusTotal=0,topZeroSum=0,zeroPairs=0;
  ofstream csv("PREFIX952_PER_CORE_Q19.csv");
  csv<<"k,witness_total,top_zero_count,top_one_count,rescue_bonus,no_witness_count,first_no_witness\n";
  int minW=99,maxW=-1,maxK=-1,maxA=-1;
  for (int k=1;k<=8191;k+=2) {
    uint64_t sum=0;
    int upperZero=0,zeros=0,first=-1;
    for (int a=A;a<M;a+=2) {
      uint64_t v=uint64_t(k)*a;
      int z=p-__builtin_popcountll(v&(M-1));
      int bonus=(a==A && k>1)?(1+int((v>>(p-1))&1)):0;
      int w=z+bonus;
      ++hist[w];sum+=w;base+=z;bonusTotal+=bonus;
      if (!((v>>(p-1))&1)) ++upperZero;
      if (!w) {++zeros;if(first<0)first=a;}
      if (w>maxW){maxW=w;maxK=k;maxA=a;}
      minW=min(minW,w);
    }
    const int bonus=k>1?2:0;
    if (sum!=uint64_t(17*N/2+upperZero+bonus))return 2;
    csv<<k<<","<<sum<<","<<upperZero<<","<<N-upperZero<<","
       <<bonus<<","<<zeros<<","<<first<<"\n";
    total+=sum;topZeroSum+=upperZero;zeroPairs+=zeros;
  }
  csv.close();
  uint64_t joint=0,commonDiag=0;
  for(int a=A;a<M;a+=2) {
    int z21=p-__builtin_popcountll((uint64_t(21)*a)&(M-1));
    int z23=p-__builtin_popcountll((uint64_t(23)*a)&(M-1));
    joint+=uint64_t(z21)*z23;
    if(z21 && z23)++commonDiag;
  }
  if(joint!=10541739 || commonDiag!=131071 || zeroPairs!=2051)return 3;
  ostringstream o;
  o<<"{\n\"schema\":\"PREFIX952_R6_DIAGONAL_MOMENTS_V1\","
   <<"\n\"configurations\":536870912,"
   <<"\n\"all_witnesses\":"<<total
   <<",\n\"ordinary_zero_bit_witnesses\":"<<base
   <<",\n\"rescue_witnesses\":"<<bonusTotal
   <<",\n\"top_zero_sum\":"<<topZeroSum
   <<",\n\"zero_witness_pairs\":"<<zeroPairs
   <<",\n\"min_witnesses\":"<<minW
   <<",\n\"max_witnesses\":"<<maxW
   <<",\n\"first_max_core\":"<<maxK
   <<",\n\"first_max_modulus\":"<<maxA
   <<",\n\"joint_resonant_21_23\":"<<joint
   <<",\n\"common_diagonal_21_23\":"<<commonDiag
   <<",\n\"histogram_0_20\":[";
  for (size_t i=0;i<hist.size();++i) {if(i)o<<",";o<<hist[i];}
  o<<"]\n}\n";
  ofstream file("PREFIX952_R6_DIAGONAL_MOMENTS_RESULTS.json");file<<o.str();
  cout<<o.str();
}
