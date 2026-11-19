// PREFIX-925 independent C++17 exact special-second-port census.
// g++ -O2 -std=c++17 PREFIX925_R6_SAME_START_UNION.cpp -o prefix925 && ./prefix925
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
using ull=uint64_t;
constexpr int L=262145,U=524287,C=33;
constexpr ull N=1ULL<<32;
ull ceildiv(ull a,ull b){return (a+b-1)/b;}
int main(){
 vector<pair<int,int>> special;
 for(int b=L;b<=U;b+=2){
  int residue=2%b,w=0;
  for(int d=1;d<=31;d++){
   if(residue==1||residue==b-1)w+=32-d;
   residue=int((2LL*residue)%b);
  }
  if(w)special.push_back({b,w});
 }
 ull added=0,cap_intersection=0,zero_intersection=0,triple=0;
 for(auto [b,w]:special)for(int a=L;a<=U;a+=2){
  bool capacity_safe=(ull)b>=C*ceildiv(N,a)&&(ull)a>=C*ceildiv(N,b);
  bool zerozero=(ull(a)/gcd(a,b))*b<N;
  if(!capacity_safe)cap_intersection++;
  if(zerozero)zero_intersection++;
  if(!capacity_safe&&zerozero)triple++;
  if(capacity_safe&&!zerozero)added++;
 }
 assert(special.size()==24&&added==1613509ULL&&
        cap_intersection==1493890ULL&&zero_intersection==93092ULL&&triple==54763ULL);
 cout<<"special_second_moduli="<<special.size()
     <<"\nsame_start_support="<<(special.size()*131072ULL)
     <<"\nextra_outside_capacity_zerozero="<<added
     <<"\nS_intersect_B="<<cap_intersection
     <<"\nS_intersect_Z="<<zero_intersection
     <<"\ntriple_intersection="<<triple
     <<"\nthree_family_union="<<(7460895462ULL+added)
     <<"\nremaining="<<(9718973722ULL-added)<<"\n";
}
