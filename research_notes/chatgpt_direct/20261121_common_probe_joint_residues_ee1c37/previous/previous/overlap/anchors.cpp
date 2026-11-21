#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <random>
#include <cstdlib>
#include <unordered_map>
using namespace std;using W=uint64_t;using M=__uint128_t;
constexpr M full=(M(1)<<125)-1;
int first(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
int card(M x){return popcount(W(x))+popcount(W(x>>64));}
struct Row{M m;int s,def;array<int,10> v;};
vector<Row> bank;
array<M,15> plane;
array<int,125> basis;
vector<int> order;
struct Search{
 int least,req,e8,maskcolumns;
 long long nodes=0,limit=1e12;
 vector<array<int,126>> depthDeg;
 vector<int> solution;
 int maxkeep=-1;
 bool dfs(M f,int k,int e,int forbidden,int essential,const vector<int>&available){
  ++nodes;if(nodes>limit)return false;
  if(k==0)return f==0;
  int newforbid=forbidden, newess=essential;
  array<int,15> deficits{};
  for(int i=0;i<15;i++){
   int rem=2*k-card(plane[i]&f);deficits[i]=rem;
   if(rem<0||rem>k)return false;
   if(!rem)newforbid|=1<<i;
   if(rem==k)newess|=1<<i;
  }
  array<int,141> deg{};
  vector<int> next;next.reserve(available.size());
  M u=0;
  for(auto id:available){
    auto&r=bank[id];
    if((r.m&~f)||(r.def&newforbid)||((~r.def)&newess)||(!e&&r.s==8))continue;
    next.push_back(id);u|=r.m;
  }
  if(u!=f)return false;
  if(k==1){for(auto id:next)if(bank[id].m==f){solution.push_back(id);return true;}return false;}
  for(auto id:next){auto&r=bank[id];
    for(int j=0;j<r.s;j++)deg[r.v[j]]++;
    if(r.s==8)deg[125]++;
    for(int q=r.def;q;q&=q-1)deg[126+countr_zero(unsigned(q))]++;
  }
  int min=1000000,target=first(f);
  if(e){min=deg[125];target=125;}
  for(M p=f;p;p&=p-1){int i=first(p);if(deg[i]<min){target=i;min=deg[i];}}
  for(int i=0;i<15;i++)if(deficits[i]>0){
    if(deg[126+i]<deficits[i])return false;
    if(deficits[i]==1&&deg[126+i]<min){target=126+i;min=deg[target];}
  }
  if(!min)return false;
  for(int id:next){auto&r=bank[id];
   if(target<125?!((r.m>>target)&1):target==125?r.s!=8:!(r.def&(1<<(target-126))))continue;
   solution.push_back(id);
   if(dfs(f^r.m,k-1,e-(r.s==8),newforbid,newess,next))return true;
   solution.pop_back();if(nodes>=limit)return false;
  }
  return false;
 }
};
#include <map>
#include <set>
#include <sstream>
int main(int argc,char**argv){
 string dir=argv[1];int sh=stoi(argv[2]),step=stoi(argv[3]),mode=stoi(argv[4]),nextra=stoi(argv[5]);long long limit=stoll(argv[6]);
 auto load=[&](string fn){vector<M>a;ifstream f(dir+"/"+fn);W l,h;while(f>>l>>h)a.push_back(M(h)<<64|l);return a;};
 vector<M> keep=load("keep9");
 for(int i=0;i<125;i++){plane[i/25]|=M(1)<<i;plane[5+i/5%5]|=M(1)<<i;plane[10+i%5]|=M(1)<<i;}
 for(int s:{8,9})for(auto m:load("full"+to_string(s))){Row r{m,s,0,{}};int t=0;for(M p=m;p;p&=p-1)r.v[t++]=first(p);for(int i=0;i<15;i++)if(card(m&plane[i])==1)r.def|=1<<i;bank.push_back(r);}
 vector<int> ids(bank.size());iota(ids.begin(),ids.end(),0);
 vector<vector<M>> bases;
 ifstream tab(argv[7]);string line;while(getline(tab,line)){istringstream ss(line);W l,h;vector<M>o;while(ss>>l>>h)o.push_back(M(h)<<64|l);bases.push_back(o);}
 int setid=0;long long total=0,nodes=0,uncertain=0;
 for(int set=0;set<512;set++)if(popcount((unsigned)set)==3){if(setid++%step!=sh)continue;
  M used=0;for(int i=0;i<9;i++)if(set>>i&1)used|=keep[i];std::set<pair<M,int>>seen;
  for(auto&g:bases){
    vector<M> avail;
    for(auto m:g)if(!(m&used))avail.push_back(m);
    if(avail.size()<nextra)continue;
    for(int z=0;z<(1<<avail.size());z++)if(popcount((unsigned)z)==nextra){
     M u=used;int e=1;for(int i=0;i<avail.size();i++)if(z>>i&1){if(u&avail[i])goto skip;u|=avail[i];e-=card(avail[i])==8;}
     if(seen.emplace(u,e).second){
      vector<int> a;for(auto i:ids)if(!(bank[i].m&u)&& (e||bank[i].s!=8))a.push_back(i);
      Search s;s.limit=limit;++total;
      if(s.dfs(full^u,11-nextra,e,0,0,a)){
       cout<<"HIT "<<set<<" "<<nextra;for(int i=0;i<avail.size();i++)if(z>>i&1){auto m=avail[i];cout<<" "<<W(m)<<" "<<W(m>>64);}
       for(int id:s.solution){auto m=bank[id].m;cout<<" "<<W(m)<<" "<<W(m>>64);}cout<<endl;return 0;
      }
      nodes+=s.nodes;uncertain+=s.nodes>=limit;
     }
     skip:;
    }
  }
  cerr<<set<<" "<<seen.size()<<" "<<nodes<<" "<<uncertain<<endl;
 }
 cout<<"DONE "<<total<<" "<<nodes<<" "<<uncertain<<endl;
}
