#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <string>
#include <cassert>
using namespace std;
int width(int q){ int b=0,v=1;while(v<q){++b;v*=2;}return b; }
struct Rec {int p,N,number,minimum_total,minimum_peak;vector<tuple<int,int,int,int>> best_total,best_peak,frontier;};
Rec solve(int p){
 int N=1<<p,count=0,bt=1000,bm=1000;
 vector<tuple<int,int,int,int>> v;
 for(int q1=3;q1<N;q1+=2){
  vector<vector<int>> buckets(q1);
  vector<int> last(q1,-1);
  for(int u=0;u<N;u++){
   for(int bit=-1;bit<p;bit++){
    int pred=(bit<0?u:(u^(1<<bit)));
    int rem=pred%q1;
    if(last[rem]!=u){buckets[rem].push_back(u);last[rem]=u;}
   }
  }
  vector<unsigned char> forbidden(N,0);
  for(const auto &b:buckets){
   for(size_t i=0;i<b.size();i++)for(size_t j=i+1;j<b.size();j++){
    int d=b[j]-b[i]; assert(d>0); forbidden[d]=1;
   }
  }
  for(int q2=3;q2<N;q2+=2){
   bool good=true;
   for(int d=q2;d<N;d+=q2)if(forbidden[d]){good=false;break;}
   if(good){
    int a=width(q1),b=width(q2);
    v.emplace_back(a,b,q1,q2);count++;
    bt=min(bt,a+b);bm=min(bm,max(a,b));
   }
  }
 }
 Rec r{p,N,count,(bt==1000?-1:bt),(bm==1000?-1:bm)};
 for(auto t:v){int a=get<0>(t),b=get<1>(t);
  if(a+b==bt)r.best_total.push_back(t);
  if(max(a,b)==bm)r.best_peak.push_back(t);
 }
 set<pair<int,int>> f;
 set<pair<int,int>> dims; for(auto t:v)dims.insert({get<0>(t),get<1>(t)});
 for(auto [a,b]:dims){bool dominated=false;for(auto [a2,b2]:dims)
  if(a2<=a && b2<=b && (a2<a || b2<b)){dominated=true;break;}
  if(!dominated)f.insert({a,b});
 }
 for(auto [a,b]:f){for(auto t:v)if(get<0>(t)==a&&get<1>(t)==b){
  r.frontier.push_back(t);break;}}
 return r;
}
void printarr(const vector<tuple<int,int,int,int>>&a,int limit){
 cout<<"["; for(int i=0;i<(int)a.size()&&i<limit;i++){
  if(i)cout<<",";auto [x,y,z,w]=a[i];
  cout<<"["<<x<<","<<y<<","<<z<<","<<w<<"]";
 }cout<<"]";
}
int main(){cout<<"{\"schema\":\"PREFIX859_ODD_PARETO_V1\",\"cases\":[";
for(int p=3;p<=11;p++){if(p!=3)cout<<",";auto r=solve(p);
cout<<"{\"p\":"<<r.p<<",\"N\":"<<r.N<<",\"successful_pairs\":"<<r.number
 <<",\"minimum_total_bits\":"<<r.minimum_total
 <<",\"minimum_peak_bits\":"<<r.minimum_peak<<",\"best_total_witnesses\":";
printarr(r.best_total,8);cout<<",\"best_peak_witnesses\":";
printarr(r.best_peak,5);cout<<",\"pareto_witnesses\":";
printarr(r.frontier,50);cout<<"}";
}cout<<"]}"<<endl;}
