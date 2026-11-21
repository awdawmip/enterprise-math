#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
using U=uint64_t;using Mask=__uint128_t;
int bit(Mask m){return U(m)?countr_zero(U(m)):64+countr_zero(U(m>>64));}
int main(int argc,char**argv){
 ifstream maps(argv[1]),basis(argv[2]);int type=stoi(argv[3]);int g[4][125];
 for(int i=0;i<=type;i++)for(auto&a:g)for(auto&b:a)maps>>b;
 int no=0;array<int,125>id;id.fill(-1);for(int i=0;i<125;i++)if(id[i]<0){for(auto&a:g)id[a[i]]=no;no++;}
 array<array<int,125>,125> ts;for(int t=0;t<125;t++)for(int i=0;i<125;i++)ts[t][i]=25*((i/25+t/25)%5)+5*((i/5%5+t/5%5)%5)+(i%5+t%5)%5;
 struct R{int c;Mask m;};unordered_map<U,R>best;U a,b;int c;
 while(basis>>c>>a>>b){Mask m=(Mask(b)<<64)|a;int arr[13],sz=0;for(auto u=m;u;u&=u-1)arr[sz++]=bit(u);
  for(auto&t:ts){U q=0;Mask x=0;int j=0;
   for(;j<sz;j++){int p=t[arr[j]];U v=U(1)<<id[p];if((q&v)||g[1][p]==p||g[2][p]==p||g[3][p]==p)break;q|=v;x|=Mask(1)<<p;}
   if(j!=sz)continue;
   auto it=best.find(q);if(it==best.end()||it->second.c>c)best[q]={c,x};
  }
 }
 vector<U>sorted;for(auto &[q,_]:best)sorted.push_back(q);sort(sorted.begin(),sorted.end());
 for(U q:sorted)cout<<q<<" "<<best[q].c<<" "<<U(best[q].m)<<" "<<U(best[q].m>>64)<<"\n";
}
