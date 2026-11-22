// Exact finite p=19, valuation-one, total vertical order nine, canonical cofactor split join.
// Author-side exploratory certificate; not Source-native, independent review pending.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <chrono>
using u64=uint64_t; using u128=unsigned __int128;
constexpr int P=19, B=2331;
constexpr u64 L=1698160464000ULL;
const int primes[]={2,3,5,7,11,13,17,19};
bool smooth(int v){for(int p:primes)while(v%p==0)v/=p;return v==1;}
std::string s128(u128 v){if(!v)return "0"; std::string s;while(v){s.push_back('0'+v%10);v/=10;}std::reverse(s.begin(),s.end());return s;}
struct A{int q,a,w;u64 x;u128 x2,x3;};
struct Part{int m,n;u64 x;u128 x2,x3;u64 mask;};
struct Target{u128 x2,x3;u64 vmask;uint32_t qmask,vi,qi;};
struct Match {uint32_t avi,aqi,bvi,bqi;std::string h3num;bool disjoint;};
std::vector<A> atoms;
std::vector<Part> vA,vB,q0;
void gen_v(std::vector<Part>&out,int start,int rem,int m,int n,u64 x,u128 x2,u128 x3,u64 mask){
 if(!rem){out.push_back({m,n,x,x2,x3,mask});return;}
 for(int i=start;i<(int)atoms.size();i++){auto&a=atoms[i];if(a.q>rem||m+a.w>B)continue;
 gen_v(out,i,rem-a.q,m+a.w,n+1,x+a.x,x2+a.x2,x3+a.x3,mask|(1ULL<<i));}
}
void gen_q(int j,int cap,int m,int n,u64 x,u128 x2,u128 x3,uint32_t mask){
 if(j==P){q0.push_back({m,n,x,x2,x3,mask});return;}
 const int w=P*j-1;const u64 c=L/j;const u128 c2=u128(c)*c,c3=c2*c;
 for(int count=0; m+count*w<=cap;count++){
  gen_q(j+1,cap,m+count*w,n+count,x+count*c,x2+count*c2,x3+count*c3,mask|(count?(1U<<(j-1)):0));
 }
}
struct Stat{u64 full=0,h01=0,h012=0,after_support=0,h013=0;};
int main(int argc,char**argv){
 if(argc!=3){std::cerr<<"Usage: checker left_q right_q (3 6 or 4 5)\n";return 2;}
 const int qa=atoi(argv[1]),qb=atoi(argv[2]);if(qa+qb!=9||qa<1||qb<1)return 2;
 for(int q=1;q<=6;q++)for(int r=1;r<P;r++){
  int a=P*q+r; if(!smooth(a))continue;
  assert(L%a==0);const u64 x=L/a;
  atoms.push_back({q,a,P*a-1,x,u128(x)*x,u128(x)*x*x});
 }
 assert(atoms.size()==64);
 for(int j=1;j<P;j++)assert(L%j==0);
 gen_v(vA,0,qa,0,0,0,0,0,0);gen_v(vB,0,qb,0,0,0,0,0,0);
 int minA=B,minB=B;for(auto&a:vA)minA=std::min(minA,a.m);for(auto&a:vB)minB=std::min(minB,a.m);
 int cap=std::max(B-minA,B-minB);
 q0.reserve(cap>=1200?10000000:600000);
 gen_q(1,cap,0,0,0,0,0,0);
 std::sort(q0.begin(),q0.end(),[](const Part&x,const Part&y){return x.m<y.m;});
 auto begin=std::chrono::steady_clock::now();
 // Build only the heavier vertical side's small target (q=6 or 5).
 std::unordered_map<u64,std::vector<Target>> targets;targets.reserve(65536);
 Stat sb,sa;
 for(uint32_t vi=0;vi<vB.size();vi++){
  const auto&v=vB[vi];
  for(uint32_t qi=0;qi<q0.size();qi++){
   const auto&q=q0[qi];if(v.m+q.m>B)break;
   sb.full++;u64 x=v.x+q.x;uint64_t n=v.n+q.n;
   assert(n<256&&x<(1ULL<<56));
   targets[x+(n<<56)].push_back({v.x2+q.x2,v.x3+q.x3,v.mask,(uint32_t)q.mask,vi,qi});
  }
 }
 std::vector<Match> sample;sample.reserve(100);
 for(uint32_t vi=0;vi<vA.size();vi++){
  const auto&v=vA[vi];
  for(uint32_t qi=0;qi<q0.size();qi++){
   const auto&q=q0[qi];if(v.m+q.m>B)break;
   sa.full++;u64 x=v.x+q.x;uint64_t n=v.n+q.n;
   assert(n<256&&x<(1ULL<<56));
   auto it=targets.find(x+(n<<56));if(it==targets.end())continue;
   for(const auto&t:it->second){sa.h01++;
    if(t.x2!=v.x2+q.x2)continue;
    sa.h012++;
    bool disjoint=!(t.vmask&v.mask)&&!(t.qmask&(uint32_t)q.mask);
    if(disjoint)sa.after_support++;
    bool h3= t.x3==v.x3+q.x3;
    if(disjoint&&h3)sa.h013++;
    if(disjoint && sample.size()<100){sample.push_back({vi,qi,t.vi,t.qi,
     (v.x3+q.x3>=t.x3?s128(v.x3+q.x3-t.x3):"-"+s128(t.x3-v.x3-q.x3)),disjoint});}
   }
  }
 }
 double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
 std::cout<<"{\"schema\":\"T6_P19_Q9_SPLIT_VALUATION_ONE_H012_JOIN_V1\",\"q_split\":["<<qa<<","<<qb<<"],\"p\":19,\"budget_each\":2331,\"cofactor_lcm\":\""<<L<<"\",\"q0_j\":[1,18],\"vertical_atoms\":"<<atoms.size()
 <<",\"vertical_side_counts\":["<<vA.size()<<","<<vB.size()<<"],\"minimum_vertical_masses\":["<<minA<<","<<minB<<"],\"q0_cap\":"<<cap<<",\"q0_multisets_generated\":"<<q0.size()
 <<",\"full_side_counts\":["<<sa.full<<","<<sb.full<<"],\"cross_pairs_H01\":"<<sa.h01<<",\"cross_pairs_H012\":"<<sa.h012<<",\"cross_pairs_H012_after_support\":"<<sa.after_support<<",\"cross_pairs_H013_after_support\":"<<sa.h013
 <<",\"elapsed_join_seconds\":"<<seconds<<",\"samples\":[";
 for(size_t i=0;i<sample.size();i++){if(i)std::cout<<",";auto&z=sample[i];std::cout<<"{\"A_indices\":["<<z.avi<<","<<z.aqi<<"],\"B_indices\":["<<z.bvi<<","<<z.bqi<<"],\"scaled_H3_diff_numerator\":\""<<z.h3num<<"\",\"disjoint\":"<<(z.disjoint?"true":"false")<<",\"A_q0_mass\":"<<q0[z.aqi].m<<",\"B_q0_mass\":"<<q0[z.bqi].m<<",\"A_q0_n\":"<<q0[z.aqi].n<<",\"B_q0_n\":"<<q0[z.bqi].n<<",\"A_q0_x\":\""<<q0[z.aqi].x<<"\",\"B_q0_x\":\""<<q0[z.bqi].x<<"\",\"A_q0_x2\":\""<<s128(q0[z.aqi].x2)<<"\",\"B_q0_x2\":\""<<s128(q0[z.bqi].x2)<<"\"}";}
 std::cout<<"]}\n";
}
