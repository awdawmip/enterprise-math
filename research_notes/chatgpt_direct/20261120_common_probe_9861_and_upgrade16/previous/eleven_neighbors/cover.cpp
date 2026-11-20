#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <vector>
using namespace std;
using Mask=__uint128_t;using Obs=array<uint64_t,4>;
int pos(Mask x){return uint64_t(x)?countr_zero(uint64_t(x)):64+countr_zero(uint64_t(x>>64));}
int card(Mask x){return popcount(uint64_t(x))+popcount(uint64_t(x>>64));}
Mask bad[125][125];Obs obs[125][125];
int cost(Mask m){int c=0;for(Mask a=m;a;a&=a-1){Obs acc{};for(Mask b=m;b;b&=b-1)for(int i=0;i<4;i++)acc[i]|=obs[pos(a)][pos(b)][i];for(auto z:acc)c+=popcount(z);}return c;}
bool legal(Mask m){for(Mask a=m;a;a&=a-1)for(Mask b=a&(a-1);b;b&=b-1)if(bad[pos(a)][pos(b)]&m)return false;return true;}
struct Row{Mask mask;int count,price;};vector<Row> sets;vector<Mask> trail,win;
int dist[14][126][14];long long nodes,completions;int best,least=8,initial_best;
int minimum[14]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
void generate(Mask used,int size,Mask pool,const Mask *banned,int wanted){
 if(size>=wanted)sets.push_back({used,size,cost(used)});
 while(pool && size+card(pool)>=wanted){int i=pos(pool);pool&=pool-1;Mask next=pool&~banned[i],nb[125];
 if(size+1+card(next)<wanted)continue;
 for(Mask a=next;a;a&=a-1){int j=pos(a);nb[j]=banned[j]|bad[j][i];}
 generate(used|(Mask(1)<<i),size+1,next,nb,wanted);
 }
}
vector<Mask> old;
void record(Mask m,int spent){
 if(spent<=11292)return;
 ++completions;
 if(spent<best){best=spent;win=trail;win.push_back(m);}
}
void pack(Mask free,int k,int spent,int maxsize,int start){
 ++nodes;int n=card(free);if(n>maxsize*k|| n<k ||spent+dist[k][n][maxsize]>best)return;
 if(k==1){if(legal(free)&&(n<maxsize||start==0||free>trail.back()))record(free,spent+cost(free));return;}
 int need=(n+k-1)/k;
 for(int i=start;i<int(sets.size());i++){auto r=sets[i];if(r.count<need)break;if(r.mask&~free ||spent+r.price+dist[k-1][n-r.count][r.count]>best)continue;
 trail.push_back(r.mask);pack(free^r.mask,k-1,spent+r.price,r.count,i+1);trail.pop_back();}
 if(need<least){
  for(Mask m=free;m>0;m=(m-1)&free){int sz=card(m);if(sz>=least||sz<need||sz>maxsize|| (sz==maxsize&&start&&m<=trail.back()))continue;
   if(legal(m)){trail.push_back(m);pack(free^m,k-1,spent+cost(m),sz,sets.size());trail.pop_back();}
  }
 }
}

int main(int argc,char**argv){
 ifstream in(argv[1],ios::binary);in.read((char*)obs,sizeof(obs));array<unsigned char,3>e;
 while(in.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=Mask(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream jf(argv[2]);string line;int id=0,start=stoi(argv[3]),end=stoi(argv[4]);
 int cap=stoi(argv[5]);least=8;
 while(getline(jf,line)){int job=id++;if(job<start||job>=end)continue;
   istringstream ss(line);uint64_t lo,hi;int k,base;ss>>lo>>hi>>k>>base;Mask free=(Mask(hi)<<64)|lo,none[125]{};
   old={};for(int j=0;j<k;j++){uint64_t l,h;ss>>l>>h;old.push_back((Mask(h)<<64)|l);}
   int n=card(free);sets.clear();int lower=max(least,n-(k-1)*13);generate(0,0,free,none,lower);
   sort(sets.begin(),sets.end(),[](auto a,auto b){return a.count!=b.count?a.count>b.count:a.mask<b.mask;});
   int lb[14];copy(minimum,minimum+14,lb);fill(lb+least,lb+14,99999);for(auto r:sets)lb[r.count]=min(lb[r.count],r.price);
   for(int z=1;z<=13;z++){for(int h=0;h<=k;h++)for(int i=0;i<=n;i++)dist[h][i][z]=99999;
     dist[0][0][z]=0;for(int h=1;h<=k;h++)for(int i=h;i<=n;i++)for(int t=1;t<=min(z,i);t++)
      dist[h][i][z]=min(dist[h][i][z],lb[t]+dist[h-1][i-t][z]);}
   nodes=completions=0;best=cap+1;win.clear();trail.clear();pack(free,k,base,13,0);
   cout<<job<<" "<<nodes<<" "<<(win.empty()?0:best);if(!win.empty())for(auto m:win)cout<<" "<<uint64_t(m)<<" "<<uint64_t(m>>64);cout<<endl;
 }
}
