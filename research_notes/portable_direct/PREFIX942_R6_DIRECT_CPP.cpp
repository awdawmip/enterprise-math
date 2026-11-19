// PREFIX-942 independent enumeration (C++17, exact integer arithmetic).
// Reports raw witnesses for k=11,13,15,17 and distinct pair overlap of W11/W13.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static constexpr uint64_t LO=262145, HI=524287, QSIZE=131072;
struct Census {uint64_t raw=0; vector<uint64_t> pairs; vector<uint64_t> by_t;};
Census census(int k, bool store_pairs){
 Census c; c.by_t.assign(64,0);
 if(store_pairs) c.pairs.reserve(18'000'000);
 for(uint64_t a=LO;a<=HI;a+=2){
   uint64_t start=(uint64_t)k*a;
   for(int j=0;j<=18;j++){
     uint64_t flipped=start^(uint64_t(1)<<j);
     for(int i=0;i<=18;i++){
       int64_t d=(int64_t)flipped-(int64_t(1)<<i);
       if(d<=0)continue;
       int64_t tl=max<int64_t>(1,(d+(int64_t)HI-1)/(int64_t)HI), th=d/(int64_t)LO;
       for(int64_t t=tl;t<=th;t++){
         if(d%t) continue;
         int64_t b=d/t;
         if(b<(int64_t)LO || b>(int64_t)HI || !(b&1))continue;
         c.raw++;
         c.by_t.at(t)++;
         if(store_pairs) c.pairs.push_back(((a-LO)/2)*QSIZE + ((b-LO)/2));
       }
     }
   }
 }
 if(store_pairs) {
  sort(c.pairs.begin(),c.pairs.end());
  c.pairs.erase(unique(c.pairs.begin(),c.pairs.end()),c.pairs.end());
 }
 return c;
}
int main(){
 auto A=census(11,true), B=census(13,true);
 uint64_t both=0; size_t i=0,j=0;
 while(i<A.pairs.size() && j<B.pairs.size()){
  if(A.pairs[i]==B.pairs[j]){both++;i++;j++;}
  else if(A.pairs[i]<B.pairs[j])i++; else j++;
 }
 cout<<"W11 raw="<<A.raw<<" unique_pairs="<<A.pairs.size()<<"\n";
 cout<<"W13 raw="<<B.raw<<" unique_pairs="<<B.pairs.size()<<"\n";
 cout<<"W11_intersect_W13="<<both<<" W13_minus_W11="<<B.pairs.size()-both<<"\n";
 for(uint64_t pair_id:B.pairs){
  if(binary_search(A.pairs.begin(),A.pairs.end(),pair_id)) continue;
  uint64_t a=LO+2*(pair_id/QSIZE),b=LO+2*(pair_id%QSIZE);
  bool found=false;
  for(int j=0;j<=18 && !found;j++)for(int i=0;i<=18 && !found;i++){
    uint64_t y=(13*a)^(uint64_t(1)<<j);
    int64_t d=(int64_t)y-(int64_t(1)<<i);
    if(d>0 && d%(int64_t)b==0){
      cout<<"W13_minus_W11_witness a="<<a<<" b="<<b<<" i="<<i<<" j="<<j<<" t="<<d/b<<" endpoint="<<y<<"\n";
      found=true;
    }
  }
  if(!found) return 2;
  break;
 }
 cout<<"by_t[11]:";
 for(size_t t=0;t<A.by_t.size();t++)if(A.by_t[t]) cout<<" "<<t<<":"<<A.by_t[t];
 cout<<"\n";
 cout<<"by_t[13]:";
 for(size_t t=0;t<B.by_t.size();t++)if(B.by_t[t]) cout<<" "<<t<<":"<<B.by_t[t];
 cout<<"\n";
 for(int k : {15,17}){
  Census c=census(k,false);
  cout<<"k="<<k<<" raw="<<c.raw<<" by_t:";
  for(size_t t=0;t<c.by_t.size();t++)if(c.by_t[t])cout<<" "<<t<<":"<<c.by_t[t];
  cout<<"\n";
 }
}
