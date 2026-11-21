// Exact construction search in the stated, bounded same-size neighbourhood.
#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using M=__uint128_t; using W=uint64_t;
constexpr M ALL=(M(1)<<125)-1;
int first(M m){return W(m)?countr_zero(W(m)):64+countr_zero(W(m>>64));}
int count(M m){return popcount(W(m))+popcount(W(m>>64));}
W obs[125][125][4]; M bad[125][125];
struct Row{M mask;int cost,changes;};
array<M,12> old;
array<vector<Row>,12> pools;
array<int,12> sizes,original;
vector<pair<int,int>> chosen,winning;
long long nodes=0,enumerated=0;
int radius,budget,input_budget,total_lower=0,shift_cost=0;
array<int,125> point_weight{};array<int,12> label_weight{};int dual_scale=1;
int price(M m){
 int c=0;
 for(M a=m;a;a&=a-1){
  W w[4]{};
  for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)w[j]|=obs[first(a)][first(b)][j];
  for(W x:w)c+=popcount(x);
 }
 return c;
}
M conflict(int p,M m){M ans=0;for(M a=m;a;a&=a-1)ans|=bad[p][first(a)];return ans;}
void additions(int label,M current,M available,int needed,int changes,int cap){
 if(!needed){
  ++enumerated;int cost=price(current);
  if(cost<=cap)pools[label].push_back({current,cost,changes});
  return;
 }
 for(;count(available)>=needed;available&=available-1){
  int p=first(available);
  additions(label,current|(M(1)<<p),(available&(available-1))&~conflict(p,current),needed-1,changes,cap);
 }
}
void deletions(int label,M keep,M available,int remaining,int changes,int cap){
 if(!remaining){
  M outside=ALL^old[label];
  for(M a=keep;a;a&=a-1)for(M b=a&(a-1);b;b&=b-1)outside&=~bad[first(a)][first(b)];
  additions(label,keep,outside,changes,changes,cap);
  return;
 }
 for(;count(available)>=remaining;available&=available-1){
  M bit=available&-available;
  deletions(label,keep^bit,available^bit,remaining-1,changes,cap);
 }
}
bool solve(M used,unsigned labels,int cost,const array<vector<int>,12>& eligible){
 ++nodes;if(nodes%100000==0)cerr<<"progress "<<nodes<<" selected "<<chosen.size()<<endl;
 if(labels==4095){if(used==ALL&&cost<=budget){winning=chosen;return true;}return false;}
 array<vector<int>,12> valid;
 int lower=cost,best_count=1000000000,best_label=-1,best_point=-1;
 array<int,125> point_counts{};
 for(int i=0;i<12;i++)if(!(labels>>i&1)){
  int cheapest=1000000000;
  for(int j:eligible[i]){
   auto &r=pools[i][j];if(r.mask&used)continue;
   valid[i].push_back(j);cheapest=min(cheapest,r.cost);
   for(M m=r.mask;m;m&=m-1)++point_counts[first(m)];
  }
  if(valid[i].empty())return false;
  lower+=cheapest;if(lower>budget)return false;
  if((int)valid[i].size()<best_count){best_count=valid[i].size();best_label=i;}
 }
 for(M m=ALL^used;m;m&=m-1){
  int p=first(m);if(!point_counts[p])return false;
  if(point_counts[p]<best_count){best_count=point_counts[p];best_point=p;best_label=-1;}
 }
 for(int i=0;i<12;i++)if(!(labels>>i&1)&&(best_label<0||best_label==i)){
  for(int j:valid[i]){
   auto &r=pools[i][j];if(best_point>=0&&!(r.mask>>best_point&1))continue;
   chosen.push_back({i,j});
   if(solve(used|r.mask,labels|(1<<i),cost+r.cost,valid))return true;
   chosen.pop_back();
  }
 }
 return false;
}
int main(int argc,char**argv){
 if(argc!=6)return 2;
 ifstream o(argv[1],ios::binary),init(argv[2]);
 radius=stoi(argv[3]);input_budget=budget=stoi(argv[4]);assert(radius>=0&&radius<=5);
 o.read((char*)obs,sizeof(obs));array<unsigned char,3>tr;int triples=0;
 while(o.read((char*)tr.data(),3)){
  ++triples;do{bad[tr[0]][tr[1]]|=M(1)<<tr[2];}while(next_permutation(tr.begin(),tr.end()));
 }assert(triples==47000);
 constexpr int mincost[14]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
 M union_old=0;
 for(int i=0;i<12;i++){
  init>>sizes[i]>>original[i];
  for(int k=0,p;k<sizes[i];k++){init>>p;old[i]|=M(1)<<p;}
  assert(count(old[i])==sizes[i]&&!(old[i]&union_old));union_old|=old[i];
  assert(price(old[i])==original[i]);total_lower+=mincost[sizes[i]];
 }assert(union_old==ALL);
 for(int i=0;i<12;i++){
  int cap=budget-total_lower+mincost[sizes[i]];
  for(int changes=0;changes<=min(radius,sizes[i]);changes++)deletions(i,old[i],old[i],changes,changes,cap);
  sort(pools[i].begin(),pools[i].end(),[](auto a,auto b){return a.cost<b.cost||(a.cost==b.cost&&a.mask<b.mask);});
  vector<M> ids;for(auto r:pools[i])ids.push_back(r.mask);sort(ids.begin(),ids.end());assert(adjacent_find(ids.begin(),ids.end())==ids.end());
  cerr<<"{\"label\":"<<i<<",\"candidates\":"<<pools[i].size()<<"}"<<endl;
 }
 ifstream weights(argv[5]);weights>>dual_scale;for(int &v:label_weight)weights>>v;for(int &v:point_weight)weights>>v;
 assert(pools[0].size()==1&&pools[1].size()==1&&pools[0][0].mask==old[0]&&pools[1][0].mask==old[1]);
 shift_cost=dual_scale*(original[0]+original[1]);for(int i=2;i<12;i++)shift_cost+=label_weight[i];
 for(M m=ALL^(old[0]|old[1]);m;m&=m-1)shift_cost+=point_weight[first(m)];
 for(int i=0;i<12;i++){
  for(auto &row:pools[i]){
   if(i<2){row.cost=0;continue;}
   int reduced=dual_scale*row.cost-label_weight[i];for(M m=row.mask;m;m&=m-1)reduced-=point_weight[first(m)];
   // Rows meeting fixed cores can never be selected; discard them explicitly.
   if(row.mask&(old[0]|old[1]))row.cost=100000000;
   else{assert(reduced>=0);row.cost=reduced;}
  }
  pools[i].erase(remove_if(pools[i].begin(),pools[i].end(),[](auto r){return r.cost==100000000;}),pools[i].end());
  sort(pools[i].begin(),pools[i].end(),[](auto a,auto b){return a.cost<b.cost||(a.cost==b.cost&&a.mask<b.mask);});
 }
 budget=dual_scale*budget-shift_cost;
 array<vector<int>,12> eligible;for(int i=0;i<12;i++)for(int j=0;j<(int)pools[i].size();j++)eligible[i].push_back(j);
 bool found=solve(0,0,0,eligible);
 cout<<"{\"complete\":true,\"found\":"<<(found?"true":"false")<<",\"radius\":"<<radius<<",\"budget\":"<<input_budget<<",\"reduced_budget\":"<<budget<<",\"objective_shift_numerator\":"<<shift_cost<<",\"dual_scale\":"<<dual_scale<<",\"search_nodes\":"<<nodes<<",\"legal_candidates_before_price_cap\":"<<enumerated<<",\"groups\":[";
 for(int k=0;k<(int)winning.size();k++){
  if(k)cout<<",";auto [i,j]=winning[k];auto r=pools[i][j];cout<<"{\"old_label\":"<<i<<",\"cost\":"<<price(r.mask)<<",\"points\":[";
  bool comma=false;for(M m=r.mask;m;m&=m-1){if(comma)cout<<",";comma=true;cout<<first(m);}cout<<"]}";
 }cout<<"]}"<<endl;
}
