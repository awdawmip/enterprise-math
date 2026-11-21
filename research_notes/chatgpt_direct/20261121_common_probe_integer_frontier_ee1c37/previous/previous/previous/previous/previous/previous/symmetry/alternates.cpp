// Test the two-minimum-core profiles at 8712 and 8715.
// Nine size-nine blocks each have a single deficient plane in each coordinate.
// A cost-747 ten-block has exactly one excess plane and one deficient plane.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using Mask=__uint128_t;
using Word=std::uint64_t;
const Mask FULL=(Mask(1)<<125)-1;
int first(Mask m){return Word(m)?__builtin_ctzll(Word(m)):64+__builtin_ctzll(Word(m>>64));}
int size(Mask m){return __builtin_popcountll(Word(m))+__builtin_popcountll(Word(m>>64));}
struct Row{Mask bits;int type;std::array<signed char,15> defect{};};
std::vector<Row> inventory;
std::vector<Mask> path;
std::uint64_t nodes;
Mask planes[15]{};
bool solve(Mask free,int n9,int good,int uneven,const std::vector<int>& prior) {
 ++nodes;
 if(!free)return true;
 const int left=n9+good+uneven;
 int deficit[15];bool restricts=false;
 for(int j=0;j<15;j++) {
   int d=2*left-size(planes[j]&free);
   if(d < -uneven || d > n9+uneven)return false;
   deficit[j]=d;
 }
 for(int j=0;j<15;j++)if(deficit[j]<=1-uneven||deficit[j]>=n9+uneven-1)restricts=true;
 Mask cover=0;
 int pop[125]{},qty[3]{};
 std::vector<int> legal;legal.reserve(prior.size());
 for(int i:prior){
   const Row&r=inventory[i];if(r.bits&~free)continue;
   const int t=r.type;
   if((t==0&&!n9)||(t==1&&!good)||(t==2&&!uneven))continue;
   const int a=n9-(t==0),b=uneven-(t==2);
   bool viable=true;
   if(restricts)for(int j=0;j<15;j++){const int d=deficit[j]-r.defect[j];if(d < -b || d>a+b){viable=false;break;}}
   if(!viable)continue;
   ++qty[t];legal.push_back(i);cover|=r.bits;
 }
 if(cover!=free || qty[0]<n9||qty[1]<good||qty[2]<uneven)return false;
 if(left==1){path.push_back(inventory[legal[0]].bits);return true;}
 int which=-1,bytype=-1,minimum=1e8;
 for(int i:legal)for(Mask v=inventory[i].bits;v;v&=v-1)++pop[first(v)];
 for(Mask v=free;v;v&=v-1){int x=first(v);if(pop[x]<minimum){which=x;minimum=pop[x];}}
 const int quota[3]={n9,good,uneven};
 for(int t=0;t<3;t++)if(quota[t]==1&&qty[t]<minimum){bytype=t;minimum=qty[t];}
 for(int i:legal){
   const auto&r=inventory[i];int t=r.type;
   if(bytype>=0?t!=bytype:!(r.bits>>which&1))continue;
   path.push_back(r.bits);
   if(solve(free^r.bits,n9-(t==0),good-(t==1),uneven-(t==2),legal))return true;
   path.pop_back();
 }
 return false;
}
int main(int argc,char**argv){
 std::ifstream data(argv[1]),pairs(argv[2]);int flank=std::stoi(argv[3]),start=std::stoi(argv[4]),stride=std::stoi(argv[5]);
 int n,s,c;
 for(int i=0;i<125;i++)for(int t=0;t<3;t++)planes[t*5+(t==0?i/25:t==1?i/5%5:i%5)]|=Mask(1)<<i;
 while(data>>s>>c>>n)for(int j=0;j<n;j++){
  Word lo,hi;int dummy;data>>lo>>hi>>dummy;
  if(c!=557&&c!=744&&c!=747)continue;
  Row r{Mask(hi)<<64|lo,c==557?0:c==744?1:2};
  std::array<int,3> cc{};
  for(int k=0;k<15;k++){int d=2-size(r.bits&planes[k]);if(d< -1||d>1)return 4;r.defect[k]=d;cc[d+1]++;}
  std::array<int,3> expected=r.type==0?std::array<int,3>{0,12,3}:r.type==1?std::array<int,3>{0,15,0}:std::array<int,3>{1,13,1};if(cc!=expected)return 5;
  inventory.push_back(r);
 }
 int id=0;Word a,b,c1,d;
 while(pairs>>a>>b>>c1>>d){
  if((id++)%stride!=start)continue;
  Mask anchor=Mask(b)<<64|a,other=Mask(d)<<64|c1;Mask free=FULL^anchor^other;
  path={anchor,other};std::vector<int> prior;
  for(int i=0;i<inventory.size();i++)if(!(inventory[i].bits&~free))prior.push_back(i);
  nodes=0;bool found=solve(free,9,2-flank,flank,prior);
  std::cout<<id-1<<" "<<flank<<" "<<nodes<<" "<<found<<std::endl;
  if(found){std::ofstream cert("hit_"+std::to_string(flank)+"_"+std::to_string(id-1)+".txt");
   for(Mask r:path){for(;r;r&=r-1)cert<<first(r)<<" ";cert<<"\n";}return 0;}
 }
}
