// PREFIX-940: exact k=11 named-XOR finite census; frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
// Compile: g++ -O3 -std=c++17 PREFIX940_R6_K11_CENSUS_CPP.cpp -o k11
// Run: ./k11 PREFIX928_R6_SORTED_PAIR_IDS.bin W2.bin W3.bin D4_sorted_cpp.bin W5.bin D6.bin W7.bin D8.bin W9.bin D10.bin W11.bin NEW11.bin
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr int Q0=262145,QMAX=524287,NQ=131072,K=11,MAX_T=22;
constexpr u64 N=(1ULL<<32), PRIOR_UNION=7552811074ULL;
inline int ix(int x){return (x-Q0)/2;}
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
void init(){
 vector<int>S,D,L;
 for(int b=Q0;b<=QMAX;b+=2){int r=1;bool e=false,l=false;
  for(int d=1;d<=52;++d){r=2LL*r%b;bool hit=(r==1||r==b-1);if(hit&&d<=31)e=true;else if(hit)l=true;}
  if(e){S.push_back(b);inS[ix(b)]=1;}else if(l)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("prior S/D count mismatch");
 L=D;for(int b:{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287})L.push_back(b);
 sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());if(L.size()!=104)throw runtime_error("L cardinality mismatch");
 for(int b:L)inL[ix(b)]=1;
 for(int t=0;t<1024;++t)inT[(77081LL*t+12345)%NQ]=1;
}
inline bool BZS(int a,int b){return (u64)b<33*((N+a-1)/a)||(u64)a<33*((N+b-1)/b)||inS[ix(b)]||((u64)a/std::gcd(a,b))*b<N;}
inline bool V(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
vector<u64> read(const char*path,size_t n){
 ifstream f(path,ios::binary);if(!f)throw runtime_error(string("Cannot read: ")+path);
 vector<u64>v;v.reserve(n);u64 id;
 while(f.read((char*)&id,8)){if(!v.empty()&&v.back()>=id)throw runtime_error("noncanonical input order");v.push_back(id);}
 if(v.size()!=n)throw runtime_error(string("Input size mismatch: ")+path+" "+to_string(v.size()));return v;
}
void write(const char*path,const vector<u64>&v){
 ofstream f(path,ios::binary);if(!f)throw runtime_error("cannot write output");
 for(u64 x:v)f.write(reinterpret_cast<const char*>(&x),8);
 if(!f)throw runtime_error("write error");
}
int main(int argc,char**argv){
 if(argc!=13)throw runtime_error("usage: k11 U W2 W3 D4 W5 D6 W7 D8 W9 D10 W11 NEW11");
 init();
 auto U=read(argv[1],5295478),W2=read(argv[2],30211412),W3=read(argv[3],19413088),D4=read(argv[4],1793182),
      W5=read(argv[5],15406809),D6=read(argv[6],1771013),W7prev=read(argv[7],14698334),D8=read(argv[8],4043794),W9prev=read(argv[9],15456919),D10=read(argv[10],1736455);
 vector<u64> W11;W11.reserve(30000000);u64 raw=0,raw_t[MAX_T+1]={};
 for(int a=Q0;a<=QMAX;a+=2){const u64 base=(u64)ix(a)*NQ;
  for(int j=0;j<=18;++j){const int y=(K*a)^(1<<j);
   if(y<=0||(u64)y>=N)throw runtime_error("endpoint out of N");
   for(int i=0;i<=18;++i){const int e=1<<i,d=y-e;
    if(d<=0)throw runtime_error("wrong positive lower bound");
    for(int t=1;t<=MAX_T;++t){if(d%t)continue;int b=d/t;
     if(b<Q0||b>QMAX||!(b&1))continue;
     if(K*a%a!=0||y%b!=e%b)throw runtime_error("invalid named witness");
     W11.push_back(base+ix(b));++raw;++raw_t[t];
    }
   }
  }
 }
 sort(W11.begin(),W11.end());W11.erase(unique(W11.begin(),W11.end()),W11.end());write(argv[11],W11);
 const vector<u64>*ds[]={&U,&W2,&W3,&D4,&W5,&D6,&W7prev,&D8,&W9prev,&D10};
 size_t pos[10]={};u64 cnt[13]={};vector<u64>New;New.reserve(12000000);u64 first=~u64(0);
 for(u64 id:W11){
  bool hit[10];
  for(int k=0;k<10;++k){auto&v=*ds[k];while(pos[k]<v.size()&&v[pos[k]]<id)++pos[k];hit[k]=(pos[k]<v.size()&&v[pos[k]]==id);}
  int a=Q0+2*int(id/NQ),b=Q0+2*int(id%NQ);
  if(BZS(a,b))++cnt[0];else if(hit[0])++cnt[1];else if(V(a,b))++cnt[2];
  else if(hit[1])++cnt[3];else if(hit[2])++cnt[4];else if(hit[3])++cnt[5];
  else if(hit[4])++cnt[6];else if(hit[5])++cnt[7];else if(hit[6])++cnt[8];else if(hit[7])++cnt[9];else if(hit[8])++cnt[10];else if(hit[9])++cnt[11];
  else{++cnt[12];New.push_back(id);if(first==~u64(0))first=id;}
 }
 if(accumulate(begin(cnt),end(cnt),u64(0))!=W11.size())throw runtime_error("partition does not cover W11");
 write(argv[12],New);
 cout<<"PREFIX940_K11_FULL\n"<<"raw="<<raw<<"\nunique="<<W11.size()<<'\n';
 for(int t=1;t<=MAX_T;++t)cout<<"raw_t"<<t<<"="<<raw_t[t]<<'\n';
 const char*labels[]={"BZS","U","V","W2","W3","D4","W5","D6","W7","D8","W9","D10","NEW"};
 for(int k=0;k<13;++k)cout<<"priority_"<<labels[k]<<"="<<cnt[k]<<'\n';
 cout<<"prior_union="<<PRIOR_UNION<<"\nnew_union="<<PRIOR_UNION+cnt[12]<<"\nremaining="<<(u64)NQ*NQ-PRIOR_UNION-cnt[12]<<'\n';
 cout<<"W11_bytes="<<W11.size()*8<<"\nNEW11_bytes="<<New.size()*8<<'\n';
 if(first!=~u64(0)){int a=Q0+2*int(first/NQ),b=Q0+2*int(first%NQ);
  cout<<"first_new_a="<<a<<"\nfirst_new_b="<<b<<'\n';
  for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){int y=(K*a)^(1<<j),d=y-(1<<i);
   if(d>0&&d%b==0){cout<<"first_i="<<i<<"\nfirst_j="<<j<<"\nfirst_t="<<d/b
    <<"\nfirst_start="<<K*a<<"\nfirst_endpoint="<<y<<"\nfirst_zero_endpoint="<<(1<<i)<<'\n';return 0;}}
  throw runtime_error("cannot reconstruct first witness");
 }
}
