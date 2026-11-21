#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;const M full=(M(1)<<125)-1;
int at(M m){return W(m)?countr_zero(W(m)):64+countr_zero(W(m>>64));}
int card(M x){return popcount(W(x))+popcount(W(x>>64));}
int g[125];M base;M mv(M m){M r=0;for(;m;m&=m-1)r|=M(1)<<g[at(m)];return r;}
struct Orb{M m;array<M,3> rows;};
vector<Orb> orbs;vector<M> nines,trail,point[125];long long leaves=0,nodes=0;int keep=3;
bool tail(M f,const vector<M>&src,int k){
 ++nodes;if(!f)return true;
 vector<M>can;array<int,125>deg{};M u=0;
 for(auto m:src)if(!(m&~f)){can.push_back(m);u|=m;for(M p=m;p;p&=p-1)deg[at(p)]++;}
 if(u!=f)return false;int x=at(f);
 for(M p=f;p;p&=p-1)if(deg[at(p)]<deg[x])x=at(p);
 for(auto m:can)if((m>>x)&1){trail.push_back(m);if(tail(f^m,can,k-1))return true;trail.pop_back();}
 return false;
}
bool outer(M f,int k,int first,const vector<int>&avail,const vector<M>&bank){
 if(!k){++leaves;return tail(f,bank,13-3*keep);}
 vector<int>next;for(int i:avail)if(i>=first&&!(orbs[i].m&~f))next.push_back(i);
 vector<M>opt;for(auto m:bank)if(!(m&~f))opt.push_back(m);
 for(int i:next){auto&o=orbs[i];for(auto r:o.rows)trail.push_back(r);if(outer(f^o.m,k-1,i+1,next,opt))return true;trail.resize(trail.size()-3);}
 return false;
}
int main(int argc,char**argv){ifstream f(argv[1]),data(argv[2]);keep=stoi(argv[3]);int rep,p,gi;W l,h;data>>rep>>l>>h>>p>>gi;base=(M(h)<<64)|l;for(int&x:g)data>>x;trail.push_back(base);
 vector<int> ids;
 while(f>>l>>h){M m=(M(h)<<64)|l;if(m&base)continue;nines.push_back(m);auto b=mv(m),c=mv(b);if(m<b&&m<c&&!(m&b)&&!(b&c)&&!(c&m)){ids.push_back(orbs.size());orbs.push_back({m|b|c,{m,b,c}});}}
 if(outer(full^base,keep,0,ids,nines))for(auto m:trail)cout<<W(m)<<" "<<W(m>>64)<<"\n";
 cerr<<nines.size()<<" "<<orbs.size()<<" "<<leaves<<" "<<nodes<<" "<<trail.size()<<endl;return 0;}
