#include <array>
#include <fstream>
#include <iostream>
#include <cstdint>
using namespace std;
using u64=uint64_t;
constexpr int L=262145,H=524287,C=131072;
int main(){array<u64,C/64>bitmap{}; ofstream out("W11_REGEN.bin",ios::binary); if(!out)return 1;
  u64 raw=0,uniq=0;
  for(int a=L;a<=H;a+=2){bitmap.fill(0);u64 base=u64((a-L)/2)*C;
   for(int i=0;i<=18;i++)for(int j=0;j<=18;j++){
    int d=(11*a ^ (1<<j))-(1<<i);
    for(int t=max(1,(d+H-1)/H);t<=d/L;t++){
     if(d%t)continue;int b=d/t;if(b<L||b>H||!(b&1))continue;
     int col=(b-L)/2;bitmap[col>>6]|=u64(1)<<(col&63);raw++;
    }
   }
   for(int w=0;w<C/64;w++){u64 x=bitmap[w];while(x){int bit=__builtin_ctzll(x);u64 id=base+w*64+bit;out.write((char*)&id,8);uniq++;x&=x-1;}}
  }
  cerr<<"W11 raw="<<raw<<" unique="<<uniq<<"\n";
  return (raw==16974425&&uniq==13144330)?0:2;
}
