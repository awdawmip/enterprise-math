#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <vector>
using M=__uint128_t;
const M FULL=(M(1)<<125)-1;
int pc(M x){return std::popcount(uint64_t(x))+std::popcount(uint64_t(x>>64));}
int at(M x){return uint64_t(x)?std::countr_zero(uint64_t(x)):64+std::countr_zero(uint64_t(x>>64));}
struct Class{M mask;int size,cost;};
std::map<M,std::vector<Class>> children;
std::array<M,15> fibers{};
uint64_t pack_nodes=0,proper_nodes=0;
uint64_t proper_union_rejects=0,proper_size_rejects=0;
std::vector<Class> embedded_witness;
std::vector<M> proper_witness;

bool pack(std::vector<M> parents,M free,M original,int n11,int n12,int leftover){
 ++pack_nodes;
 if(parents.empty()){
  if(n11||n12||pc(free)!=leftover)return false;
  M used=original^free;
  for(M h:fibers)if(pc(used&h)<13)return false;
  return true;
 }
 size_t choice=0;std::vector<Class> best;
 for(size_t i=0;i<parents.size();++i){
  std::vector<Class> options;
  for(Class c:children[parents[i]])if((c.mask&free)==c.mask&&
    ((c.size==11&&c.cost==944&&n11)||(c.size==12&&c.cost==1116&&n12)))options.push_back(c);
  if(options.empty())return false;
  if(i==0||options.size()<best.size()){choice=i;best=std::move(options);}
 }
 parents.erase(parents.begin()+choice);
 for(Class c:best)if(pack(parents,free^c.mask,original,n11-(c.size==11),n12-(c.size==12),leftover)){
  embedded_witness.push_back(c);return true;
 }
 return false;
}

bool proper(M free,int left,const std::vector<M>&pool){
 ++proper_nodes;
 if(pc(free)!=9*left){++proper_size_rejects;return false;}
 if(left==0)return free==0;
 std::vector<M> options;M covered=0;
 std::array<int,125> frequency{};
 for(M c:pool)if((c&free)==c){
  options.push_back(c);covered|=c;
  for(M x=c;x;x&=x-1)++frequency[at(x)];
 }
 if(covered!=free){++proper_union_rejects;return false;}
 if(options.size()<size_t(left))throw std::runtime_error("nine-point union exceeds its size bound");
 if(left==1){proper_witness.push_back(free);return true;}
 int point=-1,minimum=std::numeric_limits<int>::max();
 for(M x=free;x;x&=x-1)if(frequency[at(x)]<minimum){point=at(x);minimum=frequency[point];}
 for(M c:options)if((c>>point)&1)if(proper(free^c,left-1,options)){
  proper_witness.push_back(c);return true;
 }
 return false;
}

