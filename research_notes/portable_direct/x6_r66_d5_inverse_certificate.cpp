#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
 int minPop[30]; int best[30][8]; long long hits[30]={}, candidates=0,checks=0;
 for(int i=0;i<30;i++)minPop[i]=1000000;
 for(int x=-28;x<=28;x+=2)for(int y=-28;y<=28;y+=2)for(int z=-28;z<=28;z+=2)for(int w=-28;w<=28;w+=2){
  int hi=max({0,x,y,z,w}),lo=min({0,x,y,z,w}),osc=hi-lo;
  if(osc>28 || osc==0)continue;
  checks++;
  int A=1070*x-590*y+130*z-10*w;
  int B=-780*x+490*y-120*z+10*w;
  int C=305*x-205*y+55*z-5*w;
  int D=-50*x+35*y-10*z+w;
  if(A%120||B%120||C%120||D%120)continue;
  A/=120;B/=120;C/=120;D/=120;
  if(!(A||B||C||D))continue;
  candidates++;
  int pos=max(0,A)+max(0,B)+max(0,C)+max(0,D);
  int neg=max(0,-A)+max(0,-B)+max(0,-C)+max(0,-D);
  int p=max(pos,neg);
  hits[osc]++;
  if(p<minPop[osc]){minPop[osc]=p;int arr[8]={x,y,z,w,A,B,C,D};copy(arr,arr+8,best[osc]);}
 }
 printf("dual_checks=%lld integer_candidates=%lld\n",checks,candidates);
 for(int osc=2;osc<=28;osc+=2)if(hits[osc])printf("osc %d minPop %d count %lld z(%d,%d,%d,%d) a(%d,%d,%d,%d)\n",osc,minPop[osc],hits[osc],best[osc][0],best[osc][1],best[osc][2],best[osc][3],best[osc][4],best[osc][5],best[osc][6],best[osc][7]);
}
