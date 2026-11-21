#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
using Q=uint32_t;
struct Row{Q mask;int len,cost,size;};
constexpr int INF=1000000;
vector<Row> small,origin;
array<unordered_map<Q,int>,3> frame;
unordered_map<Q,int> packet;
int floorCost[13][127][3],shapeMin[5][54],cap;
long long nodes=0,checks=0,scans=0;
void build(Q left,int labels,int points,int cost,int k,int after){
 ++nodes;
 if(cost+floorCost[labels][points][k]>cap)return;
 if(labels==4*k){if(points!=4*popcount(left))return;
  auto [it,fresh]=frame[k].try_emplace(left,cost);if(!fresh)it->second=min(it->second,cost);return;}
 for(size_t j=after;j<small.size();j++){auto &r=small[j];if(r.len>labels-4*k||(r.mask&~left))continue;
 if(cost+r.cost+floorCost[labels-r.len][points-r.size][k]>cap)continue;
 build(left^r.mask,labels-r.len,points-r.size,cost+r.cost,k,j+1);}
}
int main(int argc,char**argv){
 cap=stoi(argv[2]);ifstream f(argv[1]);int r,c,n;Q q;uint64_t l,h;fill(&shapeMin[0][0],&shapeMin[0][0]+5*54,INF);
 while(f>>r>>q>>c>>n>>l>>h){
 if(r==4){packet[q]=c;shapeMin[r][n]=min(shapeMin[r][n],c);}
 else if(q&1)origin.push_back({q,r,c,n});else{small.push_back({q,r,c,n});shapeMin[r][n]=min(shapeMin[r][n],c);}
 }
 sort(small.begin(),small.end(),[](auto&a,auto&b){if(a.size!=b.size)return a.size>b.size;return a.cost<b.cost;});
 fill(&floorCost[0][0][0],&floorCost[0][0][0]+13*127*3,INF);floorCost[0][0][0]=0;
 for(int j=1;j<=12;j++)for(int p=1;p<=125;p++)for(int m=0;m<3;m++)for(int r:{1,2,4})if(j>=r&&(r<4||m))
 for(int s=1;s<=min(p,13*r);s++)floorCost[j][p][m]=min(floorCost[j][p][m],shapeMin[r][s]+floorCost[j-r][p-s][m-(r==4)]);
 for(auto&a:origin)for(int k=0;k<=2;k++)build(~a.mask,11,125-a.size,a.cost,k,0);
 cout<<"frames "<<frame[0].size()<<" "<<frame[1].size()<<" "<<frame[2].size()<<" nodes "<<nodes<<endl;
 int best=cap+1;Q winning=0,source=0;
 if(frame[0].count(0)){best=frame[0][0];if(best==cap)cerr<<"SHORT "<<best<<endl;}
 for(auto [s,c]:frame[1]){auto it=packet.find(s);if(it!=packet.end()&&c+it->second==cap)cerr<<"SINGLE "<<s<<" "<<c<<endl;if(it!=packet.end()&&c+it->second<best){best=c+it->second;source=s;winning=s;}}
 vector<pair<Q,int>> sorted;
 for(auto [s,c]:packet)sorted.push_back({s,c});
 sort(sorted.begin(),sorted.end(),[](auto a,auto b){return a.second<b.second;});
 int mini[33];fill(mini,mini+33,INF);for(auto [s,c]:sorted)mini[popcount(s)]=min(mini[popcount(s)],c);
 long long included=0;
 vector<pair<Q,int>> bysize[14];
 for(auto x:sorted)bysize[popcount(x.first)].push_back(x);
 for(auto [s,c]:frame[2]){int ss=popcount(s);
  for(int size=1;size<=min(ss/2,13);size++){int nb=ss-size;if(nb>13||nb<1||c+mini[size]+mini[nb]>best)continue;
   for(auto [a,ca]:bysize[size]){if(c+ca+mini[nb]>best)break;
    ++scans;if(a&~s)continue;++checks;
    if(size==nb && (s^a)<a)continue;auto it=packet.find(s^a);if(it!=packet.end() && c+ca+it->second==cap)cerr<<"PAIR "<<s<<" "<<a<<" "<<c<<endl;if(it!=packet.end()&&c+ca+it->second<best){best=c+ca+it->second;source=s;winning=a;cerr<<"hit "<<best<<endl;}
   }
  }
 }
 cout<<"result "<<best<<" "<<checks<<" "<<scans<<" "<<source<<" "<<winning<<endl;
}
