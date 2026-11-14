// EC49FGK exact inclusion-minimal 5/6/7 raw-key support cover census.
// Input: complete 94 (x,y,z,24-bit support mask) rows from VERIFY_EC49FGK.py.
// g++ -O3 -std=c++17 VERIFY_EC49FGK_MINIMAL.cpp -o verify_minimal
// ./verify_minimal EC49FGK_key_masks.txt
#include <cstdint>
#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
#include <array>
#include <stdexcept>
using namespace std;
int main(int argc,char**argv) {
 if(argc!=2) throw runtime_error("usage: verify_minimal key_masks.txt");
 ifstream f(argv[1]); if(!f) throw runtime_error("missing catalogue");
 vector<tuple<int,int,int,uint32_t>> data;
 int x,y,z;uint32_t m;
 while(f>>x>>y>>z>>m) data.emplace_back(x,y,z,m);
 if(data.size()!=94) throw runtime_error("expected 94 distinct raw keys");
 constexpr uint32_t FULL=(1u<<24)-1;
 uint32_t forced=0;
 vector<uint32_t> pool;
 vector<array<int,3>> keys;
 int forced_n=0;
 for(auto [a,b,c,mask]:data) {
  if((a==2&&b==1&&c==1)||(a==3&&b==0&&c==1)) {
   forced|=mask; ++forced_n;
  } else {
   pool.push_back(mask);keys.push_back({a,b,c});
  }
 }
 if(forced_n!=2||pool.size()!=92)throw runtime_error("bad forced H2 keys");
 uint64_t covers[8]={},minimal[8]={},minimal_no_311[8]={};
 for(int n=3;n<=5;++n) {
  auto test=[&](const array<size_t,5>& v) {
   uint32_t combined=forced;
   for(int i=0;i<n;++i)combined|=pool[v[i]];
   if(combined!=FULL)return;
   ++covers[n+2];
   bool essential=true,has311=false;
   for(int i=0;i<n;++i) {
    auto k=keys[v[i]];
    if(k[0]==3&&k[1]==1&&k[2]==1)has311=true;
    uint32_t reduced=forced;
    for(int j=0;j<n;++j)if(j!=i)reduced|=pool[v[j]];
    if(reduced==FULL){essential=false;break;}
   }
   if(essential) {
    ++minimal[n+2];
    if(!has311)++minimal_no_311[n+2];
   }
  };
  array<size_t,5> v{};
  for(size_t a=0;a<pool.size();++a)
   for(size_t b=a+1;b<pool.size();++b)
    for(size_t c=b+1;c<pool.size();++c) {
     v[0]=a;v[1]=b;v[2]=c;
     if(n==3)test(v);
     else for(size_t d=c+1;d<pool.size();++d) {
      v[3]=d;
      if(n==4)test(v);
      else for(size_t e=d+1;e<pool.size();++e) {
       v[4]=e;test(v);
      }
     }
    }
 }
 for(int k=5;k<=7;++k)
  cout<<"K="<<k<<" covers="<<covers[k]<<" inclusion_minimal="<<minimal[k]
      <<" minimal_without_3_1_1="<<minimal_no_311[k]<<"\n";
 if(covers[5]!=16||covers[6]!=2004||covers[7]!=108434
 ||minimal[5]!=16||minimal[6]!=628||minimal[7]!=4904
 ||minimal_no_311[5]!=0||minimal_no_311[6]!=16||minimal_no_311[7]!=612)
  return 2;
}
