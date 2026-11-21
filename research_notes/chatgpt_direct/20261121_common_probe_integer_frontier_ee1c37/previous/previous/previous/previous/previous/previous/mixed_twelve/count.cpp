#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;
int bit(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
int size(M m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
struct R{M m;unsigned zeros,ones,minus;int type;};
vector<R> inventory;M masks[15];U nodes;vector<M> table;
uint64_t leaves=0;
void record(){++leaves; ofstream out("mixed24.solutions",ios::app); for(auto m:table)out<<U(m)<<" "<<U(m>>64)<<" ";out<<"\n";}
bool solve(M free,int n9,int good,int uneven,const vector<int>&before){
 ++nodes;const int k=n9+good+uneven;
 if(!k)return !free;
 unsigned s0=0,s1=0,se=0,sf=0;int budget[15];
 for(int j=0;j<15;j++){
  const int d=2*k-size(free&masks[j]);
  if(d < -uneven || d>n9+uneven)return false;
  budget[j]=d;
  s0|=unsigned(d==-uneven)<<j;
  s1|=unsigned(d==1-uneven)<<j;
  se|=unsigned(d==n9+uneven)<<j;
  sf|=unsigned(d==n9+uneven-1)<<j;
 }
 vector<int> opts;opts.reserve(before.size());M cover=0;int counts[3]={};
 for(int i:before){auto&r=inventory[i];if(r.m&~free)continue;
  if(r.type==0){
   if(!n9 || (r.ones&s0) || (se&~r.ones))continue;
  }else if(r.type==1){
   if(!good)continue;
  }else{
   if(!uneven || (r.ones&(s0|s1)) || (r.minus&(se|sf)) || (s0&~r.minus)||(se&~r.ones))continue;
  }
  cover|=r.m;opts.push_back(i);counts[r.type]++;
 }
 if(cover!=free || counts[0]<n9||counts[1]<good||counts[2]<uneven)return false;
 if(k==1){table.push_back(inventory[opts[0]].m);record();table.pop_back();return false;}
 int pop[125]{};
 for(int i:opts)for(M m=inventory[i].m;m;m&=m-1)++pop[bit(m)];
 int minopt=10000000,pt=-1,type=-1;
 for(M v=free;v;v&=v-1){int x=bit(v);if(pop[x]<minopt){minopt=pop[x];pt=x;}}
 for(int t=0;t<3;t++)if((t==0?n9:t==1?good:uneven)==1 && counts[t]<minopt){minopt=counts[t];type=t;}
 // With no uneven rows left, a positive singleton deficit of one is a further exact-cover column.
 int slice=-1;
 if(!uneven){
  for(int j=0;j<15;j++)if(budget[j]==1){
   int cnt=0;for(int i:opts)cnt+=bool(inventory[i].ones&(1<<j));if(cnt==0)return false;
   if(cnt<minopt){minopt=cnt;slice=j;type=-1;}
  }
 }
 for(int i:opts){auto&r=inventory[i];
  if(slice>=0?!(r.ones>>slice&1):type>=0?r.type!=type:!(r.m>>pt&1))continue;
  table.push_back(r.m);if(solve(free^r.m,n9-(r.type==0),good-(r.type==1),uneven-(r.type==2),opts))return true;table.pop_back();
 }
 return false;
}
int main(int argc,char**argv){
 ifstream f(argv[1]),a(argv[2]);int begin=stoi(argv[3]),end=stoi(argv[4]);
 bool uneven=string(argv[5])=="two747";
 for(int i=0;i<125;i++){masks[i/25]|=M(1)<<i;masks[5+i/5%5]|=M(1)<<i;masks[10+i%5]|=M(1)<<i;}
 int s,c,n,i;
 while(f>>s>>c>>n)while(n--){U l,h;f>>l>>h>>i;if(c!=557&&c!=744&&c!=747)continue;
  R r{(M(h)<<64)|l,0,0,0,c==557?0:c==744?1:2};
  for(int j=0;j<15;j++){int d=2-size(r.m&masks[j]);if(d==-1)r.minus|=1<<j;else if(d==1)r.ones|=1<<j;else if(d!=0)return 2;}
  if(__builtin_popcount(r.minus)!=(r.type==2)||__builtin_popcount(r.ones)!=(r.type==2?1:r.type==0?3:0))return 3;
  inventory.push_back(r);}


 int idx=0,nfix,n9,nt;
 while(a>>nfix){
  vector<M> fixed;
  M free=(M(1)<<125)-1;
  for(int i=0;i<nfix;i++){
   U l,h;a>>l>>h;M m=(M(h)<<64)|l;fixed.push_back(m);free^=m;
  }
  a>>n9>>nt;
  if(idx<begin||idx>=end){idx++;continue;}
  vector<int>pool;
  for(int i=0;i<int(inventory.size());i++)if(inventory[i].type!=(uneven?1:2)&&!(inventory[i].m&~free))pool.push_back(i);
  table=fixed;nodes=0;bool found=solve(free,n9,uneven?0:nt,uneven?nt:0,pool);
  cout<<idx<<" "<<leaves<<" "<<nodes<<endl;
  if(found){ofstream out("hit-"+string(argv[5])+"-"+to_string(idx)+".txt");for(M m:table){for(;m;m&=m-1)out<<bit(m)<<" ";out<<"\n";}return 0;}
  idx++;
 }
}
