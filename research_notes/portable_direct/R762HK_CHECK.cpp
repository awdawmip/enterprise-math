// R762HK: fixed candidate Port model; exact sign/fibre/flip-block checks.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra R762HK_CHECK.cpp -o check && ./check
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using V = std::array<int,6>;
struct State { V residual; bool prev; bool operator<(const State& b) const {
    if (residual != b.residual) return residual < b.residual;
    return prev < b.prev;
} };
int main() {
 const std::vector<std::string> ports={
 "01","15","12","25","24","04","05","03","04","24","23","25","35","05","01"};
 constexpr int m=14;
 int mask[m+1]; for(int t=0;t<=m;t++) {
   mask[t]=(1<<(ports[t][0]-'0'))|(1<<(ports[t][1]-'0'));
 }
 assert(mask[0]==mask[m]);
 int h[m]; V d{};
 for(int t=0;t<m;t++) {
   assert(__builtin_popcount((unsigned)(mask[t]&mask[t+1]))==1);
   h[t]=mask[t]|mask[t+1];
   assert(__builtin_popcount((unsigned)h[t])==3);
   for(int j=0;j<6;j++) d[j]+=(h[t]>>j)&1;
 }
 assert((d==V{8,4,8,6,6,10}));
 for(int a:d) assert(a%2==0);
 V prefix[m+1]{};
 for(int t=0;t<m;t++) for(int j=0;j<6;j++)
   prefix[t+1][j]=prefix[t][j]+(t%2?-1:1)*((h[t]>>j)&1);
 assert((prefix[m]==V{2,0,0,0,-2,0}));
 int intervals=0, oneblock=0;
 for(int a=0;a<m;a++) for(int b=a+1;b<=m;b++) {
   intervals++;
   bool ok=true;
   for(int j=0;j<6;j++) if(2*(prefix[b][j]-prefix[a][j])!=prefix[m][j]) ok=false;
   if(ok) oneblock++;
 }
 assert(intervals==105 && oneblock==0);
 std::array<unsigned long long,m+1> brute{};
 for(unsigned bits=0;bits<(1u<<m);bits++) {
   V sum{}; int blocks=0;
   for(int t=0;t<m;t++) {
     const bool flipped=(bits>>t)&1u;
     if(flipped && (t==0 || !((bits>>(t-1))&1u)))blocks++;
     int sign=(t%2?-1:1)*(flipped?-1:1);
     for(int j=0;j<6;j++)sum[j]+=sign*((h[t]>>j)&1);
   }
   if(sum==V{})brute[blocks]++;
 }
 assert(brute[0]==0 && brute[1]==0 && brute[2]==20 && brute[3]==46 && brute[4]==36 && brute[5]==2);
 for(int k=6;k<=m;k++)assert(brute[k]==0);
 // Independent positive-coefficient transfer: group algebra in x_0..x_5,
 // count all paths by exact selected alternating-displacement and flip-block count.
 using Dist=std::array<unsigned long long,m+1>;
 std::map<State,Dist> curr,next;
 curr[State{V{},false}][0]=1;
 for(int t=0;t<m;t++) {
   next.clear();
   for(const auto& kv:curr) for(int b=0;b<=1;b++) {
     V v=kv.first.residual;
     for(int j=0;j<6;j++)v[j]+=b*(t%2?-1:1)*((h[t]>>j)&1);
     auto &counts=next[State{v,(bool)b}];
     int increment=(b && !kv.first.prev)?1:0;
     for(int k=0;k+increment<=m;k++) counts[k+increment]+=kv.second[k];
   }
   curr.swap(next);
 }
 Dist transfer{};
 V goal{};for(int j=0;j<6;j++)goal[j]=prefix[m][j]/2;
 for(int p=0;p<=1;p++) {
   auto it=curr.find(State{goal,(bool)p});
   if(it!=curr.end()) for(int k=0;k<=m;k++)transfer[k]+=it->second[k];
 }
 assert(transfer==brute);
 // Explicit two-block witness: bitmask=216, intervals [3,5), [6,8).
 const unsigned w=216; assert((w&(1u<<3))&&(w&(1u<<4))&&(w&(1u<<6))&&(w&(1u<<7)));
 V zero{}; for(int t=0;t<m;t++) {
   int eps=(t%2?-1:1)*((w>>t&1u)?-1:1);
   for(int j=0;j<6;j++)zero[j]+=eps*((h[t]>>j)&1);
 }
 assert(zero==V{});
 std::cout<<"{\"model\":\"signed_composite_port_candidate\",\"m\":14,\"parity_incidence\":[8,4,8,6,6,10],"
          <<"\"alternating_residual\":[2,0,0,0,-2,0],\"one_interval_candidates\":105,"
          <<"\"one_interval_solutions\":0,\"signed_zero_total\":104,"
          <<"\"flip_block_histogram\":{\"2\":20,\"3\":46,\"4\":36,\"5\":2},"
          <<"\"minimal_flip_blocks\":2,\"example_flip_mask\":216,"
          <<"\"verification\":\"PASS_BRUTE_FORCE_AND_INDEPENDENT_TRANSFER\"}\n";
}