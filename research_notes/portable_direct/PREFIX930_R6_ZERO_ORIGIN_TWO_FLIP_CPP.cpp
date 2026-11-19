// PREFIX-930: exact count of a source-labeled two-flip witness family
// against PREFIX-929 B/Z/S/U/V baseline. Compile with g++ -O3 -std=c++17.
// Usage: ./prefix930 PREFIX928_R6_SORTED_PAIR_IDS.bin [sorted_W.bin]
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using u64=uint64_t;
constexpr u64 N=1ULL<<32;
constexpr int Q0=262145,NQ=131072,QMAX=524287;
vector<uint8_t> inL(NQ),inT(NQ),inS(NQ);
inline int ix(int a){return (a-Q0)/2;}
inline bool bzs(int a,int b){
 const u64 ca=(N+(u64)a-1)/a,cb=(N+(u64)b-1)/b;
 if((u64)b<33*ca||(u64)a<33*cb)return true;
 if(inS[ix(b)])return true;
 return ((u64)a/std::gcd(a,b))*b<N;
}
inline bool oldV(int a,int b){
 int ai=ix(a),bi=ix(b);
 return inL[ai]||inL[bi]||
        (a>=500001&&inT[bi])||(b>=500001&&inT[ai]);
}
int main(int argc,char**argv){
 if(argc!=2&&argc!=3)throw runtime_error("usage: prefix930 verified_U.bin [sorted_W.bin]");
 vector<int>L,D,S,T;
 for(int b=Q0;b<=QMAX;b+=2){
  int r=1;bool early=false,late=false;
  for(int d=1;d<=52;++d){r=(2LL*r)%b;bool hit=r==1||r==b-1;
   if(hit&&d<=31)early=true;else if(hit)late=true;
  }
  if(early){S.push_back(b);inS[ix(b)]=1;}
  else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("S/D prior mismatch");
 L=D;const vector<int>E{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287};
 L.insert(L.end(),E.begin(),E.end());sort(L.begin(),L.end());L.erase(unique(L.begin(),L.end()),L.end());
 if(L.size()!=104)throw runtime_error("prior L count mismatch");
 for(int b:L)inL[ix(b)]=1;
 for(int t=0;t<1024;++t){int b=Q0+2*((77081LL*t+12345)%NQ);inT[ix(b)]=1;T.push_back(b);}
 sort(T.begin(),T.end());T.erase(unique(T.begin(),T.end()),T.end());
 if(T.size()!=1024)throw runtime_error("prior T count mismatch");
 vector<u64> candidates;candidates.reserve(35000000);
 u64 raw=0;
 for(int a=Q0;a<=QMAX;a+=2){
  u64 ai=(u64)ix(a)*NQ;
  for(int j=0;j<=18;++j){
   int y=a^(1<<j);
   for(int i=0;i<=18;++i){
    int d=y-(1<<i);int b=d<0?-d:d;
    if(b<Q0||b>QMAX||(b&1)==0)continue;
    if((0%a)!=(a%a)||((1<<i)%b)!=(y%b))throw runtime_error("XOR witness invalid");
    candidates.push_back(ai+ix(b));++raw;
   }
  }
 }
 sort(candidates.begin(),candidates.end());
 candidates.erase(unique(candidates.begin(),candidates.end()),candidates.end());
 if(argc==3){
  ofstream outf(argv[2],ios::binary);
  if(!outf)throw runtime_error("cannot open sorted output");
  for(u64 id:candidates)outf.write((char*)&id,8);
  if(!outf)throw runtime_error("cannot write sorted output");
 }
 ifstream in(argv[1],ios::binary);if(!in)throw runtime_error("U file missing");
 vector<u64> U;U.reserve(5295478);u64 u;
 while(in.read((char*)&u,sizeof(u))){
  if(!U.empty()&&U.back()>=u)throw runtime_error("U not sorted");
  U.push_back(u);
 }
 if(U.size()!=5295478)throw runtime_error("U count mismatch");
 u64 cBZS=0,cU=0,cV=0,increment=0;size_t pos=0;u64 wID=0;
 for(u64 id:candidates){
  while(pos<U.size()&&U[pos]<id)++pos;
  int a=Q0+2*(int)(id/NQ),b=Q0+2*(int)(id%NQ);
  bool belongsU=pos<U.size()&&U[pos]==id;
  if(bzs(a,b)){
   if(belongsU)throw runtime_error("U/BZS disjointness violated");
   ++cBZS;
  }else if(belongsU){++cU;}
  else if(oldV(a,b)){++cV;}
  else{++increment;if(!wID)wID=id;}
 }
 constexpr u64 base=7505960064ULL,total=(u64)NQ*NQ;
 if(candidates.size()!=cBZS+cU+cV+increment)throw runtime_error("partition failed");
 cout<<"raw_witness_parameters="<<raw<<"\n";
 cout<<"unique_ordered_pair_certificates="<<candidates.size()<<"\n";
 cout<<"overlap_BZS="<<cBZS<<"\n";
 cout<<"overlap_U_outside_BZS="<<cU<<"\n";
 cout<<"overlap_V_outside_K="<<cV<<"\n";
 cout<<"increment_over_PREFIX929="<<increment<<"\n";
 cout<<"new_certified_union="<<base+increment<<"\n";
 cout<<"remaining_certificate_complement="<<total-base-increment<<"\n";
 int aa=Q0+2*(int)(wID/NQ),bb=Q0+2*(int)(wID%NQ);
 cout<<"first_new_pair_a="<<aa<<" b="<<bb<<"\n";
 for(int j=0;j<=18;++j)for(int i=0;i<=18;++i){
  int y=aa^(1<<j),d=y-(1<<i),b=d<0?-d:d;
  if(b==bb){cout<<"first_witness_i="<<i<<" j="<<j<<" end0="<<(1<<i)<<" end1="<<y<<"\n";return 0;}
 }
 throw runtime_error("missing witness for new pair");
}
