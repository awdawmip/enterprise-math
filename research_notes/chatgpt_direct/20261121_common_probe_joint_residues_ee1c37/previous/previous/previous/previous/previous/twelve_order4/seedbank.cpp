#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;
int ix(int x,int y,int z){return ((x%5+5)%5)*25+((y%5+5)%5)*5+(z%5+5)%5;}
int at(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
M move(M m,const array<int,125>&a){M r=0;for(;m;m&=m-1)r|=M(1)<<a[at(m)];return r;}
int main(int argc,char**argv){const int caps[14]={0,0,0,0,0,0,84,276,461,641,824,1008,1188,1371};
 vector<array<int,125>>lin,trans;array<int,3>p{0,1,2};do{for(int z=0;z<8;z++)for(int q=1;q<=2;q++){array<int,125>a;for(int i=0;i<125;i++){array<int,3>d{i/25,i/5%5,i%5};a[i]=ix(((z&1)?-q:q)*d[p[0]],((z&2)?-q:q)*d[p[1]],((z&4)?-q:q)*d[p[2]]);}lin.push_back(a);}}while(next_permutation(p.begin(),p.end()));
 for(int t=0;t<125;t++){array<int,125>a;for(int i=0;i<125;i++)a[i]=ix(i/25+t/25,i/5%5+t/5%5,i%5+t%5);trans.push_back(a);}
 ifstream f(argv[1]);int s,c,k;map<int,set<M>> normalized;
 while(f>>s>>c){M m=0;for(int j=0;j<s;j++){f>>k;m|=M(1)<<k;}if(c>caps[s])continue;
  normalized[c].insert(m);}
 ofstream out(argv[2]);long long tot=0;
 for(auto&[c,src]:normalized){set<M> translated;
   for(M a:src){M least=~M(0);for(M b=a;b;b&=b-1){int p=at(b);int t=ix(-p/25,-(p/5%5),-(p%5));least=min(least,move(a,trans[t]));}translated.insert(least);}
   set<M> basis;for(M a:translated)for(auto &l:lin){M b=move(a,l);M least=~M(0);for(M v=b;v;v&=v-1){int p=at(v);int t=ix(-p/25,-(p/5%5),-(p%5));least=min(least,move(b,trans[t]));}basis.insert(least);}
   int sz=__builtin_popcountll(U(*basis.begin()))+__builtin_popcountll(U(*basis.begin()>>64));cout<<c<<" "<<sz<<" "<<src.size()<<" "<<basis.size()<<endl;
   for(M m:basis){out<<c<<" "<<U(m)<<" "<<U(m>>64)<<"\n";}tot+=basis.size();
 }cerr<<tot<<endl;
}
