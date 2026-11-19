// PREFIX-935: k=6 boundary (i=0 or j=0) exact finite named-XOR census.
// Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
// g++ -std=c++17 -O3 PREFIX935_R6_SIX_A_BOUNDARY_CPP.cpp -o prefix935
// ./prefix935 PREFIX928_R6_SORTED_PAIR_IDS.bin W2.bin W3.bin D4_sorted_cpp.bin W5.bin D6.bin NEW6.bin
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <stdexcept>
using namespace std;using u64=uint64_t;
constexpr int Q0=262145,QMAX=524287,NQ=131072;constexpr u64 N=1ULL<<32;
int ix(int x){return (x-Q0)/2;}
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
void init(){vector<int> L,D,S;for(int b=Q0;b<=QMAX;b+=2){int r=1;bool e=false,l=false;for(int d=1;d<=52;++d){r=2LL*r%b;bool hit=r==1||r==b-1;if(hit&&d<=31)e=true;else if(hit)l=true;}if(e){inS[ix(b)]=1;S.push_back(b);}else if(l)D.push_back(b);}if(S.size()!=24||D.size()!=91)throw runtime_error("S/D counts");L=D;for(int x:{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287})L.push_back(x);sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());if(L.size()!=104)throw runtime_error("L size");for(int x:L)inL[ix(x)]=1;for(int t=0;t<1024;++t)inT[(77081LL*t+12345)%NQ]=1;}
bool BZS(int a,int b){return (u64)b<33*((N+(u64)a-1)/a)||(u64)a<33*((N+(u64)b-1)/b)||inS[ix(b)]||((u64)a/gcd(a,b))*b<N;}
bool V(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
vector<u64> read(const char*fn,size_t expected){ifstream f(fn,ios::binary);if(!f)throw runtime_error("no input");vector<u64> v;v.reserve(expected);u64 x;while(f.read((char*)&x,8)){if(!v.empty()&&v.back()>=x)throw runtime_error("bad order");v.push_back(x);}if(v.size()!=expected)throw runtime_error("wrong size");return v;}
void write(const char*fn,const vector<u64>&v){ofstream f(fn,ios::binary);if(!f)throw runtime_error("out open");for(u64 x:v)f.write((char*)&x,8);if(!f)throw runtime_error("write");}
int main(int argc,char**argv){if(argc!=8)throw runtime_error("U W2 W3 D4 W5 D6 NEW6");init();auto U=read(argv[1],5295478),W2=read(argv[2],30211412),W3=read(argv[3],19413088),D4=read(argv[4],1793182),W5=read(argv[5],15406809);
 vector<u64>D6;u64 raw=0,raw_t[13]={};
 for(int a=Q0;a<=QMAX;a+=2){u64 base=(u64)ix(a)*NQ;
   for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){if(i>0&&j>0)continue;
     const int y=(6*a)^(1<<j),e=1<<i,d=y-e;
     if(y<0||(u64)y>=N||d<=0)throw runtime_error("out-of-range endpoint");
     for(int t=1;t<=12;++t){if(d%t)continue;int b=d/t;if(b<Q0||b>QMAX||!(b&1))continue;
       if(y%b!=e%b)throw runtime_error("bad witness");
       if((i==0&&j==0)? t%4!=2 : t%2!=1)throw runtime_error("dyadic selector mismatch");
       D6.push_back(base+ix(b));++raw;++raw_t[t];
     }
   }
 }
 sort(D6.begin(),D6.end());D6.erase(unique(D6.begin(),D6.end()),D6.end());write(argv[6],D6);
 size_t p[5]={};vector<u64> New;u64 cnt[8]={};u64 first=0;const vector<u64>* datasets[]={&U,&W2,&W3,&D4,&W5};
 for(u64 id:D6){bool hit[5];for(int k=0;k<5;++k){const auto&v=*datasets[k];while(p[k]<v.size()&&v[p[k]]<id)++p[k];hit[k]=(p[k]<v.size()&&v[p[k]]==id);}
  int a=Q0+2*int(id/NQ),b=Q0+2*int(id%NQ);
  if(BZS(a,b))++cnt[0];else if(hit[0])++cnt[1];else if(V(a,b))++cnt[2];else if(hit[1])++cnt[3];else if(hit[2])++cnt[4];else if(hit[3])++cnt[5];else if(hit[4])++cnt[6];else{++cnt[7];New.push_back(id);if(!first)first=id;}
 }
 if(accumulate(begin(cnt),end(cnt),u64(0))!=D6.size())throw runtime_error("partition invalid");write(argv[7],New);
 cout<<"PREFIX935_K6_BOUNDARY\nD6_raw="<<raw<<" D6_unique="<<D6.size()<<'\n';for(int t=1;t<=12;++t)cout<<"raw_t"<<t<<'='<<raw_t[t]<<'\n';for(int k=0;k<8;++k)cout<<"partition"<<k<<'='<<cnt[k]<<'\n';cout<<"new_union="<<7537850206ULL+cnt[7]<<"\nremaining="<<((u64)NQ*NQ-7537850206ULL-cnt[7])<<'\n';
 if(first){int a=Q0+2*int(first/NQ),b=Q0+2*int(first%NQ);cout<<"first_a="<<a<<" first_b="<<b<<'\n';for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){if(i&&j)continue;int y=(6*a)^(1<<j),d=y-(1<<i);if(d%b==0){cout<<"first_i="<<i<<" first_j="<<j<<" first_t="<<d/b<<" e="<<(1<<i)<<" x="<<6*a<<" y="<<y<<'\n';return 0;}}}
}
