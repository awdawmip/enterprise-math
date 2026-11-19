// PREFIX-932: exact W3 (three-a origin) complete finite named-XOR collision census.
// Frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d.
// g++ -std=c++17 -O3 PREFIX932_R6_TRIPLE_A_EXACT_CPP.cpp -o prefix932
// ./prefix932 PREFIX928_R6_SORTED_PAIR_IDS.bin W2.bin W3.bin
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std; using u64=uint64_t;
constexpr int Q0=262145,QMAX=524287,NQ=131072;
constexpr u64 N=1ULL<<32;
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
inline int ix(int v){return (v-Q0)/2;}
void initialize(){
 vector<int>D,S,L,T;
 for(int b=Q0;b<=QMAX;b+=2){int r=1;bool early=false,late=false;
   for(int d=1;d<=52;++d){r=(2LL*r)%b;bool hit=r==1||r==b-1;
    if(hit&&d<=31)early=true;else if(hit)late=true;}
   if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("previous S/D counts changed");
 L=D;const vector<int>E{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287};
 L.insert(L.end(),E.begin(),E.end());sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());
 if(L.size()!=104)throw runtime_error("previous full-row count changed");
 for(int b:L)inL[ix(b)]=1;
 for(int t=0;t<1024;++t){int b=Q0+2*((77081LL*t+12345)%NQ);inT[ix(b)]=1;T.push_back(b);}
 sort(T.begin(),T.end());T.erase(unique(T.begin(),T.end()),T.end());
 if(T.size()!=1024)throw runtime_error("prior highband seeds mismatch");
}
inline bool oldBZS(int a,int b){
 u64 ca=(N+(u64)a-1)/a,cb=(N+(u64)b-1)/b;
 return (u64)b<33*ca||(u64)a<33*cb||inS[ix(b)]||((u64)a/std::gcd(a,b))*b<N;
}
inline bool oldV(int a,int b){int ai=ix(a),bi=ix(b);return inL[ai]||inL[bi]||(a>=500001&&inT[bi])||(b>=500001&&inT[ai]);}
void write_binary(const char *p,const vector<u64>& v){ofstream o(p,ios::binary);if(!o)throw runtime_error("output file open failed"); for(u64 id:v)o.write((char*)&id,8);if(!o)throw runtime_error("binary write failed");}
int main(int argc,char**argv){
 if(argc!=4)throw runtime_error("usage: prefix932 U.bin W2.bin W3.bin");
 initialize();
 ifstream uf(argv[1],ios::binary);if(!uf)throw runtime_error("missing U");
 vector<u64> U;U.reserve(5295478);u64 z;
 while(uf.read((char*)&z,8)){if(!U.empty()&&U.back()>=z)throw runtime_error("U ordering");U.push_back(z);}
 if(U.size()!=5295478)throw runtime_error("U unexpected size");
 vector<u64> W2,W3; W2.reserve(40000000);W3.reserve(50000000);
 u64 raw2=0,raw3=0,raw3_t[7]={};
 for(int a=Q0;a<=QMAX;a+=2){u64 base=(u64)ix(a)*NQ;
  for(int j=0;j<=18;++j){const int y2=(2*a)^(1<<j),y3=(3*a)^(1<<j);
   for(int i=0;i<=18;++i){const int e=1<<i, d2=abs(y2-e),d3=abs(y3-e);
    for(int t=1;t<=3;++t){if(d2%t)continue;int b=d2/t;
     if(b<Q0||b>QMAX||!(b&1))continue;
     if(e%b!=y2%b||(2*a)%a!=0)throw runtime_error("W2 invalid witness");
     W2.push_back(base+ix(b));++raw2;
    }
    for(int t=1;t<=6;++t){if(d3%t)continue;int b=d3/t;
     if(b<Q0||b>QMAX||!(b&1))continue;
     if(e%b!=y3%b||(3*a)%a!=0)throw runtime_error("W3 invalid witness");
     W3.push_back(base+ix(b));++raw3;++raw3_t[t];
    }
   }
  }
 }
 sort(W2.begin(),W2.end());W2.erase(unique(W2.begin(),W2.end()),W2.end());
 sort(W3.begin(),W3.end());W3.erase(unique(W3.begin(),W3.end()),W3.end());
 if(W2.size()!=30211412||raw2!=36787554)throw runtime_error("W2 mismatch published PREFIX931");
 write_binary(argv[2],W2);write_binary(argv[3],W3);
 size_t pu=0,p2=0;u64 cB=0,cU=0,cV=0,cW2=0,cNew=0,firstId=0;
 for(u64 id:W3){while(pu<U.size()&&U[pu]<id)++pu;while(p2<W2.size()&&W2[p2]<id)++p2;
  int a=Q0+2*(int)(id/NQ), b=Q0+2*(int)(id%NQ);
  bool isU=pu<U.size()&&U[pu]==id, isW2=p2<W2.size()&&W2[p2]==id;
  if(oldBZS(a,b)){++cB;if(isU)throw runtime_error("U not disjoint from BZS");}
  else if(isU)++cU;
  else if(oldV(a,b))++cV;
  else if(isW2)++cW2;
  else {++cNew;if(!firstId)firstId=id;}
 }
 const u64 prior=7522555296ULL,total=(u64)NQ*NQ;
 if(W3.size()!=cB+cU+cV+cW2+cNew)throw runtime_error("partition mismatch");
 cout<<"PREFIX932_TRIPLE_A\n";
 cout<<"W2_raw="<<raw2<<" W2_unique="<<W2.size()<<'\n';
 cout<<"W3_raw="<<raw3<<" W3_unique="<<W3.size()<<'\n';
 for(int t=1;t<=6;++t)cout<<"W3_raw_t"<<t<<'='<<raw3_t[t]<<'\n';
 cout<<"W3_overlap_BZS="<<cB<<'\n';
 cout<<"W3_overlap_U_outside_BZS="<<cU<<'\n';
 cout<<"W3_overlap_V_outside_BZS_U="<<cV<<'\n';
 cout<<"W3_overlap_W2_outside_BZS_U_V="<<cW2<<'\n';
 cout<<"W3_increment_over_PREFIX931="<<cNew<<'\n';
 cout<<"new_certified_union="<<prior+cNew<<'\n';
 cout<<"new_certificate_complement="<<total-prior-cNew<<'\n';
 if(firstId){int a=Q0+2*(int)(firstId/NQ),b=Q0+2*(int)(firstId%NQ);
  cout<<"first_new_a="<<a<<" first_new_b="<<b<<'\n';
  for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){int e=1<<i,y=(3*a)^(1<<j),d=abs(y-e);
    if(d%b==0){cout<<"first_new_i="<<i<<" first_new_j="<<j<<" t="<<d/b<<" F0_end="<<e<<" F3a_end="<<y<<'\n';return 0;}
  }
  throw runtime_error("first witness not found");
 }
}
