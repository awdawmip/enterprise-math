// PREFIX914: exact complement count for signed dyadic k=3,l=1 vs PREFIX912 union.
// Compile: g++ -std=c++17 -O3 -Wall -Wextra -pedantic PREFIX914_R6_SIGNED_DYADIC_912_OVERLAP.cpp -o p914 && ./p914
#include <bits/stdc++.h>
using namespace std;
using LL=long long;
constexpr int A=262145,B=524287,M=131072;
constexpr LL N=1LL<<32,T=33*N;
unordered_set<int> gaps,base,mid,hi,special,panels,d907,d908,dyadic0;
void init(){
 for(int h=1;h<18;h++)base.insert(1<<h);
 for(int i=2;i<18;i++)for(int j=1;j<i;j++){base.insert((1<<i)+(1<<j));base.insert((1<<i)-(1<<j));}
 for(int m=3;m<8192;m+=2)for(int i=2;i<18;i++)for(int j=1;j<i;j++)
 for(int v:{(1<<i)+(1<<j),(1<<i)-(1<<j)})if(v%m==0){int d=v/m;if(d>0&&d<=B-A&&d%2==0&&!base.count(d))mid.insert(d);}
 for(int m=1;m<8192;m+=2)for(int i=18;i<31;i++)for(int j=1;j<18;j++)
 for(LL v:{(1LL<<i)+(1LL<<j),(1LL<<i)-(1LL<<j)})if(v%m==0){LL d=v/m;if(d>0&&d<=B-A&&d%2==0&&!base.count((int)d)&&!mid.count((int)d))hi.insert((int)d);}
 gaps=base;gaps.insert(mid.begin(),mid.end());gaps.insert(hi.begin(),hi.end());
 for(int q:{262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285})special.insert(q);
 for(int q=400011;q<400522;q+=2)special.insert(q);
 for(int q=480011;q<480522;q+=2)special.insert(q);
 for(int q=A;q<=B;q+=2)for(int h=1;h<32;h++)if(((1LL<<h)-1)%q==0||((1LL<<h)+1)%q==0){special.insert(q);break;}
 for(int j=0;j<64;j++)for(int z:{1,3,5})panels.insert(510000+z+194*j);
 for(int i=18;i<23;i++)for(int j=1;j<18;j++)for(int s:{-1,1})d907.insert((1<<i)+s*(1<<j));
 for(int i=1;i<20;i++)for(int s:{-1,1})d908.insert((1<<i)+s);
 for(int i=1;i<=22;i++)for(int s:{-1,1})dyadic0.insert((1<<i)+s);
 if(make_tuple(base.size(),mid.size(),hi.size(),special.size(),panels.size(),d907.size(),d908.size())!=
 make_tuple((size_t)258,(size_t)276,(size_t)857,(size_t)552,(size_t)192,(size_t)169,(size_t)37))throw runtime_error("old family regression mismatch");
}
bool covered(int a,int b){return LL(a)*b<T||special.count(a)||special.count(b)||LL(a/gcd(a,b))*b<N
 ||33*((N+a-1)/a)>b||33*((N+b-1)/b)>a||panels.count(a)||panels.count(b)
 ||gaps.count(abs(a-b))||d907.count(3*a-b)||d907.count(3*b-a)
 ||d908.count(2*a-b)||d908.count(2*b-a);}
bool old_mixed(int a,int b){
 for(int k=1;k<=12;k++)for(int l=1;l<=12;l++)if((k-l)&1){
   if(dyadic0.count(k*a-l*b)||dyadic0.count(k*b-l*a))return true;
 }
 return false;
}
int main(){
 init();unordered_set<int> ds;
 for(int i=2;i<=22;i++)for(int j=1;j<i;j++)for(int eps:{-1,1})for(int eta:{-1,1})
 ds.insert(eps*(1<<i)-eta*(1<<j));
 LL raw=0,rawOverlap=0,rawDiagonal=0,oldBase=0,oldMixedOnly=0,newA=0,newOverlap=0,newDiagonal=0;
 int exampleA=0,exampleB=0,exampleD=0;
 vector<pair<int,int>> classes;
 for(int d:ds){
   int lo=max(A,(int)((LL(A)+d+2)/3)),hi=min(B,(int)((LL(B)+d)/3));
   while(3LL*lo-d<A)lo++;
   while(3LL*hi-d>B)hi--;
   if(lo%2==0)lo++;
   if(lo<=hi)classes.emplace_back(d,lo);
 }
 sort(classes.begin(),classes.end());
 for(auto [d,lo]:classes){
  int hi=min(B,(int)((LL(B)+d)/3));
  while(3LL*hi-d>B)hi--;
  for(int a=lo;a<=hi;a+=2){
   int b=3*a-d;
   if(a<A||a>B||b<A||b>B||!(a&1)||!(b&1)||3*a-b!=d)throw runtime_error("invalid family construction");
   raw++;bool symmetric=ds.count(3*b-a);
   rawOverlap+=symmetric;rawDiagonal+=(a==b);
   bool old=covered(a,b);
   if(old)oldBase++;
   else if(old_mixed(a,b))oldMixedOnly++;
   else{
     newA++;newOverlap+=symmetric;newDiagonal+=(a==b);
     if(!exampleA){exampleA=a;exampleB=b;exampleD=d;}
   }
  }
 }
 cout<<"RAW "<<raw<<" RAW_INTERSECTION_TRANSPOSE "<<rawOverlap<<" RAW_DIAGONAL "<<rawDiagonal<<"\n";
 cout<<"OLD_BASE "<<oldBase<<" OLD_MIXED_ONLY "<<oldMixedOnly<<"\n";
 cout<<"NOVEL_ORIENTED "<<newA<<" NOVEL_TRANSPOSE_INTERSECTION "<<newOverlap<<" NOVEL_DIAGONAL "<<newDiagonal<<"\n";
 cout<<"NEW_SYMMETRIC_ORDERED "<<2*newA-newOverlap<<"\n";
 cout<<"UPDATED_912_UNION "<<7795529828LL+2*newA-newOverlap<<"\n";
 cout<<"EXAMPLE_UNCOVERED "<<exampleA<<" "<<exampleB<<" "<<exampleD<<"\n";
 if(raw!=3036491||rawOverlap!=362||rawDiagonal!=2)return 2;
 if(oldBase+oldMixedOnly+newA!=raw)return 3;
 if(oldBase!=2963137||oldMixedOnly!=95||newA!=73259||newOverlap!=0||newDiagonal!=0)return 4;
 return 0;
}