int main(int argc,char**argv){
 if(argc!=4)return 2;
 for(int x=0;x<125;++x){fibers[x/25]|=M(1)<<x;fibers[5+x/5%5]|=M(1)<<x;fibers[10+x%5]|=M(1)<<x;}
 uint64_t a,b,c,d;int size,cost;
 std::ifstream in(argv[1]);
 while(in>>a>>b>>size>>cost>>c>>d)children[M(a)|(M(b)<<64)].push_back({M(c)|(M(d)<<64),size,cost});
 if(children.size()!=250)return 3;
 std::vector<std::vector<M>> families;
 std::ifstream fs(argv[2]);
 while(fs>>a>>b){std::vector<M> row{M(a)|(M(b)<<64)};for(int i=1;i<6;++i){fs>>a>>b;row.push_back(M(a)|(M(b)<<64));}families.push_back(row);}
 if(families.size()!=4304)return 4;
 std::vector<M> nine;std::ifstream ns(argv[3]);
 while(ns>>a>>b){M cls=M(a)|(M(b)<<64);if(pc(cls)!=9)return 7;nine.push_back(cls);}
 if(nine.size()!=24000)return 5;
 uint64_t point_pass=0,pack_pass=0,cross_candidates=0,proper_attempts=0,proper_covers=0,
   embedding_attempts=0,embedding_cache_skips=0,prepack_nodes=0,reused_regions=0;
 std::set<std::pair<M,M>> rejected_regions;
 std::map<int,uint64_t> union_hist;
 bool found=false;M found_union=0,found_inner=0;
 for(auto parents:families){
  M u=0,z=0;
  for(M m:parents){
   u|=m;int center[3]{};
   for(int j=0;j<3;++j)for(int value=0;value<5;++value)if(pc(m&fibers[5*j+value])==5)center[j]=value;
   z|=M(1)<<(25*center[0]+5*center[1]+center[2]);
  }
  if(pc(z)!=6)continue; // Every11/944 and12/1116 class retains its mother's center.
  int allowance=pc(u)-71,minimum=10;M covered=0;
  for(M cls:nine)if(!(cls&z)){
   int overlap=pc(cls&u);minimum=std::min(minimum,overlap);
   if(overlap<=allowance)covered|=cls;
  }
  M outside=FULL^u;
  if(6*minimum>allowance||(outside&covered)!=outside)continue;
  ++point_pass;embedded_witness.clear();auto before=pack_nodes;
  bool feasible=pack(parents,u,u,1,5,allowance);prepack_nodes+=pack_nodes-before;
  if(!feasible)continue;
  ++pack_pass;++union_hist[pc(u)];
  if(pc(u)!=72)return 6; // Verified consequence of the complete finite parent/packing stage.
  std::vector<M> pure,cross;
  for(M cls:nine)if(!(cls&z)){
   int overlap=pc(cls&u);
   if(overlap==0)pure.push_back(cls);
   if(overlap==1)cross.push_back(cls);
  }
  cross_candidates+=cross.size();
  if(rejected_regions.count({u,z})){++reused_regions;continue;}
  auto previous_proper_covers=proper_covers;
  std::array<bool,125> impossible_inner{};
  for(M cls:cross){
   M inner=cls&u;int p=at(inner);
   if(impossible_inner[p]){++embedding_cache_skips;continue;}
   ++proper_attempts;proper_witness.clear();
   if(!proper(outside&~cls,5,pure))continue;
   ++proper_covers;++embedding_attempts;embedded_witness.clear();
   if(pack(parents,u^inner,u^inner,1,5,0)){
    proper_witness.push_back(cls);found=true;found_union=u;found_inner=inner;break;
   }
   impossible_inner[p]=true;
  }
  if(found)break;
  // This reuse is allowed only when no proper cover existed at all;
  // failure of a particular mother's embedded packing would not suffice.
  if(proper_covers==previous_proper_covers)rejected_regions.insert({u,z});
 }
 std::cout<<"{\"profile\":\"9-557-6_11-944-1_12-1116-5\",\"parent_families\":"<<families.size()
  <<",\"point_filter_pass\":"<<point_pass<<",\"embedded_feasible_families\":"<<pack_pass
  <<",\"cross_candidates\":"<<cross_candidates<<",\"proper_attempts\":"<<proper_attempts
  <<",\"proper_cover_nodes\":"<<proper_nodes<<",\"proper_covers\":"<<proper_covers
  <<",\"embedding_attempts\":"<<embedding_attempts<<",\"embedding_cache_skips\":"<<embedding_cache_skips
  <<",\"different_rejected_regions\":"<<rejected_regions.size()<<",\"reused_parent_regions\":"<<reused_regions
  <<",\"proper_union_rejects\":"<<proper_union_rejects<<",\"proper_size_rejects\":"<<proper_size_rejects
  <<",\"embedding_pack_nodes\":"<<pack_nodes<<",\"preliminary_pack_nodes\":"<<prepack_nodes
  <<",\"found\":"<<int(found)<<",\"union_histogram\":[";
 bool comma=false;for(auto [n,k]:union_hist){if(comma)std::cout<<",";comma=true;std::cout<<"["<<n<<","<<k<<"]";}
 std::cout<<"]";
 if(found){
  std::cout<<",\"witness\":[";comma=false;
  for(auto cls:embedded_witness){if(comma)std::cout<<",";comma=true;std::cout<<"["<<cls.size<<","<<cls.cost<<","<<uint64_t(cls.mask)<<","<<uint64_t(cls.mask>>64)<<"]";}
  for(M cls:proper_witness){if(comma)std::cout<<",";comma=true;std::cout<<"[9,557,"<<uint64_t(cls)<<","<<uint64_t(cls>>64)<<"]";}
  std::cout<<"]";
 }
 std::cout<<"}"<<std::endl;
}
