#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <map>
#include <vector>
#include <numeric>
using u64=uint64_t;using u128=unsigned __int128;
static constexpr long long B=2331, L=99891792000LL;
static const int PRIMES[]={2,3,5,7,11,13,17};
bool smooth(int n){for(int p:PRIMES)while(n%p==0)n/=p;return n==1;}
std::string str(u128 a){if(!a)return "0";std::string s;while(a){s.push_back(char('0'+a%10));a/=10;}reverse(s.begin(),s.end());return s;}
struct Atom{int q,r,a,w;u64 x;u128 x2,x3;};
struct Partial{int mass,n;u64 x;u128 x2,x3;u64 mask;};
struct Row{u64 x;u128 x2;u64 vmask,qmask;uint32_t index;uint16_t n;uint16_t qindex;};
std::vector<Atom> atoms;
std::vector<Partial> vertical, q0s;
void gen_vertical(int at,int rem,int mass,int n,u64 x,u128 x2,u128 x3,u64 mask){
 if(!rem){vertical.push_back({mass,n,x,x2,x3,mask});return;}
 for(int i=at;i<(int)atoms.size();i++){
  const auto &a=atoms[i];if(a.q>rem||mass+a.w>B)continue;
  gen_vertical(i,rem-a.q,mass+a.w,n+1,x+a.x,x2+a.x2,x3+a.x3,mask|(1ULL<<i));
 }
}
std::vector<int> qJ;
void gen_q0(int at,int mass,int n,u64 x,u128 x2,u128 x3,u64 mask){
 if(at==(int)qJ.size()){q0s.push_back({mass,n,x,x2,x3,mask});return;}
 int j=qJ[at],w=17*j-1;u64 v=L/j;u128 v2=u128(v)*v,v3=v2*v;
 for(int k=0;mass+k*w<=565;k++)gen_q0(at+1,mass+k*w,n+k,x+k*v,x2+k*v2,x3+k*v3,mask|(k?(1ULL<<(j-1)):0));
}
int main(){
 for(int q=1;q<=7;q++)for(int r=1;r<=16;r++){
  int a=17*q+r;if(!smooth(a))continue;u64 x=L/a;atoms.push_back({q,r,a,17*a-1,x,u128(x)*x,u128(x)*x*x});
 }
 assert(atoms.size()==60);
 for(int j=1;j<=16;j++)if(smooth(j))qJ.push_back(j);
 gen_vertical(0,6,0,0,0,0,0,0);
 gen_q0(0,0,0,0,0,0,0);
 assert(vertical.size()==11105);
 std::stable_sort(q0s.begin(),q0s.end(),[](const Partial&a,const Partial&b){return a.mass<b.mass;});
 std::vector<Row> rows;rows.reserve(7050875);
 for(uint32_t i=0;i<vertical.size();i++){
  const auto&v=vertical[i];
  for(uint32_t j=0;j<q0s.size();j++){
   const auto&q=q0s[j];if(v.mass+q.mass>B)break;
   rows.push_back({v.x+q.x,v.x2+q.x2,v.mask,q.mask,i,uint16_t(v.n+q.n),uint16_t(j)});
  }
 }
 std::cerr<<"catalog="<<atoms.size()<<" vertical="<<vertical.size()<<" q0="<<q0s.size()<<" full="<<rows.size()<<" sizeofRow="<<sizeof(Row)<<"\n";
 
 std::sort(rows.begin(),rows.end(),[](const Row&a,const Row&b){
  if(a.n!=b.n)return a.n<b.n;
  if(a.x!=b.x)return a.x<b.x;
  if(a.x2!=b.x2)return a.x2<b.x2;
  if(a.vmask!=b.vmask)return a.vmask<b.vmask;
  return a.qmask<b.qmask;
 });
 u64 groups=0, collGroups=0, h012Pairs=0, disjointPairs=0, h013Pairs=0,maxGroup=0;
 std::vector<std::pair<size_t,size_t>> sample;
 for(size_t start=0;start<rows.size();){
  size_t end=start+1;
  while(end<rows.size()&& rows[start].n==rows[end].n && rows[start].x==rows[end].x && rows[start].x2==rows[end].x2)end++;
  groups++;u64 len=end-start;maxGroup=std::max(maxGroup,len);
  if(len>1){collGroups++;h012Pairs+=len*(len-1)/2;
   for(size_t i=start;i<end;i++)for(size_t j=i+1;j<end;j++){
    const Row&a=rows[i],&b=rows[j];
    if((a.vmask&b.vmask)||(a.qmask&b.qmask))continue;
    disjointPairs++;
    u128 ax3=vertical[a.index].x3+q0s[a.qindex].x3;
    u128 bx3=vertical[b.index].x3+q0s[b.qindex].x3;
    if(ax3==bx3)h013Pairs++;if(sample.size()<12)sample.push_back({i,j});
   }
  }
  start=end;
 }
 std::cout<<"{\"schema\":\"T6_P17_Q12_SPLIT6_6_H012_SCAN_V1\",\"atomic_vertical_catalog\":"<<atoms.size()
          <<",\"vertical_rosters_each_side\":"<<vertical.size()<<",\"q0_multisets\":"<<q0s.size()
          <<",\"full_side_configurations\":"<<rows.size()<<",\"distinct_H012_signatures\":"<<groups
          <<",\"H012_colliding_signature_groups\":"<<collGroups<<",\"H012_unordered_pairs_before_disjoint\":"<<h012Pairs
          <<",\"H012_pairs_after_disjoint\":"<<disjointPairs<<",\"H013_pairs_after_disjoint\":"<<h013Pairs
          <<",\"max_signature_group_size\":"<<maxGroup<<",\"sample_H012\":[";
 for(size_t k=0;k<sample.size();k++){
  if(k)std::cout<<",";auto [i,j]=sample[k];const Row&a=rows[i],&b=rows[j];
  std::cout<<"{\"A\":{\"vindex\":"<<a.index<<",\"qindex\":"<<a.qindex<<",\"vmask\":"<<a.vmask<<",\"qmask\":"<<a.qmask<<"},\"B\":{\"vindex\":"<<b.index<<",\"qindex\":"<<b.qindex<<",\"vmask\":"<<b.vmask<<",\"qmask\":"<<b.qmask<<"}}";
 }
 std::cout<<"]}\n";
}