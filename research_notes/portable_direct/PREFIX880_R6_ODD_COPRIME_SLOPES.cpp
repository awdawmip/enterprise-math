// PREFIX-880 exact p=32 B=19 finite counter: g++ -std=c++17 -O3 -Wall -Wextra file.cpp -o checker && ./checker
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;
static constexpr int Q=(1<<19)-1;
set<int>D,Ds,E,S,E21;
vector<pair<int,int>> nexts={{5,2},{2,5},{7,2},{2,7},{5,4},{4,5},{7,4},{4,7}};
void init(){
 for(int i=1;i<19;i++)D.insert(1<<i);
 for(int i=2;i<19;i++)for(int j=1;j<i;j++)D.insert((1<<i)+(1<<j));
 for(int i=2;i<=19;i++)for(int j=1;j<i;j++)D.insert((1<<i)-(1<<j));
 Ds=D;Ds.insert(1<<19);Ds.insert(1<<20);
 for(int i=1;i<=19;i++)for(int t:{-1,1}){E.insert(t*((1<<i)-1));E.insert(t*((1<<i)+1));}
 for(int i=1;i<=21;i++)for(int t:{-1,1}){E21.insert(t*((1<<i)-1));E21.insert(t*((1<<i)+1));}
 for(int i=1;i<=21;i++)S.insert(1<<i);
 for(int i=2;i<=21;i++)for(int j=1;j<i;j++){S.insert((1<<i)-(1<<j));S.insert((1<<i)+(1<<j));}
 assert(D.size()==307&&Ds.size()==309&&E.size()==74&&S.size()==402&&E21.size()==82);
}
bool prev878(int x,int y){
 return D.count(abs(x-y))||Ds.count(3*x-y)||E.count(2*x-y)||E.count(2*y-x)||
 E.count(3*x-2*y)||E.count(2*x-3*y)||E.count(4*x-y)||E.count(x-4*y);
}
bool prev879(int x,int y){
 if(prev878(x,y))return true;
 for(int k:{5,7,9,11})if(S.count(abs(k*x-y))||S.count(abs(x-k*y)))return true;
 return false;
}
bool validpair(int x,int y){return x>=1&&x<=Q&&y>=1&&y<=Q&&(x&1)&&(y&1)&&x!=y;}
int main(){
 init(); long long all=0;
 cout<<"{\"schema\":\"PREFIX880_R6_RESULT_V1\",\"p\":32,\"B\":19,\"Q\":"<<Q<<",\"odd_gaps\":"<<E21.size()<<",\"slope_families\":[";
 for(size_t h=0;h<nexts.size();h++){
  int k=nexts[h].first,l=nexts[h].second;
  long long total=0,prior=0,earlier=0,fresh=0;
  for(int d:E21)for(int x=1;x<=Q;x+=2){
    int num=k*x-d;
    if(num%l)continue;
    int y=num/l;
    if(!validpair(x,y))continue;
    total++;
    if(prev879(x,y)){prior++;continue;}
    bool duplicate=false;
    for(size_t j=0;j<h;j++){
      auto [a,b]=nexts[j];
      if(E21.count(a*x-b*y)){duplicate=true;break;}
    }
    if(duplicate)earlier++;else fresh++;
  }
  assert(total==prior+earlier+fresh);
  if(h)cout<<",";
  cout<<"{\"slope\":\""<<k<<":"<<l<<"\",\"total\":"<<total<<",\"prior\":"<<prior<<",\"earlier\":"<<earlier<<",\"fresh\":"<<fresh<<"}";
  all+=fresh;
 }
 cout<<"],\"net_new\":"<<all<<",\"prior_cumulative_reported\":391001832,\"new_cumulative\":"<<(391001832LL+all)<<"}"<<endl;
}