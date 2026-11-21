#ifndef NMAX
#define NMAX 4
#endif
constexpr int num_maxima=NMAX;
constexpr int npoints=125-13*num_maxima;
constexpr int nlabels=11-num_maxima;
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using M=__uint128_t;
using R=array<uint64_t,4>;
struct Row {M mask; int defect, cost;};
vector<Row> rows;
vector<int> chosen,winner;
M forbidden[npoints][npoints];
R differences[npoints][npoints];int W[npoints],peak,scale,cut,limit;long long visited,ncatalog;bool haswin;
int first(M m){return uint64_t(m)?__builtin_ctzll(uint64_t(m)):64+__builtin_ctzll(uint64_t(m>>64));}
int order_point[13];
void enumerate(M chosen,int size,M pool,const M *bans,const R*old,int cost,int weight){
 if(size){int d=peak+scale*cost-weight;
  if(d<0){cerr<<"understated price"<<endl;exit(2);}
  if(d<=cut)rows.push_back({chosen,d,cost});
 }
 if(size==12)return;
 while(pool){
  int i=first(pool);M bit=M(1)<<i;pool^=bit;M remaining=pool&~bans[i];M newer[npoints];
  for(M t=remaining;t;t&=t-1){int j=first(t);newer[j]=bans[j]|forbidden[i][j];}
  R updated[13],mine{};int v=cost;
  for(int j=0;j<size;j++)for(int k=0;k<4;k++){auto c=differences[i][order_point[j]][k];auto prior=old[j][k];v+=__builtin_popcountll(c&~prior);updated[j][k]=prior|c;mine[k]|=c;}
  for(auto c:mine)v+=__builtin_popcountll(c);
  order_point[size]=i;updated[size]=mine;
  enumerate(chosen|bit,size+1,remaining,newer,updated,v,weight+W[i]);
 }
}
bool search(M free,int left,int budget,int start){
 ++visited;if(limit&&visited>limit){cerr<<"node cap"<<endl;exit(4);}
 if(left==1){
  auto n=__builtin_popcountll(uint64_t(free))+__builtin_popcountll(uint64_t(free>>64));
  if(n>12||!n)return false;
  int total=0,w=0;for(M t=free;t;t&=t-1){int i=first(t);R a{};w+=W[i];
    for(M v=free;v;v&=v-1){int j=first(v);if(free&forbidden[i][j])return false;for(int k=0;k<4;k++)a[k]|=differences[i][j][k];}for(auto x:a)total+=__builtin_popcountll(x);}
  int d=peak+scale*total-w;
  if(d>budget||d<rows[start-1].defect||(d==rows[start-1].defect&&free<=rows[start-1].mask))return false;
  cerr<<"FOUND final "<<uint64_t(free)<<" "<<uint64_t(free>>64)<<endl;
  for(int i:chosen)cerr<<"ROW "<<uint64_t(rows[i].mask)<<" "<<uint64_t(rows[i].mask>>64)<<endl;
  return true;
 }
 for(int i=start;i<(int)rows.size()&&rows[i].defect*left<=budget;i++){
  const auto &r=rows[i];if(r.mask&~free)continue;
  int n=__builtin_popcountll(uint64_t(free^r.mask))+__builtin_popcountll(uint64_t((free^r.mask)>>64));
  if(n<left-1||n>12*(left-1))continue;
  chosen.push_back(i);if(search(free^r.mask,left-1,budget-r.defect,i+1))return true;chosen.pop_back();
 }return false;
}
int main(int argc,char**argv){
 if (argc<3)return 2;
 FILE*f=fopen(argv[1],"rb");for(int i=0;i<npoints;i++)for(int j=0;j<npoints;j++){uint64_t x[2];if(fread(x,8,2,f)!=2)return 2;forbidden[i][j]=M(x[0])|(M(x[1])<<64);if(fread(differences[i][j].data(),8,4,f)!=4)return 2;}fclose(f);
 if(!(cin>>scale>>peak))return 2;int total=0;for(int &w:W){cin>>w;total+=w;}
 int target=atoi(argv[2]);int budget=(target-(1296*num_maxima))*scale+nlabels*peak-total;
 
 // Row chosen before terminal step has d<=budget/2; last computed directly.
 cut=budget/2;limit=argc>3?atoi(argv[3]):0;M none[npoints]{};R empty[13]{};enumerate(0,0,(M(1)<<npoints)-1,none,empty,0,0);sort(rows.begin(),rows.end(),[](const Row&a,const Row&b){return a.defect!=b.defect?a.defect<b.defect:a.mask<b.mask;});
 bool found=search((M(1)<<npoints)-1,nlabels,budget,0);cout<<budget<<" "<<rows.size()<<" "<<visited<<" "<<found<<endl;
}
