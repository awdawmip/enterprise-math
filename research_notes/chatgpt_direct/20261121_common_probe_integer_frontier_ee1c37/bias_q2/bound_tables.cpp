#include <algorithm>
#include <array>
#include <deque>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
int biasQ=0;
constexpr int excMin[14]={0,0,12,36,72,120,201,292,419,557,744,1008,1244,99999};
struct Bound {vector<int>P,E;int minE,budget;
 // Complete single-class spectrum, typed as proper (0), embedded (1),
 // or the forced outer-deletion 12-class (2).
 array<array<vector<pair<int,int>>,3>,14> typed;
 array<int,14> initialCounts{},radix{},properFloor{};
 vector<vector<int>> remainingDifference,windowWeight;
 vector<int> remainingFloor;
 int lowerCost=0,extraCap=0,stateCount=0;
 static constexpr int INF=1000000000;
 int stateOf(const array<int,14>& counts)const{
   int id=0;
   for(int s=1;s<=13;s++){
     if(counts[s]<0 || counts[s]>initialCounts[s])throw logic_error("count outside remaining spectrum");
     id+=counts[s]*radix[s];
   }
   return id;
 }
 void prepareBound(const string& filename,int lower){
   if(biasQ<=0)throw logic_error("budget-coupled bound needs positive q");
   lowerCost=lower;if(lowerCost>budget)throw logic_error("empty requested cost window");
   ifstream cat(filename);int n,s,e,c,d;if(!(cat>>n))throw logic_error("missing typed catalogue");
   for(int i=0;i<n;i++){
     if(!(cat>>s>>e>>c>>d) || s<1 || s>13 || e<0 || e>2 || c<0 || d<0)throw logic_error("bad typed catalogue");
     typed[s][e].push_back({c,d});
   }
   for(int s:P)++initialCounts[s];
   int multiplier=1,properMin=0;
   for(s=1;s<=13;s++){
     radix[s]=multiplier;multiplier*=initialCounts[s]+1;
     if(initialCounts[s]){
       if(typed[s][0].empty())throw logic_error("missing proper type");
       properFloor[s]=min_element(typed[s][0].begin(),typed[s][0].end())->first;
       if(properFloor[s]<excMin[s])throw logic_error("unsafe inherited cost bound");
       properMin+=initialCounts[s]*properFloor[s];
     }
   }
   stateCount=multiplier;
   vector<pair<int,int>> embeddedTypes;int large=0,embeddedMin=0;
   for(int s:E)large+=(s>=12);
   bool forceOuter=(large==6);
   for(int s:E){
     e=(s==12 && forceOuter)?2:1;if(e==2)forceOuter=false;
     if(typed[s][e].empty())throw logic_error("missing embedded type");
     embeddedTypes.push_back({s,e});
     embeddedMin+=min_element(typed[s][e].begin(),typed[s][e].end())->first;
   }
   if(forceOuter || embeddedMin!=minE)throw logic_error("embedded floor differs from complete typed spectrum");
   extraCap=budget-minE-properMin;if(extraCap<0)throw logic_error("profile already has empty cost window");
   remainingDifference.assign(stateCount,vector<int>(extraCap+1,-1));
   windowWeight.assign(stateCount,vector<int>(extraCap+1,INF));
   remainingFloor.resize(stateCount);
   remainingDifference[0][0]=0;
   for(auto [size,type]:embeddedTypes){
     int base=min_element(typed[size][type].begin(),typed[size][type].end())->first;
     vector<int> next(extraCap+1,-1);
     for(auto [cost,absDelta]:typed[size][type]){
       int spent=cost-base;
       for(int x=0;x+spent<=extraCap;x++)if(remainingDifference[0][x]>=0)
         next[x+spent]=max(next[x+spent],remainingDifference[0][x]+absDelta);
     }
     remainingDifference[0].swap(next);
   }
   for(int id=0;id<stateCount;id++){
     int predecessorSize=0;remainingFloor[id]=minE;
     for(s=1;s<=13;s++){
       int count=(id/radix[s])%(initialCounts[s]+1);
       remainingFloor[id]+=count*properFloor[s];if(count && !predecessorSize)predecessorSize=s;
     }
     if(id){
       s=predecessorSize;auto& previous=remainingDifference[id-radix[s]];auto& current=remainingDifference[id];
       for(auto [cost,absDelta]:typed[s][0]){
         int spent=cost-properFloor[s];
         for(int x=0;x+spent<=extraCap;x++)if(previous[x]>=0)
           current[x+spent]=max(current[x+spent],previous[x]+absDelta);
       }
     }
     // For query x, only extras in [max(0,x-(budget-lowerCost)),x]
     // can end in the requested total-cost interval.
     deque<int> queue;int width=budget-lowerCost;
     auto score=[&](int x){return biasQ*x-remainingDifference[id][x];};
     for(int x=0;x<=extraCap;x++){
       while(!queue.empty() && queue.front()<x-width)queue.pop_front();
       if(remainingDifference[id][x]>=0){
         while(!queue.empty() && score(queue.back())>=score(x))queue.pop_back();
         queue.push_back(x);
       }
       if(!queue.empty())windowWeight[id][x]=score(queue.front());
     }
   }
 }
 int budgetBound(const array<int,14>& counts,int weight,int delta)const{
   if(weight%biasQ)throw logic_error("partial weight is not q times cost");
   int id=stateOf(counts),spent=weight/biasQ;
   int extra=budget-spent-remainingFloor[id];
   if(extra<0)return INF;
   if(extra>extraCap)throw logic_error("remaining extra budget exceeds initial one");
   int score=windowWeight[id][extra];if(score==INF)return INF;
   return weight-abs(delta)+biasQ*remainingFloor[id]+score;
 }
 void dumpBound(const string& filename)const{
   ofstream f(filename);f<<stateCount<<" "<<extraCap<<" "<<minE<<" "<<budget<<" "<<lowerCost<<" "<<biasQ<<"\n";
   for(auto v:initialCounts)f<<v<<" ";f<<"\n";
   for(auto v:radix)f<<v<<" ";f<<"\n";
   for(auto v:properFloor)f<<v<<" ";f<<"\n";
   for(auto v:E)f<<v<<" ";f<<"\n";
   for(int id=0;id<stateCount;id++)for(int x=0;x<=extraCap;x++)
     f<<id<<" "<<x<<" "<<remainingDifference[id][x]<<" "<<windowWeight[id][x]<<"\n";
 }

};
vector<int> parse(string s){replace(s.begin(),s.end(),',',' ');istringstream f(s);vector<int>w;int v;while(f>>v)w.push_back(v);return w;}
int main(int argc,char**av){
 if(argc!=9)return 2;
 Bound b;b.P=parse(av[1]);b.E=parse(av[2]);b.minE=stoi(av[3]);b.budget=stoi(av[4]);int lower=stoi(av[5]);biasQ=stoi(av[6]);b.prepareBound(av[7],lower);b.dumpBound(av[8]);
 cout<<b.stateCount<<" "<<b.extraCap<<"\n";
}
