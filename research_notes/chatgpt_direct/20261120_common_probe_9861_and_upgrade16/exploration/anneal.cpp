// Exploratory annealing. Only emitted zero-conflict partitions are candidates;
// there is no exhaustive-search or lower-bound claim.
#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using M=__uint128_t; using U=uint64_t;using Obs=array<U,4>;
Obs obs[125][125];M bad[125][125];
int at(M a){return U(a)?countr_zero(U(a)):64+countr_zero(U(a>>64));}
int count(M a){return popcount(U(a))+popcount(U(a>>64));}
struct Stats{int cost,conflicts;};
Stats stats(M a){int ids[125],n=0,c=0,b=0;for(M m=a;m;m&=m-1)ids[n++]=at(m);for(int i=0;i<n;i++){Obs o{};for(int j=0;j<n;j++)for(int k=0;k<4;k++)o[k]|=obs[ids[i]][ids[j]][k];for(U v:o)c+=popcount(v);for(int j=0;j<i;j++)b+=count(bad[ids[i]][ids[j]]&a);}return{c,b/3};}
U state;U rng(){state^=state<<13;state^=state>>7;state^=state<<17;return state;}
double uniform(){return (rng()>>11)*0x1p-53;}
void write(const char* path, array<M,12> const& cl,int cost,long long steps){ofstream f(path);f<<"{\"cost\":"<<cost<<",\"steps\":"<<steps<<",\"seed\":"<<state<<",\"groups\":[";for(int i=0;i<12;i++){if(i)f<<',';f<<'[';bool flag=0;for(M m=cl[i];m;m&=m-1){if(flag)f<<',';f<<at(m);flag=1;}f<<']';}f<<"]}\n";}
int main(int argc,char**argv){
 ifstream o(argv[1],ios::binary);o.read((char*)obs,sizeof(obs));array<unsigned char,3> e;while(o.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream g(argv[2]);array<M,12> original{};array<int,125> origlab;for(int i=0;i<125;i++){g>>origlab[i];original[origlab[i]]|=M(1)<<i;}
 state=stoull(argv[3]);int seconds=stoi(argv[4]),best=999999; int near[3]={0,999999,999999}; int far[3]={0,999999,999999};long long iterations=0;auto start=chrono::steady_clock::now();array<M,12> winner=original;
 for(M m:original)best=min(best,999999);best=0;for(M m:original)best+=stats(m).cost;
 for(int round=0;;round++){
  array<M,12> cl=(round%7==0?original:winner);array<int,125> lab;for(int j=0;j<12;j++)for(M a=cl[j];a;a&=a-1)lab[at(a)]=j;
  if(round%7>=4){int shakes=12+(round%5)*6;for(int q=0;q<shakes;q++){int x=rng()%125,y=rng()%125,i=lab[x],j=lab[y];if(i==j)continue;cl[i]^=(M(1)<<x)|(M(1)<<y);cl[j]^=(M(1)<<x)|(M(1)<<y);swap(lab[x],lab[y]);}}
  array<Stats,12> scores;int total=0,conf=0;for(int j=0;j<12;j++){scores[j]=stats(cl[j]);total+=scores[j].cost;conf+=scores[j].conflicts;}
  int cycle=800000;double high=35.+(round%4)*20.;int weight=40+(round%5)*20;
  for(int it=0;it<cycle;it++,iterations++){
   if(it%8192==0&&chrono::duration<double>(chrono::steady_clock::now()-start).count()>seconds){cerr<<"done "<<iterations<<" best "<<best<<" rounds "<<round<<endl;return 0;}
   double temp=high*pow(.008,double(it)/cycle);
   int x=rng()%125,y=rng()%125,i=lab[x],j=lab[y];if(i==j)continue;
   bool single=rng()%6==0;if(single&&(count(cl[j])>=14||count(cl[i])<=5))continue;
   M a,b;if(single){a=cl[i]^(M(1)<<x);b=cl[j]^(M(1)<<x);}else{M delta=(M(1)<<x)|(M(1)<<y);a=cl[i]^delta;b=cl[j]^delta;}
   Stats sa=stats(a),sb=stats(b);int dc=sa.cost+sb.cost-scores[i].cost-scores[j].cost,db=sa.conflicts+sb.conflicts-scores[i].conflicts-scores[j].conflicts,de=dc+weight*db;
   if(de<=0 || uniform()<exp(-de/temp)){
    cl[i]=a;cl[j]=b;scores[i]=sa;scores[j]=sb;lab[x]=j;if(!single)lab[y]=i;total+=dc;conf+=db;
    int unchanged=0; if(conf>0&&conf<=2&&total<=10200)for(M a:cl)for(M b:original)unchanged+=a==b;
    if(conf>0&&conf<=2&&unchanged<=4&&total<far[conf]&&total<=10200){far[conf]=total;string fn=string(argv[5])+".far"+to_string(conf)+".json";write(fn.c_str(),cl,total,iterations);cerr<<"far "<<conf<<" cost "<<total<<" unchanged "<<unchanged<<" round "<<round<<endl;}
    if(conf>0&&conf<=2&&total<near[conf]&&total<=10040){near[conf]=total;string fn=string(argv[5])+".near"+to_string(conf)+".json";write(fn.c_str(),cl,total,iterations);cerr<<"near "<<conf<<" cost "<<total<<" round "<<round<<endl;}
    if(!conf&&total<best){best=total;winner=cl;write(argv[5],cl,best,iterations);cerr<<"best "<<best<<" round "<<round<<" iteration "<<iterations<<endl;}
   }
  }
  cerr<<"round "<<round<<" cost "<<total<<" conflicts "<<conf<<" best "<<best<<endl;
 }
}
