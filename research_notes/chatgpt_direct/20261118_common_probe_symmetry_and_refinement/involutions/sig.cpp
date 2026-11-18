#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <cstdint>
using U=uint64_t;using M=__uint128_t;using P=std::array<int,125>;
int ix(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
int add(int i,int j){return 25*((i/25+j/25)%5)+5*((i/5%5+j/5%5)%5)+(i%5+j%5)%5;}
int main(int ac,char**av){
 std::ifstream mp(av[1]);P g;for(auto&x:g)mp>>x;P col;col.fill(-1);std::vector<P>cent;P l;while(mp>>l[0]){for(int j=1;j<125;j++)mp>>l[j];cent.push_back(l);}
 int n=0;for(int i=0;i<125;i++)if(col[i]<0){
 for(auto&l:cent)for(int t=0;t<125;t++)if(g[t]==t)col[add(l[i],t)]=n;
 n++;
 }
 std::map<std::vector<int>,int> pr;
 for(int r:{1,2}){
 std::ifstream in(av[1+r]);int s,h,c;U a,b;while(in>>s>>h>>c>>a>>b){
 M m=(M(b)<<64)|a;std::vector<int>t(n+1,0);t[0]=r;for(;m;m&=m-1)t[col[ix(m)]+1]+=r;
 if(!pr.count(t)||pr[t]>c*r)pr[t]=c*r;}
 }
 std::vector<int> amt(n);for(int x:col)amt[x]++;for(int x:amt)std::cout<<x<<" ";std::cout<<"\n";for(auto&[t,c]:pr){for(int x:t)std::cout<<x<<" ";std::cout<<c<<"\n";}
}
