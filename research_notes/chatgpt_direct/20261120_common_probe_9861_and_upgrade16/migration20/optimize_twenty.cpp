#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using Mask=__uint128_t;
struct Row {Mask mask=0; std::vector<int> points;};
std::vector<Row> five,six;
std::vector<Mask> old,sixes,sevens,answer;
std::vector<Mask> local_old;
Mask region_mask=0;
std::uint64_t nodes=0,regions=0,solutions=0;
int best=126;
int first(Mask m) {auto lo=(std::uint64_t)m; return lo?__builtin_ctzll(lo):64+__builtin_ctzll((std::uint64_t)(m>>64));}
void print(Mask m){bool start=true;while(m){int x=first(m);m&=m-1;if(!start)std::cout<<",";start=false;std::cout<<x;}}
bool cover(Mask rem,const std::vector<int>& candidates,std::vector<Mask>& selected) {
 ++nodes;
 if(!rem) {
  ++solutions;
  int n=selected.size();std::vector<int> dp(1<<n,-1000);dp[0]=0;
  for(int used=0;used<(1<<n);used++){
   int i=__builtin_popcount((unsigned)used);
   if(i>=(int)local_old.size()||dp[used]<0)continue;
   for(int j=0;j<n;j++)if(!(used>>j&1)){
    Mask meet=local_old[i]&selected[j];
    int w=__builtin_popcountll((std::uint64_t)meet)+__builtin_popcountll((std::uint64_t)(meet>>64));
    dp[used|(1<<j)]=std::max(dp[used|(1<<j)],dp[used]+w);
   }
  }
  int kept=*std::max_element(dp.begin(),dp.end());
  int size=__builtin_popcountll((std::uint64_t)region_mask)+__builtin_popcountll((std::uint64_t)(region_mask>>64));
  int moved=size-kept;
  if(moved<best){
   best=moved;answer=selected;
   for(Mask r:old)if(!(r&region_mask))answer.push_back(r);
   std::cout<<"{\"moved\":"<<moved<<",\"groups\":[";
   for(int j=0;j<(int)answer.size();j++){if(j)std::cout<<",";std::cout<<"[";print(answer[j]);std::cout<<"]";}
   std::cout<<"],\"nodes\":"<<nodes<<",\"regions\":"<<regions<<",\"solutions\":"<<solutions<<"}"<<std::endl;
  }
  return false;
 }
 std::array<int,125> count{};
 Mask possible=0;
 for(int i:candidates){possible|=six[i].mask;for(int x:six[i].points)++count[x];}
 if(possible!=rem)return false;
 int p=-1;
 for(Mask m=rem;m;m&=m-1){int x=first(m);if(p<0||count[x]<count[p])p=x;}
 for(int i:candidates)if((six[i].mask>>p)&1){
  std::vector<int> next;
  for(int j:candidates)if(!(six[j].mask&six[i].mask))next.push_back(j);
  selected.push_back(six[i].mask);
  if(cover(rem^six[i].mask,next,selected))return true;
  selected.pop_back();
 }
 return false;
}
bool region(Mask m){
 ++regions;
 region_mask=m;local_old.clear();for(Mask r:old)if(r&m)local_old.push_back(r);
 std::vector<int> available;
 for(int i=0;i<(int)six.size();i++)if((six[i].mask&m)==six[i].mask)available.push_back(i);
 for(const auto &f:five)if((f.mask&m)==f.mask){
  std::vector<int> rows;
  for(int i:available)if(!(six[i].mask&f.mask))rows.push_back(i);
  std::vector<Mask> chosen{f.mask};
  if(cover(m^f.mask,rows,chosen)){
   for(Mask r:old)if(!(r&m))answer.push_back(r);
   std::cout<<"{\"groups\":[";
   for(int j=0;j<(int)answer.size();j++){if(j)std::cout<<",";std::cout<<"[";print(answer[j]);std::cout<<"]";}
   std::cout<<"],\"nodes\":"<<nodes<<",\"regions\":"<<regions<<"}"<<std::endl;
   return true;
  }
 }
 return false;
}
bool choose(int start,int need,Mask m){if(!need)return region(m);for(int i=start;i+need<=(int)sixes.size();i++)if(choose(i+1,need-1,m|sixes[i]))return true;return false;}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 std::ifstream in(argv[1]);
 Mask base=0;
 for(int k=0;k<20;k++){int s,x;in>>s;Mask m=0;for(int j=0;j<s;j++){in>>x;m|=Mask(1)<<x;}old.push_back(m);if(s==7){sevens.push_back(m);base|=m;}else sixes.push_back(m);}
 for(int s:{5,6}){int n;in>>n;auto &bank=(s==5?five:six);for(int k=0;k<n;k++){Row r;for(int j=0;j<s;j++){int x;in>>x;r.mask|=Mask(1)<<x;r.points.push_back(x);}bank.push_back(r);}}
 if(!in)return 3;
 for(int extra=std::stoi(argv[2]);extra<std::stoi(argv[3]);extra++){
  if(choose(0,extra,base))return 0;
  std::cout<<"{\"extra_sixes_exhausted\":"<<extra<<",\"nodes\":"<<nodes<<",\"regions\":"<<regions<<",\"solutions\":"<<solutions<<",\"best_moved\":"<<best<<"}"<<std::endl;
 }
}
