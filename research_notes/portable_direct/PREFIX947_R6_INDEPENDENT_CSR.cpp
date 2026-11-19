// Independent k=23 quotient-divisor CSR; different enumeration order from rowwise quotient approach.
// Validates *every* sorted W23 ID, not only random samples.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;using u64=uint64_t;
constexpr int L=262145,H=524287,C=131072,K=23;
int main(){const int limit=K*H+(1<<18), Tmax=limit/L;
 vector<uint32_t> counts(limit+2,0);u64 edges=0;
 for(int b=L;b<=H;b+=2)for(int t=1;t<=Tmax&&t*b<=limit;++t){counts[t*b]++;edges++;}
 vector<uint32_t>offset(limit+3,0);for(int d=0;d<=limit+1;d++)offset[d+1]=offset[d]+counts[d];
 if(offset[limit+2]!=edges)throw runtime_error("CSR count != edges");
 vector<uint32_t>writeptr(offset.begin(),offset.end()),bs(edges);
 for(int b=L;b<=H;b+=2)for(int t=1;t<=Tmax&&t*b<=limit;++t)bs[writeptr[t*b]++]=(b-L)/2;
 vector<u64>ids;ids.reserve(22000000);u64 raw=0;
 for(int a=L;a<=H;a+=2){u64 base=u64((a-L)/2)*C;
  for(int i=0;i<=18;i++)for(int j=0;j<=18;j++){
   int d=(K*a ^ (1<<j))-(1<<i);if(d<=0||d>limit)continue;
   for(uint32_t h=offset[d];h<offset[d+1];h++){ids.push_back(base+bs[h]);raw++;}
  }
 }
 sort(ids.begin(),ids.end());ids.erase(unique(ids.begin(),ids.end()),ids.end());
 ifstream f("PREFIX947_W23.bin",ios::binary);if(!f)throw runtime_error("primary W23 not found");
 for(u64 id:ids){u64 x; if(!f.read((char*)&x,8)||x!=id)throw runtime_error("CSR vs primary mismatch");}
 u64 extra;if(f.read((char*)&extra,8))throw runtime_error("Primary W23 has trailing data");
 cout<<"INDEPENDENT_CSR K=23 edges="<<edges<<" raw="<<raw<<" unique="<<ids.size()<<" ALL_IDS_EQUAL_PRIMARY=true\n";
 cout<<"ALL_INDEPENDENT_CSR_ASSERTIONS_PASSED\n";
}
