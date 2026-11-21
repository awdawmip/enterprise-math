// R86: independent full-shell atlas audit and global strict-winner tests.
// Build: g++ -O3 -std=c++17 x6_r86_global_nine_verify.cpp -o /tmp/r86 && /tmp/r86
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
using V=array<int,3>;using G=array<int,6>;using W=array<int,4>;
int q(V a){int p=0,n=0;for(int x:a){p+=max(0,x);n+=max(0,-x);}return max(p,n);}
G gap(V a){long long x=a[0],y=a[1],z=a[2];
 long long t[4]={0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z};
 return {int(llabs(t[1]-t[0])/2),int(llabs(t[2]-t[0])/2),int(llabs(t[3]-t[0])/2),
         int(llabs(t[2]-t[1])/2),int(llabs(t[3]-t[1])/2),int(llabs(t[3]-t[2])/2)};}
struct Ratio{int64_t n,d;};
int cmp(Ratio x, Ratio y){int64_t v=x.n*y.d-y.n*x.d;return (v>0)-(v<0);}
Ratio cost(G g,W w){const int d[6]={w[0]+w[1],w[0]+w[2],w[0]+w[3],w[1]+w[2],w[1]+w[3],w[2]+w[3]};Ratio f={0,1};for(int i=0;i<6;i++)if(int64_t(g[i])*f.d>f.n*d[i])f={g[i],d[i]};return f;}
int main(){
 const V atlas[]={ {1,0,0},{0,2,-1},{1,-3,1},{2,-3,1},{3,-1,0},{1,3,-1},{3,-4,1},{4,-1,0},
 {3,2,-1},{4,-4,1},{5,-1,0},{5,-4,1},{6,-1,0},{3,-7,2},{6,-4,1},{7,-1,0},
 {7,2,-1},{9,-5,1},{10,-5,1},{15,-6,1},{21,-7,1},{24,-14,3},{36,-16,3},
 {39,-20,4},{42,-24,5},{45,-21,4},{66,-28,5},{114,-56,11} };
 const V core[]={ {6,-4,1},{9,-5,1},{10,-5,1},{15,-6,1},{24,-14,3},
 {36,-16,3},{39,-20,4},{45,-21,4},{114,-56,11} };
 const W weights[]={ {8,8,26,187},{3,3,20,34},{2,2,2,2},{7,1,1,15},{163,165,1809,388},
 {199,41,18,18},{7,15,1,1},{1,15,7,1},{2,47,3,2} };
 const int K=9,Q=234;
 Ratio best[K];int need[K];for(int i=0;i<K;i++){best[i]=cost(gap(core[i]),weights[i]);need[i]=q(core[i]);}
 G atlasg[28];int atlasq[28];for(int i=0;i<28;i++){atlasg[i]=gap(atlas[i]);atlasq[i]=q(atlas[i]);}
 uint64_t total=0,covered=0,ties[K]={},below[K]={};V unexpected[K]={};
 for(int a=0;a<=Q;a++)for(int b=-Q;b<=Q;b++){
  if(a==0&&b<0)continue;
  int positive=a+max(b,0),negative=max(-b,0);
  if(max(positive,negative)>Q)continue;
  const int lo=negative-Q,hi=Q-positive;
  for(int c=lo;c<=hi;c++){
   if(a==0&&b==0&&c<=0)continue;
   V v={a,b,c};int demand=q(v);G g=gap(v);total++;
   bool cover=false;
   for(int i=0;i<28;i++){
    if(atlasq[i]>demand)continue;
    bool yes=true;for(int j=0;j<6;j++)if(atlasg[i][j]>g[j]){yes=false;break;}
    if(yes){cover=true;break;}
   }
   if(cover)covered++;
   else if(total-covered==1){cerr<<"ATLAS_MISS "<<a<<","<<b<<","<<c<<"\n";}
   for(int i=0;i<K;i++){
    int t=cmp(cost(g,weights[i]),best[i]);
    if(t<0){below[i]++;if(below[i]==1)unexpected[i]=v;}
    if(t==0){ties[i]++;if(v!=core[i] && ties[i]<=3)cerr<<"TIE "<<i<<" "<<a<<","<<b<<","<<c<<"\n";}
   }
  }
 }
 cout<<"{\"max_q_checked\":"<<Q<<",\"unoriented_tested\":"<<total
     <<",\"atlas_covered\":"<<covered<<",\"atlas_failures\":"<<(total-covered)<<",\"winners\":[";
 for(int i=0;i<K;i++){
  if(i)cout<<",";
  cout<<"{\"q\":"<<need[i]<<",\"vector\":["<<core[i][0]<<","<<core[i][1]<<","<<core[i][2]
      <<"],\"weights\":["<<weights[i][0]<<","<<weights[i][1]<<","<<weights[i][2]<<","<<weights[i][3]
      <<"],\"optimum_raw\":\""<<best[i].n<<"/"<<best[i].d
      <<"\",\"below\":"<<below[i]<<",\"ties\":"<<ties[i]<<"}";
 }
 cout<<"],\"pass\":"<<((total==21492159 && covered==total && all_of(ties,ties+K,[](uint64_t t){return t==1;}) && all_of(below,below+K,[](uint64_t t){return t==0;}))?"true":"false")<<"}\n";
 return (total==21492159 && covered==total && all_of(ties,ties+K,[](uint64_t t){return t==1;}) && all_of(below,below+K,[](uint64_t t){return t==0;}))?0:1;
}
