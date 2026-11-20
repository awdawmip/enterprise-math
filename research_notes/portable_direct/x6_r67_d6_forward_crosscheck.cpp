// X6 R67 D=6 independent exhaustive forward signed-difference checker.
#include <cstdio>
#include <cstdint>
#include <algorithm>
#include <array>
using namespace std;
int main() {
 const int P=57,D=6;
 int64_t b[D-1][D-1];
 for(int d=2;d<=D;d++){int64_t power=d;
   for(int t=2;t<=D;t++){power*=d;b[d-2][t-2]=power-d;}}
 int64_t best[P+1];array<int,P+1> ties{};
 array<array<int,5>,P+1> witness{};
 for(int p=0;p<=P;p++)best[p]=INT64_MAX;
 long long grid=0,feasible=0;int a[5];
 for(int a0=-P;a0<=P;a0++)
 for(int a1=-P;a1<=P;a1++)
 for(int a2=-P;a2<=P;a2++)
 for(int a3=-P;a3<=P;a3++)
 for(int a4=-P;a4<=P;a4++){
   grid++;a[0]=a0;a[1]=a1;a[2]=a2;a[3]=a3;a[4]=a4;
   int pos=0,neg=0;
   for(int j=0;j<5;j++)if(a[j]>0)pos+=a[j];else neg-=a[j];
   int q=max(pos,neg);if(q>P||q==0)continue;feasible++;
   int64_t hi=0,lo=0;
   for(int t=0;t<5;t++){int64_t z=0;
     for(int j=0;j<5;j++)z+=a[j]*b[j][t];
     hi=max(hi,z);lo=min(lo,z);}
   int64_t osc=hi-lo;
   if(osc<best[q]){best[q]=osc;ties[q]=1;
      for(int j=0;j<5;j++)witness[q][j]=a[j];}
   else if(osc==best[q])ties[q]++;
 }
 printf("grid=%lld feasible_nonzero=%lld\n",grid,feasible);
 int64_t minimum=INT64_MAX;int best_q=0;
 for(int p=1;p<=P;p++){
   if(best[p]<minimum){minimum=best[p];best_q=p;}
   if(p<6)continue;
   printf("p=%d exact_q_best=%lld cumulative_osc=%lld eta=%.4f witness_q=%d a=%d,%d,%d,%d,%d\n",
      p,(long long)best[p],(long long)minimum,minimum/4.0,best_q,
      witness[best_q][0],witness[best_q][1],witness[best_q][2],
      witness[best_q][3],witness[best_q][4]);
 }
}
