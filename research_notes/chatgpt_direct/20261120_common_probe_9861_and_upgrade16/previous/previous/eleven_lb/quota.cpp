#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using M=__uint128_t;using U=uint64_t;
int count(M x){return std::popcount(U(x))+std::popcount(U(x>>64));}
int first(M x){return U(x)?std::countr_zero(U(x)):64+std::countr_zero(U(x>>64));}
using Pools=std::array<std::vector<M>,14>;using C=std::array<int,14>;
long long nodes=0;
bool solve(M free,M picked,C& limits,const Pools& pools,int cap){
 ++nodes;if(!free)return true;
 int n=count(free);if(cap<n)return false;
 if(cap==0)return false;
 M united=0;std::array<int,125> freq{};Pools next;
 for(int s=1;s<14;s++)if(limits[s]){
  int need=n-cap+s,best=0;auto&rows=next[s];
  for(M m:pools[s])if(!(m&picked)&&count(m&free)>=need){
    rows.push_back(m);united|=m;
    for(M d=m&free;d;d&=d-1)++freq[first(d)];
  }
  if(rows.size()<limits[s])return false;
 }
 if((united&free)!=free)return false;
 int pivot=-1,small=2000000000;
 for(M d=free;d;d&=d-1){int i=first(d);if(freq[i]<small){small=freq[i];pivot=i;}}
 for(int s=1;s<14;s++)if(limits[s]){
   --limits[s];for(M m:next[s])if((m>>pivot)&1 && solve(free&~m,picked|m,limits,next,cap-s))return true;
   ++limits[s];
 }
 return false;
}
int main(int argc,char**argv){
 if(argc<4)return 2;std::ifstream in(argv[1]);C base{};int cap=0;
 std::string spec(argv[2]);size_t last=0;
 while(last<spec.size()){size_t pos=spec.find(',',last);int s=std::stoi(spec.substr(last,pos-last));++base[s];cap+=s;if(pos==std::string::npos)break;last=pos+1;}
 Pools pool;U a,b;long long size=0;
 for(int i=3;i<argc;i++){std::ifstream f(argv[i]);if(!f)return 3;int s=0;while(f>>a>>b){M m=(M(b)<<64)|a;if(!s)s=count(m);pool[s].push_back(m);size++;}}
 int cases=0,yes=0;
 while(in>>a>>b){M m=(M(b)<<64)|a;C c=base;cases++;if(solve(m,0,c,pool,cap)){++yes;std::cout<<a<<" "<<b<<"\n";}}
 std::cerr<<cases<<" "<<yes<<" "<<nodes<<" "<<size<<"\n";
}
