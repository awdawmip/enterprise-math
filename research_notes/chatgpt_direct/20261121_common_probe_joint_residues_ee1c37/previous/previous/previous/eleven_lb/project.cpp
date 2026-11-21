#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using U=uint64_t;using M=__uint128_t;
int bits(M m){return std::popcount(U(m))+std::popcount(U(m>>64));}
int main(int argc,char**argv){
 if(argc<6)return 2;
 std::ifstream pm(argv[1]);std::array<M,250> parent;
 for(auto&m:parent){U a,b;pm>>a>>b;m=(M(b)<<64)|a;}
 std::vector<int> demand;std::istringstream parser(argv[4]);int x;
 while(parser>>x)demand.push_back(x);int n=demand.size();
 int rest=std::stoi(argv[3]),subsets=1<<n;
 std::set<M> rows;
 for(int f=5;f<argc;f++){std::ifstream input(argv[f]);if(!input)return 6;U a,b;while(input>>a>>b)rows.insert((M(b)<<64)|a);}
 std::ifstream families(argv[2]);std::string line;std::set<M> remainders;
 int cases=0;long long tests=0;
 std::vector<M> un(subsets);std::vector<int> min(subsets);
 for(int b=1;b<subsets;b++)min[b]=demand[std::popcount((unsigned)b)-1];
 while(std::getline(families,line)){
  if(line.empty()||line[0]!='0')continue;
  std::istringstream in(line);for(int j=0,i;j<n;j++){if(!(in>>i))return 4;un[1<<j]=parent[i];}
  for(int b=1;b<subsets;b++)if((b&(b-1))!=0)un[b]=un[b&(b-1)]|un[b&(-b)];
  M free=((M(1)<<125)-1)^un.back();cases++;
  for(M row:rows){
   M rem=free&~row;if(bits(rem)>rest)continue;bool ok=true;
   for(int j=0;j<n;j++)if(bits(un[1<<j]&~row)<demand[0]){ok=false;break;}
   for(int b=1;ok&&b<subsets;b++)ok=bits(un[b]&~row)>=min[b];
   if(ok){tests++;remainders.insert(rem);}
  }
 }
 std::cerr<<cases<<" "<<tests<<" "<<remainders.size()<<"\n";
 for(M m:remainders)std::cout<<U(m)<<" "<<U(m>>64)<<"\n";
}
