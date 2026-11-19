// Independent exact witness census, no modular lattice or floor sums.
// Compile: g++ -O3 -std=c++17 PREFIX941_R6_DIRECT_FULL_CENSUS.cpp -o prefix941_direct
#include <iostream>
#include <vector>
#include <cstdint>
#include <cstdlib>
#include <cassert>
using namespace std;
int main(int argc, char **argv) {
  if(argc!=3) { cerr<<"Usage: prefix941_direct K TMAX\n"; return 2; }
  const int64_t k=stoll(argv[1]); const int T=stoi(argv[2]);
  const int64_t L=262145, U=524287; const int J=18;
  assert((k&1) && k>0 && T>0);
  vector<uint64_t> by(T+1,0);
  for(int64_t a=L;a<=U;a+=2){
    const int64_t x=k*a;
    for(int j=0;j<=J;++j){
      const int64_t y=x^(int64_t(1)<<j);
      for(int i=0;i<=J;++i){
        const int64_t d=y-(int64_t(1)<<i);
        if(d<=0)continue;
        const int64_t tmin=(d+U-1)/U;
        const int64_t tmax=min<int64_t>(T,d/L);
        for(int64_t t=tmin;t<=tmax;++t){
          if(d%t==0){const int64_t b=d/t;if(b>=L&&b<=U&&(b&1))++by[t];}
        }
      }
    }
  }
  uint64_t sum=0;
  cout<<"{\"k\":"<<k<<",\"raw_by_t\":[";
  for(int t=1;t<=T;t++){if(t>1)cout<<",";cout<<by[t];sum+=by[t];}
  cout<<"],\"raw_witnesses\":"<<sum<<"}\n";
}
