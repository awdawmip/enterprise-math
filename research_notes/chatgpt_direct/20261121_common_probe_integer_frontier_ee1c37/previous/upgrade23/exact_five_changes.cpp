#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using U=__uint128_t;
int pc(U x){return __builtin_popcountll((uint64_t)x)+__builtin_popcountll((uint64_t)(x>>64));}
struct C{U mask;int incoming;int id;};
vector<U> old, bank;
vector<int> sizes;
array<vector<C>,22> opts;
vector<C> chosen;
uint64_t nodes=0,eligible=0,completed=0;
int target=0;
U newq;

bool dfs(uint32_t todo,U rem,int budget){
 ++nodes;
 if(!todo)return rem==0;
 int best=-1,mincount=1000000,lb=0;
 vector<C> branch;
 vector<pair<int,C>> valid;
 array<int,125> pcount{};
 U retainable=0;
 // Every remaining old label needs one disjoint target class. The minimum
 // incoming cost for each label adds, because these labels are distinct.
 for(int i=0;i<22;i++)if(todo>>i&1){
  int mincost=100,count=0;vector<C> local;
  for(const auto &c:opts[i]){
   if(c.incoming>budget)break;
   if((c.mask&rem)!=c.mask)continue;
   mincost=min(mincost,c.incoming);count++;local.push_back(c);
   valid.emplace_back(i,c);
   retainable|=c.mask&old[i];
   U bits=c.mask;
   while(bits){int p=(uint64_t)bits?__builtin_ctzll((uint64_t)bits):64+__builtin_ctzll((uint64_t)(bits>>64));bits&=bits-1;pcount[p]++;}
  }
  if(!count)return false;
  lb+=mincost;
  if(lb>budget)return false;
  if(count<mincount){mincount=count;best=i;branch=move(local);}
 }
 // Any residual point unavailable in its original label must enter a different
 // label. Each such point contributes one incoming history to the objective.
 if(pc(rem&~retainable)>budget)return false;
 // Point coverage is a separate exact-cover constraint; branching on a sparse
 // point can be much stronger than fixing one old-label column.
 U visit=rem;
 int pointowner=-1;
 vector<pair<int,C>> pbranch;
 while(visit){
  int p=(uint64_t)visit?__builtin_ctzll((uint64_t)visit):64+__builtin_ctzll((uint64_t)(visit>>64));
  U bit=U(1)<<p;visit^=bit;
  int count=pcount[p];
  if(!count)return false;
  if(count<mincount){mincount=count;pointowner=p;}
 }
 if(pointowner>=0){
  U bit=U(1)<<pointowner;
  for(auto &v:valid)if(v.second.mask&bit)pbranch.push_back(v);
  sort(pbranch.begin(),pbranch.end(),[](auto&a,auto&b){return a.second.incoming<b.second.incoming;});
  for(auto &[i,c]:pbranch){chosen[i]=c;if(dfs(todo^(1u<<i),rem^c.mask,budget-c.incoming))return true;}
 }else{
  sort(branch.begin(),branch.end(),[](auto&a,auto&b){return a.incoming<b.incoming;});
  for(auto &c:branch){chosen[best]=c;if(dfs(todo^(1u<<best),rem^c.mask,budget-c.incoming))return true;}
 }
 return false;
}

void printrow(U r){cout<<'[';bool comma=false;for(int p=0;p<125;p++)if(r>>p&1){if(comma)cout<<',';cout<<p;comma=true;}cout<<']';}
int main(int argc,char**argv){
 if(argc<3)return 2;
 ifstream f(argv[1]);target=stoi(argv[2]);int m,s,x;f>>m;for(int i=0;i<m;i++){f>>s;U a=0;while(s--){f>>x;a|=U(1)<<x;}old.push_back(a);}f>>m;for(int i=0;i<m;i++){f>>s;sizes.push_back(s);U a=0;while(s--){f>>x;a|=U(1)<<x;}bank.push_back(a);}
 if(!f || old.size()!=22)return 3;
 array<vector<C>,22> all;
 for(int i=0;i<22;i++)for(int j=0;j<(int)bank.size();j++){int w=pc(bank[j]&~old[i]);if(w==0 || w==2)all[i].push_back({bank[j],w,j});}
 for(auto &cs:all)stable_sort(cs.begin(),cs.end(),[](auto&a,auto&b){return a.incoming<b.incoming;});
 chosen.resize(22);
 U total=(U(1)<<125)-1;
 for(int q=0;q<(int)bank.size();q++){
  if(sizes[q]!=5)continue;int budget=target-sizes[q];if(budget<0)continue;
  newq=bank[q];bool possible=true;int lower=0;
  for(int i=0;i<22;i++){
   opts[i].clear();int mw=100;
   for(const auto &c:all[i])if(!(c.mask&newq) && c.incoming<=budget){opts[i].push_back(c);mw=min(mw,c.incoming);}
   lower+=mw;
   if(lower>budget){possible=false;break;}
  }
  if(!possible)continue;
  eligible++;
  if(dfs((1u<<22)-1,total^newq,budget)){
   cout<<"{\"status\":\"FOUND\",\"budget\":"<<target<<",\"nodes\":"<<nodes<<",\"new_label\":";printrow(newq);cout<<",\"groups\":[";
   for(int i=0;i<22;i++){if(i)cout<<',';printrow(chosen[i].mask);}cout<<',';printrow(newq);cout<<"]}\n";return 0;
  }
  completed++;
  if(completed%10==0)cerr<<"completed "<<completed<<" q "<<q<<" nodes "<<nodes<<'\n';
 }
 cout<<"{\"status\":\"EXHAUSTED\",\"budget\":"<<target<<",\"eligible_new_classes\":"<<eligible<<",\"completed\":"<<completed<<",\"nodes\":"<<nodes<<"}\n";
}
