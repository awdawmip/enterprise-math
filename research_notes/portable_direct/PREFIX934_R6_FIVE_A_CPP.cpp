// PREFIX-934: exact k=5 zero-origin named-XOR collision enumeration.
// Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
// g++ -std=c++17 -O3 PREFIX934_R6_FIVE_A_CPP.cpp -o prefix934
// ./prefix934 PREFIX928_R6_SORTED_PAIR_IDS.bin W2.bin W3.bin D4_sorted_cpp.bin W5.bin NEW5.bin
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr int Q0=262145,QMAX=524287,NQ=131072;
constexpr u64 N=1ULL<<32;
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
inline int ix(int v){return (v-Q0)/2;}
void setup(){
 vector<int>D,S,L,T;
 for(int b=Q0;b<=QMAX;b+=2){int r=1;bool early=false,late=false;
  for(int d=1;d<=52;++d){r=(2LL*r)%b;bool hit=r==1||r==b-1;
   if(hit && d<=31)early=true; else if(hit)late=true;}
  if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("prior S/D mismatch");
 L=D;const vector<int>E{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287};
 L.insert(L.end(),E.begin(),E.end());sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());
 if(L.size()!=104)throw runtime_error("prior full-row mismatch");
 for(int b:L)inL[ix(b)]=1;
 for(int t=0;t<1024;++t){int b=Q0+2*((77081LL*t+12345)%NQ);inT[ix(b)]=1;T.push_back(b);}
 sort(T.begin(),T.end());T.erase(unique(T.begin(),T.end()),T.end());
 if(T.size()!=1024)throw runtime_error("prior highband mismatch");
}
inline bool oldBZS(int a,int b){
 u64 ca=(N+(u64)a-1)/a,cb=(N+(u64)b-1)/b;
 return (u64)b<33*ca||(u64)a<33*cb||inS[ix(b)]||((u64)a/std::gcd(a,b))*b<N;
}
inline bool oldV(int a,int b){int ai=ix(a),bi=ix(b);return inL[ai]||inL[bi]||(a>=500001&&inT[bi])||(b>=500001&&inT[ai]);}
vector<u64> read_ids(const char*path,size_t expected){
 ifstream f(path,ios::binary);if(!f)throw runtime_error(string("Cannot open ")+path);
 vector<u64> v;v.reserve(expected);u64 x;
 while(f.read(reinterpret_cast<char*>(&x),8)){if(!v.empty()&&v.back()>=x)throw runtime_error("sorted/unique check failed");v.push_back(x);}
 if(v.size()!=expected)throw runtime_error(string("count mismatch: ")+path+" got "+to_string(v.size()));
 return v;
}
void write_ids(const char*path,const vector<u64>&v){ofstream f(path,ios::binary);if(!f)throw runtime_error("write open failed");for(u64 x:v)f.write((char*)&x,8);if(!f)throw runtime_error("write failed");}
int main(int argc,char**argv){
 if(argc!=7)throw runtime_error("Usage: prefix934 U.bin W2.bin W3.bin D4.bin W5.bin NEW5.bin");
 setup();
 auto U=read_ids(argv[1],5295478),W2=read_ids(argv[2],30211412),W3=read_ids(argv[3],19413088),D4=read_ids(argv[4],1793182);
 vector<u64>W5;W5.reserve(50000000);u64 raw=0, raw_t[11]={};
 for(int a=Q0;a<=QMAX;a+=2){u64 base=(u64)ix(a)*NQ;
  for(int j=0;j<=18;++j){const int y=(5*a)^(1<<j);
   if(y<0||(u64)y>=N)throw runtime_error("Endpoint invalid");
   for(int i=0;i<=18;++i){const int e=1<<i,d=y-e;
    if(d<=0)throw runtime_error("positive distance invalid");
    for(int t=1;t<=10;++t){if(d%t)continue;int b=d/t;
     if(b<Q0||b>QMAX||!(b&1))continue;
     if((5*a)%a!=0||y%b!=e%b)throw runtime_error("bad witness");
     W5.push_back(base+ix(b));++raw;++raw_t[t];
    }
   }
  }
 }
 sort(W5.begin(),W5.end());W5.erase(unique(W5.begin(),W5.end()),W5.end());
 write_ids(argv[5],W5);
 size_t pu=0,p2=0,p3=0,p4=0;u64 cnt[7]={},firstId=0;
 vector<u64>New;New.reserve(12000000);
 for(u64 id:W5){
  while(pu<U.size()&&U[pu]<id)++pu;
  while(p2<W2.size()&&W2[p2]<id)++p2;
  while(p3<W3.size()&&W3[p3]<id)++p3;
  while(p4<D4.size()&&D4[p4]<id)++p4;
  int a=Q0+2*int(id/NQ),b=Q0+2*int(id%NQ);
  if(oldBZS(a,b))++cnt[0];
  else if(pu<U.size()&&U[pu]==id)++cnt[1];
  else if(oldV(a,b))++cnt[2];
  else if(p2<W2.size()&&W2[p2]==id)++cnt[3];
  else if(p3<W3.size()&&W3[p3]==id)++cnt[4];
  else if(p4<D4.size()&&D4[p4]==id)++cnt[5];
  else {++cnt[6];New.push_back(id);if(!firstId)firstId=id;}
 }
 if(accumulate(begin(cnt),end(cnt),u64(0))!=W5.size())throw runtime_error("partition mismatch");
 write_ids(argv[6],New);
 const u64 prior=7531649800ULL,universe=(u64)NQ*NQ;
 cout<<"PREFIX934_FIVE_A_EXACT\n";
 cout<<"W5_raw="<<raw<<" W5_unique="<<W5.size()<<'\n';
 for(int t=1;t<=10;++t)cout<<"W5_raw_t"<<t<<'='<<raw_t[t]<<'\n';
 const char*labels[7]={"BZS","U","V","W2","W3","D4","NEW"};
 for(int k=0;k<7;++k)cout<<"priority_"<<labels[k]<<'='<<cnt[k]<<'\n';
 cout<<"new_certified_union="<<prior+cnt[6]<<'\n';
 cout<<"new_certificate_complement="<<universe-prior-cnt[6]<<'\n';
 cout<<"W5_bytes="<<W5.size()*8<<" NEW_bytes="<<New.size()*8<<'\n';
 if(firstId){int a=Q0+2*int(firstId/NQ),b=Q0+2*int(firstId%NQ);cout<<"first_new_a="<<a<<" first_new_b="<<b<<'\n';
  for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){int y=(5*a)^(1<<j),d=y-(1<<i);
   if(d%b==0){cout<<"first_new_i="<<i<<" first_new_j="<<j<<" t="<<d/b<<" F0_end="<<(1<<i)<<" F5a_start="<<5*a<<" F5a_end="<<y<<'\n';return 0;}}
  throw runtime_error("first witness not reconstructed");
 }
}
