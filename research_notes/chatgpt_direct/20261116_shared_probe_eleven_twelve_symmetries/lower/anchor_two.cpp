#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;using M=__uint128_t;using Q=uint64_t;
int bit(M a){return Q(a)?countr_zero(Q(a)):64+countr_zero(Q(a>>64));}
const M all=(M(1)<<125)-1;
using Action=array<unsigned char,125>;
vector<Action> G;
M moved(M a,const Action&g){M b=0;for(;a;a&=a-1)b|=M(1)<<g[bit(a)];return b;}
int main(int argc,char**argv){
 int k=stoi(argv[1]),h=stoi(argv[2]),take=stoi(argv[3]);
 ifstream bank(argv[4]),frames(argv[5]);int types;bank>>types;set<M> punct;
 while(types--){int s,c,n;bank>>s>>c>>n;while(n--){Q lo,hi;int rep;bank>>lo>>hi>>rep;if(s==12&&c==1116)punct.insert(M(lo)|(M(hi)<<64));}}
 array<int,3> order={0,1,2};do{for(int a:{1,2}) for(int s=0;s<8;s++)for(int d=0;d<125;d++){
  Action g;for(int p=0;p<125;p++){int x[3]={p/25,(p/5)%5,p%5};int t[3]={d/25,d/5%5,d%5};int q=0;for(int j=0;j<3;j++)q=q*5+(10+t[j]+a*((s>>j&1)?-1:1)*x[order[j]])%5;g[p]=q;}G.push_back(g);
 }}while(next_permutation(order.begin(),order.end()));
 set<M> free;Q lo,hi;
 while(frames>>lo>>hi){vector<int>c(k);for(int&i:c)frames>>i;for(int pat=0;pat<(1<<k);pat++)if(popcount((unsigned)pat)==h){
  M f=M(lo)|(M(hi)<<64);bool ok=true;for(int j=0;j<k;j++)if(pat>>j&1){M z=M(1)<<c[j];if(!(z&f))ok=false;f&=~z;}if(ok)free.insert(f);
 }}
 if(k==0)free.insert(all);
 for(auto f:free){auto used=all^f;vector<int>stab;for(int gi=0;gi<G.size();gi++)if(moved(used,G[gi])==used)stab.push_back(gi);
  set<M> options;for(M p:punct)if(!(p&used))options.insert(p);
  vector<M> candidates(options.begin(),options.end());map<M,int>order;vector<M>reps;
  while(!options.empty()){M x=*options.begin();int oi=reps.size();reps.push_back(x);for(int g:stab){auto p=moved(x,G[g]);options.erase(p);order[p]=oi;}}

  if(argc<7 || stoi(argv[6])!=2)return 4;
  for(int i=0;i<reps.size();i++){
   M x=reps[i];set<M> admissible;for(M p:candidates)if(!(p&x)&&order[p]>=i)admissible.insert(p);
   vector<int> st2;for(int g:stab)if(moved(x,G[g])==x)st2.push_back(g);
   auto av=admissible;vector<M> reps2;map<M,int> rank2;while(!av.empty()){
    M y=*av.begin();int j=reps2.size();reps2.push_back(y);for(int g:st2){M z=moved(y,G[g]);av.erase(z);rank2[z]=j;}
   }
   for(int j=0;j<reps2.size();j++){M y=reps2[j],r=f^x^y;vector<M> remaining;
    for(M q:admissible)if(!(q&y)&&rank2[q]>=j)remaining.push_back(q);
    if(int(remaining.size())+2<take)continue;
    cout<<Q(r)<<" "<<Q(r>>64)<<" "<<remaining.size();for(M p:remaining)cout<<" "<<Q(p)<<" "<<Q(p>>64);cout<<"\n";
   }
  }}
}
