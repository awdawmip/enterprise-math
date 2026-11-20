#include <cstdio>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
using namespace std;
int main(){
 const int maxP=26;
 long long visited=0,feasible=0;
 int minOsc[maxP+1];int aa[maxP+1][4]; long long minTies[maxP+1];
 for(int p=0;p<=maxP;p++){minOsc[p]=1000000000;minTies[p]=0;}
 for(int a=-maxP;a<=maxP;a++) for(int b=-maxP;b<=maxP;b++) for(int c=-maxP;c<=maxP;c++) for(int d=-maxP;d<=maxP;d++) {
  visited++;
  if(a==0&&b==0&&c==0&&d==0)continue;
  int pos=max(0,a)+max(0,b)+max(0,c)+max(0,d);
  int neg=max(0,-a)+max(0,-b)+max(0,-c)+max(0,-d);
  int minP=max(pos,neg);if(minP>maxP)continue;
  feasible++;
  int z2=2*a+6*b+12*c+20*d;
  int z3=6*a+24*b+60*c+120*d;
  int z4=14*a+78*b+252*c+620*d;
  int z5=30*a+240*b+1020*c+3120*d;
  int hi=max({0,z2,z3,z4,z5});int lo=min({0,z2,z3,z4,z5});int osc=hi-lo;
  for(int p=max(5,minP);p<=maxP;p++){
    if(osc<minOsc[p]){minOsc[p]=osc;aa[p][0]=a;aa[p][1]=b;aa[p][2]=c;aa[p][3]=d;minTies[p]=1;}
    else if(osc==minOsc[p]) minTies[p]++;
  }
 }
 printf("visited=%lld feasible=%lld\n",visited,feasible);
 for(int p=5;p<=maxP;p++)printf("p=%d osc=%d eta=%d/4 a=(%d,%d,%d,%d) ties=%lld\n",p,minOsc[p],minOsc[p],aa[p][0],aa[p][1],aa[p][2],aa[p][3],minTies[p]);
}
