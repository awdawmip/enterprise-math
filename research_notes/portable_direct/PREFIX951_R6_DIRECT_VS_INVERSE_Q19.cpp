#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <sstream>
using namespace std;
static constexpr uint32_t P=19, H=1u<<(P-1), M=1u<<P, U=M-1, MASK=U;
static uint32_t invmod(uint32_t k){
  // Hensel / Newton lift for odd k: each pass doubles correct bits.
  uint32_t x=k;
  for(int i=0;i<5;++i)x*=2u-k*x;
  return x & MASK;
}
int main(){
  vector<uint32_t> exceptional;
  uint64_t scanned=0, validated_witnesses=0;
  for(uint32_t k=1;k<=8191;k+=2){
    uint32_t e=(M-invmod(k))&MASK;
    bool expected_missing=(e>H && (e&1u));
    uint32_t direct_missing=0,direct_bad=0;
    for(uint32_t a=H+1;a<M;a+=2){
      ++scanned;
      uint64_t x=(uint64_t)k*a;
      uint32_t low=(uint32_t)x & MASK;
      bool exists=(low!=MASK);
      if(!exists){++direct_missing; if(a!=e)++direct_bad;}
      if(k==1||k==3||k==7||k==15||k==17||k==21||k==23||k==8191){
        if(exists){
          uint32_t j=0;
          while(((x>>j)&1u)!=0)++j;
          uint64_t second=x^(uint64_t(1)<<j);
          assert(j<P && second < (uint64_t(1)<<32));
          int64_t d=(int64_t)second-(int64_t(1)<<j);
          assert(d==int64_t(k)*a && d>0);
          assert((second%a)==((uint64_t(1)<<j)%a));
          ++validated_witnesses;
        }
      }
    }
    if(direct_bad || direct_missing != (uint32_t)expected_missing){
      cerr << "Mismatch k="<<k<<" direct_missing="<<direct_missing<<" modular_exception="<<e<<"\n";return 1;
    }
    if(expected_missing)exceptional.push_back(e);
  }
  sort(exceptional.begin(),exceptional.end());
  assert(unique(exceptional.begin(),exceptional.end())==exceptional.end());
  cout << "{\n\"domain\":{\"bits\":19,\"a_odd_min\":262145,\"a_odd_max\":524287,\"core_odd_min\":1,\"core_odd_max\":8191,\"state_limit_exclusive\":4294967296},\n";
  cout << "\"test\":{\"scanned_core_modulus_pairs\":"<<scanned<<",\"independent_named_bit_witnesses_checked\":"<<validated_witnesses<<",\"direct_vs_inverse_equal\":true},\n";
  cout << "\"results\":{\"core_count\":4096,\"exceptional_count\":"<<exceptional.size()<<",\"universal_diagonal_count\":"<<131072-exceptional.size()<<",\"exceptional_first\":"<<exceptional.front()<<",\"exceptional_last\":"<<exceptional.back()<<",\"pair_21_23_diagonal_intersection\":" << 131072-int(((((M-invmod(21))&MASK)>H)?1:0)+((((M-invmod(23))&MASK)>H)?1:0)) <<"}\n}\n";
}
