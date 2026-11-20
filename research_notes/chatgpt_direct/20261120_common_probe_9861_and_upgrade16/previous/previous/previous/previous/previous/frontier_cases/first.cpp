#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

using Mask = __uint128_t;
using Word = std::uint64_t;
constexpr Mask ALL = (Mask(1) << 125) - 1;
int first(Mask m){return Word(m)?__builtin_ctzll(Word(m)):64+__builtin_ctzll(Word(m>>64));}
int number(Mask m){return __builtin_popcountll(Word(m))+__builtin_popcountll(Word(m>>64));}
struct Row { Mask mask; int price; unsigned plus,minus; };
std::vector<Row> rows;
std::array<Mask,15> slices{};
Word nodes;
std::vector<Mask> answer;
int type(int p){return p==557?0:p==564?1:p==744?2:3;}
bool solve(Mask free,int nmin,int nplus,int tens,int odd,const std::vector<int>&pool){
 ++nodes;if(!free)return nmin+nplus+tens+odd==0;int n9=nmin+nplus,labels=n9+tens+odd;
 unsigned lo=0,hi=0,lo1=0,hi1=0;int n[15];
 for(int j=0;j<15;j++){int v=2*labels-number(free&slices[j]);n[j]=v;if(v< -odd||v>n9+odd)return false;
 lo|=unsigned(v==-odd)<<j;hi|=unsigned(v==n9+odd)<<j;lo1|=unsigned(v==1-odd)<<j;hi1|=unsigned(v==n9+odd-1)<<j;}
 int cnt[4]={},need[4]={nmin,nplus,tens,odd},donors[15]={},freq[125]={};Mask cover=0;std::vector<int> opts;
 for(int i:pool){auto&r=rows[i];int t=type(r.price);if(!need[t]||r.mask&~free)continue;
 if(t<=1&&((lo&r.plus)||(hi&~r.plus)))continue;
 if(t==3&&((r.plus&(lo|lo1))||(r.minus&(hi|hi1))||(lo&~r.minus)||(hi&~r.plus)))continue;
 opts.push_back(i);cnt[t]++;cover|=r.mask;
 }
 if(cover!=free)return false;
 for(int j=0;j<4;j++)if(cnt[j]<need[j])return false;
 int few=100000,piv=-1;for(int i:opts){auto&r=rows[i];for(Mask m=r.mask;m;m&=m-1)freq[first(m)]++;if(type(r.price)<=1&&!odd)for(unsigned v=r.plus;v;v&=v-1)donors[__builtin_ctz(v)]++;}
 for(Mask m=free;m;m&=m-1){int j=first(m);if(freq[j]<few){piv=j;few=freq[j];}}
 for(int j=0;j<4;j++)if(need[j]==1 && cnt[j]<few){few=cnt[j];piv=140+j;}
 for(int j=0;j<15&&!odd;j++){if(donors[j]<n[j])return false;if(n[j]==1&&donors[j]<few){piv=125+j;few=donors[j];}}
 for(int i:opts){auto&r=rows[i];int t=type(r.price);
 if(piv<125&&!(r.mask>>piv&1))continue;if(piv>=125&&piv<140&&(t>=2||!(r.plus>>(piv-125)&1)))continue;if(piv>=140&&t!=piv-140)continue;
 answer.push_back(r.mask);if(solve(free^r.mask,nmin-(t==0),nplus-(t==1),tens-(t==2),odd-(t==3),opts))return true;answer.pop_back();
 }
 return false;
}
int main(int argc,char**argv){
 std::ifstream data(argv[1]),pairs(argv[2]);int ntypes;data>>ntypes;
 int price=std::stoi(argv[3]),chosen=std::stoi(argv[4]);
 for(int i=0;i<125;i++){slices[i/25]|=Mask(1)<<i;slices[5+i/5%5]|=Mask(1)<<i;slices[10+i%5]|=Mask(1)<<i;}
 while(ntypes--){
  int n,s,c;data>>s>>c>>n;
  while(n--){
   Word lo,hi;data>>lo>>hi;if(c!=557&&c!=564&&c!=744&&c!=price)continue;
   Mask m=Mask(hi)<<64|lo;unsigned plus=0,minus=0;
   for(int j=0;j<15;j++){int v=2-number(slices[j]&m);if(v<-1||v>1)return 3;plus|=unsigned(v==1)<<j;minus|=unsigned(v==-1)<<j;}
   rows.push_back({m,c,plus,minus});
  }
 }
 Word a,b,c,d;int idx=0;while(pairs>>a>>b>>c>>d){
  if(idx++!=chosen)continue;
  Mask x=Mask(b)<<64|a,y=Mask(d)<<64|c;std::vector<int> active;Mask used=x|y;
  for(int j=0;j<rows.size();j++)if(!(rows[j].mask&used))active.push_back(j);
  nodes=0;answer={x,y};bool found=solve(ALL^used,8,1,1,1,active);
  std::cout<<chosen<<" "<<price<<" "<<active.size()<<" "<<nodes<<" "<<found<<std::endl;
  if(found){std::ofstream out("special"+std::to_string(chosen)+"_"+std::to_string(price)+".txt");for(Mask m:answer){for(;m;m&=m-1)out<<first(m)<<" ";out<<"\n";}}
 }
}
