#include <bits/stdc++.h>
using namespace std;
// Complete abstract mask quotient: types (1),(2),(1,2),(2,2),(2,3).
// Each double phase has two distinct ports. A common mask-3 port
// always shares its unique mask-2 partner. Exact Boolean graph semantics.
const vector<vector<int>> patterns={{1},{2},{1,2},{2,2},{2,3}};
long long allow=0,cyclic=0,bad=0,four=0,finite_count=0,maxfinite=-1;
vector<int> besttype,bestlab,badtype,badlab;
struct Info{bool cyc,ret4,ret8;int longest;};
Info eval(const vector<vector<pair<int,int>>>& phases,int n){
 int N=1<<n,V=N*4;
 vector<vector<int>> ad(V);vector<int> indeg(V);
 for(int q=0;q<4;q++)for(int x=0;x<N;x++){
  int u=q*N+x;
  for(auto [j,mask]:phases[q])if(mask&(1<<((x>>j)&1))){
   int v=((q+1)%4)*N+(x^(1<<j));ad[u].push_back(v);indeg[v]++;
  }
 }
 bool ret4=false,ret8=false;vector<vector<int>> one(N);
 for(int x=0;x<N;x++){
  vector<int> cur={x};
  for(int q=0;q<4;q++){
   vector<int> nx;
   for(int z:cur)for(auto [j,mask]:phases[q])
    if(mask&(1<<((z>>j)&1)))nx.push_back(z^(1<<j));
   sort(nx.begin(),nx.end());nx.erase(unique(nx.begin(),nx.end()),nx.end());
   cur.swap(nx);if(cur.empty())break;
  }
  one[x]=cur;for(int z:cur)if(z==x)ret4=true;
 }
 for(int x=0;x<N&&!ret8;x++)for(int z:one[x])
  for(int y:one[z])if(y==x){ret8=true;break;}
 queue<int> qu;for(int u=0;u<V;u++)if(indeg[u]==0)qu.push(u);
 vector<int> longest(V,0);int done=0;
 while(!qu.empty()){
  int u=qu.front();qu.pop();done++;
  for(int v:ad[u]){
   longest[v]=max(longest[v],longest[u]+1);
   if(--indeg[v]==0)qu.push(v);
  }
 }
 int ml=0;for(int v:longest)ml=max(ml,v);
 return {done<V,ret4,ret8,ml};
}
void partrec(const vector<int>& types,int idx,int classes,vector<int>& lab){
 if(idx==(int)lab.size()){
  int cursor=0;map<int,int> partner;
  for(int q=0;q<4;q++){
   if(types[q]==4){
    int j2=lab[cursor],j3=lab[cursor+1];
    if(partner.count(j3)&&partner[j3]!=j2)return;
    partner[j3]=j2;
   }
   cursor+=patterns[types[q]].size();
  }
  allow++;
  vector<vector<pair<int,int>>> phases(4);cursor=0;
  for(int q=0;q<4;q++)for(int mask:patterns[types[q]])
   phases[q].push_back({lab[cursor++],mask});
  Info z=eval(phases,classes);
  if(z.ret4)four++;
  if(z.cyc){
   cyclic++;
   if(!z.ret8){bad++;if(bad==1){badtype=types;badlab=lab;}}
  }else{
   finite_count++;
   if(z.longest>maxfinite){maxfinite=z.longest;besttype=types;bestlab=lab;}
  }
  return;
 }
 for(int k=0;k<=classes;k++){
  bool duplicate=false;int off=0;
  for(int q=0;q<4;q++){
   int sz=patterns[types[q]].size();
   if(sz==2&&idx==off+1&&lab[off]==k)duplicate=true;
   off+=sz;
  }
  if(duplicate)continue;
  lab[idx]=k;partrec(types,idx+1,max(classes,k+1),lab);
 }
}
int main(int argc,char**argv){
 int wanted=(argc>1)?stoi(argv[1]):-1;
 for(int a=0;a<5;a++)for(int b=0;b<5;b++)
 for(int c=0;c<5;c++)for(int d=0;d<5;d++){
  vector<int> tt={a,b,c,d};int branches=0,slots=0;
  for(int t:tt){if(patterns[t].size()==2)branches++;slots+=patterns[t].size();}
  if(wanted!=-1&&branches!=wanted)continue;
  vector<int> lab(slots,0);partrec(tt,0,0,lab);
 }
 cout<<"configurations="<<allow<<" cyclic="<<cyclic<<" finite="<<finite_count
 <<" four="<<four<<" cyclic_without_eight="<<bad<<" max_acyclic_path="<<maxfinite<<"\n";
 auto show=[](string s,vector<int> t,vector<int> lab){
  cout<<s<<" types";for(int x:t)cout<<" "<<x;
  cout<<" ports";for(int x:lab)cout<<" "<<x;cout<<"\n";
 };
 show("max_witness",besttype,bestlab);
 if(bad)show("counterexample",badtype,badlab);
}
