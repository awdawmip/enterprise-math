// R762HM finite sharp threshold for one-block signing, candidate Port model.
// Compile: g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HM_CHECK.cpp -o r762hm
// Run: ./r762hm (exhaustive n=1,...,6)
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
struct Half { uint8_t end, parity; array<uint8_t,6> sup{}; };
struct Edge {uint8_t next, mask;};
static vector<int> ports;
static vector<Edge> edges[15];
static vector<Half> halves;
static vector<uint32_t> buckets[15][64];
static constexpr uint64_t BASE=0x404040404040ULL;
struct Count {uint32_t single; bool zero;};
static uint8_t fullsup[12];
static uint64_t packed_prefix[13];
void enumerate(int n,int depth,int p,int eta,Half &h){
 if(depth==n){h.end=p;h.parity=eta;uint32_t ix=halves.size();halves.push_back(h);buckets[p][eta].push_back(ix);return;}
 for(auto e:edges[p]){h.sup[depth]=e.mask;enumerate(n,depth+1,e.next,eta^e.mask,h);}
}
void assemble(const Half &a,const Half &b,int n){
 for(int t=0;t<n;t++){fullsup[t]=a.sup[t];fullsup[2*n-1-t]=b.sup[t];}
}
Count fast_count(int n){
 uint64_t cur=BASE; packed_prefix[0]=cur;
 for(int t=0;t<2*n;t++){
  uint64_t increment=0;
  int mask=fullsup[t];
  while(mask){int bit=__builtin_ctz((unsigned)mask);increment+=1ULL<<(8*bit);mask&=mask-1;}
  cur += (t&1)? -increment : increment;
  packed_prefix[t+1]=cur;
 }
 int64_t target=0; bool zero=true;
 for(int k=0;k<6;k++){
  int v=int((packed_prefix[2*n]>>(8*k))&255)-64;
  if(v&1){cerr<<"ERROR: odd alternating residual under matched parity\n";exit(3);}
  if(v)zero=false;
  target+=int64_t(v/2)*(1LL<<(8*k));
 }
 uint32_t matches=0;
 for(int a=0;a<2*n;a++)for(int b=a+1;b<=2*n;b++){
  if(packed_prefix[b]==packed_prefix[a]+uint64_t(target))return {1,zero};
 }
 return {matches,zero};
}
// Independent ordinary six-integer check on deterministic actual-path samples.
Count direct_count(int n){
 int prefix[13][6]{};
 for(int t=0;t<2*n;t++)for(int k=0;k<6;k++)
  prefix[t+1][k]=prefix[t][k]+((fullsup[t]&(1<<k))?((t&1)?-1:1):0);
 bool zero=true;
 for(int k=0;k<6;k++)if(prefix[2*n][k])zero=false;
 uint32_t matches=0;
 for(int a=0;a<2*n;a++)for(int b=a+1;b<=2*n;b++){
  bool equal=true;
  for(int k=0;k<6;k++)if(2*(prefix[b][k]-prefix[a][k])!=prefix[2*n][k]){equal=false;break;}
  matches+=equal;
 }
 return {matches,zero};
}
int main(){
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)ports.push_back((1<<i)|(1<<j));
 for(int p=0;p<15;p++)for(int q=0;q<15;q++)
  if(__builtin_popcount((unsigned)(ports[p]&ports[q]))==1)
   edges[p].push_back({uint8_t(q),uint8_t(ports[p]|ports[q])});
 const uint64_t expected_H[7]={1,8,168,4960,177536,7289184,333869824};
 cout<<"n,m,halves,parity_return,zero_block_histories,one_block_only_histories,one_block_existence_witnesses,independent_samples,failures\n";
 for(int n=1;n<=6;n++){
  halves.clear();
  for(auto &row:buckets)for(auto &b:row)b.clear();
  Half root; enumerate(n,0,0,0,root);
  uint64_t total=0,zero=0,one_hist=0,one_sources=0,samples=0,fail=0;
  for(int p=0;p<15;p++)for(int e=0;e<64;e++){
   const auto &ids=buckets[p][e];
   for(uint32_t i:ids)for(uint32_t j:ids){
    assemble(halves[i],halves[j],n);
    auto result=fast_count(n);
    ++total; zero+=result.zero; one_sources+=result.single;
    one_hist+=(!result.zero && result.single>0);
    if(result.single==0){++fail;cerr<<"FAIL n="<<n<<" i="<<i<<" j="<<j<<"\n";return 2;}
    if((total&65535ULL)==0 || (total<=32)){
      auto independent=direct_count(n); ++samples;
      if((independent.single>0)!=(result.single>0) || independent.zero!=result.zero){cerr<<"INDEPENDENT MISMATCH\n";return 4;}
    }
   }
  }
  if(total!=expected_H[n] || halves.size()!=(1ULL<<(3*n))){cerr<<"COVERAGE ERROR\n";return 5;}
  if(zero+one_hist!=total){cerr<<"MINIMUM CLASSIFICATION ERROR\n";return 6;}
  cout<<n<<","<<2*n<<","<<halves.size()<<","<<total<<","<<zero<<","<<one_hist<<","<<one_sources<<","<<samples<<","<<fail<<"\n";
 }
 cout<<"PASS: complete named Port return parity-qualified census through m=12; no one-block failure.\n";
}
