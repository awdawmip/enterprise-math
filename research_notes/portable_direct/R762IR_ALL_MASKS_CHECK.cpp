// R762IR independent dynamic-partition scan of all 2^20 support subsets.
// Compile: g++ -O3 -std=c++17 R762IR_ALL_MASKS_CHECK.cpp -o check2 && ./check2
#include <bits/stdc++.h>
using namespace std;
int main(){
 int id[6][6]={};int p=0;
 for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)id[a][b]=id[b][a]=p++;
 array<array<int,3>,20> T;int k=0;
 for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)
  for(int c=b+1;c<6;c++)T[k++]={id[a][b],id[a][c],id[b][c]};
 constexpr int N=1<<20;
 vector<uint64_t> part(N);
 uint64_t base=0;
 for(int i=0;i<15;i++)base|=(uint64_t)i<<(4*i);
 part[0]=base;
 int distribution[21]={},maxEssential=0;
 uint32_t example=0;
 long long countMinimal=0;
 int minRed[21];fill(minRed,minRed+21,100);
 for(int mask=1;mask<N;mask++){
  int bit=__builtin_ctz((unsigned)mask),prev=mask&(mask-1);
  uint64_t old=part[prev];
  int lab[15],mp[15];
  for(int i=0;i<15;i++)lab[i]=(old>>(4*i))&15;
  auto tr=T[bit];int x=lab[tr[0]],y=lab[tr[1]],z=lab[tr[2]];
  for(int i=0;i<15;i++)if(lab[i]==y||lab[i]==z)lab[i]=x;
  fill(mp,mp+15,-1);int nn=0;uint64_t enc=0;
  for(int i=0;i<15;i++){
   int &v=mp[lab[i]];
   if(v<0)v=nn++;
   enc|=(uint64_t)v<<(4*i);
  }
  part[mask]=enc;
  int total=__builtin_popcount((unsigned)mask),ess=0;
  for(int subset=mask;subset;subset&=subset-1){
   int j=__builtin_ctz((unsigned)subset);
   if(part[mask^(1<<j)]!=enc)ess++;
  }
  int red=total-ess;
  minRed[total]=min(minRed[total],red);
  distribution[ess]++;
  if(ess>maxEssential){maxEssential=ess;example=mask;}
  if(red==0)countMinimal++;
 }
 cout<<"max-essential="<<maxEssential<<" exemplar-mask="<<example
     <<" essential-only-count="<<countMinimal<<"\n";
 for(int j=1;j<=20;j++)
  cout<<"size="<<j<<" min-redundant="<<minRed[j]<<"\n";
 for(int j=0;j<=20;j++)if(distribution[j])
  cout<<"essential="<<j<<" count="<<distribution[j]<<"\n";
 assert(maxEssential==10);
 assert(minRed[10]==0 && minRed[11]==4 && minRed[14]==10);
 return 0;
}
