// R762HG: exhaustive positive-BRC half-path intersection certificate.
// Compile: g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HG_HALFPAIR_CHECK.cpp -o check
// Run: ./check 5 ; ./check 6 (also 1..4 for independent predecessor comparisons).
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
struct Step { int next; int support; };
struct Half {
  uint8_t endpoint, parity;
  vector<uint8_t> ports, supports;
  vector<uint32_t> signed_sums;
};
static vector<int> port_masks;
static vector<Step> adj[15];
static vector<Half> halves;
static vector<size_t> buckets[15][64];
static int n;

static void enumerate(int p,int parity,vector<uint8_t>&ports,vector<uint8_t>&supports) {
  if(int(supports.size())==n) {
    Half h; h.endpoint=p; h.parity=parity; h.ports=ports; h.supports=supports;
    for(int flags=0;flags<(1<<n);++flags) {
      int v[6]={0,0,0,0,0,0};
      for(int i=0;i<n;++i)
        for(int a=0;a<6;++a)
          if(supports[i]&(1<<a)) v[a]+=((flags>>i)&1)?1:-1;
      uint32_t key=0;
      for(int a=0;a<6;++a) key |= uint32_t(v[a]+8)<<(4*a);
      h.signed_sums.push_back(key);
    }
    sort(h.signed_sums.begin(),h.signed_sums.end());
    h.signed_sums.erase(unique(h.signed_sums.begin(),h.signed_sums.end()),h.signed_sums.end());
    size_t index=halves.size();
    halves.push_back(move(h)); buckets[p][parity].push_back(index);
    return;
  }
  for(const auto& st:adj[p]) {
    ports.push_back(uint8_t(st.next)); supports.push_back(uint8_t(st.support));
    enumerate(st.next,parity^st.support,ports,supports);
    ports.pop_back(); supports.pop_back();
  }
}
static bool disjoint(const vector<uint32_t>&a,const vector<uint32_t>&b) {
  size_t i=0,j=0;
  while(i<a.size()&&j<b.size()) {
    if(a[i]==b[j])return false;
    if(a[i]<b[j])++i;else ++j;
  }
  return true;
}
int main(int argc,char**argv) {
  n=argc>1?atoi(argv[1]):6;
  if(n<1||n>6) { cerr<<"Require 1<=n<=6\n";return 2; }
  for(int a=0;a<6;++a)for(int b=a+1;b<6;++b)
    port_masks.push_back((1<<a)|(1<<b));
  for(int p=0;p<15;++p)for(int q=0;q<15;++q)
    if(__builtin_popcount((unsigned)(port_masks[p]&port_masks[q]))==1)
      adj[p].push_back({q,port_masks[p]|port_masks[q]});
  vector<uint8_t> ports={0},supports;
  enumerate(0,0,ports,supports);
  const uint64_t expected_h[7]={1,8,168,4960,177536,7289184,333869824};
  uint64_t ordered=0,unordered=0;
  for(int p=0;p<15;++p)for(int eta=0;eta<64;++eta) {
    const auto& ids=buckets[p][eta];
    ordered+=uint64_t(ids.size())*ids.size();
    for(size_t i=0;i<ids.size();++i)for(size_t j=i;j<ids.size();++j) {
      ++unordered;
      const auto& a=halves[ids[i]];
      const auto& b=halves[ids[j]];
      if(disjoint(a.signed_sums,b.signed_sums)) {
        cerr<<"FALSE_POSITIVE length="<<2*n<<" middle_port="<<p
            <<" xor="<<eta<<"\n";
        for(const auto* x:{&a,&b}) {
          cerr<<"ports:";
          for(uint8_t v:x->ports)cerr<<" "<<port_masks[v];
          cerr<<"\nsupports:";
          for(uint8_t s:x->supports)cerr<<" "<<int(s);
          cerr<<"\n";
        }
        return 1;
      }
    }
  }
  cout<<"half_length="<<n
      <<" halves="<<halves.size()
      <<" H="<<ordered<<" compatible_unordered_pairs="<<unordered
      <<" disjoint=0\n";
  if(ordered!=expected_h[n]){cerr<<"H coverage mismatch\n";return 3;}
  if(halves.size()!=size_t(1)<<(3*n)){cerr<<"Half enumeration mismatch\n";return 4;}
  return 0;
}
