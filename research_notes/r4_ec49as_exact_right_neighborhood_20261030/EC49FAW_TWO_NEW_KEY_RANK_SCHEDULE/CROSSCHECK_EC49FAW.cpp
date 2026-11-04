#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
// Independent C++ scanner: literal ordered signed X6 primitive expansion at every terminal.
const map<char,vector<int>> moves={{'a',{-1,-1}},{'c',{1,2,-1,-2}},{'d',{2,1,-2,-1}},{'e',{3,1,1,-3}},{'f',{1,-1}},{'g',{2,-2}}};
const string alphabet="acdefg";
const array<int,9> initialState={0,0,0,1,1,2,2,3,4};
const array<int,9> initialPrev={0,1,2,0,2,0,1,0,0};
string observer(const string &w){
 array<int,9> state=initialState,prev=initialPrev;
 for(char c:w){for(int step:moves.at(c)){
  for(int i=0;i<9;++i){
   if(prev[i]==1&&step==2){if(state[i]==0)state[i]=1;else if(state[i]==2)state[i]=4;}
   else if(prev[i]==2&&step==1){if(state[i]==0)state[i]=2;else if(state[i]==1)state[i]=3;}
   prev[i]=step;
  }
 }}
 string s;for(int v:state)s+=char('0'+v);return s;
}
map<string,int> sig;
map<int,map<array<int,3>,int>> masks;
array<long long,10> legal{},allowed{};
void walk(int h,int n,int balance,string &w){
 if(abs(1-balance)>h-n)return;
 if(n==h){
  if(balance!=1)return;
  array<int,6> end{};array<int,3> key{};
  for(char c:w)for(int t:moves.at(c)){int ax=abs(t)-1;end[ax]+=(t>0)?1:-1;if(t>0&&t<=3)++key[ax];}
  if(end!=array<int,6>{2,0,0,0,0,0}){cerr<<"bad native endpoint";exit(3);}
  ++legal[h];const auto it=sig.find(observer(w));
  if(it!=sig.end()){masks[h][key]|=it->second;++allowed[h];}
  return;
 }
 for(char c:alphabet){w+=c;walk(h,n+1,balance+(c=='e')-(c=='a'),w);w.pop_back();}
}
bool rank9(int m){return (m&18)&&(m&20)&&(m&33)&&(m&40);}
int main(){
 const array<string,6> sw={"de","ed","ce","ec","feg","gef"};for(int i=0;i<6;i++)sig[observer(sw[i])]=1<<i;
 if(sig.size()!=6)return 1;
 for(int h=2;h<=9;h++){string s;walk(h,0,0,s);}
 vector<array<int,3>> keys;
 for(int x=0;x<=10;x++)for(int y=0;y<=10;y++)for(int z=1;z<=5;z++){
  int lo=max(x-1,y+2*z-1),hi=x+y-1;
  if(max(4,lo)<=min(9,hi))keys.push_back({x,y,z});
 }
 long long rawPairs=0,rankPairs=0;vector<pair<array<int,3>,array<int,3>>> rejected;
 for(size_t i=0;i<keys.size();i++)for(size_t j=i+1;j<keys.size();j++){
  auto a=keys[i],b=keys[j];bool cover=true,rank=true;
  for(int h=4;h<=9;h++){
   const auto feas=[&](auto k){return max(k[0]-1,k[1]+2*k[2]-1)<=h&&h<=k[0]+k[1]-1;};
   if(!feas(a)&&!feas(b))cover=false;
   if(!rank9((masks[h].count(a)?masks[h].at(a):0)|(masks[h].count(b)?masks[h].at(b):0)))rank=false;
  }
  if(cover){++rawPairs;if(rank)++rankPairs;else rejected.push_back({a,b});}
 }
 cout<<"{\"full_native_scanner\":true,\"keys\":"<<keys.size()<<",\"interval_pairs\":"<<rawPairs<<",\"rank9_pairs\":"<<rankPairs<<",\"per_h\":[";
 for(int h=2;h<=9;h++){
  if(h>2)cout<<',';int rankkeys=0;for(auto [k,m]:masks[h])rankkeys+=rank9(m);
  cout<<"{\"h\":"<<h<<",\"legal\":"<<legal[h]<<",\"allowed\":"<<allowed[h]<<",\"allowed_keys\":"<<masks[h].size()<<",\"rank9_keys\":"<<rankkeys<<"}";
 }
 cout<<"],\"rejected_pairs\":[";
 for(size_t i=0;i<rejected.size();i++){if(i)cout<<',';cout<<"[[";for(int j=0;j<3;j++){if(j)cout<<',';cout<<rejected[i].first[j];}cout<<"],[";for(int j=0;j<3;j++){if(j)cout<<',';cout<<rejected[i].second[j];}cout<<"]]";}
 cout<<"]}\n";
}
