#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using M=__uint128_t;using U=uint64_t;
int bits(M m){return std::popcount(U(m))+std::popcount(U(m>>64));}
int first(M m){return U(m)?std::countr_zero(U(m)):64+std::countr_zero(U(m>>64));}
std::vector<M> classes;
std::array<std::array<M,125>,125> bad;
std::vector<U> lookup;
int width;long long menus=0,candidate=0;
struct R{M mask=0,allowed=~M(0);int sz=0;};
bool two(M free,R r0,R r1){
 ++menus;if(!free)return true;
 if(free&~(r0.allowed|r1.allowed))return false;
 if(bits(free&~r0.allowed)>12-r1.sz||bits(free&~r1.allowed)>12-r0.sz)return false;
 M forced=free&~(r0.allowed&r1.allowed);int i=first(forced?forced:free);M bit=M(1)<<i;
 for(int j=0;j<2;j++){
  R r=j?r1:r0;
  if(r.allowed&bit){
   for(M u=r.mask;u;u&=u-1)r.allowed&=~bad[i][first(u)];
   r.mask|=bit;if(++r.sz==12)r.allowed=0;
   if(j?two(free^bit,r0,r):two(free^bit,r,r1))return true;
  }
  if(!r0.sz)break;
 }
 return false;
}
int eligible(M free){
 std::array<const U*,16> row;
 for(int i=0;i<16;i++)row[i]=lookup.data()+(i*256+int((free>>(i*8))&255))*width;
 int seen=0;
 for(int w=0;w<width;w++){
  U ids=row[0][w]&row[1][w]&row[2][w]&row[3][w];
  for(int i=4;i<16&&ids;i++)ids&=row[i][w];
  while(ids){int j=std::countr_zero(ids);ids&=ids-1;++seen;++candidate;
   M c=classes[64*w+j];if(two(free^c,R{},R{}))return -1;
  }
 }
 return seen;
}
int main(int argc,char**argv){
 if(argc<5)return 2;
 std::ifstream obs(argv[1],std::ios::binary);obs.seekg(125*125*32);unsigned char t[3];int nt=0;
 while(obs.read((char*)t,3)){nt++;for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(i!=j)bad[t[i]][t[j]]|=M(1)<<t[3-i-j];}
 if(nt!=47000)return 3;std::ifstream pm(argv[2]);std::array<M,250> par;U a,b;
 for(auto&m:par){pm>>a>>b;m=(M(b)<<64)|a;}
 for(int i=4;i<argc;i++){std::ifstream f(argv[i]);if(!f)return 4;while(f>>a>>b)classes.push_back((M(b)<<64)|a);}
 width=(classes.size()+63)/64;lookup.resize(16*256*width);
 for(int j=0;j<classes.size();j++)for(int i=0;i<16;i++){
  int need=int((classes[j]>>(8*i))&255);
  for(int h=need;h<256;h=(h+1)|need)lookup[(i*256+h)*width+j/64]|=U(1)<<(j%64);
 }
 std::ifstream records(argv[3]);std::string line;int yes=0,total=0,tests=0,hit=0;
 while(std::getline(records,line)){
  if(line.empty()||line[0]!='0')continue;
  std::istringstream in(line);M free=(M(1)<<125)-1;
  for(int j=0,i;j<8;j++){if(!(in>>i))return 5;free&=~par[i];}
  ++total;if(bits(free)<=33)continue;++tests;
  int n=eligible(free);if(n){++hit;if(n<0){yes++;std::cout<<"found "<<line<<std::endl;break;}}
 }
 std::cout<<total<<" "<<tests<<" "<<hit<<" "<<candidate<<" "<<menus<<" "<<yes<<"\n";
}
