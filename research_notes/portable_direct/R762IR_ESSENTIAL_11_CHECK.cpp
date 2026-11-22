// R762IR: complete exact 10/11-subset support-triangle census.
// Compile: g++ -O3 -std=c++17 R762IR_ESSENTIAL_11_CHECK.cpp -o check && ./check
#include <array>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdint>
using namespace std;
array<array<int,3>,20> tri;
int cnt10=0,cnt11=0,allessential10=0,allessential11=0;
vector<unsigned> sharp;
struct UF {
 int p[15];
 UF(){for(int i=0;i<15;i++)p[i]=i;}
 int rt(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
 void unite(int a,int b){p[rt(a)]=rt(b);}
 bool equiv(UF &u){
  for(int i=0;i<15;i++)
   for(int j=i+1;j<15;j++)
    if((rt(i)==rt(j))!=(u.rt(i)==u.rt(j)))return false;
  return true;
 }
};
UF build(unsigned m){
 UF a;
 for(int s=0;s<20;s++)if((m>>s)&1){
  auto t=tri[s];a.unite(t[0],t[1]);a.unite(t[1],t[2]);
 }
 return a;
}
void check(unsigned m,int count){
 UF full=build(m);bool all=true;
 for(int s=0;s<20;s++)if((m>>s)&1){
  UF rem=build(m^(1u<<s));
  if(full.equiv(rem)){all=false;break;}
 }
 if(count==10){cnt10++;if(all){allessential10++;sharp.push_back(m);}}
 else {cnt11++;if(all)allessential11++;}
}
void gen(int start,int remain,unsigned m,int len){
 if(!remain){check(m,len);return;}
 for(int j=start;j<=20-remain;j++)gen(j+1,remain-1,m|(1u<<j),len);
}
int main(){
 int i=0,id[6][6]={};
 for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)id[a][b]=id[b][a]=i++;
 i=0;
 for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)
  for(int c=b+1;c<6;c++)tri[i++]={id[a][b],id[a][c],id[b][c]};
 gen(0,10,0,10);gen(0,11,0,11);
 printf("ten=%d allessential10=%d eleven=%d allessential11=%d\n",
    cnt10,allessential10,cnt11,allessential11);
 for(unsigned m:sharp)printf("sharp_mask=%u\n",m);
 return allessential10==6&&allessential11==0
   &&cnt10==184756&&cnt11==167960?0:1;
}
