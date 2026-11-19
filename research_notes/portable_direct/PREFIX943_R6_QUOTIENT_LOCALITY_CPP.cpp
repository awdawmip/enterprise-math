// PREFIX-943B: classify distinct quotient t supports per ordered modulus pair.
// Full Q={262145,262147,...,524287}, k=17, i,j<=18; exact integer arithmetic.
// Compile: g++ -O3 -std=c++17 PREFIX943_R6_QUOTIENT_LOCALITY_CPP.cpp -o qlocal
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 const int L=262145,U=524287,Q=131072,K=17,TMAX=34;
 vector<uint64_t> keys;keys.reserve(20000000);
 for(int a=L;a<=U;a+=2){
  uint64_t ab=((uint64_t)(a-L)/2)*Q;
  for(int j=0;j<=18;++j){
   int y=(K*a)^(1<<j);
   for(int i=0;i<=18;++i){
    int d=y-(1<<i);
    for(int t=max(1,(d+U-1)/U);t<=min(TMAX,d/L);++t){
     if(d%t)continue;
     int b=d/t;
     if(b>=L&&b<=U&&(b&1))keys.push_back(((ab+(b-L)/2)<<6)|t);
    }
   }
  }
 }
 uint64_t raw=keys.size();
 sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());
 uint64_t total=0,one=0,two_adj=0,two_gap2=0,three=0,problem=0;
 uint64_t pair_t_count=keys.size();
 uint64_t adj_by_start[35]={},two_by_start[35]={},tri_by_start[35]={};
 for(size_t p=0;p<keys.size();){
  uint64_t id=keys[p]>>6;int vals[36];int n=0;
  do{vals[n++]=keys[p++]&63;}while(p<keys.size()&&(keys[p]>>6)==id);
  ++total;
  if(n==1)++one;
  else if(n==2){
   if(vals[1]-vals[0]==1){++two_adj;++adj_by_start[vals[0]];}
   else if(vals[1]-vals[0]==2){++two_gap2;++two_by_start[vals[0]];}
   else ++problem;
  }else if(n==3){
   if(vals[2]-vals[0]==2&&vals[1]-vals[0]==1){++three;++tri_by_start[vals[0]];}
   else ++problem;
  }else ++problem;
 }
 cout<<"raw="<<raw<<"\npair_t="<<pair_t_count<<"\nunique="<<total
     <<"\none="<<one<<"\ntwo_adj="<<two_adj<<"\ntwo_gap2="<<two_gap2
     <<"\nthree="<<three<<"\nproblem="<<problem<<"\n";
 for(int t=1;t<=34;++t)if(adj_by_start[t]||two_by_start[t]||tri_by_start[t])
  cout<<"t="<<t<<": adjacent_exact2="<<adj_by_start[t]<<", gap2_exact2="
      <<two_by_start[t]<<", triple="<<tri_by_start[t]<<"\n";
 if(raw!=19318164||total!=15136736||problem)return 3;
}
