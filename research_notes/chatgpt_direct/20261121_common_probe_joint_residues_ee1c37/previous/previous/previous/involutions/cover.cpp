#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <set>
using M=__uint128_t;using U=uint64_t;
const M All=(M(1)<<125)-1;
constexpr int inf=99999;
int first(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}
int pop(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
using Map=std::array<int,125>;
M image(M m,const Map&g){M u=0;for(;m;m&=m-1)u|=M(1)<<g[first(m)];return u;}
int add(int i,int j){return 25*((i/25+j/25)%5)+5*((i/5%5+j/5%5)%5)+(i%5+j%5)%5;}
struct Row{M m,seed;int r,s,h,c;};
struct Type{int r,s,h,c;};
Map perm;
M plane=0;
std::set<M>anchors;
int d[13][7][126][26],cap,basef,baseb,allh;
int lower(int f,int b,int n,int h){if(std::min({f,b,n,h})<0 || n>13*(f+2*b)||n<h)return inf;return d[f][b][n][h];}
std::vector<Row>rows;std::vector<int>path;
long long nodes[13]{},sol=0;
std::ofstream out;
bool testrow(const Row&x,M free,int f,int b,int n,int h,int budget){
 return !(x.m&~free) && x.c+lower(f-(x.r==1),b-(x.r==2),n-x.s*x.r,h-x.h)<=budget;
}
void cover(M free,int f,int b,int n,int h,int spent,const std::vector<int>&pool){
 int depth=path.size();nodes[depth]++;
 int budget=cap-spent;
 if(lower(f,b,n,h)>budget)return;
 if(n==0){
  if(f||b)return;
  sol++;cap=spent-1;out<<"cost "<<spent<<"\n";
  for(int j:path){auto &r=rows[j];out<<r.r<<" "<<r.c<<" "<<U(r.seed)<<" "<<U(r.seed>>64)<<"\n";}out<<std::flush;
  return;
 }
 int count[125]{};M support=0;std::vector<int> candidates;
 for(int j:pool){auto&r=rows[j];if(!testrow(r,free,f,b,n,h,budget))continue;
  candidates.push_back(j);support|=r.m;for(M m=r.m;m;m&=m-1)++count[first(m)];
 }
 if(support!=free)return;
 int p=first(free);
 for(M a=free;a;a&=a-1){int k=first(a);if(count[k]<count[p])p=k;}
 for(int j:candidates){auto&r=rows[j];if(!(r.m&(M(1)<<p)))continue;
  path.push_back(j);cover(free^r.m,f-(r.r==1),b-(r.r==2),n-r.s*r.r,h-r.h,spent+r.c,candidates);path.pop_back();
 }
}
int main(int ac,char**av){
 if(ac!=9)return 2;
 std::ifstream mp(av[1]);for(int&i:perm)mp>>i;std::vector<Map>cent;
 Map l;while(mp>>l[0]){for(int i=1;i<125;i++)mp>>l[i];cent.push_back(l);}
 for(int i=0;i<125;i++)if(perm[i]==i)plane|=M(1)<<i;
 allh=pop(plane);baseb=std::stoi(av[4]);basef=12-2*baseb;cap=std::stoi(av[5]);out.open(av[6]);
 std::map<std::array<int,3>,int>prices;
 for(int r:{1,2}){
  std::ifstream in(av[1+r]);int s,h,c;U a,b;
  while(in>>s>>h>>c>>a>>b){
   auto key=std::array{r,s,h};if(!prices.count(key)||prices[key]>r*c)prices[key]=r*c;
   M seed=(M(b)<<64)|a;rows.push_back({r==1?seed:(seed|image(seed,perm)),seed,r,s,h,r*c});
  }
 }
 // Small/expensive discarded pairs only need their unrestricted relaxation here.
 int lower_cost[14]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
 if(allh==25 && perm[25]==100){int axis[14]={0,0,12,36,72,128,208,298,423,569,792,960,inf,inf};std::copy(axis,axis+14,lower_cost);}
 for(int s=1;s<=13;s++)prices[{2,s,0}]=2*lower_cost[s];
 for(int f=0;f<=basef;f++)for(int b=0;b<=baseb;b++)for(int n=0;n<=125;n++)for(int h=0;h<=allh;h++){
  auto&val=d[f][b][n][h];val=n||h||f||b?inf:0;
  for(auto&[t,c]:prices){auto[r,s,hc]=t;if((r==1 && f==0)||(r==2 && b==0))continue;val=std::min(val,c+lower(f-(r==1),b-(r==2),n-r*s,h-hc));}
 }
 std::vector<int>pool,root;
 std::sort(rows.begin(),rows.end(),[](auto&a,auto&b){return a.c<b.c;});
 for(int j=0;j<(int)rows.size();j++){
  auto &x=rows[j];if(!testrow(x,All,basef,baseb,125,allh,cap))continue;pool.push_back(j);
  if(x.r!=1 || !(x.m&1) || anchors.count(x.m))continue;
  for(auto&g:cent){M u=image(x.m,g);for(int t=0;t<125;t++)if(t==perm[t]){
   M v=0;for(M a=u;a;a&=a-1)v|=M(1)<<add(first(a),t);if(v&1)anchors.insert(v);
  }}
  root.push_back(j);
 }
 int lo=std::stoi(av[7]),hi=std::stoi(av[8]);
 std::cerr<<"labels "<<basef<<"+"<<2*baseb<<" pool "<<pool.size()<<" anchors "<<root.size()<<"\n";
 for(int i=lo;i<std::min(hi,(int)root.size());i++){
  int j=root[i];auto &x=rows[j];path={j};cover(All^x.m,basef-1,baseb,125-x.s,allh-x.h,x.c,pool);
  std::cout<<i<<" "<<cap<<" "<<sol;for(int z=1;z<13;z++)std::cout<<" "<<nodes[z];std::cout<<std::endl;
 }
}
