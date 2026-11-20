#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using M=uint64_t;
struct Row{ M mask; int size,cost; };
int pop(M a){return __builtin_popcountll(a);}
int low(M a){return __builtin_ctzll(a);}
M bad[60][60],readmask[60][60][4];vector<Row> rows;
long long nodes,covers;
int best=50000;
vector<M> win,chosen;
bool legal(M s){
 for(M p=s;p;p&=p-1)for(M q=p&(p-1);q;q&=q-1)if(bad[low(p)][low(q)]&s)return false;
 return true;
}
int cost(M s){
 int val=0;
 for(M p=s;p;p&=p-1){M m[4]{};for(M q=s;q;q&=q-1)for(int h=0;h<4;h++)m[h]|=readmask[low(p)][low(q)][h];for(M u:m)val+=pop(u);}
 return val;
}
bool after(M s,M prev){return pop(s)<pop(prev)||(pop(s)==pop(prev)&&s>prev);}
void dfs(M free,int k,const vector<int>& can,int acc,M prev);
void subsets(M free,M rest,M chosenrow,int need,int k,const vector<int>&can,int acc,M prev){
 if(!need){
  if(!after(chosenrow,prev)||!legal(chosenrow))return;
  vector<int> next; // Subsequent choices can include size nine if this row had size nine (handled by the catalogue).
  chosen.push_back(chosenrow);dfs(free^chosenrow,k-1,next,acc+cost(chosenrow),chosenrow);chosen.pop_back();
  return;
 }while(pop(rest)>=need){M b=rest&-rest;rest^=b;subsets(free,rest,chosenrow|b,need-1,k,can,acc,prev);}
}
void dfs(M free,int k,const vector<int>&can,int acc,M prev){
 ++nodes;
 int n=pop(free);
 if(n<k||n>pop(prev)*k)return;
 if(k==1){
  if(after(free,prev)&&legal(free)){
   ++covers;int c=acc+cost(free);cout<<"table "<<c;for(auto row:chosen)cout<<" "<<row;cout<<" "<<free<<"\n";
   if(c<best){best=c;win=chosen;win.push_back(free);}
  }return;
 }
 int need=(n+k-1)/k;
 for(int pos=0;pos<(int)can.size();++pos){
  int j=can[pos];auto [s,b,c]=rows[j];if(b<need)break;
  vector<int> next;
  // Filter the eligible suffix only, restoring the unique descending order.
  
  
  if(k==2){chosen.push_back(s);dfs(free^s,1,{},acc+c,s);chosen.pop_back();continue;}
  for(int i=pos+1;i<(int)can.size();i++){
   // Descending list preserves smaller rows even if unusable *next*: later they may be needed.
   if(!(rows[can[i]].mask&s))next.push_back(can[i]);
  }
  chosen.push_back(s);dfs(free^s,k-1,next,acc+c,s);chosen.pop_back();
 }
 for(int q=need;q<=min(8,pop(prev));q++)subsets(free,free,0,q,k,can,acc,prev);
}
int main(int argc,char**argv){
 string s=argv[1];ifstream a("p5sets"+s+".dat"),b("p5bad"+s+".dat"),c("p5cost"+s+".dat");
 M m;int v,x,y;while(a>>m>>v)rows.push_back({m,pop(m),v});
 while(b>>x>>y>>m)bad[x][y]=bad[y][x]=m;
 while(c>>x>>y)for(int i=0;i<4;i++)c>>readmask[x][y][i];
 for(auto& row:rows)row.cost=cost(row.mask);
 sort(rows.begin(),rows.end(),[](auto a,auto b){return a.size>b.size||(a.size==b.size&&a.mask<b.mask);});
 vector<int> can(rows.size());for(int i=0;i<(int)rows.size();i++)can[i]=i;
 dfs((M(1)<<60)-1,6,can,0,~M(0));
 cout<<s<<" "<<covers<<" "<<best<<" "<<nodes;for(auto u:win)cout<<" "<<u;cout<<endl;
}
