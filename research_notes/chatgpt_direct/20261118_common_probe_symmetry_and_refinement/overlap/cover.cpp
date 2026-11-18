#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using W=uint64_t;
using M=__uint128_t;
struct Row{M m;int size;};
int at(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
struct Search{
 vector<Row> rows;
 array<vector<W>,125> points;
 vector<vector<W>> compatible;
 vector<W> only_nines,only_eights;
 vector<int> path;
 long long nodes=0;
 int words=0;
 void build(const vector<Row>&bank,M free){
  for(auto r:bank)if(!(r.m&~free))rows.push_back(r);
  words=(rows.size()+63)/64;
  for(auto&p:points)p.assign(words,0);
  only_nines.assign(words,0);only_eights.assign(words,0);
  compatible.assign(rows.size(),vector<W>(words));
  for(int i=0;i<(int)rows.size();i++){
   W b=W(1)<<(i%64);
   for(M m=rows[i].m;m;m&=m-1)points[at(m)][i/64]|=b;
   (rows[i].size==9?only_nines:only_eights)[i/64]|=b;
   for(int j=0;j<i;j++)if(!(rows[i].m&rows[j].m)){
    compatible[j][i/64]|=b;compatible[i][j/64]|=W(1)<<(j%64);}
  }
 }
 bool cover(M free,bool need8,const vector<W>&avail){
  ++nodes;
  if(!free)return !need8;
  int least=100000,pivot=-1;
  if(need8){least=0;for(int i=0;i<words;i++)least+=popcount(only_eights[i]&avail[i]);if(!least)return false;}
  for(M q=free;q;q&=q-1){int x=at(q),sum=0;
   for(int i=0;i<words&&sum<least;i++)sum+=popcount(points[x][i]&avail[i]);
   if(sum==0)return false;if(sum<least){least=sum;pivot=x;}
  }
  auto& target=pivot<0?only_eights:points[pivot];vector<W> next(words);
  for(int i=0;i<words;i++)for(W b=avail[i]&target[i];b;b&=b-1){
   int j=64*i+countr_zero(b);auto&r=rows[j];bool still=need8&&r.size!=8;
   for(int w=0;w<words;w++){next[w]=avail[w]&compatible[j][w];if(!still)next[w]&=only_nines[w];}
   path.push_back(j);if(cover(free^r.m,still,next))return true;path.pop_back();}
  return false;
 }
};
int main(int argc,char**argv){string root=argv[1];ifstream data(root+"/keep9");W a,b;vector<M>keep;while(data>>a>>b)keep.push_back((M(b)<<64)|a);
 vector<Row>bank;for(int s:{8,9}){ifstream f(root+"/full"+to_string(s));while(f>>a>>b)bank.push_back({(M(b)<<64)|a,s});}
 int n=stoi(argv[2]),shard=stoi(argv[3]),step=stoi(argv[4]),k=0;
 for(int set=0;set<512;set++)if(popcount(unsigned(set))==n){if(k++%step!=shard)continue;
  M free=(M(1)<<125)-1;for(int i=0;i<(int)keep.size();i++)if(set&(1<<i))free^=keep[i];
  Search s;s.build(bank,free);vector<W>all(s.words,~W(0));bool yes=s.cover(free,true,all);cout<<set<<" "<<s.nodes<<" "<<yes;
  if(yes)for(auto j:s.path){M m=s.rows[j].m;cout<<" "<<W(m)<<" "<<W(m>>64);}cout<<endl;
 }}
