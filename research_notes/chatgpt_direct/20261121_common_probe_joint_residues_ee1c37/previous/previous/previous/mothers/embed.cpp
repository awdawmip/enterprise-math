#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <tuple>
#include <array>
using namespace std;
using U=uint64_t;using M=__uint128_t;
int bits(M m){return popcount(U(m))+popcount(U(m>>64));}
int main(int argc,char**argv){
 if(argc!=3)return 2;
 ifstream masks(argv[1]);array<M,250> pars;
 for(auto& p:pars){U a,b;masks>>a>>b;p=(M(b)<<64)|a;}
 ifstream f(argv[2]);string line;set<tuple<int,int,int>> types;
 while(getline(f,line)){istringstream row(line);int s,v;row>>s>>v;M m=0;for(int i=0,j;i<s;i++){row>>j;m|=M(1)<<j;}
 int best=0;for(M p:pars)best=max(best,bits(m&p));types.emplace(s,v,best);}
 for(auto [s,c,v]:types)cout<<s<<" "<<c<<" "<<v<<"\n";
}
