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
int main(int n,char**argv){ifstream lin(argv[1]),f(argv[2]),mp(argv[3]);ofstream out(argv[4]);vector<Act>L(96),T(125);Act g{};for(int &p:g.p)mp>>p;g.build();for(auto &l:L){for(int &p:l.p)lin>>p;l.build();}for(int i=0;i<125;i++){for(int j=0;j<125;j++)T[i].p[j]=add(j,i);T[i].build();}int cap[]={0,0,0,0,0,0,0,0,476,656,836,1023,1203,1383},s,c;unordered_set<M,Hash>seen;unordered_map<M,Pair,Hash>bank;map<int,int>minima;map<int,int>shapes;std::ifstream caps(argv[5]); for(auto &price:cap)caps>>price; while(f>>s>>c){M m=0;for(int i=0,j;i<s;i++){f>>j;m|=M(1)<<j;}if(c>cap[s]||seen.count(m))continue;set<M> linear;
 for(auto&l:L){M a=l.apply(m);linear.insert(a);for(M x=a;x;x&=x-1)seen.insert(T[minus_pt(at(x))].apply(a));}shapes[s]++;
 for(M a:linear)for(auto&t:T){M r=t.apply(a),z=g.apply(r);if(r&z)continue;if(!minima.count(s)||minima[s]>c)minima[s]=c;M q=r|z;auto it=bank.find(q);if(it==bank.end()||it->second.c>c)bank[q]={r,c};}
 }
 for(auto [q,r]:bank){int sz=__builtin_popcountll(U(r.seed))+__builtin_popcountll(U(r.seed>>64));out<<sz<<" 0 "<<r.c<<" "<<U(r.seed)<<" "<<U(r.seed>>64)<<"\n";}
 for(auto [k,v]:minima)cout<<k<<" "<<v<<" "<<shapes[k]<<endl;
}
