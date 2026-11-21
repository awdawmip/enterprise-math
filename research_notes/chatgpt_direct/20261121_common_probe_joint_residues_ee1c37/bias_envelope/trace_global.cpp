#include <algorithm>
#include <functional>
#include <tuple>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 if(argc!=4)return 2;int cap=stoi(argv[2]);ifstream in(argv[1]);int n;in>>n;vector<pair<int,int>> option[13];int mincost[13];fill(mincost,mincost+13,1000000);
 for(int i=0;i<n;i++){int size,cost,diff;in>>size>>cost>>diff;if(size<1||size>13||cost<0||diff<0||diff>cost||((cost-diff)&1))return 3;int deficit=13-size;option[deficit].push_back({cost,diff});mincost[deficit]=min(mincost[deficit],cost);}
 for(auto&v:option)sort(v.begin(),v.end());
 constexpr int K=11,T=18,INF=1000000;int least[K+1][T+1];for(auto& row:least)fill(row,row+T+1,INF);least[0][0]=0;
 for(int k=1;k<=K;k++)for(int d=0;d<=T;d++)for(int s=0;s<=min(12,d);s++)least[k][d]=min(least[k][d],least[k-1][d-s]+mincost[s]);
 size_t stride=cap+1,N=(T+1)*stride;vector<int16_t>a(N,-1),b(N,-1);a[0]=0;vector<vector<int16_t>>history{a};uint64_t updates=0,states=0;
 for(int k=0;k<K;k++){
  fill(b.begin(),b.end(),-1);
  for(int d=0;d<=T;d++){
   int hi=cap-least[K-k][T-d];if(least[k][d]>hi)continue;
   for(int cost=least[k][d];cost<=hi;cost++){
    int previous=a[d*stride+cost];if(previous<0)continue;states++;
    for(int s=0;s<=min(12,T-d);s++){
     int nextd=d+s,maxnext=cap-least[K-k-1][T-nextd];if(maxnext<cost+mincost[s])continue;
     for(auto [price,diff]:option[s]){
      int nextc=cost+price;if(nextc>maxnext)break;int candidate=previous+diff;if(candidate>32767)return 4;
      auto&target=b[nextd*stride+nextc];if(candidate>target){target=candidate;updates++;}
     }
    }
   }
  }
  a.swap(b);history.push_back(a);
 }
 cerr<<"states "<<states<<" updates "<<updates<<" peak_dp_bytes "<<(history.size()+2)*N*sizeof(int16_t)<<" global_minimum_cost "<<least[K][T]<<"\n";
 int target=stoi(argv[3]);if(target<0||target>cap)return 9;int value=a[T*stride+target];if(value<0)return 10;
 vector<tuple<int,int,int>>all;for(int d=0;d<=12;d++)for(auto [c,v]:option[d])all.push_back({d,c,v});sort(all.begin(),all.end());vector<int>chosen;uint64_t traces=0,witnesses=0;
 function<void(int,int,int,int,int)>trace=[&](int k,int d,int c,int v,int last){
  traces++;if(k==0){if(d||c||v)return;witnesses++;cout<<"witness";for(int j:chosen){auto [dd,cc,vv]=all[j];cout<<" "<<13-dd<<":"<<cc<<":"<<vv;}cout<<"\n";return;}
  for(int j=0;j<=last;j++){auto [dd,cc,vv]=all[j];if(dd>d||cc>c||vv>v)continue;int prior=history[k-1][(d-dd)*stride+c-cc];if(prior<0||prior+vv!=v)continue;chosen.push_back(j);trace(k-1,d-dd,c-cc,v-vv,j);chosen.pop_back();}
 };trace(K,T,target,value,(int)all.size()-1);cerr<<"trace_nodes "<<traces<<" witnesses "<<witnesses<<" value "<<value<<"\n";
}
