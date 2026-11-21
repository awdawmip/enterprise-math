#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
using namespace std;using M=__uint128_t;using U=uint64_t;using W=array<U,4>;
int at(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}int sz(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
M bad[125][125],sets[125];W ob[125][125];int reflection[125],mins[14],seen[14];long long nodes;int pts[14];
ofstream writer;
void search(int k,M pool,const array<M,125>& blocked,const W* masks,int cost){
 ++nodes;seen[k]++;if((k==8&&cost<=503)||(k==9&&cost<=671)||(k==10&&cost<=894)||(k==11&&cost<=1091)){writer<<k<<" ";for(int j=0;j<k;j++)writer<<pts[j]<<" ";writer<<cost<<"\n";}mins[k]=min(mins[k],cost);
 while(pool){int v=at(pool);pool&=pool-1;W next[14]{},nw{};int cc=cost;
  for(int j=0;j<k;j++)for(int t=0;t<4;t++){U w=ob[pts[j]][v][t];next[j][t]=masks[j][t]|w;cc+=__builtin_popcountll(w&~masks[j][t]);nw[t]|=w;}
  for(U w:nw)cc+=__builtin_popcountll(w);next[k]=nw;M q=pool&~blocked[v]&~(M(1)<<reflection[v]);array<M,125> bl;
  for(M a=q;a;a&=a-1){int i=at(a);bl[i]=blocked[i]|bad[i][v];}
  pts[k]=v;search(k+1,q,bl,next,cc);
 }
}
int main(int argc,char**argv){writer.open(argv[2]);ifstream f(argv[1],ios::binary);f.read((char*)ob,sizeof(ob));array<unsigned char,3>e;while(f.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 for(int i=0;i<125;i++)reflection[i]=((5-i/25)%5)*25+i%25;
 fill(mins,mins+14,10000000);
 // Translate the two free plane coordinates and scale the first to make any one point (1,0,0).
 int p=25;M free=((M(1)<<125)-1)^((M(1)<<25)-1);free&=~((M(1)<<p)|(M(1)<<reflection[p]));pts[0]=p;
 array<M,125> forb{};for(int j=0;j<125;j++)forb[j]=bad[p][j];
 W price[1]{};search(1,free,forb,price,0);cout<<nodes<<"\n";for(int n=1;n<14;n++)if(seen[n])cout<<n<<" "<<mins[n]<<" "<<seen[n]<<endl;}
