#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;using Row=array<M,12>;using Permit=array<vector<Row>,5>;
int bit(M m){return U(m)?countr_zero(U(m)):64+countr_zero(U(m>>64));}
M bad[125][125];array<U,4>obs[125][125];Permit slabs;long long visit[6]{},wins[6]{};int finals[100000]{};int best;int level[5];Row answer;
int price(Row &row){int c=0;for(auto m:row)for(M x=m;x;x&=x-1){array<U,4>v{};for(M y=m;y;y&=y-1)for(int t=0;t<4;t++)v[t]|=obs[bit(x)][bit(y)][t];for(U w:v)c+=popcount(w);}return c;}
bool merge(const Row& before,const Row& extra,Row& out){
 for(int j=0;j<12;j++){M a=before[j],b=extra[j];for(M x=b;x;x&=x-1){
  for(M y=a;y;y&=y-1)if(bad[bit(x)][bit(y)]&(a|b))return false;}
  out[j]=a|b;
 }
 return true;
}
void cover(int f,const Row&before){
 visit[f]++;
 if(f==5){Row z=before;int c=price(z);finals[c]++;if(c<best){best=c;answer=z;cerr<<"hit "<<c<<endl;}return;}
 for(auto &option:slabs[f]){Row z;if(!merge(before,option,z))continue;wins[f]++;cover(f+1,z);}
}
int plus5(int x){return (x%5+5)%5;}
int main(int argc,char**argv){
 ifstream f(argv[1],ios::binary),t(argv[2]);f.read((char*)obs,sizeof(obs));array<unsigned char,3>e;while(f.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 int axis=stoi(argv[3]),family=stoi(argv[4]);Row original;for(auto &m:original){U lo,hi;t>>lo>>hi;m=M(hi)<<64|lo;}best=stoi(argv[5])+1;
 for(int i=0;i<5;i++)level[i]=i;int idx=-1;do{if(++idx%stoi(argv[7])!=stoi(argv[6]))continue;for(auto &v:slabs)v.clear();for(int slab=0;slab<5;slab++){
  for(int a=0;a<5;a++)for(int b=0;b<5;b++)for(int c=0;c<5;c++)for(int e=0;e<5;e++)for(int u=0;u<5;u++)for(int v=0;v<5;v++){
   if((a*e-b*c)%5==0)continue;
   if(slab==0 && (u||v))continue;
   if(slab==0){
     array<int,4> mat{a,b,c,e};bool lowest=true;
     for(int row_swap=0;row_swap<2;row_swap++)for(int s:{1,4})for(int t:{1,4}){
       array<int,4> other= row_swap?array<int,4>{s*c%5,s*e%5,t*a%5,t*b%5}:array<int,4>{s*a%5,s*b%5,t*c%5,t*e%5};if(other<mat)lowest=false;
     }
     if(!lowest)continue;
   }
   Row out{};for(int j=0;j<12;j++)for(M x=original[j];x;x&=x-1){int p=bit(x);array<int,3>z{p/25,p/5%5,p%5};
    if(z[axis]!=level[slab])continue;int h=(axis+1)%3,k=(axis+2)%3;int h0=z[h],k0=z[k];
    z[axis]=slab;z[h]=plus5(a*h0+b*k0+u);z[k]=plus5(c*h0+e*k0+v);
    out[j]|=M(1)<<(25*z[0]+5*z[1]+z[2]);
   }
   bool legal=true;for(M m:out){for(M x=m;x;x&=x-1)for(M y=x&(x-1);y;y&=y-1)if(bad[bit(x)][bit(y)]&m)legal=false;}
   if(legal)slabs[slab].push_back(out);
  }
 }
 cover(0,{});}while(next_permutation(level,level+5));cout<<best;for(auto n:visit)cout<<" "<<n;cout<<endl;
 for(int i=0;i<100000;i++)if(finals[i])cerr<<i<<" "<<finals[i]<<endl;if(answer[0])for(auto m:answer){for(;m;m&=m-1)cout<<bit(m)<<" ";cout<<endl;}
}
