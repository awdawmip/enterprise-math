#include <array>
#include <algorithm>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
using namespace std;
using U=uint64_t;using M=__uint128_t;using O=array<U,4>;
int ix(M x){return U(x)?countr_zero(U(x)):64+countr_zero(U(x>>64));}
int count(M x){return popcount(U(x))+popcount(U(x>>64));}
O obs[125][125];M bad[125][125];int caps[14],least;unsigned char selected[13];ofstream out;
struct Rec{array<unsigned char,13> pts;unsigned char s;uint16_t cost;};static_assert(sizeof(Rec)==16);
void generate(int size,M pool,const M *ban,const O *old,int spent){
 if(size>=least && spent<=caps[size]){Rec a;a.pts.fill(125);copy(selected,selected+size,a.pts.begin());a.s=size;a.cost=spent;out.write((char*)&a,sizeof(a));}
 while(pool&&size+count(pool)>=least){int x=ix(pool);pool&=pool-1;M next=pool&~ban[x];
  if(size+1+count(next)<least)continue;
  M nb[125];for(M b=next;b;b&=b-1){int p=ix(b);nb[p]=ban[p]|bad[p][x];}
  O own{},state[14];int total=spent;
  for(int k=0;k<size;k++)for(int h=0;h<4;h++){U w=obs[selected[k]][x][h];state[k][h]=old[k][h]|w;total+=popcount(w&~old[k][h]);own[h]|=w;}
  state[size]=own;for(U w:own)total+=popcount(w);selected[size]=x;
  generate(size+1,next,nb,state,total);
 }
}
int main(int argc,char**argv){ifstream n(argv[1],ios::binary),input(argv[2]);out.open(argv[3],ios::binary);
 n.read((char*)obs,sizeof(obs));array<unsigned char,3> e;while(n.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 U a,b;int high;input>>a>>b>>least>>high;for(int j=least;j<=high;j++)input>>caps[j];M none[125]{};O state[14]{};
 generate(0,(M(b)<<64)|a,none,state,0);
}
