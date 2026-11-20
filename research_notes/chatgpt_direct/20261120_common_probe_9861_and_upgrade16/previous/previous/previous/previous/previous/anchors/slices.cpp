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
int type(int p){return p==557?0:p==744?1:2;}
bool solve(Mask free,int ns,int nt,int odd,const std::vector<int>& pool){
    ++nodes;
    if(!free)return !ns&&!nt&&!odd;
    int labels=ns+nt+odd;
    unsigned lo=0,hi=0,lo1=0,hi1=0;
    int need[15];
    for(int j=0;j<15;j++){
        int d=2*labels-number(free&slices[j]);
        if(d< -odd || d>ns+odd)return false;
        need[j]=d;
        lo|=unsigned(d==-odd)<<j;hi|=unsigned(d==ns+odd)<<j;
        lo1|=unsigned(d==1-odd)<<j;hi1|=unsigned(d==ns+odd-1)<<j;
    }
    int count[3]={};int fqty[15]={};Mask union_rows=0;
    std::vector<int> active;active.reserve(pool.size());
    for(int i:pool){
        auto &r=rows[i];int k=type(r.price);if(r.mask&~free)continue;
        if(k==0&&(!ns||(r.plus&lo)||(hi&~r.plus)))continue;
        if(k==1&&!nt)continue;
        if(k==2&&(!odd||(r.plus&(lo|lo1))||(r.minus&(hi|hi1))||(lo&~r.minus)||(hi&~r.plus)))continue;
        union_rows|=r.mask;active.push_back(i);count[k]++;
        if(k==0&&odd==0)for(unsigned z=r.plus;z;z&=z-1)fqty[__builtin_ctz(z)]++;
    }
    if(union_rows!=free||count[0]<ns||count[1]<nt||count[2]<odd)return false;
    if(labels==1){answer.push_back(rows[active[0]].mask);return true;}
    int hist[125]={},best=100000,pivot=-1;
    for(int i:active)for(Mask m=rows[i].mask;m;m&=m-1)hist[first(m)]++;
    for(Mask m=free;m;m&=m-1){int p=first(m);if(hist[p]<best){best=hist[p];pivot=p;}}
    int max[3]={ns,nt,odd};
    for(int j=0;j<3;j++)if(max[j]==1&&count[j]<best){best=count[j];pivot=140+j;}
    if(!odd)for(int j=0;j<15;j++){
        if(fqty[j]<need[j])return false;
        if(need[j]==1&&fqty[j]<best){best=fqty[j];pivot=125+j;}
    }
    for(int i:active){
        auto &r=rows[i];int t=type(r.price);
        if(pivot<125&&!(r.mask>>pivot&1))continue;
        if(125<=pivot&&pivot<140&&(t!=0||!(r.plus>>(pivot-125)&1)))continue;
        if(pivot>=140&&t!=pivot-140)continue;
        answer.push_back(r.mask);
        if(solve(free^r.mask,ns-(t==0),nt-(t==1),odd-(t==2),active))return true;
        answer.pop_back();
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
   Word lo,hi;data>>lo>>hi;if(c!=557&&c!=744&&c!=price)continue;
   Mask m=Mask(hi)<<64|lo;unsigned plus=0,minus=0;
   for(int j=0;j<15;j++){int v=2-number(slices[j]&m);if(v<-1||v>1)return 3;plus|=unsigned(v==1)<<j;minus|=unsigned(v==-1)<<j;}
   rows.push_back({m,c,plus,minus});
  }
 }
 Word a,b,c,d;int idx=0;while(pairs>>a>>b>>c>>d){
  if(idx++!=chosen)continue;
  Mask x=Mask(b)<<64|a,y=Mask(d)<<64|c;std::vector<int> active;Mask used=x|y;
  for(int j=0;j<rows.size();j++)if(!(rows[j].mask&used))active.push_back(j);
  nodes=0;answer={x,y};bool found=solve(ALL^used,9,1,1,active);
  std::cout<<chosen<<" "<<price<<" "<<active.size()<<" "<<nodes<<" "<<found<<std::endl;
  if(found){std::ofstream out("special"+std::to_string(chosen)+"_"+std::to_string(price)+".txt");for(Mask m:answer){for(;m;m&=m-1)out<<first(m)<<" ";out<<"\n";}}
 }
}
