// PREFIX-879: exact C++17 finite certificate for p=32, B=19.
// g++ -std=c++17 -O3 -Wall -Wextra PREFIX879_R6_MULTI_ODD_RATIO_CPP.cpp -o check && ./check
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
static constexpr int Q=(1<<19)-1;
set<int>D,Ds,E,S;
long long floorDiv(long long x,long long y){assert(y>0);long long q=x/y,r=x%y;if(r<0)--q;return q;}
long long ceilDiv(long long x,long long y){return -floorDiv(-x,y);}
void initialize(){
 for(int i=1;i<19;i++)D.insert(1<<i);
 for(int i=2;i<19;i++)for(int j=1;j<i;j++)D.insert((1<<i)+(1<<j));
 for(int i=2;i<=19;i++)for(int j=1;j<i;j++)D.insert((1<<i)-(1<<j));
 Ds=D; Ds.insert(1<<19); Ds.insert(1<<20);
 for(int i=1;i<=19;i++)for(int t:{-1,1}){
  E.insert(t*((1<<i)-1)); E.insert(t*((1<<i)+1));
 }
 for(int i=1;i<=21;i++)S.insert(1<<i);
 for(int i=2;i<=21;i++)for(int j=1;j<i;j++){
  S.insert((1<<i)-(1<<j)); S.insert((1<<i)+(1<<j));
 }
 assert(D.size()==307 && Ds.size()==309 && E.size()==74 && S.size()==402);
}
bool prev(int x,int y){
 return D.count(abs(x-y))||Ds.count(3*x-y)||E.count(2*x-y)||
 E.count(2*y-x)||E.count(3*x-2*y)||E.count(2*x-3*y)||
 E.count(4*x-y)||E.count(x-4*y);
}
int main(){
 initialize();
 vector<int> ks={5,7,9,11};
 const long long expectedFresh[]={34453483,34443526,24704877,24696971,
                                   19173855,19169655,15678760,15668855};
 long long grand=0;
 cout<<"{\"new_families\":[";
 int line=0;
 for(int k:ks)for(int ori=0;ori<2;ori++){
  long long total=0,old=0,earlier=0,fresh=0;
  for(int z:S)for(int sig:{-1,1}){
   int d=sig*z;
   long long lo,hi;
   if(ori==0){lo=ceilDiv(d+1,k);hi=floorDiv(Q+d,k);} // y=k*x-d
   else {lo=ceilDiv(1-d,k);hi=floorDiv(Q-d,k);} // x=k*y+d
   lo=max(1LL,lo);hi=min((long long)Q,hi);
   if(lo%2==0)lo++;
   for(int t=(int)lo;t<=hi;t+=2){
    int x=ori==0?t:k*t+d;
    int y=ori==0?k*t-d:t;
    if(x==y)continue;
    assert(x>0&&x<=Q&&y>0&&y<=Q&&(x&1)&&(y&1));
    total++;
    if(prev(x,y)){old++;continue;}
    bool duplicate=false;
    for(int pk:ks){
     if(pk>k)break;
     if(pk==k && ori==0)break;
     if(S.count(abs(pk*x-y)))duplicate=true;
     if(pk<k && S.count(abs(x-pk*y)))duplicate=true;
     if(duplicate)break;
    }
    if(duplicate)earlier++;else fresh++;
   }
  }
  assert(fresh==expectedFresh[line]);
  if(line++)cout<<",";
  cout<<"{\"ratio\":\""<<k<<(ori==0?":1":":reversed")
      <<"\",\"total\":"<<total<<",\"old\":"<<old
      <<",\"earlier_new\":"<<earlier<<",\"fresh\":"<<fresh<<"}";
  grand+=fresh;
 }
 assert(grand==187989982);
 cout<<"],\"net_new\":"<<grand
     <<",\"previous_coverage\":203011850"
     <<",\"cumulative\":"<<(203011850+grand)<<"}"<<endl;
}
