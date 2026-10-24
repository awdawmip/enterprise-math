// Independent C++17 moment calculation by unique first-return block grammar.
// This deliberately does not use the Python (q,r,epsilon,k) edge DP.
#include <boost/multiprecision/cpp_int.hpp>
#include <cassert>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
struct Mass { cpp_int c=0, m=0, v=0; };
int main() {
  constexpr int N=100;
  std::vector<Mass> plus(N+1), minus(N+1);
  plus[0].c=1;
  for(int n=0;n<=N;n++) {
    for(int j=0;n+j+3<=N;j++) {
      int a=j+1, lenA=j+3;
      for(int sign=0;sign<2;sign++) {
        const Mass &s=sign ? minus[n] : plus[n];
        Mass &t=sign ? minus[n+lenA] : plus[n+lenA];
        t.c += s.c;
        t.m += s.m-a*s.c;
        t.v += s.v-2*a*s.m+a*a*s.c;
      }
      int b=j+2, lenB=j+4;
      if(n+lenB>N) continue;
      for(int sign=0;sign<2;sign++) {
        const Mass &s=sign ? minus[n] : plus[n];
        Mass &t=sign ? plus[n+lenB] : minus[n+lenB];
        t.c += s.c;
        t.m += -s.m-b*s.c;
        t.v += s.v+2*b*s.m+b*b*s.c;
      }
    }
  }
  for(int n : {3,7,10,30,60,80,100}) {
    cpp_int c=plus[n].c+minus[n].c;
    cpp_int m=plus[n].m+minus[n].m;
    cpp_int v=plus[n].v+minus[n].v;
    std::cout<<n<<" "<<c<<" "<<m<<" "<<v<<"\n";
  }
  assert(plus[30].c+minus[30].c==372099);
  assert(plus[30].m+minus[30].m==-1461242);
  assert(plus[30].v+minus[30].v==31153476);
  std::cout<<"PASS independent_cpp17_first_return_moments n=0..100\n";
}
