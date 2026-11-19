// PREFIX-931: zero-origin vs two-a start named two-flip collision certificates.
// Exact, integer-only census and full intersection with PREFIX-930 B/Z/S/U/V/W.
// Build: g++ -O3 -std=c++17 PREFIX931_R6_DOUBLE_MULTIPLE_CENSUS.cpp -o prefix931
// Run: ./prefix931 PREFIX928_R6_SORTED_PAIR_IDS.bin [W2_sorted_uint64le.bin] [W1_sorted_uint64le.bin]
#include <algorithm>
#include <cstdint>
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
inline u64 idof(int a,int b){return (u64)ix(a)*NQ+ix(b);}
void writeids(const char* path,const vector<u64>& v){
 ofstream o(path,ios::binary);if(!o)throw runtime_error("output open failed");
 for(u64 x:v)o.write(reinterpret_cast<const char*>(&x),8);
 if(!o)throw runtime_error("output write failed");
}
inline bool oldBZS(int a,int b){
 u64 ca=(N+(u64)a-1)/a,cb=(N+(u64)b-1)/b;
 return (u64)b<33*ca||(u64)a<33*cb||inS[ix(b)]||((u64)a/std::gcd(a,b))*b<N;
}
inline bool oldV(int a,int b){
 int ai=ix(a),bi=ix(b);
 return inL[ai]||inL[bi]||(a>=500001&&inT[bi])||(b>=500001&&inT[ai]);
}
void initialize(){
 vector<int> D,S,L;
 for(int b=Q0;b<=QMAX;b+=2){
  int r=1;bool early=false,late=false;
  for(int d=1;d<=52;++d){r=(2LL*r)%b;bool hit=r==1||r==b-1;
   if(hit&&d<=31)early=true;else if(hit)late=true;
  }
  if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("S/D anchor mismatch");
 L=D;const vector<int>E{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287};
 L.insert(L.end(),E.begin(),E.end());sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());
 if(L.size()!=104)throw runtime_error("L anchor mismatch");
 for(int b:L)inL[ix(b)]=1;
 vector<int>T;
 for(int t=0;t<1024;++t){int b=Q0+2*((77081LL*t+12345)%NQ);inT[ix(b)]=1;T.push_back(b);}
 sort(T.begin(),T.end());T.erase(unique(T.begin(),T.end());
 if(T.size()!=1024)throw runtime_error("T anchor mismatch");
}
int main(int argc,char**argv){
 if(argc<2||argc>4)throw runtime_error("usage: prefix931 U.bin [W2.bin] [W1.bin]");
 initialize();
 vector<u64> U;U.reserve(5295478);
 ifstream f(argv[1],ios::binary);if(!f)throw runtime_error("missing exact U input");
 u64 z;
 while(f.read((char*)&z,8)) {if(!U.empty()&&z<=U.back())throw runtime_error("invalid U ordering");U.push_back(z);}
 if(U.size()!=5295478)throw runtime_error("invalid U size");
 vector<u64> W1,W2;W1.reserve(30000000);W2.reserve(45000000);
 u64 raw1=0,raw2=0,raw2t1=0,raw2t2=0,raw2t3=0;
 for(int a=Q0;a<=QMAX;a+=2){
  const u64 ai=(u64)ix(a)*NQ;
  for(int j=0;j<=18;++j){
   const int y1=a^(1<<j),y2=(2*a)^(1<<j);
   for(int i=0;i<=18;++i){
    const int end0=1<<i;
    const int d1=abs(y1-end0);
    if(d1>=Q0&&d1<=QMAX&&(d1&1)){
     if((end0%d1)!=(y1%d1))throw runtime_error("old W1 witness invalid");
     W1.push_back(ai+ix(d1));++raw1;
    }
    const int d2=abs(y2-end0);
    // d2<2^20, b>=Q0, so every legal divisor b has quotient 1..3.
    for(int t=1;t<=3;++t){
     if(d2%t)continue;
     int b=d2/t;
     if(b<Q0||b>QMAX||(b&1)==0)continue;
     if(2*a>=N||(end0%b)!=(y2%b)||0%a!=(2*a)%a)throw runtime_error("W2 trace invalid");
     W2.push_back(ai+ix(b));++raw2;
     if(t==1)++raw2t1;else if(t==2)++raw2t2;else ++raw2t3;
    }
   }
  }
 }
 sort(W1.begin(),W1.end());W1.erase(unique(W1.begin(),W1.end()),W1.end());
 sort(W2.begin(),W2.end());W2.erase(unique(W2.begin(),W2.end()),W2.end());
 if(W1.size()!=29360142||raw1!=35782672)throw runtime_error("W1 published count mismatch");
 if(argc>=3)writeids(argv[2],W2);
 if(argc>=4)writeids(argv[3],W1);
 u64 cntBZS=0,cntU=0,cntV=0,cntW1=0,newCount=0;
 u64 newID=0;size_t pu=0,pw=0;
 for(u64 id:W2){
  while(pu<U.size()&&U[pu]<id)++pu;
  while(pw<W1.size()&&W1[pw]<id)++pw;
  int a=Q0+2*(id/NQ),b=Q0+2*(id%NQ);
  bool isU=pu<U.size()&&U[pu]==id;
  bool isW=pw<W1.size()&&W1[pw]==id;
  if(oldBZS(a,b)){++cntBZS;if(isU)throw runtime_error("U not disjoint from BZS");}
  else if(isU)++cntU;
  else if(oldV(a,b))++cntV;
  else if(isW)++cntW1;
  else{++newCount;if(!newID)newID=id;}
 }
 const u64 prior=7522177912ULL,total=(u64)NQ*NQ;
 if(W2.size()!=cntBZS+cntU+cntV+cntW1+newCount)throw runtime_error("partition mismatch");
 cout<<"PREFIX931_W1_check_raw="<<raw1<<"\nPREFIX931_W1_check_unique="<<W1.size()<<'\n';
 cout<<"W2_raw_parameters="<<raw2<<"\nW2_raw_t1="<<raw2t1<<"\nW2_raw_t2="<<raw2t2<<"\nW2_raw_t3="<<raw2t3<<'\n';
 cout<<"W2_unique_oriented_pairs="<<W2.size()<<"\nW2_overlap_BZS="<<cntBZS<<"\nW2_overlap_U_outside_BZS="<<cntU<<"\nW2_overlap_V_outside_BZS_U="<<cntV<<"\nW2_overlap_W1_outside_prior="<<cntW1<<"\n";
 cout<<"W2_increment_over_PREFIX930="<<newCount<<"\nPREFIX931_total_certified_union="<<prior+newCount<<"\nPREFIX931_certificate_complement="<<total-prior-newCount<<'\n';
 if(newID){int a=Q0+2*(newID/NQ),b=Q0+2*(newID%NQ);
  cout<<"first_new_a="<<a<<" b="<<b<<'\n';
  for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){int y=(2*a)^(1<<j),d=abs(y-(1<<i));if(d%b==0){cout<<"first_new_i="<<i<<" j="<<j<<" t="<<d/b<<" end0="<<(1<<i)<<" end2a="<<y<<'\n';return 0;}}
  throw runtime_error("missing witness for new pair");
 }
}
