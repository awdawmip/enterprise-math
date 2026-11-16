#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
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
void record(Mask m,int spent){++completions;if(spent<best){best=spent;win=trail;win.push_back(m);}}
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

void evaluate(Mask free, int k, int outercost, int cap, int outer, int choice) {
  {
   int lb[14];
   copy(minimum,minimum+14,lb);
   fill(lb+least,lb+14,99999);
   for(const auto& row:sets)if(!(row.mask&~free))lb[row.count]=min(lb[row.count],row.price);
   const int n=card(free);
   for(int z=1;z<=13;z++){
     for(int j=0;j<=k;j++)for(int h=0;h<=n;h++)dist[j][h][z]=99999;
     dist[0][0][z]=0;
     for(int j=1;j<=k;j++)for(int h=j;h<=n;h++)for(int t=1;t<=min(h,z);t++)
       dist[j][h][z]=min(dist[j][h][z],lb[t]+dist[j-1][h-t][z]);
   }
  }
  nodes=completions=0;
  best=cap+1;
  win.clear();trail.clear();
  pack(free,k,outercost,13,0);
  cout<<outer<<" "<<choice<<" "<<nodes<<" "<<(win.empty()?0:best)<<endl;
}
int main(int argc,char**argv){int ncores=stoi(argv[1]),labels=stoi(argv[2]),bound=stoi(argv[3]),maxfull=stoi(argv[4]);ifstream in(argv[5],ios::binary);in.read((char*)obs,sizeof(obs));array<unsigned char,3>e;
 while(in.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=Mask(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 for(int maxs=1;maxs<=13;maxs++){for(int k=0;k<=13;k++)for(int n=0;n<=125;n++)dist[k][n][maxs]=99999;
 dist[0][0][maxs]=0;for(int k=1;k<=13;k++)for(int n=1;n<=125;n++)for(int s=1;s<=min(n,maxs);s++)dist[k][n][maxs]=min(dist[k][n][maxs],minimum[s]+dist[k-1][n-s][maxs]);}
 ifstream f(argv[6]);uint64_t lo,hi;int outer=0;
 if(argc==8 && string(argv[7])=="regions"){

  if(labels==12)least=5;
  int base;
  while(f>>lo>>hi>>base){
   Mask free=(Mask(hi)<<64)|lo,none[125]{};
   sets.clear();generate(0,0,free,none,least);
   sort(sets.begin(),sets.end(),[](const auto&a,const auto&b){return a.count!=b.count?a.count>b.count:a.mask<b.mask;});
   evaluate(free,labels-ncores,base,bound,outer++,base);
  }
  return 0;
 }
 while(f>>lo>>hi){vector<int>center(ncores);for(int&i:center)f>>i;Mask orig=(Mask(hi)<<64)|lo;
 sets.clear();Mask none[125]{};generate(0,0,orig,none,least);
 sort(sets.begin(),sets.end(),[](auto&a,auto&b){return a.count!=b.count?a.count>b.count:a.mask<b.mask;});
 for(int which=0;which<(1<<ncores);which++){int nfull=popcount((unsigned)which);if(nfull>maxfull)continue;Mask free=orig;bool ok=true;
  for(int i=0;i<ncores;i++)if(which>>i&1){Mask m=Mask(1)<<center[i];if(!(free&m)){ok=false;break;}free^=m;}if(!ok)continue;
  evaluate(free,labels-ncores,1104*ncores+192*nfull,bound,outer,which);
 }outer++;}
}
