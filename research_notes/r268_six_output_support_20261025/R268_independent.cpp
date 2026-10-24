// Independent C++17 exact checker for R268 formal positive affine BRC.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
using Key=tuple<int,int,int,int>;
using Mass=uint64_t;
using Effect=pair<int,int>;
struct Edge {int target,sign,increment;};
const Edge E[3][2]={{{2,-1,-1},{2,1,-1}},{{0,-1,-1},{0,1,-1}},{{1,1,1},{2,1,-1}}};
const int R[3][2]={{1,0},{2,0},{2,2}};
Key brc_step(Key s,int a){auto[q,r,eps,k]=s;auto e=E[q][a];return {e.target,R[r][a],e.sign*eps,e.sign*k+e.increment};}
Key word_value(uint64_t word,int n){Key s={0,0,1,0};for(int i=n-1;i>=0;i--)s=brc_step(s,((word>>i)&1));return s;}
int main(){
 map<Key,Mass> p; p[{0,0,1,0}]=1;
 int expected[8]={1,1,1,3,4,4,5,6};
 const Effect g7={1,-3},g8={1,0},g9={-1,-1};
 const array<Mass,6> counts7={2,2,3,1,1,9},counts8={1,6,1,9,2,16},counts9={1,19,2,20,4,28};
 for(int m=0;m<=20;m++){
   Mass total=0;map<Effect,array<Mass,6>> joint;
   for(auto &[s,weight]:p){auto[q,r,eps,k]=s;total+=weight;auto &v=joint[{eps,k}];v[2*q+(r==2)]+=weight;}
   assert(total==(Mass(1)<<m));
   int max_support=0;
   for(auto &[g,v]:joint){int sz=count_if(v.begin(),v.end(),[](Mass x){return x!=0;});max_support=max(max_support,sz);}
   if(m<=7)assert(max_support==expected[m]);
   if(m>=7)assert(max_support==6);
   if(m==7)assert(joint[g7]==counts7);
   if(m==8)assert(joint[g8]==counts8);
   if(m==9)assert(joint[g9]==counts9);
   if(m<=11){map<Key,Mass> brute;for(uint64_t word=0;word<(Mass(1)<<m);word++)brute[word_value(word,m)]++;assert(p==brute);}
   map<Key,Mass> nx;for(auto &[s,w]:p)for(int a=0;a<2;a++)nx[brc_step(s,a)]+=w;p.swap(nx);
 }
 cout<<"PASS R268 C++17 exact positive BRC, depths 0..20, word enumeration 0..11, first full six at 7"<<endl;
}
