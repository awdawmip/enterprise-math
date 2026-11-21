#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
using Mask=__uint128_t;
using Word=uint64_t;
using Lines=uint32_t;
using Menus=array<Word,4>;
constexpr int INF=1000000;
constexpr Lines ALL=(1u<<25)-1;
int first(Mask m){return Word(m)?countr_zero(Word(m)):64+countr_zero(Word(m>>64));}
int size(Mask m){return popcount(Word(m))+popcount(Word(m>>64));}
Menus obs[125][125];Mask bad[125][125]{};
int lin[96][125],tr[25][125],proj[125],line[25][5],price[25][25],direction[3];
int point(int x,int y,int z){return 25*((x+10)%5)+5*((y+10)%5)+(z+10)%5;}
int move(int i,int t){return point(i/25+t*direction[0],i/5%5+t*direction[1],i%5+t*direction[2]);}
struct Row{int cost=INF;Mask points=0;};
struct Fixed{Lines mask;int cost;Mask points;};
struct Result{int cost=INF;vector<Mask> group;};
int native(Mask m){int v=0;for(Mask i=m;i;i&=i-1){Menus a{};int r=first(i);for(Mask j=m;j;j&=j-1)for(int w=0;w<4;w++)a[w]|=obs[r][first(j)][w];for(Word h:a)v+=popcount(h);}return v;}
bool legal(Mask m){for(Mask i=m;i;i&=i-1)for(Mask j=i&(i-1);j;j&=j-1)if(m&bad[first(i)][first(j)])return false;return true;}
Mask cell[25];vector<Fixed> fixed_rows;
unordered_map<Lines,Row> memo;
long long probes=0;
void cheapest(Lines left,Mask chosen,Mask excluded,Row& best){
  if(!left){int c=native(chosen);if(c<best.cost)best={c,chosen};return;}
  int slot=-1,lowest=6;
  for(Lines t=left;t;t&=t-1){int j=countr_zero(t);int avail=size(cell[j]&~excluded);
   if(!avail)return;if(avail<lowest){slot=j;lowest=avail;}}
  for(Mask cand=cell[slot]&~excluded;cand;cand&=cand-1){
    int p=first(cand);Mask future=excluded;for(Mask j=chosen;j;j&=j-1)future|=bad[p][first(j)];
    cheapest(left^(1u<<slot),chosen|(Mask(1)<<p),future,best);
  }
}
Row lookup(Lines m){auto [it,newkey]=memo.try_emplace(m);if(newkey){++probes;int i=countr_zero(m);cheapest(m^(1u<<i),Mask(1)<<line[i][0],0,it->second);}return it->second;}
struct Transformation{array<int,25> q;int g,t;};
vector<Transformation> aut;
void symmetries(){
 aut.clear();map<array<int,25>,pair<int,int>> uniq;
 for(int g=0;g<96;g++){if(proj[lin[g][line[0][0]]]!=proj[lin[g][line[0][1]]])continue;
  for(int t=0;t<25;t++){array<int,25> q;for(int i=0;i<25;i++)q[i]=proj[tr[t][lin[g][line[i][0]]]];
    uniq.emplace(q,pair{g,t});}}
 for(auto&[q,a]:uniq)aut.push_back({q,a.first,a.second});
}
Lines image(Lines m,const array<int,25>&g){Lines v=0;for(;m;m&=m-1)v|=1u<<g[countr_zero(m)];return v;}
Mask act(Mask m,int g,int t){Mask v=0;for(;m;m&=m-1)v|=Mask(1)<<tr[t][lin[g][first(m)]];return v;}
using Cat=map<Lines,Row>;
Cat anchors(const vector<Row>&seeds){
 unordered_map<Lines,Row> raw;
 for(auto seed:seeds)for(int g=0;g<96;g++){Lines q=0;Mask r=0;
   for(Mask m=seed.points;m;m&=m-1){int j=lin[g][first(m)];q|=1u<<proj[j];r|=Mask(1)<<j;}
   if(popcount(q)!=size(r))continue;auto&best=raw[q];if(seed.cost<best.cost)best={seed.cost,r};
 }
 Cat out;unordered_map<Lines,Lines> canon;
 for(const auto&[q,r]:raw){
  auto it=canon.find(q);Lines k=ALL;
  if(it==canon.end()){for(auto&a:aut)k=min(k,image(q,a.q));for(auto&a:aut)canon[image(q,a.q)]=k;}
  else k=it->second;
  auto &b=out[k];if(b.cost<=r.cost)continue;
  for(auto&a:aut)if(image(q,a.q)==k){b={r.cost,act(r.points,a.g,a.t)};break;}
 }
 return out;
}
void put(Result&best,const vector<Mask>&f,const vector<Mask>&seeds,int c){
 if(c>=best.cost)return;vector<Mask> groups=f;
 for(Mask s:seeds)for(int t=0;t<5;t++){Mask r=0;for(Mask m=s;m;m&=m-1)r|=Mask(1)<<move(first(m),t);groups.push_back(r);}
 Mask u=0;int sum=0;for(Mask h:groups){assert(!(u&h)&&legal(h));u|=h;sum+=native(h);}
 assert(size(u)==125&&c==sum);best={c,groups};
}
void fixed_cover(Lines left,int count,int c,Mask anchor,vector<Mask>&chosen,Result&best){
 if(c>=best.cost||popcount(left)>2*count||popcount(left)<count)return;
 if(!left){if(!count)put(best,chosen,{anchor},c);return;}
 int i=countr_zero(left);for(const auto&f:fixed_rows)if((f.mask&(1u<<i))&&(f.mask&left)==f.mask){
  chosen.push_back(f.points);fixed_cover(left^f.mask,count-1,c+f.cost,anchor,chosen,best);chosen.pop_back();}
}
int mincost[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
void two(int labels,Lines q,Row a,Result&best){
 int s=popcount(q);
 for(size_t i=0;i<fixed_rows.size();i++){auto f=fixed_rows[i];if(q&f.mask)continue;
  auto rest=[&](Lines used,int fc,Mask second){
   Lines v=ALL^(q|used);int n=popcount(v);
   if(n>s||n>13||n<1||fc+5*(a.cost+mincost[n])>=best.cost)return;
   auto b=lookup(v);if(b.cost==INF)return;
   vector<Mask>fix{f.points};if(second)fix.push_back(second);
   put(best,fix,{a.points,b.points},fc+5*(a.cost+b.cost));};
  if(labels==11){rest(f.mask,f.cost,0);continue;}
  for(size_t j=i+1;j<fixed_rows.size();j++){auto h=fixed_rows[j];if(h.mask&(q|f.mask))continue;rest(f.mask|h.mask,f.cost+h.cost,h.points);}
 }
}
int main(int argc,char**argv){
 ifstream ob(argv[1],ios::binary),geo(argv[2]),se(argv[3]);ob.read((char*)obs,sizeof(obs));array<unsigned char,3> edge;
 while(ob.read((char*)edge.data(),3)){sort(edge.begin(),edge.end());do{bad[edge[0]][edge[1]]|=Mask(1)<<edge[2];}while(next_permutation(edge.begin(),edge.end()));}
 for(auto&g:lin)for(auto &i:g)geo>>i;
 vector<Row> seeds;int s,c;while(se>>s>>c){Mask m=0;for(int j=0;j<s;j++){int p;se>>p;m|=Mask(1)<<p;}if(s>=11)seeds.push_back({c,m});}
 int id=stoi(argv[4]);
 for(int d=0;d<=id;d++){for(int&i:direction)geo>>i;for(int&i:proj)geo>>i;for(auto&l:line)for(int&i:l)geo>>i;
  for(auto&t:tr)for(int&i:t)geo>>i;for(auto&r:price)for(int&i:r)geo>>i;}
 for(int i=0;i<25;i++)for(int p:line[i])cell[i]|=Mask(1)<<p;
 for(int i=0;i<25;i++)for(int j=i;j<25;j++)if(price[i][j]>=0)fixed_rows.push_back({(1u<<i)|(1u<<j),price[i][j],cell[i]|cell[j]});
 symmetries();auto A=anchors(seeds);cerr<<id<<" quotient "<<aut.size()<<" anchors "<<A.size()<<endl;
 for(int labels:{11,12}){
  Result single,doublet;
  for(const auto&[q,a]:A){vector<Mask>f;fixed_cover(ALL^q,labels-5,5*a.cost,a.points,f,single);}
  // First try cheaper anchors so attained witnesses give tighter pruning.
  vector<pair<Lines,Row>> order(A.begin(),A.end());sort(order.begin(),order.end(),[](auto a,auto b){return tie(a.second.cost,a.first)<tie(b.second.cost,b.first);});
  for(const auto&[q,a]:order)two(labels,q,a,doublet);
  cout<<id<<" "<<labels<<" "<<single.cost<<" "<<doublet.cost<<" "<<A.size()<<" "<<aut.size()<<endl;
  auto winner=single.cost<doublet.cost?single:doublet;
  if(winner.cost<INF){ofstream out(string(argv[5])+"/table"+to_string(id)+"_"+to_string(labels)+".txt");for(auto m:winner.group){for(;m;m&=m-1)out<<first(m)<<" ";out<<"\n";}}
 }
}
