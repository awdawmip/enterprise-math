#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
struct Hash{size_t operator()(M x)const{return U(x)^(U(x>>64)*0x9e3779b97f4a7c15ULL);}};
struct Act{int p[125];M tab[16][256]{};void build(){for(int j=0;j<16;j++)for(int h=1;h<256;h++){int d=8*j+__builtin_ctz(h);tab[j][h]=tab[j][h&(h-1)]|(d<125?M(1)<<p[d]:0);}}M apply(M a)const{M b=0;for(int k=0;a;k++,a>>=8)b|=tab[k][(unsigned char)a];return b;}};
int add(int a,int b){return 25*((a/25+b/25)%5)+5*((a/5%5+b/5%5)%5)+(a%5+b%5)%5;}
int minus_pt(int a){return 25*((5-a/25)%5)+5*((5-a/5%5)%5)+(5-a%5)%5;}
struct Pair{M seed;int c;};
struct MaskRec{U lo,hi;unsigned c,s;};
int main(int n,char**argv){
 ifstream lin(argv[1]),f(argv[2]),caps(argv[3]);ofstream out(argv[4],ios::binary);
 vector<Act>L(96),T(125);
 for(auto&l:L){for(int&i:l.p)lin>>i;l.build();}
 for(int d=0;d<125;d++){for(int i=0;i<125;i++)T[d].p[i]=add(i,d);T[d].build();}
 int cap[14];for(int&v:cap)caps>>v;
 unordered_set<M,Hash>seen;int s,c;
 map<pair<int,int>,int>counts;
 while(f>>s>>c){M m=0;
  for(int i=0,j;i<s;i++){f>>j;m|=M(1)<<j;}
  if(c>cap[s]||seen.count(m))continue;
  set<M>linear;
  for(auto&l:L){M a=l.apply(m);linear.insert(a);
   for(M x=a;x;x&=x-1)seen.insert(T[minus_pt(at(x))].apply(a));
  }
  unordered_set<M,Hash> orbit;
  for(M a:linear)for(auto&t:T)orbit.insert(t.apply(a));
  counts[{s,c}]+=orbit.size();
  M rep=*min_element(orbit.begin(),orbit.end());for(M a:orbit){MaskRec row{U(a),U(a>>64),(unsigned)c,(unsigned)s+(a==rep?256:0)};out.write((char*)&row,sizeof(row));}
 }
 for(auto[n,k]:counts)cout<<n.first<<" "<<n.second<<" "<<k<<endl;
}
