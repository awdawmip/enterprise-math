// Exhaustive integer set-cover search for the strictly positive BRC-N4 S23 time signatures.
// g++ -O3 -std=c++17 em_cover_exact.cpp -o em_cover_exact && ./em_cover_exact
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
using Point=array<int,4>;
using Pair=array<int,2>;
using Box=array<Pair,4>;
vector<Point> pts;
vector<int> wt;
vector<uint64_t> boxes;
vector<Box> raw_boxes;
map<uint64_t,Box> representative;
vector<vector<int>> bypt;
unordered_map<uint64_t,int> failed;
uint64_t calls=0,prune_pop=0,prune_weight=0,prune_memo=0,prune_dom=0;
vector<uint64_t> chosen;
void insert(Point p,int w){pts.push_back(p);wt.push_back(w);}
void prepare(){
 insert({1,1,1,1},16);
 for(int x=2;x<=4;x++)for(int y=2;y<=4;y++)insert({1,1,x,y},5);
 for(int x=2;x<=4;x++)for(int y=2;y<=4;y++)insert({x,y,1,1},5);
 for(int x=2;x<=4;x++)for(int y=2;y<=4;y++)insert({2,x,2,y},6);
 for(int x=3;x<=4;x++)for(int u=2;u<=4;u++)for(int y=3;y<=4;y++)for(int v=2;v<=4;v++)insert({x,u,y,v},2);
 assert(pts.size()==64);
 // Independently recover the signatures from ALL genuine deterministic S23 policy tables.
 const int origin[6]={0,0,1,2,2,3},first[4]={0,0,1,1},second[4]={0,1,0,2};
 set<Point> legal_signatures;int policy_count=0;
 for(int a=0;a<4;a++)for(int b=0;b<8;b++)for(int c=0;c<64;c++){
  int stop[6];
  for(int j=0;j<6;j++){
   int v=origin[j];
   stop[j]=!(a&(1<<first[v]))?1:(!(b&(1<<second[v]))?2:((c&(1<<j))?3:4));
  }
  if(stop[0]==stop[1]&&stop[3]==stop[4])legal_signatures.insert({stop[0],stop[2],stop[3],stop[5]});
  policy_count++;
 }
 assert(policy_count==2048 && legal_signatures.size()==64);
 assert((set<Point>(pts.begin(),pts.end())==legal_signatures));
 const int Q[4][2]={{10,10},{20,20},{15,15},{15,15}};
 const int P[4][2]={{9,11},{5,5},{3,27},{30,30}};
 for(int law=0;law<2;law++){
  int total=0;
  for(int i=0;i<4;i++)for(int j=0;j<2;j++){int v=law?P[i][j]:Q[i][j];assert(v>0);total+=2*v;}
  assert(total==240);
 }
 auto test=pts; sort(test.begin(),test.end()); assert(unique(test.begin(),test.end())==test.end());
 vector<Pair> pairs;
 for(int a=1;a<=4;a++)for(int b=a+1;b<=4;b++)pairs.push_back({a,b});
 set<uint64_t> unique_masks;
 for(auto A:pairs)for(auto B:pairs)for(auto C:pairs)for(auto D:pairs){
  Box box={A,B,C,D};uint64_t m=0;
  for(int i=0;i<64;i++){
   bool ok=true;
   for(int j=0;j<4;j++)if(pts[i][j]!=box[j][0]&&pts[i][j]!=box[j][1]){ok=false;break;}
   if(ok)m|=uint64_t(1)<<i;
  }
  unique_masks.insert(m);representative.emplace(m,box);raw_boxes.push_back(box);
 }
 assert(raw_boxes.size()==1296);
 assert(unique_masks.size()==949);
 assert(accumulate(wt.begin(),wt.end(),0)==232);
 for(auto x:unique_masks){
  bool dominated=false;
  for(auto y:unique_masks)if(x!=y && (x&y)==x){dominated=true;break;}
  if(!dominated)boxes.push_back(x);
 }
 assert(boxes.size()==270);
 for(auto m:boxes)assert(__builtin_popcountll(m)<=16);
 bypt.resize(64);
 for(int k=0;k<int(boxes.size());k++)for(int i=0;i<64;i++)if((boxes[k]>>i)&1)bypt[i].push_back(k);
 int maxw=0;
 for(auto m:boxes){int w=0;auto n=m;while(n){int i=__builtin_ctzll(n);w+=wt[i];n&=n-1;}maxw=max(w,maxw);}
 assert(maxw==32);
}
int weight(uint64_t m){int v=0;while(m){int i=__builtin_ctzll(m);v+=wt[i];m&=m-1;}return v;}
bool solve(uint64_t rem, int r){
 calls++;
 if(!rem)return true;
 if(r<=0)return false;
 if(__builtin_popcountll(rem)>16*r){prune_pop++;return false;}
 if(weight(rem)>32*r){prune_weight++;return false;}
 auto f=failed.find(rem);
 if(f!=failed.end()&&f->second>=r){prune_memo++;return false;}
 if(r==1){
  for(auto m:boxes)if((m&rem)==rem){chosen.push_back(m);return true;}
  failed[rem]=max(failed[rem],r);return false;
 }
 int bestPt=-1,nmin=1000;
 auto tmp=rem;
 while(tmp){int i=__builtin_ctzll(tmp);tmp&=tmp-1;int nn=bypt[i].size();if(nn<nmin){bestPt=i;nmin=nn;}}
 vector<tuple<int,uint64_t,uint64_t>> cand;set<uint64_t> active_seen;
 for(int i:bypt[bestPt]){
  uint64_t mask=boxes[i]&rem;
  if(!active_seen.insert(mask).second)continue;
  cand.emplace_back(__builtin_popcountll(mask),mask,boxes[i]);
 }
 sort(cand.begin(),cand.end(),[](const auto &a,const auto &b){return get<0>(a)>get<0>(b) || (get<0>(a)==get<0>(b)&&get<1>(a)>get<1>(b));});
 // For the selected pivot, if a box covers a subset of another on remaining points, only the larger set matters.
 vector<uint64_t> keep;
 for(auto [gain,m,whole]:cand){
  bool dominated=false;
  for(auto k:keep)if((m&k)==m){dominated=true;break;}
  if(dominated){prune_dom++;continue;}
  uint64_t next=rem&~m;
  if(__builtin_popcountll(next)>16*(r-1)){prune_pop++;continue;}
  if(weight(next)>32*(r-1)){prune_weight++;continue;}
  if(solve(next,r-1)){chosen.push_back(whole);return true;}
  keep.push_back(m);
 }
 failed[rem]=max(failed[rem],r);
 return false;
}
int main(){
 prepare();cout<<"S23_tables=2048 signatures=64 boxes=1296 unique_masks=949 total_weight=232 nondominated="<<boxes.size()<<" max_box_points=16 max_box_weight=32"<<"\n";uint64_t all=~uint64_t(0);
 for(int r=8;r<=10;r++){
  bool v=solve(all,r);
  cout<<"target="<<r<<" exists="<<v<<" calls="<<calls<<" memo="<<failed.size()<<" prune_pop="<<prune_pop<<" prune_weight="<<prune_weight<<" prune_memo="<<prune_memo<<" prune_dom="<<prune_dom<<"\n"<<flush;
  if(v){uint64_t uni=0;for(auto m:chosen)uni|=m;assert(uni==all);cout<<"witness("<<chosen.size()<<") masks=";for(auto m:chosen)cout<<hex<<m<<" ";cout<<dec<<"\n";
   for(auto it=chosen.rbegin();it!=chosen.rend();++it){auto box=representative.at(*it);cout<<"BOX";for(auto pair:box)cout<<" ["<<pair[0]<<","<<pair[1]<<"]";cout<<"\n";}break;}
 }
}
