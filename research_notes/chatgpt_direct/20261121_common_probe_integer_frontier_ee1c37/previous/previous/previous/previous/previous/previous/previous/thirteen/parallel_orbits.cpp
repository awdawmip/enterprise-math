#include <array>
#include <algorithm>
#include <bit>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;
using Mask=uint64_t;using Global=__uint128_t;using Obs=array<uint64_t,4>;
Obs obs[125][125],ob[35][35];Global bad[125][125];Mask ba[35][35];int pts[35],best=9015;

struct Row {Mask m;int c;};vector<Row> bank[14];unordered_map<Mask,int> costs;int minima[14];Mask answer[4];
void gen(Mask m,Mask cand,Mask* forbid,int k, int *sel, Obs *old,int cost){
 if(k>=1){bank[k].push_back({m,cost});costs[m]=cost;minima[k]=min(cost,minima[k]);}
 while(cand){int x=countr_zero(cand);cand&=cand-1;Obs next[14]{},count{};int c=cost;
 for(int i=0;i<k;i++){auto &w=ob[x][sel[i]];for(int t=0;t<4;t++){next[i][t]=old[i][t]|w[t];count[t]|=w[t];c+=popcount(w[t]&~old[i][t]);}}
 for(int t=0;t<4;t++)c+=popcount(count[t]);next[k]=count;sel[k]=x;
 Mask avail=cand&~forbid[x],fnext[35];for(Mask a=avail;a;a&=a-1){int v=countr_zero(a);fnext[v]=forbid[v]|ba[v][x];}
 gen(m|Mask(1)<<x,avail,fnext,k+1,sel,next,c);
 }}
int main(int argc,char **argv){
 ifstream in(argv[1],ios::binary);in.read((char*)obs,sizeof(obs));array<unsigned char,3>e;while(in.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=Global(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream f(argv[2]);int size1,size2,n;
 for(int h=0;f>>size1>>size2>>n;h++){
  Mask full=(Mask(1)<<n)-1;int base=5*((size1==9?557:size1==10?744:936)+(size2==9?557:size2==10?744:936));
  for(int i=0;i<n;i++)f>>pts[i];for(int i=0;i<n;i++)for(int j=0;j<n;j++){
    ob[i][j]=obs[pts[i]][pts[j]];Mask w=0;for(int k=0;k<n;k++)if(bad[pts[i]][pts[j]]>>pts[k]&1)w|=Mask(1)<<k;ba[i][j]=w;}
  costs.clear();for(auto &z:bank)z.clear();fill(minima,minima+14,99999);int sel[14];Mask empty[35]{};gen(0,full,empty,0,sel,nullptr,0);
  for(auto &z:bank)sort(z.begin(),z.end(),[](auto &i,auto &j){return i.c<j.c;});
  for(int i=1;i<=13;i++)for(int j=i;j<=13;j++){
   int k=n-i-j;if(k<j||k>13)continue;array<int,3>s{i,j,k};sort(s.begin(),s.end(),[](int u,int v){return bank[u].size()<bank[v].size();});
   auto [a,b,c]=s;
   for(auto u:bank[a]){if(base+u.c+minima[b]+minima[c]>=best)break;for(auto v:bank[b]){
    if(base+u.c+v.c+minima[c]>=best)break;if((u.m&v.m)||(a==b&&u.m>=v.m))continue;Mask rem=full^u.m^v.m;if(b==c&&v.m>=rem)continue;
    auto it=costs.find(rem);if(it!=costs.end()&&base+u.c+v.c+it->second<best){best=base+u.c+v.c+it->second;cout<<"BEST "<<h<<" "<<best<<" "<<u.m<<" "<<v.m<<" "<<rem<<endl;}
   }}
  }
  if(h%100==0)cerr<<h<<" "<<best<<endl;
 }
}
