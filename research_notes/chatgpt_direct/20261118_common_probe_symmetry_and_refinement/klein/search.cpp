#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
using U=uint64_t;
struct R {U q;int r,price,x,y,z;};
U xmask,ymask,zmask,all;int best,lo[3][13][6][25][33],K;long long nodes,work,frames;
constexpr int INF=1000000;
constexpr int minima[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
vector<R> rows;vector<int> by[64],path,saved;
int lb(int k,int x,int y,int z){return lo[K][k][x][y][z];}
struct Sim{U table[6][256]{};U rot(U f)const{U out=0;for(int i=0;f;i++,f>>=8)out|=table[i][f&255];return out;}};
vector<Sim>sims;array<unordered_map<U,int>,13> memo;
bool enumerate_frames=false;
int leaf(U f,int z,int cap);
struct Block {int r,x,y,z;vector<int> list;};
vector<Block> blocks[65];
U got1=0,got2=0;extern U part1,part2;
void seek(U f,int k,int price,int x,int y,int z,int start){
 ++nodes;if(price+lb(k,x,y,z)>=best)return;
 if(!enumerate_frames){U canon=f;for(auto &sim:sims)canon=min(canon,sim.rot(f));auto [it,added]=memo[k].emplace(canon,price);if(!added){if(it->second<=price)return;it->second=price;}}
 if(k==4*K){if(x||y)return;++frames;int c=leaf(f,z,best-price-1);if(c+price<best){if(enumerate_frames){cout<<"FRAME "<<c+price;for(int i:path)cout<<" "<<rows[i].r<<" "<<rows[i].q<<" "<<rows[i].price;cout<<endl;return;}best=c+price;saved=path;got1=part1;got2=part2;cerr<<"win "<<best<<" "<<f<<" "<<K<<" "<<price<<endl;}return;}
 U must=f&(xmask|ymask);int pivot=64;long lowest=1000000000;
 auto cut=[&](const Block &b){if(b.r>k-4*K||b.x>x||b.y>y||b.z>z)return -1;
   return best-1-price-lb(k-b.r,x-b.x,y-b.y,z-b.z);};
 for(U t=must;t;t&=t-1){int bit=countr_zero(t);long count=0;
  for(auto &b:blocks[bit]){int c=cut(b);if(c<0||rows[b.list.front()].price>c)continue;
   auto e=upper_bound(b.list.begin(),b.list.end(),c,[](int c,int i){return c<rows[i].price;});
   auto n=e-b.list.begin();if(n<80){for(auto it=b.list.begin();it!=e;it++)count+=!(rows[*it].q&~f);}
   else count+=n;if(count>=lowest)break;}
  if(!count)return;if(count<lowest){lowest=count;pivot=bit;}}
 for(auto &b:blocks[pivot]){int c=cut(b);if(c<0)continue;
  for(int i:b.list){if(rows[i].price>c)break;if(enumerate_frames&&pivot==64&&i<start)continue;++work;
   auto&a=rows[i];if(a.q&~f)continue;
   path.push_back(i);seek(f^a.q,k-a.r,price+a.price,x-a.x,y-a.y,z-a.z,pivot==64?i+1:0);path.pop_back();}
 }

}
#include "phases.hpp"
int main(int argc,char**argv){
 string dir=argv[1],id=argv[2];int cap=stoi(argv[3]);enumerate_frames=argc>4;best=cap+1;
 ifstream ks(dir+"/ksz"+id);ks>>xmask>>ymask>>zmask;all=xmask|ymask|zmask;
 init(dir,id);ifstream sy(dir+"/norm"+id);int nOrb=popcount(all);vector<int> perm(nOrb);while(sy>>perm[0]){Sim a;for(int j=1;j<nOrb;j++)sy>>perm[j];for(int p=0;p<nOrb;p++)for(int b=0;b<256;b++)if(b>>(p%8)&1)a.table[p/8][b]|=U(1)<<perm[p];sims.push_back(a);}
 int X=popcount(xmask),Y=popcount(ymask),Z=popcount(zmask);if(X>5||Y>24||Z>32)return 3;
 map<pair<U,int>,int> cheapest;
 for(int f=0;f<4;f++){int r=(f==0?1:2);string filename=f==0?"fbank"+id:("pbank"+id+"."+to_string(f));
  ifstream in(dir+"/"+filename);U q;int c;while(in>>q>>c){if(r>1){U l,h;in>>l>>h;}auto [p,ok]=cheapest.emplace(make_pair(q,r),c*r);if(!ok)p->second=min(p->second,c*r);}}
 map<array<int,4>,int> mincost;
 for(auto [key,v]:cheapest){auto[q,r]=key;int x=popcount(q&xmask),y=popcount(q&ymask),z=popcount(q&zmask);
  array<int,4> shape{r,x,y,z};auto [p,ok]=mincost.emplace(shape,v);if(!ok)p->second=min(p->second,v);}
 int restricted[14];
 for(int j=1;j<=13;j++)restricted[j]=max(guaranteed[j]+1,minima[j]);
 ifstream qf(dir+"/qbank"+id);U q,l,h;int c;
 while(qf>>q>>c>>l>>h)restricted[popcount(q)]=min(restricted[popcount(q)],c);
 for(int j=1;j<=13;j++)mincost[{4,0,0,j}]=4*restricted[j];
 fill(&lo[0][0][0][0][0],&lo[0][0][0][0][0]+3*13*6*25*33,INF);lo[0][0][0][0][0]=0;
 for(K=0;K<=2;K++)for(int k=1;k<=12;k++)for(int x=0;x<=X;x++)for(int y=0;y<=Y;y++)for(int z=0;z<=Z;z++)
 for(auto&[shape,v]:mincost){auto[r,a,b,c]=shape;int h=(r==4);if(h<=K&&r<=k&&a<=x&&b<=y&&c<=z)lo[K][k][x][y][z]=min(lo[K][k][x][y][z],v+lo[K-h][k-r][x-a][y-b][z-c]);}
 for(K=0;K<=(enumerate_frames?0:2);K++){
 best=cap+1;nodes=work=frames=0;
 for(auto &book:memo)book.clear();rows.clear();for(auto&v:by)v.clear();
 for(auto [key,v]:cheapest){auto[q,r]=key;int x=popcount(q&xmask),y=popcount(q&ymask),z=popcount(q&zmask);
  if(v+lb(12-r,X-x,Y-y,Z-z)>=best)continue;
  int i=rows.size();rows.push_back({q,r,v,x,y,z});for(U u=q;u;u&=u-1)by[countr_zero(u)].push_back(i);}
 for(auto&v:by)sort(v.begin(),v.end(),[](int a,int b){return rows[a].price<rows[b].price;});
 cerr<<id<<" start "<<K<<" "<<lb(12,X,Y,Z)<<" rows "<<rows.size()<<endl;
 vector<int> allids;for(int j=0;j<int(rows.size());j++)allids.push_back(j);
 for(int j=0;j<65;j++){blocks[j].clear();map<array<int,4>,vector<int>> m;
   for(int i:(j==64?allids:by[j])){auto &a=rows[i];m[{a.r,a.x,a.y,a.z}].push_back(i);}
   for(auto &[key,v]:m){sort(v.begin(),v.end(),[](int a,int b){return rows[a].price<rows[b].price;});auto[r,x,y,z]=key;blocks[j].push_back({r,x,y,z,move(v)});}}
 int before=best;saved.clear();seek(all,12,0,X,Y,Z,0);
 cout<<id<<" "<<K<<" "<<lb(12,X,Y,Z)<<" "<<rows.size()<<" "<<nodes<<" "<<work<<" "<<frames<<" "<<best<<endl;
 if(best<before)cout<<"quads "<<got1<<" "<<got2<<endl;
 if(best<before)for(auto i:saved)cout<<"row "<<rows[i].r<<" "<<rows[i].q<<" "<<rows[i].price<<endl;
 }
}
