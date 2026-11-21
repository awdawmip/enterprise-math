#include <array>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;using S=uint64_t;
int at(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}
int pop(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
struct P{S q;int r,c,n;M m;};int g[125],norb,cyc[125],wgt[64],per,low[13][126],best=10131;map<pair<S,int>,P> store;vector<P> rows,ans;vector<int> by[64];long long nodes,limit;S all;
int countp(S q){int n=0;for(;q;q&=q-1)n+=wgt[__builtin_ctzll(q)];return n;}
M moved(M m){M a=0;for(;m;m&=m-1)a|=M(1)<<g[at(m)];return a;}
void add(M a,int c){M m=a,u=0;int r=0;do{if(u&m)return;u|=m;m=moved(m);r++;if(m<a)return;}while(m!=a);if(r>12)return;
 S q=0;for(M v=u;v;v&=v-1)q|=S(1)<<cyc[at(v)];int n=pop(u);auto it=store.find({q,r});if(it==store.end() || it->second.c>c*r)store[{q,r}]={q,r,c*r,n,a};}
int main(int argc,char**argv){ifstream gm(argv[1]);gm>>per;for(int&i:g)gm>>i;int maxsize=0;limit=stoll(argv[3]);int cap=stoi(argv[5]);best=cap+1;
 for(int p=0;p<125;p++){if(cyc[p])continue;int q=p;do{cyc[q]=norb+1;++wgt[norb];q=g[q];}while(q!=p);norb++;}if(norb>64)return 2;for(int&i:cyc)--i;all=norb==64?~S(0):((S(1)<<norb)-1);
 array<array<int,125>,125> translate;
 for(int t=0;t<125;t++)for(int p=0;p<125;p++)translate[t][p]=((p/25+t/25)%5)*25+((p/5%5+t/5%5)%5)*5+(p%5+t%5)%5;
 ifstream db(argv[2]);int price;U l,h;while(db>>price>>l>>h){M base=(M(h)<<64)|l;for(auto &tr:translate){M z=0;for(M m=base;m;m&=m-1)z|=M(1)<<tr[at(m)];add(z,price);}}
 if(argc>=7){ifstream fixed(argv[6]);int r,c;S q;U a,b;while(fixed>>r>>q>>c>>a>>b){M m=(M(b)<<64)|a;auto it=store.find({q,r});if(it==store.end() || it->second.c>c)store[{q,r}]={q,r,c,r*pop(m),m};}}
 for(auto &h:store){auto &r=h.second;cout<<r.r<<" "<<r.q<<" "<<r.c<<" "<<r.n<<" "<<U(r.m)<<" "<<U(r.m>>64)<<"\n";} }