// X6 R67 D=6 exact inverse certificate: exhaustive parity/range enumeration.
#include <cstdio>
#include <algorithm>
#include <cstdint>
#include <array>
using namespace std;
int main() {
 constexpr int K=5, DEN=720, B=60;
 const int64_t N[K][K] = {
 {10530,-6915,2055,-285,15},
 {-10160,7440,-2420,360,-20},
 {5940,-4605,1605,-255,15},
 {-1944,1560,-570,96,-6},
 {274,-225,85,-15,1}};
 const int64_t M[K][K] = {
 {2,6,12,20,30},
 {6,24,60,120,210},
 {14,78,252,620,1290},
 {30,240,1020,3120,7770},
 {62,726,4092,15620,46650}};
 for(int i=0;i<K;i++) for(int j=0;j<K;j++) {
   int64_t t=0; for(int k=0;k<K;k++) t+=M[i][k]*N[k][j];
   if(t!=(i==j?DEN:0)) {printf("BAD_INVERSE %d %d\n",i,j);return 2;}
 }
 int minQ[62]; array<array<int,5>,62> witness{};long long counts[62]={};
 for(int i=0;i<62;i++)minQ[i]=999999;
 long long grid=0,slice=0,integers=0;int64_t z[K],a[K];
 for(int j0=-B;j0<=B;j0+=2)
 for(int j1=-B;j1<=B;j1+=2)
 for(int j2=-B;j2<=B;j2+=2)
 for(int j3=-B;j3<=B;j3+=2)
 for(int j4=-B;j4<=B;j4+=2) {
   grid++; z[0]=j0;z[1]=j1;z[2]=j2;z[3]=j3;z[4]=j4;
   int64_t lo=min<int64_t>(0,min({z[0],z[1],z[2],z[3],z[4]}));
   int64_t hi=max<int64_t>(0,max({z[0],z[1],z[2],z[3],z[4]}));
   int osc=(int)(hi-lo);
   if(osc==0||osc>=62)continue;
   slice++; bool valid=true;
   for(int k=0;k<K;k++) {
     int64_t t=0;for(int j=0;j<K;j++)t+=N[k][j]*z[j];
     if(t%DEN!=0){valid=false;break;}
     a[k]=t/DEN;
   }
   if(!valid)continue;
   integers++;int pos=0,neg=0;
   for(int k=0;k<K;k++)if(a[k]>0)pos+=(int)a[k];else neg-=(int)a[k];
   int q=max(pos,neg);
   if(q<minQ[osc]){minQ[osc]=q;for(int k=0;k<K;k++)witness[osc][k]=(int)a[k];}
   counts[osc]++;
 }
 printf("grid=%lld osc_sliced=%lld integral_nonzero=%lld\n",grid,slice,integers);
 for(int osc=2;osc<62;osc+=2)if(minQ[osc]<999999)
   printf("osc=%d min_q=%d candidates=%lld a=%d,%d,%d,%d,%d\n",
      osc,minQ[osc],counts[osc],witness[osc][0],witness[osc][1],
      witness[osc][2],witness[osc][3],witness[osc][4]);
}
