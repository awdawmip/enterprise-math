#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;
constexpr M domain=(M(1)<<125)-1;
int at(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
int card(M x){return popcount(W(x))+popcount(W(x>>64));}
struct Row{M m;int c;};
struct Hash{size_t operator()(M m)const{return W(m)^(W(m>>64)*0x9e3779b97f4a7c15ULL);}};
array<unordered_map<M,int,Hash>,14> lookup;
constexpr int excMin[14]={0,0,12,36,72,120,201,292,419,557,744,1008,1244,99999};
struct Node{M common;int floor;int lo,hi,left,right;};
struct Index{
 vector<Row> rows;vector<Node> tree;
 int build(int lo,int hi){
   int id=tree.size();tree.push_back({domain,99999,lo,hi,-1,-1});M common=domain,un=0;int floor=99999;
   for(int i=lo;i<hi;i++){common&=rows[i].m;un|=rows[i].m;floor=min(floor,rows[i].c);}
   tree[id].common=common;tree[id].floor=floor;
   if(hi-lo<=32)return id;
   array<int,125> counts{};int samples=min(hi-lo,160);
   for(int j=0;j<samples;j++)for(M m=rows[lo+W(j)*(hi-lo)/samples].m&~common;m;m&=m-1)++counts[at(m)];
   int best=at(un&~common),score=-1;
   for(M m=un&~common;m;m&=m-1){int j=at(m),v=min(counts[j],samples-counts[j]);if(v>score){score=v;best=j;}}
   M bit=M(1)<<best;int mid=partition(rows.begin()+lo,rows.begin()+hi,[&](auto&r){return !(r.m&bit);})-rows.begin();
   if(lo==mid||mid==hi)throw logic_error("split");int left=build(lo,mid),right=build(mid,hi);tree[id].left=left;tree[id].right=right;return id;
 }
 template<class F>bool query(int id,M banned,M outside,int slack,int cap,F&fn){
   const Node& n=tree[id];if(n.floor>cap||(n.common&banned)||card(n.common&outside)>slack)return false;
   if(n.left>=0)return query(n.left,banned,outside,slack,cap,fn)||query(n.right,banned,outside,slack,cap,fn);
   for(int i=n.lo;i<n.hi;i++){auto&r=rows[i];if(r.c<=cap&&!(r.m&banned)&&card(r.m&outside)<=slack&&fn(r))return true;}
   return false;
 }
};
array<Index,14> idx;
array<array<array<M,256>,16>,125> plusMap,minusMap;
int shift(int x,int y,int sign){return ((x/25+sign*(y/25)+5)%5)*25+((x/5%5+sign*(y/5%5)+5)%5)*5+(x%5+sign*(y%5)+5)%5;}
M move(M m,const array<array<M,256>,16>&p){M r=0;for(int i=0;i<16;i++,m>>=8)r|=p[i][unsigned(m&255)];return r;}
W obs[125][125][4];M bad[125][125];
int price(M m){int c=0;for(M a=m;a;a&=a-1){auto&row=obs[at(a)];W h[4]{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)h[j]|=row[at(b)][j];for(W x:h)c+=popcount(x);}return c;}
array<vector<Row>,14> globalBank;
long long nodes=0,settlements=0,done=0,leaves=0,possible=0;
struct Search{
 vector<int> E,P;int k,budget,minE,caseNo;
 array<M,7> mothers{};M u=0;
 vector<M> picked;vector<M> win;array<vector<Row>,14> region;
 bool assign(int it,const vector<int>&pts,array<M,7>&parts){
   if(it==(int)pts.size()){
     vector<int> sizes;int c=0;for(int j=0;j<k;j++){sizes.push_back(card(parts[j]));}sort(sizes.begin(),sizes.end());if(sizes!=E)return false;
     for(int j=0;j<k;j++)c+=price(parts[j]);for(M m:picked)c+=price(m);if(c>budget)return false;
     win=picked;for(int j=0;j<k;j++)win.push_back(parts[j]);return true;
   }
   int x=pts[it];M b=M(1)<<x;
   for(int j=0;j<k;j++)if(mothers[j]&b && card(parts[j])<E.back()){parts[j]|=b;if(assign(it+1,pts,parts))return true;parts[j]^=b;}
   return false;
 }
 bool settle(M used){
   ++settlements;if((domain&~used)&~u)return false;
   M free=domain&~used;array<M,7> parts{};vector<int> shared;
   for(M a=free;a;a&=a-1){int x=at(a),last=-1,n=0;for(int j=0;j<k;j++)if((mothers[j]>>x)&1){last=j;n++;}if(n==1)parts[last]|=M(1)<<x;else shared.push_back(x);}
   return assign(0,shared,parts);
 }
 bool capacity(M used){
   array<int,7> slots{};for(int j=0;j<k;j++)slots[j]=card(mothers[j]&~used);sort(slots.begin(),slots.begin()+k);
   for(int j=0;j<k;j++)if(slots[j]<E[j])return false;return true;
 }
 int point(M free){
   int pivot=at(free),highest=-1;
   for(M a=free;a;a&=a-1){int x=at(a);int v=0;for(M b=free;b;b&=b-1)v+=card(bad[x][at(b)]&free);
     if(v>highest){pivot=x;highest=v;}}
   return pivot;
 }
 bool solve(M free,M used,array<int,14>&counts,int kLeft,int space,int slack){
   ++nodes;
   if(!kLeft)return settle(used);
   int need=card(free),d=space-need;if(d<0||!capacity(used))return false;
   if(!free){throw logic_error("no obliged outside point with unfilled proper label");}
   int rare=-1;array<vector<Row>,14> choices;
   for(int s=11;s<=12;s++)if(counts[s]){
     auto &c=choices[s];for(auto&r:region[s])if(r.c<=excMin[s]+slack && !(r.m&used) && card(r.m&~free)<=d)c.push_back(r);
     if(c.size()<(size_t)counts[s])return false;
     if(rare<0||c.size()<choices[rare].size())rare=s;
   }
   if(rare!=-1){
     --counts[rare];for(auto&r:choices[rare]){
       picked.push_back(r.m);++leaves;bool ok=solve(free&~r.m,used|r.m,counts,kLeft-1,space-rare,slack-r.c+excMin[rare]);picked.pop_back();
       if(ok){++counts[rare];return true;}
     }
     ++counts[rare];return false;
   }
   for(int s=1;s<8;s++)if(counts[s])throw logic_error("unexpected small-class bank required");
   int x=point(free);M avoid=move(used,minusMap[x]),outside=move(domain&~free,minusMap[x]);
   for(int s=12;s>=8;s--)if(counts[s]){
     --counts[s];
     auto check=[&](const Row&r){M row=move(r.m,plusMap[x]);picked.push_back(row);++leaves;
       bool ok=solve(free&~row,used|row,counts,kLeft-1,space-s,slack-r.c+excMin[s]);picked.pop_back();return ok;};
     bool yes=!idx[s].rows.empty()&&idx[s].query(0,avoid,outside,d,slack+excMin[s],check);++counts[s];if(yes)return true;
   }
   return false;
 }
 bool run(){
   u=0;for(int j=0;j<k;j++)u|=mothers[j];int space=0,base=minE;array<int,14>counts{};
   for(int s:P){space+=s;base+=excMin[s];++counts[s];}
   int d=space-card(domain^u);
   for(int s=12;s>=11;s--)if(counts[s]){
     region[s].clear();for(auto&r:globalBank[s])if(card(r.m&u)<=d)region[s].push_back(r);
     if(region[s].size()<(size_t)counts[s])return false;
   }
   return solve(domain^u,0,counts,P.size(),space,budget-base);
 }
};
vector<int> parse(string s){replace(s.begin(),s.end(),',',' ');istringstream f(s);vector<int> w;int v;while(f>>v)w.push_back(v);return w;}
int main(int argc,char**av){
  ifstream ob(av[1],ios::binary),pp(av[2]);ob.read((char*)obs,sizeof(obs));array<unsigned char,3>tr;
  while(ob.read((char*)tr.data(),3))do{bad[tr[0]][tr[1]]|=M(1)<<tr[2];}while(next_permutation(tr.begin(),tr.end()));
  array<M,250> parents;for(auto&m:parents){W l,h;pp>>l>>h;m=M(h)<<64|l;}
  for(int x=0;x<125;x++)for(int b=0;b<16;b++)for(int z=1;z<256;z++){
    int first=countr_zero((unsigned)z)+8*b;
    plusMap[x][b][z]=plusMap[x][b][z&(z-1)];minusMap[x][b][z]=minusMap[x][b][z&(z-1)];
    if(first<125){plusMap[x][b][z]|=M(1)<<shift(first,x,1);minusMap[x][b][z]|=M(1)<<shift(first,x,-1);}
  }
  Search job;job.P=parse(av[5]);job.E=parse(av[6]);job.k=job.E.size();job.minE=stoi(av[7]);job.budget=stoi(av[8]);
  int slack=job.budget-job.minE;for(int s:job.P)slack-=excMin[s];int first=stoi(av[9]),end=stoi(av[10]);
  for(int s:job.P)if(s>=8 && idx[s].rows.empty()){
    ifstream f(string(av[3])+to_string(s),ios::binary);if(!f)return 4;W r[3];while(f.read((char*)r,24))if(int(r[2])<=excMin[s]+slack)idx[s].rows.push_back({(M(r[1])<<64)|r[0],int(r[2])});
    if(s>=11){for(auto&r:idx[s].rows)for(int x=0;x<125;x++){M m=move(r.m,plusMap[x]);if(at(m)==x)globalBank[s].push_back({m,r.c});}}
    if(!idx[s].rows.empty())idx[s].build(0,idx[s].rows.size());
  }
  ifstream frames(av[4]);string line;int id=0;
  while(getline(frames,line)){
    if(id++<first)continue;if(id>end)break;istringstream st(line);for(int j=0,m;j<job.k;j++){if(!(st>>m))return 8;job.mothers[j]=parents[m];}
    ++done;if(job.run()){++possible;cout<<"hit "<<id<<" ";for(M r:job.win)cout<<W(r)<<":"<<W(r>>64)<<" ";cout<<endl;break;}
  }
  cerr<<done<<" "<<nodes<<" "<<leaves<<" "<<settlements<<" "<<possible<<"\n";
}
