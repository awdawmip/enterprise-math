#include <algorithm>
#include <bit>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
struct Opt{int h,b,mass=0; vector<pair<int,uint64_t>> words;};
struct Branch{
 int k,P,n,w; vector<int>D,hs,R;
 Branch(istream& in){int h,r;in>>k>>P>>n>>h>>r;for(int i=0,x;i<n;i++){in>>x;D.push_back(x);}for(int i=0,x;i<h;i++){in>>x;hs.push_back(x);}for(int i=0,x;i<r;i++){in>>x;R.push_back(x);}w=(n+63)/64;}
};
struct Run{
 Branch B; bool rev; vector<Opt> opts; vector<vector<int>> at, checked;
 vector<uint8_t> blocked; vector<int> chosen, cap; vector<uint64_t> full;
 vector<vector<uint64_t>> used;
 uint64_t visited=0, kept=0, shapes=0;
 ostream& out;
 Run(Branch b,bool r,ostream& o):B(move(b)),rev(r),out(o){
  full.assign(B.w,~uint64_t(0)); if(B.n%64)full.back()=(uint64_t(1)<<(B.n%64))-1;
  at.resize(B.n); if(rev) {reverse(B.D.begin(),B.D.end());reverse(B.hs.begin(),B.hs.end());}
  for(int h:B.hs){
   vector<int> ids(h,-1);
   for(int i=0;i<B.n;i++){int a=B.D[i]%h;
    int& j=ids[a];
    if(j<0){j=opts.size();opts.push_back({h,a});}
    Opt& v=opts[j]; if(v.words.empty()||v.words.back().first!=i/64)v.words.emplace_back(i/64,0);
    v.words.back().second|=uint64_t(1)<<(i%64);
    v.mass++;at[i].push_back(j);
   }
  }
  vector<int>M;for(const auto& o:opts)M.push_back(o.mass);
  sort(M.rbegin(),M.rend());cap.push_back(0);
  for(int i=0;i<B.k;i++)cap.push_back(cap.back()+(i<(int)M.size()?M[i]:0));
  blocked.assign(opts.size(),0);used.assign(B.k+1,vector<uint64_t>(B.w));checked.resize(B.k);
  for(auto& a:checked)a.reserve(B.hs.size());
 }
 void emit(){
  shapes++;
  for(int j:chosen){
   auto& o=opts[j]; bool priv=false;
   auto other=vector<uint64_t>(B.w);
   for(int i:chosen)if(i!=j)for(auto [p,u]:opts[i].words)other[p]|=u;
   for(auto [p,u]:o.words)if(u&~other[p]){priv=true;break;}
   if(!priv)return;
  }
  kept++;
  vector<pair<int,int>> slots; for(int r:B.R)slots.emplace_back(7,r);
  for(int x:chosen)slots.emplace_back(opts[x].h,opts[x].b);
  sort(slots.begin(),slots.end());
  for(size_t i=0;i<slots.size();i++){if(i)out<<',';out<<slots[i].first<<':'<<slots[i].second;}out<<'\n';
 }
 void dfs(int depth,int missing,int from){
  visited++;
  if(!missing){emit();return;}
  int remain=B.k-depth;if(remain==0||missing>cap[remain])return;
  const auto& state=used[depth];
  int idx=from;
  while((state[idx]&full[idx])==full[idx])++idx;
  int pivot=idx*64+countr_zero(full[idx]&~state[idx]);
  auto& done=checked[depth];done.clear();
  for(int j:at[pivot]){
   if(blocked[j])continue;
   const Opt& o=opts[j];
   if(o.mass+cap[remain-1]>=missing){
    int added=0;
    for(auto [p,u]:o.words)added+=popcount(u&~state[p]);
    if(added+cap[remain-1]>=missing){
     chosen.push_back(j);
     if(added==missing){visited++;emit();}
     else{
      auto& next=used[depth+1];copy(state.begin(),state.end(),next.begin());
      for(auto [p,u]:o.words)if(p>=idx)next[p]|=u;
      dfs(depth+1,missing-added,idx);
     }
     chosen.pop_back();
    }
   }
   blocked[j]=1;done.push_back(j);
  }
  for(int j:done)blocked[j]=0;
 }
 void go(){if(!opts.empty())dfs(0,B.n,0);}
};
int main(int argc,char**argv){
 if(argc!=4)return 2;
 ifstream in("branches.txt");int n;in>>n;
 int lo=stoi(argv[1]),hi=stoi(argv[2]);bool rev=stoi(argv[3]);
 for(int t=0;t<n;t++){
  Branch b(in);int i=t;
  // Both directions read the same immutable branch indices.
  if(i<lo||i>=hi||b.hs.empty())continue;
  string p="branch-"+to_string(i)+"-"+to_string((int)rev);
  ifstream already(p+".txt");if(already.good())continue;
  ofstream out(p+".tmp"); Run r(move(b),rev,out); r.go();
  out<<"# "<<i<<' '<<r.visited<<' '<<r.shapes<<' '<<r.kept<<' '<<r.B.P<<'\n';
  out.close(); if(rename((p+".tmp").c_str(),(p+".txt").c_str()))return 3;
 }
}
