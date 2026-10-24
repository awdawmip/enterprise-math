// R269 independent exact positive BRC checker (finite verification, not infinity proof).
// Original six formal slots use affine effect (eps,k), not native X6.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using State=std::tuple<int,int,int,int>; // q,r,eps,k
using Counts=std::map<State,std::uint64_t>;
using Eff=std::pair<int,int>;
const std::array<std::array<std::array<int,3>,2>,3> EDGES = {{
 {{{2,-1,-1},{2,+1,-1}}},
 {{{0,-1,-1},{0,+1,-1}}},
 {{{1,+1,+1},{2,+1,-1}}}
}};
const std::array<std::array<int,2>,3> DELTA = {{{{1,0}},{{2,0}},{{2,2}}}};
const std::map<std::pair<int,int>,std::pair<int,int>> OFFSETS={
 {{0,0},{2,-8}},{{0,2},{4,-4}},{{1,1},{2,-6}},
 {{1,2},{4,-4}},{{2,0},{0,-6}},{{2,1},{8,-4}},{{2,2},{2,-6}}
};
State step(const State &s, int a) {
 auto [q,r,e,k]=s;
 const auto &row=EDGES[q][a];
 return {row[0],DELTA[r][a],row[1]*e,row[1]*k+row[2]};
}
Counts advance(const Counts &c) {
 Counts d;
 for(const auto &[s,w]:c)
   for(int a=0;a<2;a++)d[step(s,a)]+=w;
 return d;
}
std::set<int> interval(int n,int a,int b){
 std::set<int> s;
 for(int k=-n+a;k<=n+b;k+=2)s.insert(k);
 return s;
}
void check(int n,const Counts &c){
 std::map<std::tuple<int,int,int>,std::set<int>> state_support;
 std::map<Eff,std::set<std::pair<int,int>>> seven,six;
 std::uint64_t total=0;
 for(auto &[s,w]:c){
   assert(w>0);
   auto [q,r,e,k]=s;total+=w;
   state_support[{q,r,e}].insert(k);
   seven[{e,k}].insert({q,r});
   six[{e,k}].insert({q,r==2?1:0});
 }
 assert(total==(std::uint64_t(1)<<n));
 for(const auto &[qr,offset]:OFFSETS){
   for(int e:{-1,1}){
     auto actual=state_support[{qr.first,qr.second,e}];
     assert(actual==interval(n,offset.first,offset.second));
   }
 }
 int all7=0,all6=0,sixbutnot7=0;
 for(const auto &[g,x]:seven){
   bool s7=x.size()==7,s6=six[g].size()==6;
   all7+=s7;all6+=s6;sixbutnot7+=s6&&!s7;
 }
 assert(int(seven.size())==2*n-2);
 assert(all7==2*n-14);
 assert(all6==2*n-10);
 assert(sixbutnot7==4);
}
void base_enumeration(){
 Counts enumeration;
 for(int word=0;word<1024;word++){
   State s={0,0,1,0};
   for(int i=9;i>=0;i--)s=step(s,(word>>i)&1);
   enumeration[s]++;
 }
 Counts dynamics;dynamics[{0,0,1,0}]=1;
 for(int n=0;n<10;n++)dynamics=advance(dynamics);
 assert(enumeration==dynamics);
 check(10,dynamics);
}
void interval_induction_certificate(){
 std::map<std::pair<int,int>,std::vector<std::pair<int,int>>> input;
 for(const auto &[qr,offset]:OFFSETS){
   for(int a=0;a<2;a++){
     const auto &row=EDGES[qr.first][a];
     int e=row[1],beta=row[2],na,nb;
     if(e==1){na=offset.first+beta+1;nb=offset.second+beta-1;}
     else{na=-offset.second+beta+1;nb=-offset.first+beta-1;}
     input[{row[0],DELTA[qr.second][a]}].push_back({na,nb});
   }
 }
 assert(input.size()==OFFSETS.size());
 for(const auto &[dest,offset]:OFFSETS){
   std::set<int> union_at_11;
   int min_a=999,max_b=-999;
   for(const auto &[a,b]:input[dest]){
     min_a=std::min(min_a,a);max_b=std::max(max_b,b);
     auto part=interval(11,a,b);
     union_at_11.insert(part.begin(),part.end());
   }
   assert(min_a==offset.first&&max_b==offset.second);
   assert(union_at_11==interval(11,offset.first,offset.second));
   // Since each constituent [-n+a,n+b] expands monotonically with n,
   // adjacency at n=11 proves gaplessness for all n>=11 (with parity flip).
 }
}
int main(){
 base_enumeration();interval_induction_certificate();
 Counts dp;dp[{0,0,1,0}]=1;
 for(int n=0;n<=30;n++){
   if(n>=10)check(n,dp);
   if(n<30)dp=advance(dp);
 }
 std::cout<<"R269_CPP17_PASS base_1024; symbolic_interval_images_7; recurrence_depth_30\n";
}
