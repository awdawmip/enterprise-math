#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using M=__uint128_t;using U=uint64_t;
int count(M x){return std::popcount(U(x))+std::popcount(U(x>>64));}
int first(M x){return U(x)?std::countr_zero(U(x)):64+std::countr_zero(U(x>>64));}
long long nodes=0;
bool solve(M free,M used,int left,const std::vector<M>&pool){
 ++nodes;if(!free)return true;if(!left)return false;
 int n=count(free),must=n-10*(left-1);M all=0;
 std::vector<M> rows;int hits[125]{};
 for(M m:pool)if(!(used&m)&&count(m&free)>=must){
     rows.push_back(m);all|=m;for(M d=m&free;d;d&=d-1)hits[first(d)]++;
 }
 if((all&free)!=free)return false;
 if(left==1)return true;
 int pivot=-1,best=10000000;
 for(M d=free;d;d&=d-1){int p=first(d);if(hits[p]<best){best=hits[p];pivot=p;}}
 for(M m:rows)if((m>>pivot)&1)if(solve(free&~m,used|m,left-1,rows))return true;
 return false;
}
int main(int argc,char**argv){
 if(argc<4)return 2;std::vector<M> catalog;U a,b;
 for(int i=3;i<argc;i++){std::ifstream f(argv[i]);if(!f)return 3;while(f>>a>>b)catalog.push_back((M(b)<<64)|a);}
 std::ifstream in(argv[1]);int left=std::stoi(argv[2]),cases=0,yes=0;
 while(in>>a>>b){M r=(M(b)<<64)|a;cases++;if(solve(r,0,left,catalog)){yes++;std::cout<<a<<" "<<b<<"\n";}}
 std::cerr<<cases<<" "<<yes<<" "<<nodes<<" "<<catalog.size()<<"\n";
}
