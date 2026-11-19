// PREFIX-945 R6: exactly enumerate W19 and subtract full predecessor union P17
// Scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d
// Model: auxiliary named XOR two-port observer. GNU C++17, deterministic integers.
// Run in directory with frozen U/W2..D10 and W13.bin:
//   g++ -O3 -std=c++17 -Wall -Wextra PREFIX945_R6_W15_W17_PRIORITY_CPP.cpp -o prefix944
//   ./prefix944 | tee PREFIX945_R6_CENSUS.txt
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
constexpr int L=262145, H=524287, C=131072, MAXBIT=18;
constexpr u64 N=1ULL<<32, PRIOR_UNION=7577727669ULL;
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
 if(Z.size()!=104)throw runtime_error("historical V exception count mismatch");
 for(int b:Z)inL[ix(b)]=1;
 for(int t=0;t<1024;++t)inT[(77081LL*t+12345)%C]=1;
}
inline bool BZS(int a,int b){return (u64)b<33*((N+a-1)/a)||(u64)a<33*((N+b-1)/b)||inS[ix(b)]||((u64)a/gcd(a,b))*b<N;}
inline bool V(int a,int b){return inL[ix(a)]||inL[ix(b)]||(a>=500001&&inT[ix(b)])||(b>=500001&&inT[ix(a)]);}
vector<u64> read(const char*name,size_t expected){
 ifstream f(name,ios::binary);if(!f)throw runtime_error(string("cannot open ")+name);
 vector<u64>out;out.reserve(expected);u64 id;
 while(f.read((char*)&id,8)){
  if(id>=u64(C)*C)throw runtime_error(string("invalid pair ID ")+name);
  if(!out.empty()&&out.back()>=id)throw runtime_error(string("unsorted or duplicated pair IDs ")+name);
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
 SSet s; s.pairs.reserve(21000000);
 for(int a=L;a<=H;a+=2){
  const u64 base=u64(ix(a))*C;
  for(int j=0;j<=MAXBIT;++j){
   int y=k*a^(1<<j);
   if((u64)y>=N)throw runtime_error("illegal endpoint");
   for(int i=0;i<=MAXBIT;++i){
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
void output(int k,const SSet&cur,const vector<vector<u64>>&prior,const SSet& W11,
            const vector<u64>& W13,const vector<u64>*W15,const vector<u64>*W17,u64 old_union,const char*nameprefix){
 vector<const vector<u64>*> refs;
 for(auto &v:prior)refs.push_back(&v);
 refs.push_back(&W11.pairs);refs.push_back(&W13);
 if(W15)refs.push_back(W15);
 if(W17)refs.push_back(W17);
 vector<string> labels={"BZS","U","V","W2","W3","D4","W5","D6","W7","D8","W9","D10","W11","W13"};
 if(W15)labels.push_back("W15");
 if(W17)labels.push_back("W17");
 labels.push_back("NEW");
 vector<u64>cnt(labels.size());
 vector<size_t>pos(refs.size());
 vector<u64>added;added.reserve(8000000);
 u64 first=~u64(0);
 for(u64 id:cur.pairs){
  int a=L+2*(id/C),b=L+2*(id%C);
  int bucket=-1;
  if(BZS(a,b))bucket=0;
  else if(V(a,b)){
    const auto &u=*refs[0];size_t &p=pos[0];while(p<u.size()&&u[p]<id)++p;
    bucket=(p<u.size()&&u[p]==id)?1:2;
  }else{
    const auto &u=*refs[0];size_t &p=pos[0];while(p<u.size()&&u[p]<id)++p;
    if(p<u.size()&&u[p]==id)bucket=1;
  }
  if(bucket<0){
   for(size_t r=1;r<refs.size();++r){
    const auto &v=*refs[r];size_t &p=pos[r];
    while(p<v.size()&&v[p]<id)++p;
    if(p<v.size()&&v[p]==id){bucket=int(r)+2;break;}
   }
  }
  if(bucket<0){bucket=int(labels.size())-1;added.push_back(id);if(first==~u64(0))first=id;}
  ++cnt.at(bucket);
 }
 if(accumulate(cnt.begin(),cnt.end(),u64(0))!=cur.pairs.size())throw runtime_error("partition mismatch");
 const string nameW=string(nameprefix)+"_W"+to_string(k)+".bin",nameNew=string(nameprefix)+"_NEW"+to_string(k)+".bin";
 write(nameW.c_str(),cur.pairs);write(nameNew.c_str(),added);
 cout<<"PREFIX945_k="<<k<<"\n";
 cout<<"raw_W"<<k<<"="<<cur.raw<<"\nunique_W"<<k<<"="<<cur.pairs.size()<<"\n";
 for(size_t h=0;h<labels.size();++h)cout<<"priority_"<<labels[h]<<"="<<cnt[h]<<"\n";
 cout<<"old_union="<<old_union<<"\nnet_new="<<added.size()<<"\nnew_union="<<old_union+added.size()<<"\nremaining="<<u64(C)*C-old_union-added.size()<<"\n";
 for(int t=1;t<64;++t)if(cur.by_t[t])cout<<"raw_t"<<t<<"="<<cur.by_t[t]<<"\n";
 if(first!=~u64(0)){
  int a=L+2*(first/C),b=L+2*(first%C);
  cout<<"first_new_a="<<a<<"\nfirst_new_b="<<b<<"\n";
  bool found=false;
  for(int i=0;i<=MAXBIT&&!found;++i)for(int j=0;j<=MAXBIT&&!found;++j){
   int y=k*a^(1<<j),d=y-(1<<i);
   if(d>0&&d%b==0){found=true;cout<<"first_new_i="<<i<<"\nfirst_new_j="<<j<<"\nfirst_new_t="<<d/b<<"\nfirst_new_start="<<k*a<<"\nfirst_new_end="<<y<<"\nfirst_zero_end="<<(1<<i)<<"\n";}
  }
  if(!found)throw runtime_error("first new has no witness");
 }
 cout<<"\n";
}
int main(){
 init();
 const char *oldnames[]={"PREFIX928_R6_SORTED_PAIR_IDS.bin","W2.bin","W3.bin","D4_sorted_cpp.bin","W5.bin","D6.bin","W7.bin","D8.bin","W9.bin","D10.bin"};
 size_t expected[]={5295478,30211412,19413088,1793182,15406809,1771013,14698334,4043794,15456919,1736455};
 vector<vector<u64>> prior(10);
 for(int q=0;q<10;++q)prior[q]=read(oldnames[q],expected[q]);
 auto W13=read("W13.bin",12993739);
 auto W15=read("PREFIX944_W15.bin",16762415);
 auto W17=read("PREFIX944_W17.bin",15136736);
 SSet W11=build(11);
 write("W11_REGEN.bin",W11.pairs);
 if(W11.raw!=16974425||W11.pairs.size()!=13144330)throw runtime_error("W11 regression mismatch");
 SSet W19=build(19);
 if(W19.raw!=16565914||W19.pairs.size()!=12701275)throw runtime_error("W19 regression mismatch");
 output(19,W19,prior,W11,W13,&W15,&W17,PRIOR_UNION,"PREFIX945");
 cout<<"ALL_FULL_DOMAIN_PRIORITY_ASSERTIONS_PASSED\n";
}
