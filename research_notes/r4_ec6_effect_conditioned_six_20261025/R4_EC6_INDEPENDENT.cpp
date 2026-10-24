#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <tuple>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using S=std::tuple<int,int,int,int>;
S step(S s,int bit){
 auto [q,r,e,k]=s;
 const int qp0[]={2,0,1},qp1[]={2,0,2};
 const int eta0[]={-1,-1,1},eta1[]={1,1,1};
 const int b0[]={-1,-1,1},b1[]={-1,-1,-1};
 const int r0[]={1,2,2},r1[]={0,0,2};
 int q1=(bit?qp1:qp0)[q],eta=(bit?eta1:eta0)[q],b=(bit?b1:b0)[q];
 return {q1,(bit?r1:r0)[r],e*eta,eta*k+b};
}
int main(){
 std::map<S,cpp_int> H;H[{0,0,1,0}]=1;
 for(int n=0;n<=40;n++){
  cpp_int total=0;for(auto const& [s,c]:H)total+=c;
  assert(total==(cpp_int(1)<<n));
  if(n<=12){
   std::map<S,cpp_int> brute;
   for(unsigned bits=0;bits<(1u<<n);++bits){
    S s={0,0,1,0};
    for(int j=n-1;j>=0;--j)s=step(s,(bits>>j)&1);
    ++brute[s];
   }
   assert(brute==H);
  }
  if(n==7){
   assert(H.at({2,0,-1,1})==1 && H.at({2,1,-1,1})==1);
   std::map<std::pair<int,int>,cpp_int> channels;
   for(auto const& [s,c]:H){
    auto [q,r,e,k]=s;if(e==1&&k==-3)channels[{q,int(r==2)}]+=c;
   }
   assert(channels.size()==6);
   assert(channels.at({0,0})==2 && channels.at({0,1})==2);
   assert(channels.at({1,0})==3 && channels.at({1,1})==1);
   assert(channels.at({2,0})==1 && channels.at({2,1})==9);
  }
  if(n>=10){
   std::map<std::tuple<int,int>,std::array<cpp_int,2>> fibers;
   for(auto const& [s,c]:H){
    auto [q,r,e,k]=s;
    if(q==2&&r!=2)fibers[{e,k}][r]+=c;
   }
   int a=0,b=0,m=0;
   for(auto const& [g,ar]:fibers){
    if(ar[0]>0&&ar[1]>0)++m;
    else if(ar[0]>0)++a;
    else if(ar[1]>0)++b;
   }
   assert(m==2*(n-6) && a==8 && b==2);
  }
  if(n<40){
   std::map<S,cpp_int> next;
   for(auto const& [s,c]:H){next[step(s,0)]+=c;next[step(s,1)]+=c;}
   H.swap(next);
  }
 }
 std::cout<<"PASS: independent exact integer n<=40, brute n<=12, mixing law\n";
}
