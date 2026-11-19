// PREFIX-945 R6: exhaustive k=19 named XOR witness and W19 pair IDs
// Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr int L=262145,H=524287,C=131072,MAXBIT=18;
struct WitnessSet {vector<u64>ids;u64 raw=0;array<u64,64> by_t{};};
int main(){
 const int k=19;
 const u64 N=1ULL<<32;
 WitnessSet s;
 s.ids.reserve(21000000);
 for(int a=L;a<=H;a+=2){
  u64 base=u64((a-L)/2)*C;
  for(int j=0;j<=MAXBIT;++j){
   int y=k*a^(1<<j);
   if(u64(y)>=N)throw runtime_error("endpoint outside state domain");
   for(int i=0;i<=MAXBIT;++i){
    int d=y-(1<<i);
    if(d<=0)continue;
    int tl=max(1,(d+H-1)/H), th=d/L;
    for(int t=tl;t<=th;++t){
     if(d%t)continue;
     int b=d/t;
     if(b<L||b>H||!(b&1))continue;
     s.ids.push_back(base+(b-L)/2);++s.raw;++s.by_t.at(t);
    }
   }
  }
 }
 sort(s.ids.begin(),s.ids.end());
 s.ids.erase(unique(s.ids.begin(),s.ids.end()),s.ids.end());
 ofstream f("PREFIX945_W19.bin",ios::binary);
 if(!f)throw runtime_error("cannot create W19");
 for(u64 id:s.ids)f.write((char*)&id,sizeof(id));
 if(!f)throw runtime_error("write W19 failed");
 cout<<"PREFIX945_k="<<k<<"\nraw="<<s.raw<<"\nunique="<<s.ids.size()<<"\n";
 for(int t=1;t<64;++t)if(s.by_t[t])cout<<"raw_t"<<t<<"="<<s.by_t[t]<<"\n";
 cout<<"FULL_DOMAIN_EXACT_PRIMARY_COMPLETED\n";
}
