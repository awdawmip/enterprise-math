// PREFIX-933, frozen f42f2906d77f24085c123f3ccfe9667d41caa96d
// g++ -O3 -std=c++17 PREFIX933_R6_FOUR_A_BOUNDARY_EXACT_CPP.cpp -o p933
// ./p933 U.bin W2.bin W3.bin D4.bin
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

vector<u64> read_ids(const char*p,size_t n){
 ifstream f(p,ios::binary);if(!f)throw runtime_error("missing input");
 vector<u64> a; a.reserve(n);u64 z;
 while(f.read((char*)&z,8)){if(!a.empty()&&a.back()>=z)throw runtime_error("unsorted input");a.push_back(z);}
 if(a.size()!=n)throw runtime_error("wrong input size");return a;
}
int main(int argc,char**argv){
 if(argc!=5)throw runtime_error("usage: p933 U W2 W3 D4");
 initialize();
 auto U=read_ids(argv[1],5295478),W2=read_ids(argv[2],30211412),W3=read_ids(argv[3],19413088);
 vector<u64>D4;D4.reserve(2000000);u64 raw=0,raw_t[9]={},raw_i0=0,raw_j0=0;
 for(int a=Q0;a<=QMAX;a+=2){u64 off=(u64)ix(a)*NQ;int x=4*a;
  for(int j=0;j<=18;j++){int y=x^(1<<j);
   for(int i=0;i<=18;i++){if(i&&j)continue;int h=1<<i,d=y-h;
    if(d<=0)throw runtime_error("nonpositive difference");
    for(int t=1;t<=8;t++){if(d%t)continue;int b=d/t;
     if(b<Q0||b>QMAX||!(b&1))continue;
     if(x%a||y%b!=h%b)throw runtime_error("invalid witness");
     D4.push_back(off+ix(b));raw++;raw_t[t]++;if(i==0)raw_i0++;else raw_j0++;
    }
   }
  }
 }
 sort(D4.begin(),D4.end());D4.erase(unique(D4.begin(),D4.end()),D4.end());
 ofstream o(argv[4],ios::binary);for(u64 z:D4)o.write((char*)&z,8);if(!o)throw runtime_error("cannot write D4");
 size_t pu=0,p2=0,p3=0;u64 B=0,Uc=0,V=0,W2c=0,W3c=0,Nc=0,first=0;
 for(u64 z:D4){while(pu<U.size()&&U[pu]<z)pu++;while(p2<W2.size()&&W2[p2]<z)p2++;while(p3<W3.size()&&W3[p3]<z)p3++;
  int a=Q0+2*(z/NQ),b=Q0+2*(z%NQ);
  bool u=pu<U.size()&&U[pu]==z,w2=p2<W2.size()&&W2[p2]==z,w3=p3<W3.size()&&W3[p3]==z;
  if(oldBZS(a,b)){B++;if(u)throw runtime_error("U/BZS overlap");}
  else if(u)Uc++;else if(oldV(a,b))V++;else if(w2)W2c++;else if(w3)W3c++;
  else{Nc++;if(!first)first=z;}
 }
 if(B+Uc+V+W2c+W3c+Nc!=D4.size())throw runtime_error("partition error");
 cout<<"raw="<<raw<<" unique="<<D4.size()<<" raw_i0="<<raw_i0<<" raw_j0_positive="<<raw_j0<<'\n';
 for(int t=1;t<=8;t++)cout<<"raw_t"<<t<<'='<<raw_t[t]<<'\n';
 cout<<"BZS="<<B<<" U="<<Uc<<" V="<<V<<" W2="<<W2c<<" W3="<<W3c<<" new="<<Nc<<'\n';
 cout<<"union="<<7530824145ULL+Nc<<" complement="<<(u64)NQ*NQ-7530824145ULL-Nc<<'\n';
 if(first){int a=Q0+2*(first/NQ),b=Q0+2*(first%NQ);cout<<"first_a="<<a<<" first_b="<<b<<'\n';}
}
