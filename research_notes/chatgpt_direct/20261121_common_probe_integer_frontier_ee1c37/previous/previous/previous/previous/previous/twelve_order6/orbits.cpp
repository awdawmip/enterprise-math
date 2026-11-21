#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
using M=__uint128_t;using U=uint64_t;using S=uint32_t;
int idx(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}
int pop(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
using W=array<U,4>;
M bad[125][125];W obs[125][125];int g[125],period,norbits,labelcount;
struct Rec{int cost;M seed; long long ways=1;};
struct Part{S support;int length;Rec d;};
map<S,Rec> best[13];vector<int> cycles[32];vector<M> choices[32];vector<int> loc;
int kmax=13,ar=0;long long seednodes[13]={};
M banned(M orig,M add,M prev){
 for(M a=add;a;a&=a-1){int p=idx(a);if(prev&(M(1)<<p))return ~M(0);for(M b=orig;b;b&=b-1)prev|=bad[p][idx(b)];orig|=M(1)<<p;}
 return prev;
}
int price(M m){
 int cost=0;for(M a=m;a;a&=a-1){W w{};int p=idx(a);for(M b=m;b;b&=b-1){auto &o=obs[p][idx(b)];for(int j=0;j<4;j++)w[j]|=o[j];}for(U v:w)cost+=__builtin_popcountll(v);}
 return cost;
}
void gen(int i,int r,M row,M illegal,S support){
 ++seednodes[r];
 if(row){
  int p=price(row)*r;auto z=best[r].find(support);
  if(z==best[r].end()||p<z->second.cost)best[r][support]={p,row,1};else if(z->second.cost==p)++z->second.ways;
 }
 for(int j=i;j<loc.size();j++){
  int t=loc[j];const int nm=cycles[t].size()/r;if(pop(row)+nm>kmax)continue;
  for(M m:choices[t]){if(m&illegal)continue;M f=banned(row,m,illegal);if(f!=~M(0))gen(j+1,r,row|m,f,support|(1u<<t));if(!row)break;}
 }
}
void init(int r){
 loc.clear();for(int t=0;t<norbits;t++){
  choices[t].clear();auto& cyc=cycles[t];if(cyc.size()%r)continue;
  for(int j=0;j<r;j++){M m=0;for(int z=j;z<cyc.size();z+=r)m|=M(1)<<cyc[z];choices[t].push_back(m);}
  loc.push_back(t);
 }
}
const int mins[14]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
int best_final=10000000,cap;vector<Part> table,path;vector<Part> parts;vector<int> by[32];S all;long long covernodes,forcednodes,complements;map<S,vector<Part>> tailpack;
long long wins=0;int BOUND;map<S,long long> pathcount;
void last(int i,int n,M row,M illegal,S support,int prefix){
 ++forcednodes;
 if(i==loc.size()){
  int cost=price(row)*6+prefix;if(cost==BOUND)wins+=pathcount[support];
  if(cost<best_final){best_final=cost;table=path;table.push_back({support,6,{cost-prefix,row}});cerr<<"best "<<cost<<endl;}return;
 }
 int t=loc[i];
 for(M m:choices[t]){if(!(m&illegal)){M f=banned(row,m,illegal);if(f!=~M(0))last(i+1,n,row|m,f,support,prefix);}if(!row)break;}
}
int lower[20][126];unordered_map<uint64_t,int> oldcost;
int pointcount(S s){int n=0;for(;s;s&=s-1)n+=cycles[__builtin_ctz(s)].size();return n;}
void cover(S free,int count,int cost){
 ++covernodes;
 if(!count){if(!free && cost==BOUND){long long m=1;for(auto&t:path)m*=t.d.ways;wins+=m;}if(!free && cost<best_final){best_final=cost;table=path;cerr<<"best "<<cost<<endl;}return;}
 if(!free || cost+lower[count][pointcount(free)]>BOUND)return;
 auto key=(uint64_t(free)<<5)|count;
 auto ii=oldcost.find(key);if(ii!=oldcost.end()&&ii->second<cost)return;oldcost[key]=cost;
 int pivot=-1,few=10000000;
 for(S t=free;t;t&=t-1){int id=__builtin_ctz(t);int n=0;for(int j:by[id]){auto&r=parts[j];if(r.length<=count && (r.support&free)==r.support)++n;}if(n<few){few=n;pivot=id;}}
 for(int j:by[pivot]){auto&r=parts[j];if(r.length>count||(r.support&free)!=r.support)continue;path.push_back(r);cover(free^r.support,count-r.length,cost+r.d.cost);path.pop_back();}
}
void patches(S free,int remaining,int cost,int after){
 if(cost+lower[remaining+6][pointcount(free)]>BOUND)return;
 if(!remaining){
  int n=0;for(S b=free;b;b&=b-1){int k=cycles[__builtin_ctz(b)].size();if(k%6)return;n+=k;}
  if(n<6||n>78||cost+6*mins[n/6]>cap)return;
  long long mult=1;for(auto &r:path)mult*=r.d.ways;auto it=tailpack.find(free);if(it==tailpack.end()){tailpack[free]=path;pathcount[free]=mult;}else{int e=0;for(auto&r:it->second)e+=r.d.cost;if(cost<e){it->second=path;pathcount[free]=mult;}else if(cost==e)pathcount[free]+=mult;}
  return;
 }
 // The origin belongs to a fixed class. Enforce it first, then enumerate the other orbits in increasing order.
 for(int j=after;j<parts.size();j++){
  auto&r=parts[j];if(path.empty() && !(r.support&1))continue;
  if(r.length>remaining || (r.support&free)!=r.support)continue;
  if(cost+r.d.cost+lower[remaining+6-r.length][pointcount(free^r.support)]>BOUND)continue;
  path.push_back(r);patches(free^r.support,remaining-r.length,cost+r.d.cost,path.size()==1?0:j+1);path.pop_back();
 }
}
int main(int argc,char**argv){
 ifstream f(argv[1],ios::binary);f.read((char*)obs,sizeof(obs));array<unsigned char,3> e;while(f.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 ifstream perm(argv[2]);perm>>period;for(int&i:g)perm>>i;labelcount=stoi(argv[3]);cap=stoi(argv[4]);BOUND=cap;best_final=cap+1;
 array<bool,125>seen{};for(int p=0;p<125;p++)if(!seen[p]){int q=p;do{cycles[norbits].push_back(q);seen[q]=true;q=g[q];}while(q!=p);++norbits;}
 if(norbits>31)return 2;
 for(int k=0;k<20;k++)for(int n=0;n<=125;n++)lower[k][n]=1000000;lower[0][0]=0;
 for(int k=1;k<20;k++)for(int n=1;n<=125;n++)for(int j=1;j<=min(13,n);j++)lower[k][n]=min(lower[k][n],mins[j]+lower[k-1][n-j]);
 all=(1u<<norbits)-1;
 for(int r=1;r<6;r++)if(period%r==0){init(r);gen(0,r,0,0,0);for(auto &u:best[r]){int id=parts.size();parts.push_back({u.first,r,u.second});for(S t=u.first;t;t&=t-1)by[__builtin_ctz(t)].push_back(id);}cerr<<"bank "<<r<<" "<<best[r].size()<<" "<<seednodes[r]<<endl;}
 cover(all,labelcount,0);cerr<<"small-only "<<covernodes<<" "<<best_final<<endl;
 patches(all,labelcount-6,0,0);cerr<<"complements "<<tailpack.size()<<endl;
 vector<pair<int,S>> order;for(auto& t:tailpack){int price=0;for(auto&r:t.second)price+=r.d.cost;order.push_back({price,t.first});}
 sort(order.begin(),order.end());
 for(auto [q,t]:order){init(6);int n=0;loc.erase(remove_if(loc.begin(),loc.end(),[&](int z){return !(t>>z&1);}),loc.end());for(int z:loc)n+=cycles[z].size();
 if(q+6*mins[n/6]>BOUND)continue;++complements;path=tailpack.at(t);last(0,n/6,0,0,t,q);}
 cout<<best_final<<" "<<covernodes<<" "<<tailpack.size()<<" "<<complements<<" "<<forcednodes<<"\n";
 cerr<<"multiplicity "<<wins<<endl;for(auto&r:table){M a=r.d.seed;for(int j=0;j<r.length;j++){for(M b=a;b;b&=b-1)cout<<idx(b)<<" ";cout<<"\n";M next=0;for(M b=a;b;b&=b-1)next|=M(1)<<g[idx(b)];a=next;}}
}
