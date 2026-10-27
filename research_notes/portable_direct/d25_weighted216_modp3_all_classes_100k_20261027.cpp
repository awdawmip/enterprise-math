// D25 original weighted-216 modulo p^3 falsifier; AUTHOR-SIDE, not native H0/B0.
// Compile: c++ -O2 -std=c++17 -o d25_falsifier d25_weighted216_modp3_all_classes_100k_20261027.cpp
// Run: ./d25_falsifier 100000
// Numerical scope p>=5, p<=100000, mod=p^3; no W_p theorem claimed.
#include <cstdint>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <chrono>
static inline uint64_t mul(uint64_t a, uint64_t b, uint64_t m) {
  return uint64_t((__uint128_t(a) * b) % m);
}
static uint64_t inverse(uint64_t a, uint64_t m) {
  __int128 t=0, next=1, r=m, nr=a;
  while (nr) {
    __int128 k=r/nr, tt=t-k*next, rr=r-k*nr;
    t=next; next=tt; r=nr; nr=rr;
  }
  if (r!=1) std::abort();
  return uint64_t((t % (__int128)m + m) % m);
}
static uint64_t W_mod(uint64_t p) {
  uint64_t mod=p*p*p;
  std::vector<uint64_t> inv(p);
  inv[1]=1;
  // Works over Z/p^3 since every i in [1,p) and every nonzero remainder <p is a unit.
  for (uint64_t i=2;i<p;i++)
    inv[i]=mod-mul(mod/i,inv[mod%i],mod);
  const uint64_t inv36=inverse(36,mod);
  uint64_t q=1, sum=1;
  // q(n+1)/q(n) = (2n+1)(3n+1)(3n+2) / (36(n+1)^3).
  for (uint64_t n=0;n<p-1;n++) {
    uint64_t t=mul(inv[n+1],inv[n+1],mod);
    t=mul(t,inv[n+1],mod);
    t=mul(t,inv36,mod);
    t=mul(t,2*n+1,mod);
    t=mul(t,3*n+1,mod);
    t=mul(t,3*n+2,mod);
    q=mul(q,t,mod);
    sum=(sum+mul(6*(n+1)+1,q,mod))%mod;
  }
  return sum;
}
int main(int argc,char** argv) {
  int limit=argc>1?std::atoi(argv[1]):100000;
  if(limit<5 || limit>200000) return 2; // 64-bit safety range; tested at 100000.
  std::vector<char> prime(limit+1,1);
  prime[0]=prime[1]=0;
  for(int i=2;i*i<=limit;i++) if(prime[i])
    for(int j=i*i;j<=limit;j+=i) prime[j]=0;
  uint64_t count[24]={0},bad[24]={0},last[24]={0};
  auto start=std::chrono::steady_clock::now();
  for(uint64_t p=5;p<=(uint64_t)limit;p++) if(prime[p]) {
    uint64_t w=W_mod(p), mod=p*p*p;
    uint64_t expected=(p%3==1 ? p : mod-p); // Legendre(-3/p)*p.
    count[p%24]++; last[p%24]=p;
    if(w!=expected) {
      bad[p%24]++;
      std::printf("COUNTEREXAMPLE p=%llu W=%llu expected=%llu\n",
        (unsigned long long)p,(unsigned long long)w,(unsigned long long)expected);
    }
  }
  for(int c: {1,5,7,11,13,17,19,23})
    std::printf("CLASS %d checked=%llu failures=%llu maxp=%llu\n",
      c,(unsigned long long)count[c],(unsigned long long)bad[c],
      (unsigned long long)last[c]);
  std::printf("seconds=%.3f\n",
    std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count());
}
