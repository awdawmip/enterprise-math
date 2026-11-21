#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
using W=uint64_t;
using M=__uint128_t;
using O=array<W,4>;
O pair_menu[125][125];
M bad[125][125];
int budgets[14],max_size,min_size;
int point(M m){return W(m)?countr_zero(W(m)):64+countr_zero(W(m>>64));}
int count(M m){return popcount(W(m))+popcount(W(m>>64));}
int charge(M selected){
 int cost=0;
 for(M a=selected;a;a&=a-1){O seen{};for(M b=selected;b;b&=b-1)for(int j=0;j<4;j++)seen[j]|=pair_menu[point(a)][point(b)][j];for(W w:seen)cost+=popcount(w);}return cost;
}
void generate(int size,M selected,M pool,const M *excluded){
 if(size>=min_size){int c=charge(selected);if(c<=budgets[size])cout<<W(selected)<<" "<<W(selected>>64)<<" "<<size<<" "<<c<<"\n";}
 if(size==max_size)return;
 for(;pool&&size+count(pool)>=min_size;){int i=point(pool);pool&=pool-1;M next=pool&~excluded[i],exc[125];
 if(size+1+count(next)<min_size)continue;
 for(M b=next;b;b&=b-1){int j=point(b);exc[j]=excluded[j]|bad[i][j];}
 generate(size+1,selected|(M(1)<<i),next,exc);}
}
int main(int argc,char**argv){ifstream in(argv[1],ios::binary);in.read((char*)pair_menu,sizeof(pair_menu));array<unsigned char,3>t;
 while(in.read((char*)t.data(),3))do{bad[t[0]][t[1]]|=M(1)<<t[2];}while(next_permutation(t.begin(),t.end()));
 W l,h;cin>>l>>h>>min_size>>max_size;
 for(int i=min_size;i<=max_size;i++)cin>>budgets[i];
 M empty[125]{};generate(0,0,(M(h)<<64)|l,empty);
}
