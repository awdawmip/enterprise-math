// PREFIX-943 exact W13-minus-prior-union census, auxiliary named-XOR two-port observer
// Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
// Build: g++ -O3 -std=c++17 -Wall -Wextra PREFIX943_R6_W13_FULL_PRIOR_UNION_CPP.cpp -o prefix943
// Run: cd inputdir && ./prefix943 PREFIX928_R6_SORTED_PAIR_IDS.bin W2.bin W3.bin D4_sorted_cpp.bin W5.bin D6.bin W7.bin D8.bin W9.bin D10.bin W13.bin NEW13.bin
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
constexpr int L=262145, H=524287, C=131072;
constexpr u64 N=1ULL<<32, PRIOR_UNION=7558699988ULL;
inline int ix(int a){return (a-L)/2;}
vector<uint8_t> inL(C),inT(C),inS(C);
void init(){
 vector<int>S,D,Z;
 for(int b=L;b<=H;b+=2){int r=1; bool early=false,late=false;
  for(int d=1;d<=52;++d){r=2LL*r%b; bool hit=(r==1||r==b-1); if(hit&&d<=31)early=true;else if(hit)late=true;}
  if(early){S.push_back(b);inS[ix(b)]=1;}else if(late)D.push_back(b);
 }
 if(S.size()!=24||D.size()!=91)throw runtime_error("historical S and D cardinality mismatch");
 Z=D;for(int b:{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287})Z.push_back(b);
 sort(Z.begin(),Z.end());Z.erase(unique(Z.begin(),Z.end()),Z.end());
 if(Z.size()!=104)throw runtime_error("historical V exceptional set mismatch");
 for(int b:Z)inL[ix(b)]=1;
 for(int t=0;t<1024;++t)inT[(77081LL*t+12345)%C]=1;
}
inline bool BZS(int a,int b){return (u64)b<33*((N+a-1)/a)||(u64)a<33*((N+b-1)/b)||inS[ix(b)]||((u64)a/gcd(a,b))*b<N;}
inline bool V(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
vector<u64> read(const char*name,size_t expected){
 ifstream f(name,ios::binary);if(!f)throw runtime_error(string("cannot open ")+name);
 vector<u64>out;out.reserve(expected);u64 id;
 while(f.read((char*)&id,8)){
  if(id>=u64(C)*C)throw runtime_error("invalid pair ID");
  if(!out.empty()&&out.back()>=id)throw runtime_error("unsorted or duplicated pair IDs");
  out.push_back(id);
 }
 if(out.size()!=expected)throw runtime_error(string("count mismatch: ")+name+" got "+to_string(out.size()));
 return out;
}
void write(const char*name,const vector<u64>&v){
 ofstream f(name,ios::binary);if(!f)throw runtime_error("cannot create output");
 for(u64 x:v)f.write((char*)&x,sizeof(x));
 if(!f)throw runtime_error("output write failed");
}
struct SSet {vector<u64> pairs; u64 raw=0;array<u64,64> by_t{};};
SSet build(int k){
 SSet s; s.pairs.reserve(19000000);
 for(int a=L;a<=H;a+=2){
  const u64 base=u64(ix(a))*C;
  for(int j=0;j<=18;++j){
   int y=k*a^(1<<j);
   if((u64)y>=N)throw runtime_error("illegal endpoint");
   for(int i=0;i<=18;++i){
    int d=y-(1<<i); if(d<=0)continue;
    int tl=max(1,(d+H-1)/H), th=d/L;
    for(int t=tl;t<=th;++t){
     if(d%t)continue;
     int b=d/t;
     if(b<L||b>H||!(b&1))continue;
     s.pairs.push_back(base+ix(b));++s.raw;++s.by_t.at(t);
    }
   }
  }
 }
 sort(s.pairs.begin(),s.pairs.end());s.pairs.erase(unique(s.pairs.begin(),s.pairs.end()),s.pairs.end());
 return s;
}
int main(int argc,char**argv){
 if(argc!=13)throw runtime_error("usage: binary U W2 W3 D4 W5 D6 W7 D8 W9 D10 W13.bin NEW13.bin");
 init();
 const char* labels[]={"BZS","U","V","W2","W3","D4","W5","D6","W7","D8","W9","D10","W11","NEW"};
 vector<vector<u64>> prior(10);
 size_t expected[]={5295478,30211412,19413088,1793182,15406809,1771013,14698334,4043794,15456919,1736455};
 for(int q=0;q<10;++q)prior[q]=read(argv[q+1],expected[q]);
 auto W11=build(11);auto W13=build(13);
 if(W11.raw!=16974425||W11.pairs.size()!=13144330)throw runtime_error("old W11 census mismatch");
 if(W13.raw!=16796156||W13.pairs.size()!=12993739)throw runtime_error("old W13 census mismatch");
 write(argv[11],W13.pairs);
 array<u64,14>cnt{};
 array<size_t,11>pos{};
 vector<u64>NEW; NEW.reserve(7500000);u64 inter11=0;u64 first=~0ULL;
 for(u64 id:W13.pairs){
  bool match[11]={};
  for(int h=0;h<10;++h){
   auto &v=prior[h];size_t &p=pos[h];while(p<v.size()&&v[p]<id)++p;match[h]=(p<v.size()&&v[p]==id);
  }
  auto &v=W11.pairs;size_t &p=pos[10];while(p<v.size()&&v[p]<id)++p;match[10]=(p<v.size()&&v[p]==id);
  inter11+=match[10];
  int a=L+2*(id/C),b=L+2*(id%C);
  int bucket=-1;
  if(BZS(a,b))bucket=0;
  else if(match[0])bucket=1;
  else if(V(a,b))bucket=2;
  else {for(int h=1;h<10;++h)if(match[h]){bucket=h+2;break;}}
  if(bucket<0&&match[10])bucket=12;
  if(bucket<0){bucket=13;NEW.push_back(id);if(first==~0ULL)first=id;}
  ++cnt[bucket];
 }
 if(inter11!=134197)throw runtime_error("W11-intersect-W13 mismatch");
 if(accumulate(cnt.begin(),cnt.end(),u64(0))!=W13.pairs.size())throw runtime_error("priority sum mismatch");
 write(argv[12],NEW);
 cout<<"PREFIX943_W13_VS_FULL_PRIOR_UNION\n";
 cout<<"frozen_pin=f42f2906d77f24085c123f3ccfe9667d41caa96d\n";
 cout<<"raw_W11="<<W11.raw<<"\nunique_W11="<<W11.pairs.size()<<"\n";
 cout<<"raw_W13="<<W13.raw<<"\nunique_W13="<<W13.pairs.size()<<"\n";
 cout<<"W11_inter_W13="<<inter11<<"\n";
 for(size_t h=0;h<cnt.size();++h)cout<<"priority_"<<labels[h]<<"="<<cnt[h]<<"\n";
 cout<<"old_union="<<PRIOR_UNION<<"\nnet_new="<<NEW.size()<<"\nnew_union="<<PRIOR_UNION+NEW.size()<<"\nremaining="<<u64(C)*C-PRIOR_UNION-NEW.size()<<"\n";
 cout<<"W13_bytes="<<W13.pairs.size()*8<<"\nNEW13_bytes="<<NEW.size()*8<<"\n";
 for(int t=1;t<=32;++t)if(W13.by_t[t])cout<<"raw_t"<<t<<"="<<W13.by_t[t]<<"\n";
 if(first!=~0ULL){
  int a=L+2*(first/C),b=L+2*(first%C);
  cout<<"first_new_a="<<a<<"\nfirst_new_b="<<b<<"\n";
  bool found=false;
  for(int i=0;i<=18&&!found;++i)for(int j=0;j<=18&&!found;++j){
   int y=13*a^(1<<j),d=y-(1<<i);
   if(d>0&&d%b==0){found=true;cout<<"first_new_i="<<i<<"\nfirst_new_j="<<j<<"\nfirst_new_t="<<d/b<<"\nfirst_new_start="<<13*a<<"\nfirst_new_end="<<y<<"\nfirst_zero_end="<<(1<<i)<<"\n";}
  }
  if(!found)throw runtime_error("first new lacks witness");
 }
}
