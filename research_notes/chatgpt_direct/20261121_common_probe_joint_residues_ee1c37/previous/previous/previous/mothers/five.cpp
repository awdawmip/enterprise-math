#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using U=uint64_t;using M=__uint128_t;constexpr M ALL=(M(1)<<125)-1;
int bits(M m){return std::popcount(U(m))+std::popcount(U(m>>64));}
int main(int argc,char**argv){
 if(argc<4)return 2;
 std::ifstream ms(argv[1]);std::array<M,250> parents;
 for(auto&m:parents){U a,b;ms>>a>>b;m=(M(b)<<64)|a;}
 std::ifstream records(argv[2]);std::string line;
 std::set<M> exc;
 for(int i=3;i<argc;i++){std::ifstream prop(argv[i]);if(!prop)return 4;U a,b;while(prop>>a>>b)exc.insert((M(b)<<64)|a);}
 int cases=0;long long near=0,valid=0;std::set<M> residues;
 while(std::getline(records,line)){
   if(line.empty()||line[0]!='0')continue;
   std::istringstream in(line);std::array<M,6> q;std::array<M,64> united{};
   for(auto&m:q){int i;if(!(in>>i))return 3;m=parents[i];}
   for(int b=1;b<64;b++)united[b]=united[b&(b-1)]|q[std::countr_zero((unsigned)b)];
   M rem=ALL^united[63];cases++;
   for(M x:exc){
     if(bits(rem&~x)>40)continue;
     bool ok=true;
     for(M m:q)if(bits(m&x)>1){ok=false;break;}
     if(!ok)continue;
     ++near;
     for(int b=1;b<64;b++)if(bits(united[b]&~x)<12*std::popcount((unsigned)b)){ok=false;break;}
     if(!ok)continue;
     bool hall=false;
     for(int a=0;a<6&&!hall;a++)for(int c=a+1;c<6&&!hall;c++){
       int both=(1<<a)|(1<<c);bool valid=true;
       for(int b=1;b<64&&valid;b++)valid=bits(united[b]&~x)>=12*std::popcount((unsigned)b)+std::popcount((unsigned)(b&both));
       hall|=valid;
     }
     if(hall){++valid;residues.insert(rem&~x);}
   }
 }
 std::cerr<<cases<<" "<<near<<" "<<valid<<" "<<residues.size()<<"\n";
 for(M r:residues)std::cout<<U(r)<<" "<<U(r>>64)<<"\n";
}
