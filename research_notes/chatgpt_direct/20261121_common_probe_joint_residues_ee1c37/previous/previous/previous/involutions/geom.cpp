#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using Sig=std::array<int,6>;
struct Shape{int id,c;Sig mass;};
struct Slot{std::vector<Shape>rows;int count,first;};
std::map<int,std::vector<Shape>>families;std::vector<Slot>slots;
int orig,limit;std::ofstream out;
std::vector<int>path;long long nodes,sol;
bool fits(const Sig&a,const Sig&b){for(int i=0;i<6;i++)if(a[i]>b[i])return false;return true;}
void rec(Sig goal,int budget,int n){
 nodes++;
 if(n==0){if(goal!=Sig{})return;sol++;out<<orig;for(int i:path)out<<" "<<i;out<<"\n";return;}
 int total=0,mins[12]{};for(int k=0;k<(int)slots.size();k++){auto&sl=slots[k];if(!sl.count)continue;
 int j=sl.first;while(j<(int)sl.rows.size()&&!fits(sl.rows[j].mass,goal))j++;
 if(j==(int)sl.rows.size())return;
 mins[k]=sl.rows[j].c;total+=sl.count*mins[k];}
 if(total>budget)return;
 int small=1000000,pick=-1;std::vector<int>idx;Sig low{},high{};
 for(int k=0;k<(int)slots.size();k++){auto&sl=slots[k];if(!sl.count)continue;
 int hi=mins[k]+(budget-total)/sl.count;
 int any=mins[k]+budget-total;
 Sig mn{100,100,100,100,100,100},mx{};std::vector<int> cand;
 for(int j=sl.first;j<(int)sl.rows.size()&&sl.rows[j].c<=any;j++){auto&t=sl.rows[j];if(!fits(t.mass,goal))continue;
 for(int a=0;a<6;a++){mn[a]=std::min(mn[a],t.mass[a]);mx[a]=std::max(mx[a],t.mass[a]);}
 if(t.c<=hi)cand.push_back(j);}
 if(cand.empty())return;
 for(int a=0;a<6;a++){low[a]+=sl.count*mn[a];high[a]+=sl.count*mx[a];}
 if((int)cand.size()<small){small=cand.size();pick=k;idx=std::move(cand);}
 }
 if(!fits(low,goal)||!fits(goal,high))return;
 auto&sl=slots[pick];int old=sl.first;sl.count--;
 for(int j:idx){auto &s=sl.rows[j];Sig rest=goal;for(int a=0;a<6;a++)rest[a]-=s.mass[a];sl.first=j;path.push_back(s.id);rec(rest,budget-s.c,n-1);path.pop_back();}
 sl.first=old;sl.count++;
}
int main(int ac,char**av){
 std::ifstream sig(av[1]),prof(av[2]),dual(av[3]);out.open(av[4]);limit=std::stoi(av[5]);Sig goal;for(int&x:goal)sig>>x;int r,id=0;
 while(sig>>r){Shape s;s.id=id++;int n=0;for(int&x:s.mass){sig>>x;n+=x;}sig>>s.c;families[100*r+n/r].push_back(s);}
 int n;orig=0;while(prof>>n){std::map<int,int>ct;for(int i=0,t;i<n;i++){prof>>t;ct[t]++;}
 int k;dual>>k;assert(k==orig);Sig w;int budget=limit*1000;for(int a=0;a<6;a++){dual>>w[a];budget-=w[a]*goal[a];}
 slots.clear();for(auto[t,n]:ct){Slot sl;sl.rows=families[t];sl.count=n;sl.first=0;for(auto&s:sl.rows){s.c*=1000;for(int a=0;a<6;a++)s.c-=w[a]*s.mass[a];}
 std::sort(sl.rows.begin(),sl.rows.end(),[](auto&a,auto&b){return a.c!=b.c?a.c<b.c:a.id<b.id;});slots.push_back(std::move(sl));}
 nodes=sol=0;rec(goal,budget,n);std::cout<<orig++<<" "<<nodes<<" "<<sol<<std::endl;}
}
