// PREFIX-947: first-principles k23 rowwise candidate census and 16-file historical subtraction.
// Frozen input: f42f2906d77f24085c123f3ccfe9667d41caa96d
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr int L=262145,H=524287,C=131072,K=23,NW=C/64;
constexpr u64 N=u64(1)<<32;
int ix(int a){return (a-L)/2;}
array<uint8_t,C> inS{},inL{},inT{};
void init(){
 vector<int>S,D,Z;
 for(int b=L;b<=H;b+=2){int r=1;bool early=false,late=false;
  for(int d=1;d<=52;++d){r=2LL*r%b;bool hit=r==1||r==b-1;
   if(hit&&d<=31)early=true;else if(hit)late=true;}
  if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("S/D historical census mismatch");
 Z=D;for(int b:{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287})Z.push_back(b);
 sort(Z.begin(),Z.end());Z.erase(unique(Z.begin(),Z.end()),Z.end());
 if(Z.size()!=104)throw runtime_error("V exception count mismatch");
 for(int b:Z)inL[ix(b)]=1;
 for(int t=0;t<1024;++t)inT[(77081LL*t+12345)%C]=1;
}
bool oldBZS(int a,int b){return (u64)b<33*((N+a-1)/a)||(u64)a<33*((N+b-1)/b)||inS[ix(b)]||((u64)a/gcd(a,b))*b<N;}
bool oldV(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
struct OldStream{
 string name;ifstream f;u64 next=0,count=0;bool has=false;
 explicit OldStream(const string&n):name(n),f(n,ios::binary){if(!f)throw runtime_error("Missing input: "+n);advance();}
 void advance(){u64 old=next;
  if(f.read((char*)&next,8)){if(count&&next<=old)throw runtime_error("Input unsorted: "+name);has=true;++count;}
  else{if(!f.eof())throw runtime_error("Input truncated: "+name);has=false;}
 }
 void clear_row(u64 base,array<u64,NW>&bitmap){const u64 high=base+C;
  while(has&&next<high){if(next>=base){int col=int(next-base);bitmap[col>>6]&=~(u64(1)<<(col&63));}advance();}
 }
};
int main(){
 init();const vector<string>files={
 "PREFIX928_R6_SORTED_PAIR_IDS.bin","W2.bin","W3.bin","D4_sorted_cpp.bin",
 "W5.bin","D6.bin","W7.bin","D8.bin","W9.bin","D10.bin","W11_REGEN.bin",
 "W13.bin","PREFIX944_W15.bin","PREFIX944_W17.bin","PREFIX945_W19.bin","PREFIX946_W21.bin"};
 vector<OldStream>old;old.reserve(files.size());for(auto&f:files)old.emplace_back(f);
 ofstream full("PREFIX947_W23.bin",ios::binary),added("PREFIX947_NEW23.bin",ios::binary);
 if(!full||!added)throw runtime_error("cannot create output");
 array<u64,NW>bits{};u64 raw=0,total=0,net=0,old_union=0;
 int firstA=0,firstB=0,firstI=-1,firstJ=-1,firstT=-1;
 for(int a=L;a<=H;a+=2){bits.fill(0);u64 base=u64(ix(a))*C;
  for(int i=0;i<=18;++i)for(int j=0;j<=18;++j){int d=(K*a^(1<<j))-(1<<i);
   if(d<=0)continue;
   for(int t=max(1,(d+H-1)/H);t<=d/L;++t){if(d%t)continue;
    int b=d/t;if(b<L||b>H||!(b&1))continue;
    int col=ix(b);bits[col>>6]|=u64(1)<<(col&63);++raw;
   }
  }
  for(int word=0;word<NW;++word){u64 x=bits[word];while(x){int bit=__builtin_ctzll(x),col=word*64+bit;u64 id=base+col;full.write((char*)&id,8);++total;x&=x-1;}}
  for(auto&stream:old)stream.clear_row(base,bits);
  for(int word=0;word<NW;++word){u64 x=bits[word];while(x){int bit=__builtin_ctzll(x),col=word*64+bit,b=L+2*col;
    if(!oldBZS(a,b)&&!oldV(a,b)){
     u64 id=base+col;added.write((char*)&id,8);++net;
     if(!firstA){firstA=a;firstB=b;
       for(int i=0;i<=18&&firstI<0;i++)for(int j=0;j<=18;j++){
         int d=(K*a^(1<<j))-(1<<i);if(d>0&&d%b==0){firstI=i;firstJ=j;firstT=d/b;break;}
       }
       if(firstI<0)throw runtime_error("first witness not found");
     }
    }
    x&=x-1;
  }}
 }
 for(auto&s:old)if(s.has)throw runtime_error("unconsumed input stream "+s.name);
 u64 hit=total-net;
 cout<<"PREFIX947 k="<<K<<" raw="<<raw<<" unique="<<total<<" old_overlap="<<hit<<" new="<<net<<" row_bitmap_bytes="<<sizeof(bits)<<"\n";
 cout<<"first_new a="<<firstA<<" b="<<firstB<<" i="<<firstI<<" j="<<firstJ<<" t="<<firstT<<" xor_expression="<<((K*firstA ^ (1<<firstJ))-(1<<firstI))<<"\n";
 cout<<"prior_union=7590547816 updated_union="<<7590547816ULL+net<<" uncovered="<<u64(C)*C-7590547816ULL-net<<"\n";
 cout<<"ALL_PRIMARY_EXACT_ASSERTIONS_PASSED\n";
}
