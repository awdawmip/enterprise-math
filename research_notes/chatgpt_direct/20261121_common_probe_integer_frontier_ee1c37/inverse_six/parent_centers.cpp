#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using M=__uint128_t;
int pc(M a){return std::popcount(uint64_t(a))+std::popcount(uint64_t(a>>64));}
int main(int argc,char**argv){
 if(argc<2)return 2;
 std::ofstream families(argc>2?argv[2]:"/dev/null");
 std::ifstream in(argv[1]);
 std::array<std::array<std::array<std::vector<M>,5>,5>,5> by;
 std::array<M,15> fibers{};
 for(int x=0;x<125;x++){fibers[x/25]|=M(1)<<x;fibers[5+x/5%5]|=M(1)<<x;fibers[10+x%5]|=M(1)<<x;}
 for(int k=0;k<250;k++){
  uint64_t lo,hi;in>>lo>>hi;M m=M(lo)|(M(hi)<<64);std::array<int,3> c{};
  for(int j=0;j<3;j++)for(int a=0;a<5;a++)if(pc(m&fibers[5*j+a])==5)c[j]=a;
  by[c[0]][c[1]][c[2]].push_back(m);
 }
 for(auto&u:by)for(auto&v:u)for(auto&w:v){if(w.size()!=2)return 3;std::sort(w.begin(),w.end());}
 std::vector<std::array<int,5>> sequence;
 for(int value=0;value<3125;value++){
  int q=value,seen=1;std::array<int,5> a;
  for(int j=0;j<5;j++){a[j]=q%5;q/=5;seen|=1<<a[j];}
  if(seen==31)sequence.push_back(a);
 }
 if(sequence.size()!=360)return 4;
 M anchor=by[0][0][0][0];
 uint64_t total=0,distinct=0,large=0,capacity=0;std::map<int,uint64_t> unionHist,capHist;std::array<uint64_t,16> deficits{};
 std::array<M,6> witness{};bool got=false;
 for(auto y:sequence)for(auto z:sequence){
  std::array<std::array<M,2>,5> choices;
  for(int j=0;j<5;j++)choices[j]={by[j][y[j]][z[j]][0],by[j][y[j]][z[j]][1]};
  for(int bits=0;bits<32;bits++){
   total++;std::array<M,6> ms;ms[0]=anchor;M u=anchor;
   for(int j=0;j<5;j++){ms[j+1]=choices[j][(bits>>j)&1];u|=ms[j+1];}
   if(ms[1]==anchor)continue;
   distinct++;int n=pc(u);unionHist[n]++;
   if(n<71)continue;
   large++;int deficit=0;
   for(auto f:fibers)deficit+=std::max(13-pc(u&f),0);
   if(deficit<16)deficits[deficit]++;
   if(deficit)continue;
   capacity++;capHist[n]++;for(auto m:ms)families<<uint64_t(m)<<" "<<uint64_t(m>>64)<<" ";families<<"\n";if(!got){witness=ms;got=true;}
  }
 }
 std::cout<<"{\"normalized_candidates\":"<<total<<",\"distinct_parents\":"<<distinct<<",\"union_at_least_71\":"<<large<<",\"all_fiber_capacity\":"<<capacity<<",\"capacity_union_histogram\":[";
 bool first=true;for(auto[n,k]:capHist){if(!first)std::cout<<",";first=false;std::cout<<"["<<n<<","<<k<<"]";}
 std::cout<<"],\"all_union_histogram\":[";first=true;for(auto[n,k]:unionHist){if(!first)std::cout<<",";first=false;std::cout<<"["<<n<<","<<k<<"]";}
 std::cout<<"],\"first_witness_limbs\":[";first=true;if(got)for(auto m:witness){if(!first)std::cout<<",";first=false;std::cout<<"["<<uint64_t(m)<<","<<uint64_t(m>>64)<<"]";}
 std::cout<<"]}\n";
}
